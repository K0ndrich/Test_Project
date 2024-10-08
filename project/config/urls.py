"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# django
from django.contrib import admin
from django.urls import path

# django_rest
from rest_framework.routers import SimpleRouter

# my_project
from orders.views import orders_page, OrderView , orders_app


router = SimpleRouter()
router.register("api/orders/", OrderView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", orders_page),
    path("orders_page/", orders_app),
]

# добавление путей роутера django_rest к глобальным url путям
urlpatterns += router.urls
