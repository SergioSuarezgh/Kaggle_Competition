##      >>Competición de Kaggle para Bootcamp de Data OCT'22:snake: semana 7 en [Ironhack](https://www.ironhack.com/)<<

<p align="center"> <img src="https://github.com/OrianAmpuero/Kaggle_Competition/blob/main/img/predict.jpg" width="700" height="350">  </p>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  [¡¡¡QUE EMPIECE EL JUEGO!!!](https://www.kaggle.com/competitions/predecir-salario-data)  

## 📁ESTRUCTURA

-  DATA/     &emsp;&emsp;                    # contiene los csv  

-  IMG/     &emsp;&emsp;                     # contiene imagénes referentes al proyecto 
 
-  PPTS/      &emsp;&emsp;                   # para cargar las presentaciones

-  .gitignore    &emsp;&emsp;                # archivo para ignorar documentos    

-  README.md  



## 📚RECURSOS

- Salaries_data.csv (Datos para trabajar)
- Testeo.csv (Datos para predecir)
- Muestra.csv (Ejemplo de resultados que deben subir a Kaggle)


## 🔍INFO DE COLUMNAS 
- *work_year:* The year the salary was paid.
- *experience_level:* The experience level in the job during the year
- *employment_type:* The type of employment for the role
- *job_title:* The role worked in during the year.
- *salary:* The total gross salary amount paid.
- *salary_currency:* The currency of the salary paid as an ISO 4217 currency code.
- *salaryinusd:* The salary in USD
- *employee_residence:* Employee's primary country of residence in during the work year as an ISO 3166 country code.
- *remote_ratio:* The overall amount of work done remotely
- *company_location:* The country of the employer's main office or contracting branch
- *company_size:* The median number of people that worked for the company during the year


## 📈OBJECTIVO

- Preparar los datos para los diversos modelos (proceso empírico) 
- Entrenar y Testear modelos de Machine Learning
- Subir los resultados con el mejor modelo entrenado de Machine Learning
- Hacer pull request con la presentación en la carpeta de 'PPTS' 
- Crear repo propio del proyecto (issue)

<br />

![Alt text](img/challenge-accepted-himym.gif)

##Primer Intento

-Modificamos la columna de job_title. Agrupando todos los trabajos en 4.

-Transformamos las columnas categóricas con LabelEncoder.

-Testeamos todos los modelos con la EDA anteriormente señalada y el mejor es LGBRM con un 47572 de mse.

-Una vez subido la mejor puntuación es LGBRM con 68157

![Alt text](img/coyote.gif)

##Segundo intento

-Volvemos a modificar la columna de job_title en 4 opciones

-Ponderamos todas las columnas categóricas en base al salario medio y usamos LabelEncoder con las columnas categóricas

-Testeamos todos los modelos con la EDA anteriormente señalada y el mejor resultado con el mse es ExtraTreeRegressor con un 30498 y el pero SVR con 70247

-Subimos el modelo ExtraTreeRegressor que es el mejor pero empeoramos resultado con un 80678 y al subir el SVR mejoramos con un 51907

![Alt text](img/barney-stinson.gif)


##Tercer intento

-En esta ocasión simplemente hacemos un get-dummies de todas las columnas sin cribas para probar.

-Testeamos nuevamente todos los modelos con el mse y el mejor es XGBR con 31209 y el peor SVR con 70476.

-Subimos el modelo XGBR al ser el que mejor puntación tiene y nos da un resultado de 58533.

![Alt text](img/omg-gasp.gif)

-Subimos también el modelo RIDGE y para nuestra sorpresa nos da un resultado de 36707.

![Alt text](img/explota-la-cabeza-bum.gif)

##Cuarto intento

-Para este intento volvemos a retomar la opción de get_dummies

-En este caso usamos un GridResearch para tratar de mejorar los modelos. En este caso usamos Ridge y RandomForestRegressor para modificar los parámetros

-Usamos los parámetros que nos da el grid. El mse de RandomForestRegressor es 35453 y el de Ridge es 43941. Como vemos empeoramos el Ridge.

-Pero sorpresa, al subirlo nos da el mejor resultado que hemos obtenido 33268

![Alt text](img/3DHAIGQ.gif)

##Conclusiones

-Mis modelos predictivos testeados con  mi información no funcionaban igual que una vez subidos, incluso el peor modelo testado con mse funcionaba mejor que el que menor fallo tenía en mi mse

-En general, los modelos utilizados con LabelEncoder funcionan mucho peor que los que ejecutamos el get_dummies

![Alt text](img/giphy.gif)


-Solamente ha mejorado el modelo un poco usando un GridSearch para buscar los mejores hiperparámetros aunque en mi mse eso no se reflejará pero una vez subido si había una ligera mejora

![Alt text](img/images.jpeg)


##GRACIAS






