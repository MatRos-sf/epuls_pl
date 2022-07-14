from django  import forms
from .models import Account

class CreateUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    password_two = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    username = forms.CharField()

    class Meta:
        model = Account
        fields = ('username', 'email', )

    def clean_passwordTwo(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_two']:
            raise forms.ValidationError('Password must be the same')
        return cd['password']