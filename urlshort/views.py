from django.shortcuts import render, redirect
from .models import FullURL
from django.http import HttpResponse
from . import helper

def index(request):
    return render(request, 'urlshort/index.html')

def results(request):
    if request.method == 'POST':
        full_url = request.POST['full_url']
        if helper.full_url_is_in_db(full_url):
            q = FullURL.objects.get(full_url_string=full_url)
            short_url = q.short_url
        else:
            domain = request.META['HTTP_HOST']
            full_url = helper.check_for_protocol(full_url)
            short_url = helper.shorten_url(full_url)
            if (short_url==(-1)):
                return render(request, '500.htlm')

            short_url_text = "/".join([domain, "urlshort", short_url])
            q = FullURL(full_url_string=full_url, short_url = short_url)
            q.save()
        context = {
            'full_url': full_url,
            'short_url': short_url,
            'short_url_text': short_url_text
        }
        print("short:", short_url, "shor text: ", short_url_text," full: ", full_url)
    return render(request, 'urlshort/result.html', context)

def redirect_to_full_url(request, short_url):
    print("i got short:", short_url)
    q = FullURL.objects.get(short_url=short_url)
    full_url = q.full_url_string
    print("full is: ", full_url)
    response = redirect(full_url)
    return response
