#<p>11) ¿Cuál es el año con la mayor cantidad de productos vendidos? Responder con número de año. Ejemplo: 2024 </p>
select year(Fecha), sum(Cantidad) from venta
GROUP BY year(Fecha)
order by sum(Cantidad) desc;

#12) ¿Cuál es el canal de venta que tiene la segunda posición en cantidad de ventas en 2020? </p>
select venta.IdCanal, canal_venta.Canal, sum(venta.Cantidad) from venta
join canal_venta on canal_venta.IdCanal = venta.IdCanal
where year(Fecha) = 2020
GROUP BY IdCanal
order by sum(Cantidad) desc
limit 2;


#13) ¿Cuál es el Id del empleado que menor cantidad de productos vendió en el histórico de ventas de la empresa?
select IdEmpleado, sum(Cantidad) from venta
Group by IdEmpleado
order by sum(Cantidad) asc;


#14) Se define el tiempo de entrega como el tiempo en días transcurrido entre que se realiza la compra y se efectua la entrega. 
#Para analizar mejoras en el servicio, la dirección desea saber: cuál es el año con el promedio más alto de este tiempo de entrega. 
#(Fecha = Fecha de venta; Fecha_Entrega = Fecha de entrega)
select year(Fecha), avg(timestampdiff(day,Fecha,Fecha_Entrega)) as Entrega from venta
GROUP BY year(Fecha)
order by Entrega desc;


#15) ¿Cuál es el promedio de precio de los productos cuyo concepto comienza con la letra C?
select avg(Precio) from producto
where Concepto like 'C%';

#16) ¿Cuantos productos tienen la palabra " CD " (mayúsculas o minúsculas) 
#en alguna parte de su descripción (Concepto = Descripción del Producto) y su precio es mayor a 500?
###ESTE SCRIPT NO ME FUNCIONÓ. LO SAQUÉ DE TABLA
select count(IDProducto) from producto
where Concepto like ' CD ' 
and producto.Precio > 500;


#17) ¿Cuál es el id del Producto cuyo nombre es EPSON COPYFAX 2000?
select IDProducto, Concepto from producto
where Concepto = 'EPSON COPYFAX 2000';


#18) Cual fue el mes (Fecha = Fecha de Venta) con menor venta (Venta = Precio*Cantidad) de la sucursal 13 para el año 2015 ?
Select IDSucursal, DATE_FORMAT( Fecha,'%Y%m'), sum(Precio*Cantidad) as Ventas from venta
where IDSucursal = 13 and DATE_FORMAT( Fecha,'%Y%m') like '2015%'
group by (DATE_FORMAT( Fecha,'%Y%m'))
order by Ventas asc;

