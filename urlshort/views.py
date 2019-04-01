from django.shortcuts import render, redirect
from .models import FullURL
from django.http import HttpResponse
from . import helper



def index(request):
    return render(request, 'urlshort/index.html')

def results(request):
    if request.method == 'POST':
        full_url = request.POST['full_url']
        full_url = helper.check_for_protocol(full_url)
        domain = request.META['HTTP_HOST']
        short_url = ""
        if FullURL.objects.filter(full_url_string=full_url).exists():
            q = FullURL.objects.get(full_url_string=full_url)
            short_url = q.short_url
        else:
            short_url = helper.shorten_url(full_url)
            if (short_url==(-1)):
                return render(request, '500.html')
            q = FullURL(full_url_string=full_url, short_url = short_url)
            q.save()
        short_url_text = "/".join([domain, short_url])
        context = {
            'full_url': full_url,
            'short_url': short_url,
            'short_url_text': short_url_text

        }

    return render(request, 'urlshort/result.html', context)

def redirect_to_full_url(request, short_url):
    if FullURL.objects.filter(short_url=short_url).exists() :
        q = FullURL.objects.get(short_url=short_url)
        full_url = q.full_url_string
        return redirect(full_url)
    else:
        return render(request, "404.html")
