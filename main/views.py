from django.shortcuts import render, redirect
from .models import Link, Generator
from .function import create_qrcode, generator_qrcode


def welcome(request):
    links = Link.objects.all()
    generators = Generator.objects.all()
    context = {'links': links, 'generators': generators}
    return render(request, 'main/welcome.html', context)


def link_views(request):
    links = Link.objects.all().order_by('-id')
    context = {'links': links}
    return render(request, 'main/links.html', context)


def link_create(request):
    links = Link.objects.all()
    context = {'links': links}
    if request.method == 'POST':
        url = request.POST['url']
        link = Link.objects.create(url=url)
        img = create_qrcode(request, link)
        link.img = img
        link.save()
        return redirect('main:links')
    return render(request, 'main/links.html', context)


def generators_views(request):
    generators = Generator.objects.all().order_by('-id')
    context = {'generators': generators}
    return render(request, 'main/generators.html', context)


def generator_view(request, pk):
    generator = Generator.objects.get(pk=pk)
    img = generator_qrcode(generator)
    generator.img = img
    generator.save()
    return render(request, 'main/generator.html', {'generator': generator})


def about_view(request):
    return render(request, 'main/about.html')

