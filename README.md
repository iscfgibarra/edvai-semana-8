# Ejercicio de la semana 8 Jueves


## 0) Dataset 💧🌎

Nos basamos en el dataset de Kaggle: [Water Quality](https://www.kaggle.com/datasets/adityakadiwal/water-potability).

Fue el utilizado para entrenar el modelo de la semana 7: Fastapi.
<br>Así que usen el modelo `rf.pkl` y las columnas del get dummies `categories_ohe.pickle`.

## 1) Consideraciones para el Docker

- Van a utilizar el puerto **5000**. 
- No olviden el tema del manejo de paths.
    ```
    import os
    MAIN_FOLDER = os.path.dirname(__file__)
    MODEL_PATH = os.path.join(MAIN_FOLDER, "model/rf.pkl")
    COLUMNS_PATH = os.path.join(MAIN_FOLDER, "model/categories_ohe.pickle")
    ```
- Llamen a su imagen como `proyecto_bootcamp_edvai_jueves`.


Esto no lo ejecute tal cual modifique el nombre de la imagen y le puse en el tag una version

## Para crear la imagen
```
docker build -t edvai-semana-8:0.1.0 .
```

**-t:** tags

## Para crear el container
```
docker run -p 5000:5000 -e ID_USER=Carlos123 edvai-semana-8:0.1.0
```

**-p:** publish

**-e:** env -> Variable de entorno
