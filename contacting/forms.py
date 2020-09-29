from django import forms

from contacting.models import Category


class UserForm(forms.Form):
    name = forms.CharField(max_length=64)
    surname = forms.CharField(max_length=64)
    description = forms.CharField(max_length=500, required=False)
    type = (forms.ModelChoiceField(
        label="category",
        # widget=forms.CheckboxInput,
        queryset=Category.objects.all(),
        to_field_name='name'
    ))


class AddressForm(forms.Form):
    city = forms.CharField(max_length=64)
    street = forms.CharField(max_length=64)
    house_nr = forms.IntegerField()
    flat_nr = forms.IntegerField(required=False)
    code = forms.CharField(max_length=6)


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=64)
#
# class RegistrationForm(forms.Form):
#     password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'placeholder': "Hasło"}),
#                                validators=[validate_password])
#     password2 = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'placeholder': "Powtórz hasło"}),
#                                 validators=[validate_password])
#     email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={'placeholder': "Email"}))
#     name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': "Imię"}))
#     surname = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': "Nazwisko"}))
#
#
# class DonationForm(forms.Form):
#     bags = forms.IntegerField(widget=forms.NumberInput
#     (attrs={'id': 'quantity'}))
#     categories = forms.ModelMultipleChoiceField(
#         label="categories",
#         widget=forms.CheckboxSelectMultiple,
#         queryset=Category.objects.all(),
#         # to_field_name='name',
#     )
#     institution = forms.ModelChoiceField(
#         label="institution",
#         widget=forms.RadioSelect,
#         queryset=Institution.objects.all(),
#         # to_field_name='name',
#     )
#     address = forms.CharField(max_length=100, widget=forms.TextInput
#     (attrs={'id': 'address'}))
#     phone_number = forms.CharField(max_length=15, widget=forms.TextInput
#     (attrs={'id': 'phone_number'}))
#     city = forms.CharField(max_length=100, widget=forms.TextInput
#     (attrs={'id': 'city'}))
#     zip_code = forms.CharField(max_length=6, widget=forms.TextInput
#     (attrs={'id': 'zip_code'}))
#     pick_up_date = forms.DateField(widget=forms.DateInput(attrs={'id': 'pick_up_date'}))
#     pick_up_time = forms.TimeField(widget=forms.TimeInput(attrs={'id': 'pick_up_time', 'class': 'timepicker'}))
#     pick_up_comment = forms.CharField(max_length=255, required=False,
#                                       widget=forms.Textarea(attrs={'id': 'pick_up_comment'}))
#
#
# # class TakenForm(forms.Form):
# #     donation_id = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'pick_up_comment'}))
#
#
# class PasswordChangingForm(forms.Form):
#     old_password = forms.CharField(label="Stare hasło", max_length=40, widget=forms.PasswordInput)
#     new_password = forms.CharField(label="Nowe hasło", max_length=40, widget=forms.PasswordInput)
#     new_password_2 = forms.CharField(label="Powtórz nowe hasło", max_length=40, widget=forms.PasswordInput)