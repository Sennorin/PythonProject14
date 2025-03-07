from django import forms
from userprofile.models import UserProfile
from IT.models import Restaurant
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            return forms.ValidationError('两次输入的密码不一致，请重新输入！')

class RegisterrestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = ['owner', 'rating']  # 排除不需要在表单中显示的字段



class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)


class restaurant_update_Form(forms.ModelForm):
        class Meta:
            model = Restaurant
            exclude = ['owner', 'rating','created']  # 排除不需要在表单中显示的字段

        main_image = forms.ImageField(required=False)  # 不强制要求上传新图片
        restaurant_image = forms.ImageField(required=False)  # 不强制要求上传新图片


