from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Persona(models.Model):
	opt_sexo = ((0, 'Masculino'), (1, 'Femenino'))
	patron_numero_cedula = RegexValidator(regex = r'^\+?1?\d{9, 15}$')
	patron_numero_celular = RegexValidator(regex = r'^\+?\?\d{9, 10}$')
	patron_solo_string = RegexValidator(regex='^[a-zA-Z]*$')
	cedula = models.CharField(primary_key=True, max_length=30, validators=[patron_numero_cedula])
	nombre = models.CharField(max_length=30, validators=[patron_solo_string])
	apellidos = models.CharField(max_length=40, validators=[patron_solo_string])
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

class InstitucionEducativa(models.Model):
	opt_zona = ((0, 'Urbana'), (1, 'Urbana marginal'), (2, 'Rural'), (3, 'Rural de difícil acceso'))
	opt_modalidad = ((0, 'Académica'),(1, 'Ténica'), (2, 'Agropecuaria'),(3, 'Comercial'),(4, 'Promoción Social')
		,(5, 'Finanzas'),(6, 'Administación'),(7, 'Ecología'),(8, 'Medio Ambiente'),(9, 'Industrial'),(10, 'Informática'),
		(11, 'Minería'),(12, 'Salud'),(13, 'Recreación'),(14, 'Turismo'),(15, 'Deporte'), (16, 'Otro'))
	codigo = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=100)
	sede = models.CharField(max_length=100)
	municipio = models.CharField(max_length=50)
	zona = models.PositiveSmallIntegerField(choices=opt_zona)
	modalidad = models.PositiveSmallIntegerField(choices=opt_modalidad)
	slug = models.SlugField()

	def __str__(self):
		return self.nombre + " Sede: " + self.sede

	def save (self, *args, **kwargs):
		self.slug = self.codigo
		super(InstitucionEducativa, self).save(*args, **kwargs)

class SecretariaEducacion(models.Model):
	opt_entidad = ((0, 'Municipal'),(1, 'Departamental'))
	codigo = models.CharField(max_length=15, primary_key=True)
	entidad = models.PositiveSmallIntegerField(choices=opt_entidad)
	nombre = models.CharField(max_length=50)
	slug = models.SlugField()

	class Meta:
		ordering = ['nombre']

	def __str__(self):
		return nombre

	def save(self, *args, **kwargs):
		self.slug = self.codigo
		super(InstitucionEducativa, self).save(*args, **kwargs)