"""copia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from app.views import CrearLeader, EditarLeader, DetallesLeader, BorrarLeader, ListarLeader

leaderteacher_url = patterns ('',
	url(r'^registrar$', CrearLeader.as_view(), name='crear_leader'),
    url(r'^listados$', ListarLeader.as_view(), name='listar_LT'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarLeader.as_view(), name='editar_LT'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesLeader.as_view(), name='consultar_LT'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarLeader.as_view(), name='eliminar_LT'),
)

urlpatterns = patterns ('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^leader/', include(leaderteacher_url)),
)
