from django import forms
from .models import CountyCustomer, Defaulter, Enterprise, Service
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user  

class CountyCustomerForm(forms.ModelForm):
    class Meta:
        model = CountyCustomer
        fields = ['name', 'contact_number', 'email', 'address', 'enterprises']

class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['name', 'registration_number', 'address', 'contact_number']
from .models import Revenue

class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ['county_customer', 'enterprise', 'service', 'amount']

class ServiceForm(forms.ModelForm):
    class Meta:
        model=Service
        fields = ('__all__')
    def clean_field(self):
        data = self.cleaned_data('fields')

from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer', 'amount', 'invoice_number', 'issued_date'] 

class DefaulterForm(forms.ModelForm):
    class Meta:
        model=Defaulter
        fields = ('__all__')
    def clean_field(self):
        data = self.cleaned_data('fields')
# forms.py


class MpesaExpressForm(forms.Form):
    PartyA = forms.CharField(max_length=12)
    Amount = forms.DecimalField(max_digits=10, decimal_places=2)





