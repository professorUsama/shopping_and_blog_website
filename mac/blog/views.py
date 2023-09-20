from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blogpost
# Create your views here.
def index(request):
    postData = Blogpost.objects.all()
    data = {"postData": postData}
    return render(request, 'blog/index.html', data)


def blogpost(request, post_id):
    getData = Blogpost.objects.filter(post_id=post_id)
    postData = {"data":getData}
    print(postData)
    return render(request, 'blog/blogpost.html', postData)