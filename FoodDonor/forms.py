from django import forms
from . models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=['email','mobile_number','address','area']
        widgets={
            'address': forms.TextInput(attrs={'placeholder':'Enter your address'}),
            'email': forms.EmailInput(attrs={'placeholder':'Enter your mail..'}),
            'area': forms.TextInput(attrs={'placeholder':'Enter main area..'}),
            'mobile_number': forms.TextInput(attrs={'placeholder':'Enter your mobile number..'})
        }