# <h1 align=center> **Análisis del Mercado de Telecomunicaciones Argentino** </h1>

# <h1 align=center>**`Análisis descriptivo, situación actual y propuesta de oportunidades de crecimiento en el sector de internet`**</h1>

# **Autor: Cristian Biava**

## **Propuesta de trabajo**</h2>

La propuesta es estudiar la evolución y el comportamiento de los servicios de telecomunicación a nivel nacional. Particularmente, enfocado en el mercado de internet. 

La finalidad es identificar oportunidades de crecimiento y poder plantear soluciones personalizadas a los posibles usuarios.

La propuesta incluye:

**`Extracción de datos a traves de un API:`**
Los datos se extrajeron en formato .csv desde la pagina oficial de ENACOM (Ente Nacional de Comunicaciones), institución encargada de promover la inclusión digital en todo el país.
Para esto se hizo uso de la API de la página.

* Tecnologías y librerías utilizadas: Python, Request, Pandas, os


**`ETL y EDA de los datos originales:`** 
Se realizó un análisis exploratorio de los datos, enfocado en el sector de internet, donde se obtuvieron conclusiones en cuanto a la evolución del número de usuarios y las tecnologías más frecuentes.

Así mismo, se detectaron regiones con oportunidades de crecimiento que podrían ser aprovechadas por empresas proveedoras del servicio.

* Tecnologías y librerías utilizadas: Python, Pandas, Matplotlib

**`Desarrollo de un Dashboard interactivo:`** Se desarrolló un dashboard interactivo cuyo propósito es navegar en las diferentes opciones que presentan los Datasets y evaluar distintos escenarios.

* Tecnologías utilizadas: Power BI, Lenguaje DAX, Inclusión de datos a Power BI a través de Python.


## **Trabajo realizado**</h2>

# **`Extracción de datos`**</h3>

Haciendo uso de la librería requests y de la clave de autenticación provista por la página de ENACOM, se desacargaron 16 archivos .csv relacionados con el sector de internet y 14 datasets con información complementaria de otros sectores.

Los mismo se guardaron en la carpeta Datasets de este proyecto.

Más detalles: ['Extracción de datasets.ipynb']()

# **`ETL y EDA de los datos originales`**</h3>

El análisis del sistema de telecomunicaciones se realizó haciendo foco en el sector de Servicios de Internet, con el objetivo de detectar posibles oportunidades de crecimiento. Haciendo hincapié también, en sus características particulares y la evolución de sus tendencias con la finalidad de plantear soluciones de calidad a los potenciales clientes.

Las preguntas que propone responder este análisis son las siguientes:

1) ¿En qué provicias se pueden encontrar oportunidades de inserción temprana en el mercado?

2) ¿Con qué tipo de servicio sería más conveniente ingresar? ¿Cuál es la tendencia en estos distritos? ¿Cuál es la tendencia en los mercados más avanzados?

3) ¿Qué tecnologías se encuentran en uso en los mercados con oportunidad de crecimiento? ¿Cómo es la situación en las regiones más avanzadas?

4) ¿Cuál es la perspectiva de crecimiento a nivel ingresos en el sector?

A continuación, se mencionan las principales conclusiones.

### **Accesos a internet**

Un análisis en la cantidad de accesos por cada 100 hogares evidencia que un crecimiento en los últimos 8 años que duplicó la cantidad de hogares conectados al servicio.

Es importante destacar que el 70% de los hogares ya cuenta con conexión a internet. Un porcentaje relativamente alto que haría pensar que ya es tarde para entrar cómo proveedor del servicio.

[Cantidad de Accesos por cada 100 hogares_Evolución por trimestre](<Imagenes/Cantidad de Accesos por cada 100 hogares_Evolución por trimestre.png>)

Sin embargo, analisis más minucioso a nivel provincial revela que hay distritos con una accesibilidad por debajo del 40% (al 3° trimestre del año 2022), lo cual podría suponer una buena oportunidad de incursionar en estos mercados en una etapa relativamente temprana.

Estas provincias son: Santa Cruz, Formosa, Chaco, Santiago Del Estero y Corrientes. Destacar también que, salvo Santa Cruz, el resto son provincias muy cercanas con lo que se podría simplificar la expansión interprovincial del servicio.

[Cantidad de Accesos por cada 100 hogares_Por Provincia](<Imagenes\Cantidad de Accesos por cada 100 hogares_Por Provincia.png>)

Si se considera la evolución en estas provicias a lo largo del tiempo, ee puede ver que los hogares con acceso a internet están en plena expansión.

En Chaco y Corrientes aumentó al doble. En el caso de Formosa y Santiago Del Estero, más del 400%.

[Cantidad de Accesos por cada 100 hogares_Por Provincias de interes](<Imagenes\Cantidad de Accesos por cada 100 hogares_Por Provincias de interes.png>)


### **Calidad del servicio**

A nivel nacional, el estudio sobre los datos de velocidades señala una tendencia hacia velocidades cada vez mayores (+30 Mbps).

En contrapartida, velocidades por debajo de 30 Mbps son cada vez menos aceptadas por el mercado.

[Cantidad de accesos por Velocidad_Evolución por trimestre](<Imagenes\Cantidad de accesos por Velocidad_Evolución por trimestre.png>)

Así mismo, un zoom en las provincias detectadas con potencial de crecimiento, muestra la misma tendencia en Chaco y Corrientes, en donde se observa un salto pronunciado en la cantidad de accesos a velocidades altas durante el año 2019, pasando de menos de 10.000 accesos a más de 50.000 el caso de Corrientes y más de 80.000 para Chaco en 2022.

Sin embargo, en Formosa y Santiago Del Estero aún no se dio esa explosión y continúan predominando las velocidades bajas.

[Cantidad de accesos por Velocidad_Chaco](<Imagenes\Cantidad de accesos por Velocidad_Chaco.png>)

[Cantidad de accesos por Velocidad_Corrientes](<Imagenes\Cantidad de accesos por Velocidad_Corrientes.png>)

[Cantidad de accesos por Velocidad_Santiago](<Imagenes\Cantidad de accesos por Velocidad_Santiago.png>)

[Cantidad de accesos por Velocidad_Formosa](<Imagenes\Cantidad de accesos por Velocidad_Formosa.png>)

### **Tecnologías**

En línea con lo anterior, el uso de tecnologías de Cable Modem y Fibra Óptica, asociadas a las altas velocidades, va en aumento.

En el caso de la Fibra Óptica se demuestra un aumento significativo de las curva de crecimiento a partir del 2019. Esto guarda relación con lo examinado en el apratado anterior.

[Tecnologías_Evolución por trimestre](<Imagenes\Tecnologías_Evolución por trimestre.png>)

El que sigue es un cuadro comparativo de las tecnologías y los rangos de velocidad que proveen, que se agrega a este informe a modo de referencia.

| Tecnología      | Velocidad (Mbps)            |
| --------------- | --------------------------- |
| ADSL            | 2-24 Mbps                   |
| Cablemódem      | 10-1000 Mbps                |
| Fibra óptica    | 100-1000 Mbps (o más)       |
| Wireless        | 1-100 Mbps                  |

Si indagamos la situación en las provincias al 3° trimestre del año 2022, en aquellas con mayor penetración, la alta velocidad es ampliamente dominante (Cable modem, en naranja. Fibra Óptica, en verde).

[Tecnologías_Por Provincias](<Imagenes\Tecnologías_Por Provincias.png>)

Posando la lupa en las provincias con potencial de crecimiento, se evidencia que el uso de la tecnología ADSL (para velocidades inferiores a 24), que predominaba el mercado hasta el año 2019, está sufriendo un gran descenso. Por el contrario, el Cable Modem y la Fibra Óptica tomaron relevancia desde entonces.

Es de notar, además, que en Formosa la adopción de mejores tecnologías tiene un retraso respecto del resto puesto que el salto importante de estas se da recién en 2022.

[Tecnologías_Chaco](<Imagenes\Tecnologías_Chaco.png>)

[Tecnologías_Corrientes](<Imagenes\Tecnologías_Corrientes.png>)

[Tecnologías_Santiago](<Imagenes\Tecnologías_Santiago.png>)

[Tecnologías_Formosa](<Imagenes\Tecnologías_Formosa.png>)

### **Ingresos**

Es obvio que los ingresos en el sector de internet van en constante y pronunciado aumento, también influenciado por el avance a nivel mundial de tendencias, tecnologías y estilos de vida vinculados con el servicio de internet.

[Ingresos](<Imagenes\Ingresos.png>)

Más detalles: ['ETL y EDA.ipynb']()

# **`Desarrollo de Dashboard interactivo`**</h3>

En desarrollo.
