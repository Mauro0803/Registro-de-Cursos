from .models import Curso, Profesor, Direccion, Estudiante, ProfesorCurso, EstudianteCurso

def crear_curso(nuevoCodigo, nuevoNombre):
    nuevo_curso = Curso(codigo = nuevoCodigo, nombre = nuevoNombre)
    nuevo_curso.save()
    print('Curso creado correctamente')

def crear_profesor(nuevoRut, nuevoNombre, nuevoApellido, estadoActivo, creadoPor):
    nuevo_profesor = Profesor(rut = nuevoRut, nombre = nuevoNombre, apellido = nuevoApellido, activo = estadoActivo, creado_por = creadoPor)
    nuevo_profesor.save()
    print('Profesor creado correctamente')

def crear_estudiante(nuevoRut, nuevoNombre, nuevoApellido, nuevaFechaNac, estadoActivo, creadoPor):
    nuevo_estudiante = Estudiante(rut = nuevoRut, nombre = nuevoNombre, apellido = nuevoApellido, fecha_nac = nuevaFechaNac, activo = estadoActivo, creado_por = creadoPor)
    nuevo_estudiante.save()
    print('Estudiante creado correctamente')

def crear_direccion(nuevaCalle, nuevoNumero, nuevoDpto, nuevaComuna, nuevaCiudad, nuevaRegion, idEstudiante):
    nueva_direccion = Direccion(calle = nuevaCalle, numero = nuevoNumero, dpto = nuevoDpto, comuna = nuevaComuna, ciudad = nuevaCiudad, region = nuevaRegion, estudiante_id = idEstudiante)
    nueva_direccion.save()
    print('Direccion creada correctamente')

def obtiene_estudiante(rut_estudiante):
    estudiante = Estudiante.objects.get(rut = rut_estudiante)
    return estudiante.nombre

def obtiene_profesor(rut_profesor):
    profesor = Profesor.objects.get(rut = rut_profesor)
    return profesor.nombre

def obtiene_curso(codigo_a_obtener):
    curso = Curso.objects.get(codigo = codigo_a_obtener)
    return curso.nombre

def agrega_profesor_a_curso(rut_profesor, codigo_curso):
    profesor = Profesor.objects.get(rut = rut_profesor)
    curso = Curso.objects.get(codigo = codigo_curso)

    if ProfesorCurso.objects.filter(profesor=profesor, curso_codigo=curso).exists():
        return 'El Profesor ya está en el Curso'

    ProfesorCurso.objects.create(profesor=profesor, curso_codigo=curso)
    return 'Profesor se añadió al curso correctamente'

def agrega_cursos_a_estudiante(rut_estudiante, codigo_curso):
    estudiante = Estudiante.objects.get(rut = rut_estudiante)
    curso = Curso.objects.get(codigo = codigo_curso)

    if EstudianteCurso.objects.filter(estudiante=estudiante, curso_codigo=curso).exists():
        return 'El Estudiante ya está en el Curso'

    EstudianteCurso.objects.create(estudiante=estudiante, curso_codigo=curso)
    return 'Estudiante se añadió al curso correctamente'

def imprime_estudiante_cursos(id_estudiante):
    estudiante = Estudiante.objects.get(rut=id_estudiante)
    estudiante_cursos = EstudianteCurso.objects.filter(estudiante=id_estudiante)
    cursos_del_estudiante = [ec.curso_codigo for ec in estudiante_cursos]

    print(f"Estudiante: {estudiante.nombre.strip()} {estudiante.apellido}\nCursos:")

    for curso in cursos_del_estudiante:
        print(f"- {curso.nombre}")
    