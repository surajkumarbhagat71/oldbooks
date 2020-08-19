from django.shortcuts import render,redirect
from django.contrib import  messages
from .forms import *
from .models import *

def home(r):
    data = {
        "books":Books.objects.all(),
        "cat":Category.objects.all(),
        "topic":Topic.objects.all()
    }
    return render(r,"home.html",data)

def insert(r):
    form = BookInsert(r.POST or None,r.FILES or None)
    data = {
        "form":form,
        "cat" : Category.objects.all()
    }
    if r.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(r,"Data inserted successfully")
        else:
            messages.warning(r,"Failed to submit..")
        return redirect(insert)
    return render(r,"insert.html",data)

def search(r):
    if r.method == "GET":
        searchdata = r.GET.get('search')
        data = {
            "books":Books.objects.filter(book_title__icontains=searchdata),
            "cat":Category.objects.all(),
            "topic":Topic.objects.all()
        }
        return render(r,"home.html",data)
    else:
        redirect(home)

def category(r,cat_id):
    data = {
        "books":Books.objects.filter(book_topic__topic_category__cat_id=cat_id),
        "cat":Category.objects.all(),
        "topic":Topic.objects.all()
    }
    return render(r,'home.html',data)

def topic(r,topic_id):
    data = {
        "books" : Books.objects.filter(book_topic__topic_id = topic_id),
        "cat" : Category.objects.all(),
        "topic" : Topic.objects.all()
    }
    return render(r,'home.html',data)

def items(r,book_id):
    data = {
        "books" : Books.objects.filter(book_id = book_id),
        "relatedbooks" : Books.objects.all().exclude(book_id = book_id),
        "cat" : Category.objects.all(),
        "topic" : Topic.objects.all()
    }
    return render(r,'item.html',data)