from django.contrib import admin
from .models import Estudiante, Curso, Profesor, Direccion, EstudianteCurso, ProfesorCurso

# Register your models here.
admin.site.register(Curso)
admin.site.register(Direccion)
admin.site.register(Estudiante)
admin.site.register(EstudianteCurso)
admin.site.register(Profesor)
admin.site.register(ProfesorCurso)
