# auth_app/forms.py

from django import forms
from study_app.validators import CustomPasswordValidator
from study_app.models import User  # Assuming your User model is in `study_app`

class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean_current_password(self):
        current_password = self.cleaned_data.get('current_password')
        if not self.user.check_password(current_password):
            raise forms.ValidationError("Current password is incorrect.")
        return current_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password != confirm_new_password:
            raise forms.ValidationError("The new passwords do not match.")
        
        CustomPasswordValidator.validate_password(new_password, self.user)

    def save(self):
        new_password = self.cleaned_data["new_password"]
        self.user.set_password(new_password)
        self.user.save()
        return self.user

class PasswordResetForm(forms.Form):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is associated with this email.")
        return email

    def get_user(self):
        return User.objects.get(email=self.cleaned_data['email'])

class OTPVerificationForm(forms.Form):
    email = forms.EmailField(required=True)
    otp = forms.CharField(max_length=6, required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        otp = cleaned_data.get("otp")

        try:
            user = User.objects.get(email=email)
            if user.otp_code != otp:
                raise forms.ValidationError("Invalid OTP.")
        except User.DoesNotExist:
            raise forms.ValidationError("Invalid email.")
        
        cleaned_data['user'] = user
        return cleaned_data
