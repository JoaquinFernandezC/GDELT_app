# GDELT_app
[Proyecto Django]
Los controladores estan por ahora hardcodeados con los resultados de las consultas hechas por los códigos de la carpeta scripts/. Se hizo
así a modo de pre-procesamiento de las consultas, para luego solo mostrar los datos recopilados.
Las posibles rutas del proyecto son:
	/tone/: muestra, para cada fecha, el tono promedio
	/tone/count_resume/: muestra, para cada tono, las veces que aparece en el dataset. Lo mismo para el go�ldstein scale
	/tone/events/: muestra, para cada evento, el porcentaje de apariciones en el dataset

