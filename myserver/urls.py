"""myserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', views.predict_view, name='product'),
    path('success', views.success, name = 'success'),
    path('',views.main_page, name="main_page"),
    path('last_result/',views.previous_result,name= 'result'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
