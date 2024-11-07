from django.shortcuts import render, redirect
from .models import Link
from .function import create_qrcode


def welcome(request):
    return render(request, 'main/welcome.html')


def link_views(request):
    links = Link.objects.all()
    context = {'links': links}
    return render(request, 'main/links.html', context)


def link_create(request):
    if request.method == 'POST':
        url = request.POST['link']
        link = Link.objects.create(url=url)
        img = create_qrcode(request, link)
        link.img = img
        link.save()
        return redirect('main:link_views')

    return render(request, 'main/links.html')

