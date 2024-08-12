from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField(blank=True, null=True)
    profesor = models.ForeignKey('Profesor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.OneToOneField('Estudiante', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'direccion'


class Estudiante(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateField(blank=True, null=True)
    modificacion_registro = models.DateField(blank=True, null=True)
    creado_por = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


class EstudianteCurso(models.Model):
    estudiante = models.OneToOneField(Estudiante, models.DO_NOTHING, primary_key=True)  # The composite primary key (estudiante_id, curso_codigo) found, that is not supported. The first column is selected.
    curso_codigo = models.ForeignKey(Curso, models.DO_NOTHING, db_column='curso_codigo')

    class Meta:
        managed = False
        db_table = 'estudiante_curso'
        unique_together = (('estudiante', 'curso_codigo'),)


class Profesor(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateField(blank=True, null=True)
    modificacion_registro = models.DateField(blank=True, null=True)
    creado_por = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor'


class ProfesorCurso(models.Model):
    profesor = models.OneToOneField(Profesor, models.DO_NOTHING, primary_key=True)  # The composite primary key (profesor_id, curso_codigo) found, that is not supported. The first column is selected.
    curso_codigo = models.ForeignKey(Curso, models.DO_NOTHING, db_column='curso_codigo')

    class Meta:
        managed = False
        db_table = 'profesor_curso'
        unique_together = (('profesor', 'curso_codigo'),)