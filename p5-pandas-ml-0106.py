import numpy as np
import pandas as pd
# Samuel Nicola NC 0106
## datos matriz 4 x 3
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas y
# Y almacenar la tabla en la variable df dataframe
print("-----datos a partir de una matrix de 5 x 3-----")
df=pd.DataFrame(datos_alumno,columns=["ci","marcas","paquete"])
print(df)
# datos a partir de un diccionario
print("---- Datos a partir de un diccionario ----")
alumno_diccionario= {
  "nombre":["Samuel","Joel","Mario","Daniel","Alonso","Santiago"],
  "califa":[60,90,100,80,70,50],
  "edad": [64,15,16,16,18,14],
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Samuel Nicola NC 0106")