"""
Copia URL Configuration

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
from app.views import CrearMatricula, EditarMatricula, DetallesMatricula, BorrarMatricula, ListarMatricula
from app.views import CrearCohorte, EditarCohorte, DetallesCohorte, BorrarCohorte, ListarCohorte
from app.views import CrearCurso, EditarCurso, DetallesCurso, BorrarCurso, ListarCurso
from app.views import CrearArea, EditarArea, DetallesArea, BorrarArea, ListarArea
from app.views import CrearUsuario, EditarUsuario, DetallesUsuario, BorrarUsuario, ListarUsuario
from app.views import CrearActividad, EditarActividad, DetallesActividad, BorrarActividad, ListarActividad
from app.views import CrearTernaria, EditarTernaria, DetallesTernaria, BorrarTernaria, ListarTernaria
from app.views import CrearHistorialAcademico, EditarHistorialAcademico, DetallesHistorialAcademico,BorrarHistorialAcademico, ListarHistorialAcademico
from app.views import CrearMaster, ListarMaster, EditarMaster, DetallesMaster, BorrarMaster
from app.views import CrearSecretariaEducacion, BorrarSecretariaEducacion, ListarSecretariaEducacion, DetallesSecretariaEducacion, EditarSecretariaEducacion
from app.views import secretaria


leaderteacher_url = patterns ('',
	url(r'^registrar$', CrearLeader.as_view(), name='crear_leader'),
    url(r'^listados$', ListarLeader.as_view(), name='listar_LT'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarLeader.as_view(), name='editar_LT'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesLeader.as_view(), name='consultar_LT'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarLeader.as_view(), name='eliminar_LT'),
)


##Url master teacher

masterteacher_url = patterns ('',
    url(r'^registrar$', CrearMaster.as_view(), name='crear_master'),
    url(r'^listados$', ListarMaster.as_view(), name='listar_MT'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarMaster.as_view(), name='editar_MT'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesMaster.as_view(), name='consultar_MT'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarMaster.as_view(), name='eliminar_MT')
)

#+--------------------------------------------------+
#+                  CODIGO NUEVO                    +
#+--------------------------------------------------+
#+--------------------------------------------------+
#+                  CLASE MATRICULA                 +
#+--------------------------------------------------+
matricula_url = patterns ('',
    url(r'^registrar$', CrearMatricula.as_view(), name='crear_matricula'),
    url(r'^listados$', ListarMatricula.as_view(), name='listar_matricula'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarMatricula.as_view(), name='editar_matricula'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesMatricula.as_view(), name='consultar_matricula'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarMatricula.as_view(), name='eliminar_matricula'),
)

#+--------------------------------------------------+
#+                  CLASE COHORTE                   +
#+--------------------------------------------------+
cohorte_url = patterns ('',
    url(r'^registrar$', CrearCohorte.as_view(), name='crear_cohorte'),
    url(r'^listados$', ListarCohorte.as_view(), name='listar_cohorte'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarCohorte.as_view(), name='editar_cohorte'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesCohorte.as_view(), name='consultar_cohorte'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarCohorte.as_view(), name='eliminar_cohorte'),
)

#+--------------------------------------------------+
#+                  CLASE CURSO                     +
#+--------------------------------------------------+
curso_url = patterns ('',
    url(r'^registrar$', CrearCurso.as_view(), name='crear_curso'),
    url(r'^listados$', ListarCurso.as_view(), name='listar_curso'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarCurso.as_view(), name='editar_curso'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesCurso.as_view(), name='consultar_curso'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarCurso.as_view(), name='eliminar_curso'),
)

#+--------------------------------------------------+
#+                  CLASE AREA                      +
#+--------------------------------------------------+
area_url = patterns ('',
    url(r'^registrar$', CrearArea.as_view(), name='crear_area'),
    url(r'^listados$', ListarArea.as_view(), name='listar_area'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarArea.as_view(), name='editar_area'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesArea.as_view(), name='consultar_area'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarArea.as_view(), name='eliminar_area'),
)

#+--------------------------------------------------+
#+                  CLASE USUARIO                   +
#+--------------------------------------------------+
usuario_url = patterns ('',
    url(r'^registrar$', CrearUsuario.as_view(), name='crear_usuario'),
    url(r'^listados$', ListarUsuario.as_view(), name='listar_usuario'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarUsuario.as_view(), name='editar_usuario'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesUsuario.as_view(), name='consultar_usuario'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarUsuario.as_view(), name='eliminar_usuario'))

#+--------------------------------------------------+
#+                  CLASE ACTIVIDAD                 +
#+--------------------------------------------------+
actividad_url = patterns ('',
    url(r'^registrar$', CrearActividad.as_view(), name='crear_actividad'),
    url(r'^listados$', ListarActividad.as_view(), name='listar_actividad'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarActividad.as_view(), name='editar_actividad'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesActividad.as_view(), name='consultar_actividad'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarActividad.as_view(), name='eliminar_actividad'))

#+--------------------------------------------------+
#+                  CLASE TERNARIA                  +
#+--------------------------------------------------+
ternaria_url = patterns ('',
    url(r'^registrar$', CrearTernaria.as_view(), name='crear_ternaria'),
    url(r'^listados$', ListarTernaria.as_view(), name='listar_ternaria'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarTernaria.as_view(), name='editar_ternaria'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesTernaria.as_view(), name='consultar_ternaria'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarTernaria.as_view(), name='eliminar_ternaria'))

#+--------------------------------------------------+
#+            CLASE HISTORIALACADEMICO              +
#+--------------------------------------------------+
historialacademico_url = patterns ('',
    url(r'^registrar$', CrearHistorialAcademico.as_view(), name='crear_historialacademico'),
    url(r'^listados$', ListarHistorialAcademico.as_view(), name='listar_historialacademico'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarHistorialAcademico.as_view(), name='editar_historialacademico'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesHistorialAcademico.as_view(), name='consultar_historialacademico'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarHistorialAcademico.as_view(), name='eliminar_historialacademico'))

secretaria_url = patterns ('',
    url(r'^lista$', secretaria, name='lista_secretaria'),
    url(r'^registrar$', CrearSecretariaEducacion.as_view(), name='crear_secretaria'),
    url(r'^listados$', ListarSecretariaEducacion.as_view(), name='listar_secretarias'),
    url(r'^(?P<slug>[\w-]+)/actualizar$', EditarSecretariaEducacion.as_view(), name='editar_secretaria'),
    url(r'^(?P<slug>[\w-]+)/consultar$', DetallesSecretariaEducacion.as_view(), name='consultar_secretaria'),
    url(r'^(?P<slug>[\w-]+)/eliminar$', BorrarSecretariaEducacion.as_view(), name='eliminar_secretaria')
)


urlpatterns = patterns ('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^leader/', include(leaderteacher_url)),
    url(r'^secretaria/', include(secretaria_url)),
    url(r'^matricula/', include(matricula_url)),
    url(r'^cohorte/', include(cohorte_url)),
    url(r'^curso/', include(curso_url)),
    url(r'^area/', include(area_url)),
    url(r'^actividad/', include(actividad_url)),
    url(r'^ternaria/', include(ternaria_url)),
    url(r'^historial_academico/', include(historialacademico_url)),
    url(r'^usuario/', include(usuario_url)),
    url(r'^master/', include(masterteacher_url)),
    url(r'^secretaria/', include(secretaria_url)),
)
