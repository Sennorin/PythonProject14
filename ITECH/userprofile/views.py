from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from userprofile.forms import  LoginForm,RegisterForm,RegisterrestaurantForm,RegisterForm,ProfileForm,restaurant_update_Form
from IT.models import Restaurant,Review
from userprofile.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
def user_login(request):
    if request.method == "GET":
        login_form = LoginForm()
        context = {"login_form": login_form}
        return render(request, "userprofile/login.html", context)
    else:
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("IT:restaurant_list")
            else:
                return HttpResponse('The account password was entered incorrectly, please re-enter it!')
        else:
            context = {'obj': login_form, 'error': login_form.errors}
            return render(request, 'userprofile/login.html', context)
# Create your views here.
def user_logout(request):
    logout(request)
    return redirect("IT:restaurant_list")

def user_register(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'userprofile/register.html', context)
    else:
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            return redirect("userprofile:user_login")
        else:
            context = {'obj': register_form, 'error': register_form.errors}
            return render(request, 'userprofile/register.html', context)


@login_required(login_url='userprofile:user_login')
def user_profile(request):
    if request.method == "GET":
        # 获取当前用户的信息
        information = UserProfile.objects.filter(id=request.user.id)
        # 获取当前用户的餐厅
        if isinstance(request.user, UserProfile):
            restaurants = Restaurant.objects.filter(owner=request.user)
        else:
            restaurants = Restaurant.objects.none()  # 如果不是 UserProfile 类型，返回空查询集

        # 构建上下文数据
        context = {
            'information': information,
            'restaurants': restaurants,
        }
        # 渲染模板，返回上下文数据
        return render(request, 'userprofile/profile.html', context)

    else:  # POST 请求处理
        profile = UserProfile.objects.get(id=request.user.id)
        profile_form =ProfileForm(request.POST, request.FILES)  # 处理文件上传

        if profile_form.is_valid():
            profile_form_data = profile_form.cleaned_data
            if 'avatar' in request.FILES:
                profile.avatar = profile_form_data['avatar']
            profile.save()
            return redirect('userprofile:user_profile')  # 成功后重定向回个人主页
        else:
            return HttpResponse('There is an error in the content of the form, please refill it!')


@login_required(login_url='userprofile:user_login')
def register_restaurant(request):
    if request.method == 'POST':
        register_restaurant_form = RegisterrestaurantForm(request.POST, request.FILES)
        if register_restaurant_form.is_valid():
            restaurant = register_restaurant_form.save(commit=False)
            restaurant.owner = request.user
            restaurant.save()
            return redirect('userprofile:user_profile')
        else:
            print(register_restaurant_form.errors)  # 打印错误信息，方便调试
            return HttpResponse('There is an error in the content of the form, please refill it!')
    else:
        register_restaurant_form = RegisterrestaurantForm()
    return render(request, 'userprofile/register_restaurant.html', {'register_restaurant_form': register_restaurant_form})

@login_required(login_url='userprofile:user_login')
def user_restaurants(request):
    print(f"User Type: {type(request.user)}")  # 打印用户类型

def restaurant_delete(request, id):
    if request.method == "GET":
        restaurant = Restaurant.objects.get(id=id)
        if restaurant.owner.id == request.user.id:
            restaurant.delete()
            return redirect("IT:restaurant_list")
        else:
            return HttpResponse('You do not have the right to delete it！')


@login_required(login_url='userprofile:user_login')
def restaurant_update(request, id):
    # 获取现有的餐厅对象
    restaurant = Restaurant.objects.get(id=id)

    if request.method == "GET":
        # 渲染页面时，传入现有的餐厅对象
        context = {"restaurant": restaurant}
        return render(request, "userprofile/update.html", context)
    else:
        # 将现有的餐厅对象传递给表单，确保表单是基于当前的餐厅对象进行更新
        register_restaurant_form = restaurant_update_Form(request.POST, request.FILES, instance=restaurant)

        if register_restaurant_form.is_valid():
            # 如果没有上传新图片，保留旧的图片
            if not request.FILES.get('main_image'):  # 如果没有上传新的主图片
                register_restaurant_form.instance.main_image = restaurant.main_image
            if not request.FILES.get('restaurant_image'):  # 如果没有上传新的餐厅图片
                register_restaurant_form.instance.restaurant_image = restaurant.restaurant_image

            # 验证用户是否是餐厅的所有者
            if restaurant.owner.id == request.user.id:
                # 保存更新后的餐厅对象
                register_restaurant_form.save()
                return redirect('IT:restaurant_detail', id=id)
            else:
                return HttpResponse('You do not have the right to modify it!')
        else:
            print(register_restaurant_form.errors)  # 打印表单的错误信息，方便调试
            return HttpResponse("There is an error in the content of the form, please refill it!")


