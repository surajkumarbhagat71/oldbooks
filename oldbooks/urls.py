"""oldbooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from datawork import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('insert/',views.insert,name='insert'),
    path('category/<int:cat_id>',views.category,name="category"),
    path('search/',views.search,name="search"),
    path('topic/<int:topic_id>',views.topic,name="topic"),
    path('item/<int:book_id>',views.items,name="items")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
