from django import forms
from .models import LeaderTeacher

class LeaderTeacherForm(forms.ModelForm):
	class Meta:
		model = LeaderTeacher
		fields = ('cedula', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'email', 'celular',
			'institucion', 'nivel_estudio')