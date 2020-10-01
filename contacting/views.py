from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from contacting.forms import UserForm, CategoryForm, AddressForm, PhoneForm, EmailForm
from contacting.models import User, Category, Address, Phone, Email
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View


def show_all(request):
    users = User.objects.all().order_by('name', 'surname')
    ctx = {
            "users": users,
            }
    return render(request, "panel.html", ctx)


def person_details(request, id):
    user = get_object_or_404(User, pk=id)
    ctx = {
        "user": user,
    }
    return render(request, "details.html", ctx)


class Add_new(View):

    def get(self, request):
        user_form = UserForm()
        address_form = AddressForm(initial={'code': "XX-XXX"})

        ctx = {
            "user_form": user_form,
            "address_form": address_form
        }
        return render(request, "add_person.html", ctx)

    def post(self, request):
        user_form = UserForm(request.POST)
        address_form = AddressForm(request.POST)
        if not user_form.is_valid() or not address_form.is_valid():
            messages.add_message(request, messages.WARNING, 'Person NOT added. Try again!')
            return render(request,
                          "add_person.html",
                          {"user_form": user_form,
                           "address_form": address_form
                           })
        name = user_form.cleaned_data['name']
        surname = user_form.cleaned_data['surname']
        description = user_form.cleaned_data['description']
        type = user_form.cleaned_data['type']

        city = address_form.cleaned_data['city']
        street = address_form.cleaned_data['street']
        house_nr = address_form.cleaned_data['house_nr']
        flat_nr = address_form.cleaned_data['flat_nr']
        code = address_form.cleaned_data['code']

        address = Address.objects.create(city=city, street=street, house_nr=house_nr, flat_nr=flat_nr, code=code)

        if description is None:
            User.objects.create(name=name, surname=surname, address=address,
                                type=Category.objects.filter(pk=type))
        User.objects.create(name=name, surname=surname, description=description, address=address, type=type)
        messages.add_message(request, messages.SUCCESS, 'New person added successfully')
        return redirect("index")


class Add_category(View):
    def get(self, request):
        form = CategoryForm()
        ctx = {
            "form": form
        }
        return render(request, "add_category.html", ctx)
    def post(self, request):
        form = CategoryForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, 'Category NOT added. Try again!')
            return render(request, "add_category.html", {"form": form})
        name = form.cleaned_data['name']
        Category.objects.create(name=name)
        messages.add_message(request, messages.SUCCESS, 'New category added successfully')
        return redirect("index")


class Add_phone(View):
    def get(self, request, id):
        form = PhoneForm()
        ctx = {
            "form": form
        }
        return render(request, "add_phone.html", ctx)

    def post(self, request, id):
        form = PhoneForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, 'Email NOT added. Try again!')
            return render(request, "add_phone.html", {"form": form})
        number = form.cleaned_data['number']
        type = form.cleaned_data['type']
        Phone.objects.create(number=number, type=type, user_id=id)
        messages.add_message(request, messages.SUCCESS, 'Phone added successfully')
        return redirect("details", id=id)


class Add_email(View):
    def get(self, request, id):
        form = EmailForm()
        ctx = {
            "form": form
        }
        return render(request, "add_email.html", ctx)

    def post(self, request, id):
        form = EmailForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, 'Email NOT added. Try again!')
            return render(request, "add_email.html", {"form": form})
        email = form.cleaned_data['email']
        email_type = form.cleaned_data['email_type']
        Email.objects.create(email=email, email_type=email_type, user_id=id)
        messages.add_message(request, messages.SUCCESS, 'Email added successfully')
        return redirect("details", id=id)