from django import forms
from .models import LeaderTeacher, Matricula, Cohorte, Curso, Area, Usuario, Actividad, Ternaria

class LeaderTeacherForm(forms.ModelForm):
	class Meta:
		model = LeaderTeacher
		fields = ('cedula', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'email', 'celular',
			'institucion', 'nivel_estudio')

#+--------------------------------------------------+
#+                  CODIGO NUEVO                    +
#+--------------------------------------------------+
#+--------------------------------------------------+
#+                  CLASE MATRICULA                 +
#+--------------------------------------------------+

class MatriculaForm(forms.ModelForm):
	class Meta:
		model = Matricula
		fields = ('identificacion_leader_teacher', 'identificacion_curso', 'estado_matricula')

#+--------------------------------------------------+
#+                  CLASE COHORTE                   +
#+--------------------------------------------------+
class CohorteForm(forms.ModelForm):
	class Meta:
		model = Cohorte
		fields = ('numero_cohorte', 'semestre', 'fecha_inicio', 'fecha_fin')

#+--------------------------------------------------+
#+                  CLASE CURSO                     +
#+--------------------------------------------------+
class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = ('codigo_curso', 'nombre', 'descripcion')

#+--------------------------------------------------+
#+                  CLASE AREA                      +
#+--------------------------------------------------+
class AreaForm(forms.ModelForm):
	class Meta:
		model = Area
		fields = ('codigo_area', 'nombre', 'descripcion')

#+--------------------------------------------------+
#+                  CLASE USUARIO                   +
#+--------------------------------------------------+
class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('usuario', 'contrasena', 'perfil')

#+--------------------------------------------------+
#+                  CLASE ACTIVIDAD                 +
#+--------------------------------------------------+
class ActividadForm(forms.ModelForm):
	class Meta:
		model = Actividad
		fields = ('codigo', 'titulo', 'descripcion', 'porcentaje', 'fecha_inicio', 'fecha_cierre')

#+--------------------------------------------------+
#+                  CLASE TERNARIA                  +
#+--------------------------------------------------+
class TernariaForm(forms.ModelForm):
	class Meta:
		model = Ternaria
		fields = ('identificador', 'leader_teacher', 'actividad', 'cohorte', 'nota')