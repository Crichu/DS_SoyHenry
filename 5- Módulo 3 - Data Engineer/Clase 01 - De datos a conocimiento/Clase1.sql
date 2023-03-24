#Módulo 3 - Clase 1

drop DATABASE henry_m3;
create DATABASE henry;
use henry;

drop table canal_venta;

CREATE TABLE if not EXISTS canal_venta
(
IdCanalDeVenta INTEGER,
Descripción varchar (100)
)
default char set=utf8mb4 
collate=utf8mb4_spanish_ci;

LOAD DATA INFILE 'CanalDeVenta.csv'
INTO TABLE canal_venta
FIELDS TERMINATED BY ';'
enclosed by ''
LINES TERMINATED BY '\n'
ignore 1 lines
(IdCanalDeVenta, Descripción);


drop table clientes;


create TABLE clientes
(
IdCliente integer,
Provincia VARCHAR(150),
Nombre_Apellido varchar(150),
Domicilio varchar (150),
Teléfono varchar (150),
Edad integer,
Localidad varchar (150),
X varchar(50),
Y varchar (50),
Fecha_Alta date,
Usuario_Alta VARCHAR(50),
Fecha_Última_Modificación DATE,
Usuario_Última_Modificación VARCHAR(50),
Marca_Baja integer,
Col10 varchar(20)
)
default char set=utf8mb4 
collate=utf8mb4_spanish_ci;

LOAD DATA INFILE 'Clientes.csv'
INTO TABLE clientes
FIELDS TERMINATED BY ';'
enclosed by ''
LINES TERMINATED BY '\n'
ignore 1 lines
(IdCliente,
Provincia,
Nombre_Apellido,
Domicilio,
Teléfono,
Edad,
Localidad,
X,
Y,
Fecha_Alta,
Usuario_Alta,
Fecha_Última_Modificación,
Usuario_Última_Modificación,
Marca_Baja,
Col10);

DROP table venta;

create TABLE venta
(
IdVenta integer,
Fecha DATE,
Fecha_Entrega date,
IdCanal INTEGER,
IdCliente integer,
IdSucursal integer,
IdEmpleado integer,
IdProducto integer,
Precio VARCHAR(10),
Cantidad varchar(10)
)
default char set=utf8mb4 
collate=utf8mb4_spanish_ci;


LOAD DATA INFILE 'Venta.csv'
INTO TABLE venta
FIELDS TERMINATED BY ','
enclosed by ''
LINES TERMINATED BY '\n'
ignore 1 lines;

SELECT count(*) from venta;

