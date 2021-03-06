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


def random_page(request):
    random_page = random.choice(util.list_entries())
    
    return redirect("detail_page", page_title=random_page)


def new_entry(request):
    form = forms.NewEntry

    if request.method == "POST":
        form = forms.NewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            existing_entries = [entry.lower() for entry in util.list_entries()]
            
            if title.lower() in existing_entries:
                messages.error(request, f'A page already exists for {title}')
                return redirect('new_entry')

            content = form.cleaned_data.get('content')
            
            util.save_entry(title, content)
            messages.success(request, f'New page created for {title}')
            
            return redirect('detail_page', page_title=title)

    context = {
        'title': 'New Wiki Page',
        'form': form
    }
    return render(request, "encyclopedia/new_entry.html", context)


def edit_entry(request, page_title):
    entry = util.get_entry(page_title)
    form = forms.EditEntry

    if request.method == "POST":
        form = forms.EditEntry(request.POST)
        if form.is_valid():
            title = page_title
            content = form.cleaned_data.get('content')

            util.save_entry(title, content)
            messages.success(request, f'Changes saved to {title}')

            return redirect('detail_page', page_title=page_title)

    context = {
        'title': f"Edit: {page_title}",
        'entry': entry,
        'form': form
    }
    return render(request, "encyclopedia/edit_entry.html", context)


def detail_page(request, page_title):
    entry = util.get_entry(page_title)
    if entry == None:
        return render(request, "encyclopedia/no_page.html")
    
    html = markdown(entry)

    context = {
        'title': page_title,
        'entry': html,
    }
    return render(request, "encyclopedia/detail.html", context)


def search(request):
    query = request.POST['query']
    entries = util.list_entries()

    match = [entry for entry in entries if query.lower() == entry.lower()]
    if len(match) > 0:
        return redirect('detail_page', page_title=match[0])

    partial_matches = [entry for entry in entries if query.lower() in entry.lower()]
    context = {
        'title': 'Search results...',
        'query': query,
        'partial_matches': partial_matches,
    }
    return render(request, "encyclopedia/search.html", context)
