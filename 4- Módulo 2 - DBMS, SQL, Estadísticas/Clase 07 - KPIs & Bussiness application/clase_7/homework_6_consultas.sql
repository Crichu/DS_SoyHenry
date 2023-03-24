select * from alumno;


select * from cohorte where idCohorte in (1245, 1246);

delete from cohorte where idCohorte in (1245, 1246);


select * from cohorte where idCohorte = 1243;


select * from alumno where idAlumno = 165;

update alumno set apellido = 'Ramírez' where idAlumno = 165;

update cohorte set fechaInicio = '2023-05-16' where idCohorte = 1243;




select idAlumno, cedulaIdentidad, nombre, apellido, fechaNacimiento, fechaIngreso, idCohorte
from alumno where idCohorte = 1235
and year(fechaIngreso) = 2019;

select distinct instructor.idInstructor, instructor.cedulaIdentidad,
instructor.nombre, instructor.apellido, instructor.fechaNacimiento,
instructor.fechaIncorporacion 
from cohorte 
join instructor
on instructor.idInstructor = cohorte.idInstructor
where cohorte.idCarrera = 1;


select * from carrera;








SELECT alumno.nombre, alumno.apellido, alumno.fechaNacimiento, carrera.nombre
FROM alumno
INNER JOIN cohorte
ON cohorte.idCohorte = alumno.idCohorte
INNER JOIN carrera
ON carrera.idCarrera = cohorte.idCarrera
where carrera.nombre like 'Full Stack Developer';


SELECT alumno.nombre, alumno.apellido, alumno.fechaNacimiento, carrera.nombre
FROM alumno
INNER JOIN cohorte
ON cohorte.idCohorte = alumno.idCohorte
INNER JOIN carrera
ON carrera.idCarrera = cohorte.idCarrera
where carrera.nombre not like 'Data Science';

SELECT alumno.nombre, alumno.apellido, alumno.fechaNacimiento, carrera.nombre
FROM alumno
INNER JOIN cohorte
ON cohorte.idCohorte = alumno.idCohorte
INNER JOIN carrera
ON carrera.idCarrera = cohorte.idCarrera
where carrera.idCarrera = 1;