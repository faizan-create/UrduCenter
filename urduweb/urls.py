"""UrduCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from urduweb.views import (home, about, disclaimer, PrivacyPolicy,
                           CreatePost, PostDetailView, CatListView, Contactus, TagIndexView, search
                           )
app_name = 'urduweb'

urlpatterns = [

    path('', home, name='home'),

    path('about', about),
    path('disclaimer', disclaimer),
    path('createpost', CreatePost.as_view(), name='add_post'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='duas-detail'),
    path('tag/<slug>', TagIndexView.as_view(), name='post_tag'),
    path('PrivacyPolicy', PrivacyPolicy),
    path('search', search),
    path('contact', Contactus.as_view(), name="contact"),
    path('category/<str:Category>', CatListView.as_view(), name="category")

]
