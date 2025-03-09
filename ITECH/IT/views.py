from django.db.models import Q, Avg,Value,FloatField
from django.http import HttpResponse
from django.shortcuts import render
from IT.models import Restaurant,Review
from comment.models import Comment
from django.db.models.functions import Coalesce
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.paginator import Paginator


from django.db.models import Avg, Value, FloatField
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator

def restaurant_list(request):
    search = request.GET.get('search', '')
    order = request.GET.get('order','')  # 默认按评分排序

    # 查询餐厅数据，并计算每个餐厅的平均评分
    restaurants = Restaurant.objects.all()

    # 计算每个餐厅的平均评分
    restaurants = restaurants.annotate(
        avg_rating=Coalesce(Avg('comment__rating'), Value(0), output_field=FloatField())
    )

    # 搜索功能
    if search:
        restaurants = restaurants.filter(Q(Name__icontains=search) | Q(Introduction__icontains=search))

    # 排序功能
    if order == 'rating':  # 按评分降序
        restaurants = restaurants.order_by('-avg_rating')
    elif order == 'created':  # 按创建时间（发布时间）降序
        restaurants = restaurants.order_by('-created')

    # 分页功能
    paginator = Paginator(restaurants, 5)  # 每页显示 5 个餐厅
    page = request.GET.get('page')  # 获取 url 中的页码
    restaurants = paginator.get_page(page)

    # 传递到模板的上下文
    context = {
        'restaurants': restaurants,
        'search': search,
        'order': order
    }

    return render(request, "IT/list.html", context=context)

def restaurant_detail(request, id):
    restaurants = Restaurant.objects.get(id=id)
    comments = Comment.objects.filter(restaurant=restaurants)
    context = {'restaurants': restaurants,'comments': comments}
    return render(request, "IT/detail.html", context)


def introduction(request):
    return render(request, "IT/introduction.html")
# Create your views here.
