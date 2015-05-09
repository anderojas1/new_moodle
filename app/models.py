from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Persona(models.Model):
	opt_sexo = ((0, 'Masculino'), (1, 'Femenino'))
	patron_numero_cedula = RegexValidator(regex = r'^\+?1?\d{9, 15}$')
	patron_numero_celular = RegexValidator(regex = r'^\+?\?\d{9, 10}$')
	cedula = models.CharField(primary_key=True, max_length=30, validators=[patron_numero_cedula])
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=40)
	fecha_nacimiento = models.DateField()
	sexo = models.PositiveSmallIntegerField(choices=opt_sexo)
	email = models.EmailField(max_length=50)
	celular = models.CharField(validators=[patron_numero_celular], max_length=10)
	fecha_registro = models.DateField(auto_now_add=True)
	slug = models.SlugField(null=True)

	def getSexo(self):
		if self.sexo == 0:
			return 'Masculino'
		else:
			return 'Femenino'


class LeaderTeacher(Persona):
	opt_nivel_estudio = ((0, 'Bachillerato'), (1, 'Licenciatura'),(2, 'Especialización'), (3, 'Maestría'), (4, 'Doctorado'))
	institucion = models.CharField(max_length=60)
	nivel_estudio = models.PositiveSmallIntegerField(choices=opt_nivel_estudio)

	class Meta:
		ordering = ['fecha_registro']

	def __str__(self):
		return self.nombre + " " + self.apellidos

	def save(self, *args, **kwargs):
		self.slug = self.cedula
		super(LeaderTeacher, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return ('consultar_LT', [self.slug])

	@models.permalink
	def get_update_url(self):
		return ('actualizar_LT', [self.slug])

	@models.permalink
	def get_delete_url(self):
		return ('borrar_LT', [self.slug])
