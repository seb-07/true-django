from django import forms
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    comfirm=forms.CharField(max_length=20,label="Parolayı doğrula",widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        if password and confirm and password !=confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor..")
        values ={"username":username,"password":password,"confirm":confirm}
        return values
class loginform(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)