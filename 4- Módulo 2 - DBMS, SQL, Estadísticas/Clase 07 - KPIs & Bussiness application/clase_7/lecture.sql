select count(alumno.idAlumno), cohorte.codigo, carrera.nombre
from alumno
join cohorte
on cohorte.idCohorte = alumno.idCohorte
join carrera
on carrera.idCarrera = cohorte.idCarrera
group by cohorte.codigo, carrera.nombre
having carrera.nombre = 'Data Science';


select distinct instructor.nombre, instructor.apellido, carrera.nombre
from instructor
join cohorte
on cohorte.idInstructor = instructor.idInstructor
join carrera
on cohorte.idCarrera = carrera.idCarrera;

select nombre, apellido, concat(nombre, ' ', apellido) as nombre_completo from instructor;


select nombre from alumno;