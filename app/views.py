from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from .forms import LeaderTeacherForm, MatriculaForm, CohorteForm, CursoForm, AreaForm, UsuarioForm, ActividadForm, TernariaForm, HistorialAcademicoForm
from .models import LeaderTeacher, Matricula, Cohorte, Curso, Area, Usuario, Actividad, Ternaria, HistorialAcademico
# Create your views here.

class LeaderMixin(object):
	model = LeaderTeacher
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'LeaderTeacher'})
		return kwargs

class LeaderFormMixin(LeaderMixin):
	form_class = LeaderTeacherForm
	template_name = 'app/object_form.html'

class DetallesLeader(LeaderMixin, DetailView):
    pass

class CrearLeader(LeaderFormMixin, CreateView):
    pass

class EditarLeader(LeaderFormMixin, UpdateView):
    pass

class BorrarLeader(LeaderMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return reverse_lazy('listar_LT')

class ListarLeader(LeaderMixin, ListView):
	template_name = 'app/listado_lt.html'

#+--------------------------------------------------+
#+                  CODIGO NUEVO                    +
#+--------------------------------------------------+
#+--------------------------------------------------+
#+                  CLASE MATRICULA                 +
#+--------------------------------------------------+
class MatriculaMixin(object):
	model = Matricula
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Matricula'})
		return kwargs

class MatriculaFormMixin(MatriculaMixin):
	form_class = MatriculaForm
	template_name = 'app/object_form.html'

class DetallesMatricula(MatriculaMixin, DetailView):
    pass

class CrearMatricula(MatriculaFormMixin, CreateView):
    pass

class EditarMatricula(MatriculaFormMixin, UpdateView):
    pass

class BorrarMatricula(MatriculaMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return reverse_lazy('listar_matricula')

class ListarMatricula(MatriculaMixin, ListView):
	template_name = 'app/listado_matricula.html'

#+--------------------------------------------------+
#+                  CLASE COHORTE                   +
#+--------------------------------------------------+
class CohorteMixin(object):
	model = Cohorte
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Cohorte'})
		return kwargs

class CohorteFormMixin(CohorteMixin):
	form_class = CohorteForm
	template_name = 'app/object_form.html'

class DetallesCohorte(CohorteMixin, DetailView):
    pass

class CrearCohorte(CohorteFormMixin, CreateView):
    pass

class EditarCohorte(CohorteFormMixin, UpdateView):
    pass

class BorrarCohorte(CohorteMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return reverse_lazy('listar_cohorte')

class ListarCohorte(CohorteMixin, ListView):
	template_name = 'app/listado_cohorte.html'

#+--------------------------------------------------+
#+                  CLASE CURSO                     +
#+--------------------------------------------------+
class CursoMixin(object):
	model = Curso
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Curso'})
		return kwargs

class CursoFormMixin(CursoMixin):
	form_class = CursoForm
	template_name = 'app/object_form.html'

class DetallesCurso(CursoMixin, DetailView):
    pass

class CrearCurso(CursoFormMixin, CreateView):
    pass

class EditarCurso(CursoFormMixin, UpdateView):
    pass

class BorrarCurso(CursoMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return reverse_lazy('listar_curso')

class ListarCurso(CursoMixin, ListView):
	template_name = 'app/listado_curso.html'

#+--------------------------------------------------+
#+                  CLASE AREA                      +
#+--------------------------------------------------+
class AreaMixin(object):
	model = Area
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Area'})
		return kwargs

class AreaFormMixin(AreaMixin):
	form_class = AreaForm
	template_name = 'app/object_form.html'

class DetallesArea(AreaMixin, DetailView):
    pass

class CrearArea(AreaFormMixin, CreateView):
    pass

class EditarArea(AreaFormMixin, UpdateView):
    pass

class BorrarArea(AreaMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return reverse_lazy('listar_area')

class ListarArea(CursoMixin, ListView):
	template_name = 'app/listado_area.html'

#+--------------------------------------------------+
#+                  CLASE USUARIO                   +
#+--------------------------------------------------+
class UsuarioMixin(object):
	model = Usuario
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Usuario'})
		return kwargs

class UsuarioFormMixin(UsuarioMixin):
	form_class = UsuarioForm
	template_name = 'app/object_form.html'

class DetallesUsuario(UsuarioMixin, DetailView):
    pass

class CrearUsuario(UsuarioFormMixin, CreateView):
    pass

class EditarUsuario(UsuarioFormMixin, UpdateView):
    pass

class BorrarUsuario(UsuarioMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return ('listar_usuario')

class ListarUsuario(UsuarioMixin, ListView):
	template_name = 'app/listado_usuario.html'

#+--------------------------------------------------+
#+                  CLASE ACTIVIDAD                 +
#+--------------------------------------------------+
class ActividadMixin(object):
	model = Actividad
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Actividad'})
		return kwargs

class ActividadFormMixin(ActividadMixin):
	form_class = ActividadForm
	template_name = 'app/object_form.html'

class DetallesActividad(ActividadMixin, DetailView):
    pass

class CrearActividad(ActividadFormMixin, CreateView):
    pass

class EditarActividad(ActividadFormMixin, UpdateView):
    pass

class BorrarActividad(ActividadMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return ('listar_actividad')

class ListarActividad(ActividadMixin, ListView):
	template_name = 'app/listado_actividad.html'

#+--------------------------------------------------+
#+                  CLASE TERNARIA                  +
#+--------------------------------------------------+
class TernariaMixin(object):
	model = Ternaria
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Ternaria'})
		return kwargs

class TernariaFormMixin(TernariaMixin):
	form_class = TernariaForm
	template_name = 'app/object_form.html'

class DetallesTernaria(TernariaMixin, DetailView):
    pass

class CrearTernaria(TernariaFormMixin, CreateView):
    pass

class EditarTernaria(TernariaFormMixin, UpdateView):
    pass

class BorrarTernaria(TernariaMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return ('listar_ternaria')

class ListarTernaria(TernariaMixin, ListView):
	template_name = 'app/listado_ternaria.html'

#+--------------------------------------------------+
#+            CLASE HISTORIALACADEMICO              +
#+--------------------------------------------------+
class HistorialAcademicoMixin(object):
	model = HistorialAcademico
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'HistorialAcademico'})
		return kwargs

class HistorialAcademicoFormMixin(HistorialAcademicoMixin):
	form_class = HistorialAcademicoForm
	template_name = 'app/object_form.html'

class DetallesHistorialAcademico(HistorialAcademicoMixin, DetailView):
    pass

class CrearHistorialAcademico(HistorialAcademicoFormMixin, CreateView):
    pass

class EditarHistorialAcademico(HistorialAcademicoFormMixin, UpdateView):
    pass

class BorrarHistorialAcademico(HistorialAcademicoMixin, DeleteView):
	template_name = 'app/object_confirm_delete.html'
	def get_success_url(self):
		return ('listar_historialacademico')

class ListarHistorialAcademico(HistorialAcademicoMixin, ListView):
	template_name = 'app/listado_historialacademico.html'