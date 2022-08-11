"""blog_em URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Hom
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from browser.views import home_view, search_views, create_spaces_view
from blog.views import frontpage_view, space_detail_view, create_post_view, post_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('create_spaces/', create_spaces_view, name='create_spaces'),
    path('results/', search_views, name='results'),
    path('frontpage/', frontpage_view, name='frontpage'),
    path('<slug:space_slug>/', space_detail_view, name='space_detail'),
    path('<slug:space_slug>/<slug:post_slug>/', post_detail_view, name='post_detail'),
    path('<slug:space_slug>/create_post/', create_post_view, name='create_post'),
]
