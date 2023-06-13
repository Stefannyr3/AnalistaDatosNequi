# AnalistaDatosNequi
Acerca del conjunto de datos
Contexto
La enfermedad por coronavirus (COVID-19) es una enfermedad infecciosa causada por un coronavirus recién descubierto. La mayoría de las personas infectadas con el virus COVID-19 experimentarán una enfermedad respiratoria leve a moderada y se recuperarán sin requerir tratamiento especial. Las personas mayores y aquellas con problemas médicos subyacentes como enfermedades cardiovasculares, diabetes, enfermedades respiratorias crónicas y cáncer tienen más probabilidades de desarrollar enfermedades graves.
Durante todo el curso de la pandemia, uno de los principales problemas a los que se han enfrentado los proveedores de atención médica es la escasez de recursos médicos y un plan adecuado para distribuirlos de manera eficiente. En estos tiempos difíciles, ser capaz de predecir qué tipo de recurso podría necesitar un individuo en el momento de dar positivo o incluso antes de eso será de inmensa ayuda para las autoridades, ya que podrían obtener y organizar los recursos necesarios para salvar la vida de ese paciente.

El objetivo principal de este proyecto es construir un modelo de aprendizaje automático que, dado el síntoma, el estado y el historial médico actuales de un paciente con Covid-19, prediga si el paciente está en alto riesgo o no.

contenido
El conjunto de datos fue proporcionado por el gobierno mexicano (enlace). Este conjunto de datos contiene una enorme cantidad de información anónima relacionada con el paciente, incluidas las condiciones previas. El conjunto de datos sin procesar consta de 21 características únicas y 1.048.576 pacientes únicos. En las características booleanas, 1 significa "sí" y 2 significa "no". valores como 97 y 99 faltan datos.

Sexo: 1 para mujeres y 2 para hombres.
Edad: del paciente.
Clasificación: Resultados de la prueba COVID. Los valores 1-3 significan que el paciente fue diagnosticado con covid en diferentes
grados. 4 o superior significa que el paciente no es portador de covid o que la prueba no es concluyente.
Tipo de paciente: tipo de atención que el paciente recibió en la unidad. 1 para regresar a casa y 2 para hospitalización.
Neumonía: si el paciente ya tiene inflamación de los sacos de aire o no.
Embarazo: si la paciente está embarazada o no.
Diabetes: si el paciente tiene diabetes o no.
EPOC: Indica si el paciente tiene enfermedad pulmonar obstructiva crónica o no.
Asma: si el paciente tiene asma o no.
Inmsupr: si el paciente está inmunosuprimido o no.
Hipertensión: si el paciente tiene hipertensión o no.
Cardiovascular: si el paciente tiene una enfermedad relacionada con el corazón o los vasos sanguíneos.
Renal crónica: si el paciente tiene enfermedad renal crónica o no.
Otra enfermedad: si el paciente tiene otra enfermedad o no.
Obesidad: si el paciente es obeso o no.
Tabaco: si el paciente es consumidor de tabaco.
usmr: Indica si el paciente trató unidades médicas de primer, segundo o tercer nivel.
unidad médica: tipo de institución del Sistema Nacional de Salud que prestó la atención.
Intubado: si el paciente estaba conectado al ventilador.
UCI: Indica si el paciente había sido ingresado en una Unidad de Cuidados Intensivos.
Fecha de fallecimiento: Si el paciente falleció indique la fecha de fallecimiento, y 9999-99-99 en caso contrario.

Limpieza de datos
Cargar dataset, convertirlo a dataframe para realizar limpieza de datos.
Se toma la columna de la fecha de muerte y se realiza limpieza de datos ya que hay este valor 9999-99-99 en donde no ha fallecido este paciente
por tanto se remplaza por Nan, valor nulo en python, en la columna de edad se remplazan los pacientes que tienen edad mayor de 100 por Nan
y las demas columnas se verifica que sean numericas, se toman los valores de 1:True y 2:False , se cambian los demas valores a Nan

