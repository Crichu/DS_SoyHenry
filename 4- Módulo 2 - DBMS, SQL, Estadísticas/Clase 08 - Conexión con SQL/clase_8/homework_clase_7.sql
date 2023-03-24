-- 1. ¿Cuántas carreras tiene Henry?

Select count(idCarrera) as Cantidad_de_carreras from carrera;

-- 2. ¿Cuantos alumnos hay en total?
select count(idAlumno) as cantidad_de_alumnos from alumno;


-- 3. ¿Cuantos alumnos tiene cada cohorte?
select count(alumno.idAlumno) as cantidad_de_alumnos_por_cohorte,
cohorte.codigo
from alumno
join cohorte
on cohorte.idCohorte = alumno.idCohorte
group by alumno.idCohorte;

-- 4. Confecciona un listado de los alumnos ordenado por los últimos alumnos que ingresaron, 
-- con nombre y apellido en un solo campo.
select concat(nombre, ' ', apellido) as nombre_completo,
fechaIngreso
from alumno
order by fechaIngreso desc;


-- 5. ¿Cual es el nombre del primer alumno que ingreso a Henry?
-- 6. ¿En que fecha ingreso?

select concat(nombre, ' ', apellido) as nombre_completo,
fechaIngreso
from alumno
order by fechaIngreso
limit 1;


-- 7. ¿Cual es el nombre del ultimo alumno que ingreso a Henry?
select concat(nombre, ' ', apellido) as nombre_completo,
fechaIngreso
from alumno
order by fechaIngreso desc
limit 1;


-- 8. La función YEAR le permite extraer el año de un campo date, 
-- utilice esta función y especifique cuantos alumnos ingresarona a Henry por año.
select count(idAlumno), year(fechaIngreso)
from alumno
group by year(fechaIngreso)
order by year(fechaIngreso);


-- 9. ¿Cuantos alumnos ingresaron por semana a henry?, indique también el año. WEEKOFYEAR()
select count(idAlumno), weekofyear(fechaIngreso), year(fechaIngreso)
from alumno
group by weekofyear(fechaIngreso), year(fechaIngreso)
order by year(fechaIngreso), weekofyear(fechaIngreso);

-- 10. ¿En que años ingresaron más de 20 alumnos?
select year(fechaIngreso), count(idAlumno)
from alumno
group by year(fechaIngreso)
having count(idAlumno) > 20
order by year(fechaIngreso);

-- 11. Investigue las funciones TIMESTAMPDIFF() y CURDATE(). 
-- ¿Podría utilizarlas para saber cual es la edad de los instructores?. 
-- ¿Como podrías verificar si la función cálcula años completos? Utiliza DATE_ADD().

select nombre, apellido, fechaNacimiento,
timestampdiff(year, fechaNacimiento, curdate()) as edad,
date_add(fechaNacimiento, INTERVAL timestampdiff(year, fechaNacimiento, curdate()) YEAR)
from instructor;

-- Cálcula:
-- - La edad de cada alumno.
select nombre, apellido, fechaNacimiento,
timestampdiff(year, fechaNacimiento, curdate()) as edad
from alumno;

-- - La edad promedio de los alumnos de henry.
select avg( timestampdiff(year, fechaNacimiento, curdate()) ) as "Edad promedio" from alumno;

-- alumno con fecha de nacimiento errónea
select * from alumno
where fechaNacimiento is not null
order by fechaNacimiento
limit 1;

-- - La edad promedio de los alumnos de cada cohorte.
select avg( timestampdiff(year, alumno.fechaNacimiento, curdate()) ) as "Edad promedio",
cohorte.codigo
from alumno
join cohorte
on cohorte.idCohorte = alumno.idCohorte
group by cohorte.codigo;

-- Elabora un listado de los alumnos que superan la edad promedio de Henry.
select nombre, apellido,
timestampdiff(year, alumno.fechaNacimiento, curdate()) as edad
from alumno
where timestampdiff(year, alumno.fechaNacimiento, curdate()) > (select avg( timestampdiff(year, alumno.fechaNacimiento, curdate()) ) from alumno);