# PRESENTACION DEL PROYECTO

## TITULO
### Desarrollo de una Analitica predictiva para cantidad de kilómetros que recorren los vehículos en un día, con base en la fecha de entrega y registros anteriores de kilometraje.

## OBJETIVOS
### •	Fortalecer y aplicar los conocimientos del curso electivo Gestión del Conocimiento, de la Maestría en Ingeniería del PJIC.
### •	Implementar dos modelos analíticos de I.A. para el desarrollo predictivo de los kilómetros recorridos en un día por un vehículo.
### •	Seleccionar el mejor de los dos modelos, sustentado en la analítica de los resultados de entrenamiento y validación.
### •	Desarrollar conocimientos en herramientas tecnológicas, aplicables a las I.A. con lenguaje de programación como Python y aplicaciones colaborativas como GitHub.

## INTEGRANTES
### •	Gabriel Antonio Echavarría Vásquez. CC 1152197844. gabriel_echavarria82101@elpoli.edu.co
### •	Alvaro José Berdugo Mendoza. CC 73162633. alvaroberdugo@elpoli.edu.co

## METODOLOGIA
## El proyecto se va a desarrollar en tres fases, descritas a continuación:

## Fase I.

### •	Esta primera fase consiste en determinar con claridad el problema a tratar, el cual consiste en predecir la cantidad de kilómetros recorridos en un día dada la fecha de entrega del mismo y los datos de los kilómetros recorridos en sus últimos tres ingresos al taller.

### •	Se tendrá en cuenta la base de datos correspondientes a 231390 registros de vehículos, incluyendo fechas de entrega, y tres últimos ingresos al taller. Además, el total de kilómetros recorridos para cada fecha de ingreso a taller.

### •	Se realizará una limpieza de datos, la cual consiste en depurar todos los registros según su tipo, para que estos puedan ser aplicados en los modelos predictivos elegidos.

## Fase II

### •	Se establece un Dataframe con todos los datos a tener en cuenta en el modelo, los cuales serán tratados con las librerías y funciones propias Python. Este último será el lenguaje en el cual se realizará la codificación del proyecto.

### •	Se seleccionarán dos modelos de los estudiados en el curso de Analítica Predictiva, los cuales serán desarrollados y aplicados al Dataframe por medio de entrenamiento y validación. 

### •	Se tomarán los resultados de los dos modelos aplicados, para su posterior análisis.

## Fase III

### •	Se analizarán los diferentes parámetros a tener en cuenta en el modelo, así como los diferentes métodos para calcular su error estimado, con el objetivo de elegir el mejor modelo aplicado.

### •	Se presentaron los resultados del modelo elegido desde la analítica.
## DESARROLLO DE MODELADO
### El desarrollo se realizo por modulos existiendo 3 modulos:

### •  Modulo de lectura y analisis de datos: El archivo cleannig_datanb.ipynb se realiza una lectura de los archivos csv con ayuda de la libreria glob, los cuales son concatenados con ayuda de la libreria de pandas. Posteriormente se realiza un reemplazo de datos erroneos y una conversion a tipo fecha a los campos fecha entrega, fecha ultima, fecha penultima y fecha antepenultima; finalmnete se realiza una exploraciomn de los datos.
### Este modulo fue convertido en un archivo .py para poder ser consumidos desde los otros 2 modulos.

### •  Modulo del Perceptron: En el archivo perceptron.ipynb se desarrollo el modelo predictivo de un perceptron simple, inicialmente consumiendo los datos desde el modulo de cleannig_data y posteriormente realizando el escalamiento y transformaciones necesarias para que todos nlos datos quedaran tipo numerico. Con ayuda de modulos como datetime, ColumnTransformer y StandardScaler. Posteriormente, realizando una division de los datos para entrenamiento y prueba con ayuda de la funcion train_test_split. Se desarrolla el Perceptron desde el modulo de linear_model con los datos de entrenamiento, finalizando con el desarrollo de una matriz de confusion, con los datos de prueba ayudado por modulos como metrics y pyplot.

### •  Modulo de Maquina de Soporte Vectorial : En el archivo soporte_vectorial.ipynb se desarrollo el modelo predictivo de una Maquina de Soporte Vectorial, inicialmente consumiendo los datos desde el modulo de cleannig_data y posteriormente realizando el escalamiento y transformaciones necesarias para que todos nlos datos quedaran tipo numerico. Con ayuda de modulos como datetime, ColumnTransformer y StandardScaler. Posteriormente, realizando una division de los datos para entrenamiento y prueba con ayuda de la funcion train_test_split. Se desarrolla la Maquina de Soporte Vectorial desde el modulo de svm con los datos de entrenamiento, finalizando con el desarrollo de una matriz de confusion, con los datos de prueba ayudado por modulos como metrics y pyplot.

## CONCLUSIONES
### • Se evidencia la necesidad de tener una buena calidad en los datos, para ptener una mejor score en los modelos predictivos
### • 
### • 

## TRABAJOS FUTUROS

### •	El desarrollo del proyecto hace parte del trabajo de investigación de la Maestría en Ingeniería, actualmente cursada en PJIC.

### •	El proyecto se plantea como un pilar fundamental para futuras predicciones de ingresos al taller automotriz.

### •	Desarrollo de un modelo predictivo con más variables que las planteadas en este proyecto.

## APRENDIZAJES DESTACADOS

### •	Herramientas tecnológicas: Python, GitHub.
### •	Modelos de Analítica predictiva

## REFERENCIAS
### • Juan D. Velasquez 2019-2021,Curso de Analitica y Maching Learning. https://jdvelasq.github.io/courses/index.html

# SELECCION DEL DATASET
### Los datos recolectados corresponden a información extraída de 6 diferentes concesionarios de Colombia, basados en sus históricos de entregas, e ingresos al taller.
### Cada uno de los registros contienen los siguientes campos: 

### •	Fecha de entrega: Corresponde a la fecha en formato yyyy-mm-dd, en la cual el vehículo fue entregado por el concesionario. Si este no fue entregado, no tendrá fecha de entrega.

### •	Fecha de ultimo ingreso al taller: Corresponde a la fecha en formato yyyy-mm-dd, en la cual el vehículo ingreso por última vez a los talleres del concesionario. Si este nunca ha ingresado al taller, no tendrá fecha de ultimo ingreso.

### •	Fecha de penúltimo ingreso al taller: Corresponde a la fecha en formato yyyy-mm-dd, en la cual el vehículo ingreso por penúltima vez a los talleres del concesionario. Si este nunca ha ingresado por más de dos ocasiones al taller, no tendrá fecha de penúltimo ingreso.

### •	Fecha de antepenúltimo ingreso al taller: Corresponde a la fecha en formato yyyy-mm-dd, en la cual el vehículo ingreso por antepenúltima vez a los talleres del concesionario. Si este nunca ha ingresado por más de tres ocasiones al taller, no tendrá fecha de antepenúltimo ingreso.

### •	Kilometraje reportado en el último ingreso: Corresponde a la cantidad de kilómetros registrados en el Odómetro del vehículo en su último ingreso al taller. Si este nunca ha ingresado al taller, este valor será cero.

### •	Kilometraje reportado en el penúltimo ingreso: Corresponde a la cantidad de kilómetros registrados en el Odómetro del vehículo en su penúltimo ingreso al taller. Si este nunca ha ingresado más de dos veces al taller, este valor será cero.

### •	Kilometraje reportado en el antepenúltimo ingreso: Corresponde a la cantidad de kilómetros registrados en el Odómetro del vehículo en su antepenúltimo ingreso al taller. Si este nunca ha ingresado más de tres veces al taller, este valor será cero.

### •	Ingreso al taller en el mes en curso: Corresponde a un valor binario siendo 1 que el vehiculo ingreso a los talleres del consecionario en el mes en cuerso, siendo 0 lo contrario.

### Cada uno de los 6 paquetes de información, fueron extraídos desde las bases de datos SQL de los concesionarios a archivos CSV, los cuales fueron concatenados, transformados y limpiados por medio de lenguaje Python.

### De los datos recolectados se tomo una cantidad de 30% para para pruebas de los modelos, es decir que el 70% restante son datos utilizados para el entrenamiento de los modelos seleccionados.

# DEFINICION DEL PROBLEMA

### En los talleres del sector automotriz se sufren falencias ya que los ingresos de los vehículos aun poseen la necesidad de tener una proyección de entradas por lapsos de tiempo más largos, ya que actualmente se está en la modalidad de citas y es a muy corto plazo. Contando actualmente con proyecciones en algoritmos tradicionales, los cuales no poseen la habilidad de procesar grandes volúmenes de datos al mismo tiempo, también herramientas de proyección muy empíricas y por juicios de expertos que aún no cuentan con la suficiente habilidad de prever una cifra más exacta.

### Si la proyección existiera, con ésta se podría poseer un valor estimado de entradas y valor monetario por un periodo de tiempo definido más exacto, prever campañas comerciales o promocionales a sus próximos ingresos, tener con antelación repuestos y recursos necesarios para las próximas entradas, prever caídas en ingresos, para planear contingencias y saber con antelación si se logrará las metas propuestas por las marcas y distribuidoras a quienes deben cumplir para continuar con la concesión y la gerencia de los concesionarios puedan tomar con antelación decisiones para maximizar sus ganancias.

# MODELOS ANALITICOS
### Se considero que la prediccion era categorica y por ende se seleccionaron dos modelos predictivos de clasificacion: 

### • Perceptron Simple: Para este modelo se tuvieron en cuenta los siguientes parametros: sin penalizacion, alfa= 0,0001 , red elastica= 0.9 , intercepto de entrenamiento, maximo de iteracciones = 100000, tolerancia = 0.001 , constante de multiplicidad = 1 , earling stopping = true , mezcla de datos de entrenamiento y teniendo en cuenta resultados anteriores. 

### • Maquina de Soporte Vectorial: Para este modelo se tuvieron en cuenta los siguientes parametros: Kernel= lineal , parametro de regularizacion = 1 , gama =  escalado , tolerancia = 0.001 , forma de decision de la funcion = ovr. 

# ENTRENAMIENTO Y VALIDACION DE LOS MODELOS PREDICTIVOS
### Los modelos seleccionados fueron entrenados y posteriormente validados a gtraves de Matriz de Confusion.
### • Perceptron Simple: El entrenamiento del modelo arrojo como resultado un score de 52%......
### • Maquina de Soporte Vectorial: El entrenamiento del modelo arrojo como resultado un score de 54%......

# SELECCION DEL MEJOR MODELO: Se selecciona el modelo de Maquina de Soporte Vectorial, porque tiene un score de 54%......

# APLICAION DEL MODELO A LA GESTION DE CONOCIMIENTO

