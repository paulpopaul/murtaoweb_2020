from django.shortcuts import render, get_list_or_404
from .models import Post

# Create your Views here.

def blog_list(request):
    post_list = Post.objects.order_by('creado').filter(estado='Publicado')
    context = {
        'post_list': post_list,
    }
    template = 'blogapp/blog_list.html'
    return render(request, template, context)


def blog_detail(request, slug):
    post = get_list_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    template = 'blogapp/blog_detail.html'
    return render(request,template,context)

