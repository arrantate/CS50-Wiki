from django.shortcuts import render, HttpResponse, redirect

import random
from markdown2 import markdown

from . import util, forms


def index(request):
    context = {
        "entries": util.list_entries()
    }
    return render(request, "encyclopedia/index.html", context)


def new_entry(request):
    context = {
        'form': forms.NewEntry()
    }
    return render(request, "encyclopedia/new_entry.html", context)


def random_page(request):
    random_wiki = random.choice(util.list_entries())
    return redirect(f"/wiki/{random_wiki}")


def detail_page(request, page_title):
    entry = util.get_entry(page_title)
    if entry == None:
        return HttpResponse('No such entry')
    
    html = markdown(entry)

    context = {
        'title': page_title,
        'entry': html,
    }
    return render(request, "encyclopedia/detail.html", context)