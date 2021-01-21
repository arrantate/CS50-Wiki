from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

import random
from markdown2 import markdown

from . import util, forms


def index(request):
    context = {
        "entries": util.list_entries()
    }
    return render(request, "encyclopedia/index.html", context)


def new_entry(request):
    form = forms.NewEntry

    if request.method == "POST":
        form = forms.NewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            title_underscore = title.replace(" ", "_")
            content = form.cleaned_data.get('content')

            util.save_entry(title_underscore, content)

            messages.success(request, f'New page created for {title}')
            return redirect('detail_page', page_title=title_underscore)

    context = {
        'form': forms.NewEntry()
    }
    return render(request, "encyclopedia/new_entry.html", context)


def random_page(request):
    random_page = random.choice(util.list_entries())
    
    return redirect(f"/wiki/{random_page}")


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