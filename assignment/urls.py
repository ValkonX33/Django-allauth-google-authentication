"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
# from django.conf.urls import url
from django.conf import settings
from loginPage import views
# from views import googleLogin

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    # path('form/', TemplateView.as_view(template_name="form.html"), name='form'),
    path('form/', views.form, name='form'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    # path('social-auth/', include('social_djnago.urls', namespace='social')),
    # path('', include('googleLogin.urls')),
    # path('google', views.googleLogin, name="googleLogin" ),
    # path('social/signup/', views.signup_redirect, name="signup_redirect" ),
    #  path('accounts/google/login/', views.dashboard_view, name="dashboard_view" ),
]