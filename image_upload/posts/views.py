from django.http import HttpResponse

from django.shortcuts import render

from django.template import loader

from .models import Posts


def index_home(request):
    latest_images_list = Posts.objects.all()
    my_name            = Posts.objects.all()   
    template = loader.get_template('posts/index.html')
    context = {
        'latest_images_list': latest_images_list,
        'my_name': my_name
    }
    return HttpResponse(template.render(context, request))


def script_home(request):
    latest_images_list = Posts.objects.all()
    my_name            = Posts.objects.all()   
    template = loader.get_template('posts/index.html')
    context = {
        'latest_images_list': latest_images_list,
        'my_name': my_name
    }
    return HttpResponse(template.render(context, request))



def gadha_home(request):
    
    return render(request, "posts/script.html")