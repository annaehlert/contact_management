from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from contacting.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

def show_all(request):
    users = User.objects.all().order_by('name', 'surname')
    ctx = {
            "users": users,
            }
    return render(request, "base.html", ctx)

def person_details(request, id):
    user = get_object_or_404(User, pk=id)
    ctx = {
        "user": user,
    }
    return render(request, "details.html", ctx)

@method_decorator(csrf_exempt, name='dispatch')
class Add_new(View):
    def get(self, request):
        return render(request, "add_person.html")
    # def post(self, request):

