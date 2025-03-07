from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from IT.models import Restaurant,Review
from userprofile.models import UserProfile
from django.shortcuts import redirect
from comment.forms import CommentForm
from django.http import HttpResponse

@login_required(login_url='userprofile:login')
def comment_post(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.restaurant=restaurant
            new_comment.user = request.user
            new_comment.save()
            return redirect(restaurant)
        else:
            print(comment_form.errors)
            return HttpResponse('from content error！')
    else:
        return HttpResponse('only POST！')
# Create your views here.
