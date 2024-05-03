#En este archivo voy a practicar casi todos los conocimmientos adquiridos

Usuario = input('escribe tu usuario')
Contra = int(input('Escribe tu Contraseña'))

'''if Usuario == 'Estudiante' or Usuario == 'Profesor':
    print("Sólo puedes ver la sección en la que estás matriculado")
else : 
    print('Eres del equipo administrativo')

if not (Usuario == 'Profesor' or 'Estudiante' or 'Director'):
    print('Eres coordinador')'''

# A evaluar varias condicioanles en Python se usa ELIF

if Usuario == 'Estudiante' and Contra == 12345678:
    print('Eres un estudiante, solo tienes acceso a tu grado')
elif Usuario == 'Docente' and Contra == 123456789:
    print('Eres docente, tienes acceso a todos los estudiantes de tu curso')
else:
    print('Acceso denegado')







