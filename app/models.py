from django.db import models

# Create your models here.
class Persona(models.Model):
	opt_sexo = ((0, 'Masculino'), (1, 'Femenino'))
	cedula = models.CharField(primary_key=True, max_length=30)
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=40)
	sexo = models.PositiveSmallIntegerField(choices=opt_sexo)
	fecha_registro = models.DateField(auto_now_add=True)
	slug = models.SlugField(null=True)

	def getSexo(self):
		if self.sexo == 0:
			return 'Masculino'
		else:
			return 'Femenino'


class LeaderTeacher(Persona):
	institucion = models.CharField(max_length=60)

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
