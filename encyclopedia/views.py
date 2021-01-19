from django.shortcuts import render

from . import util


def index(request):
    context = {
        "entries": util.list_entries()
    }
    return render(request, "encyclopedia/index.html", context)


def create_new_page(request):
    pass


def random_page(request):
    pass


def detail_page(request):
    pass