from django.shortcuts import render

from pages.models import BlogModel, InfoModel


def home_page_view(request):
    kits = BlogModel.objects.all().order_by('-created_at')[:3]
    infoes = InfoModel.objects.all().order_by('-created_at')[:3]
    context = {
        "kits": kits,
        "infoes": infoes
    }
    return render(request, 'home.html', context)


def contact_page_view(request):
    return render(request, 'contact.html')


def about_page_view(request):
    return render(request, 'about-us.html')

def blog_page_view(request):
    blogs = BlogModel.objects.all().order_by('-created_at')[:6]
    recent_blogs = BlogModel.objects.all().order_by('-updated_at')[:3]
    context = {
        "blogs": blogs,
        "recent_blogs": recent_blogs,
    }
    return render(request, 'blog-list.html', context)
