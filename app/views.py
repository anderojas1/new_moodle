from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from .forms import LeaderTeacherForm
from .models import LeaderTeacher
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