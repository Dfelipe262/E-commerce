"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from produtos.views import produto_criar, produto_editar, produto_listar, produto_remover,pagina_inicial, produto_detalhes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pagina_inicial,name='pagina_inicial'),
    path('produto/',produto_criar,name='produto_criar'),
    path('produto/editar/<int:id>/', produto_editar, name='produto_editar'),
    path('produto/remover/<int:id>/',produto_remover,name='produto_remover'),
    path('produto/detalhes/<int:id>/',produto_detalhes,name='produto_detalhes'),
    path('produto/listar',produto_listar,name='produto_listar'),

]
