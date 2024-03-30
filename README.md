# PyQt_Prueba V1.0

Este es un programa que permite al usuario colocar imágenes en una escena y dibujar líneas entre ellas. El programa está escrito en Python utilizando la biblioteca PyQt5 para la interfaz gráfica.

## Funcionalidades

- **Interfaz Gráfica**: La ventana principal muestra una escena donde se pueden colocar imágenes y un botón para activar/desactivar el modo de dibujo de líneas.
  
- **Botón de Línea**: Al hacer clic en este botón, se activa el modo de dibujo de líneas. En este modo, el cursor se convierte en una cruz y el usuario puede seleccionar dos imágenes para dibujar una línea entre ellas.

- **Selección de Imágenes**: El usuario puede seleccionar imágenes desde un dock widget en el lado izquierdo de la ventana. Se proporcionan tres imágenes predeterminadas para seleccionar.

- **Dibujar Líneas**: Cuando se seleccionan dos imágenes en el modo de dibujo de líneas, se dibuja una línea entre ellas.

## Uso

1. Instalar las dependencias ejecutando `pip install -r requirements.txt`.
2. Ejecutar el programa con `python <nombre_del_archivo>.py`.
3. Seleccionar una imagen desde el dock widget.
4. Colocar la imagen en la escena haciendo clic en un área vacía de la ventana.
5. Activar el modo de dibujo de líneas haciendo clic en el botón "Linea".
6. Seleccionar dos imágenes en la escena para dibujar una línea entre ellas.
7. Desactivar el modo de dibujo de líneas haciendo clic nuevamente en el botón "Linea".

## Requisitos del Sistema

- Python 3.12
- PyQt5

## Estructura del Código

- **MyMainWindow**: Clase que define la ventana principal y todas las funcionalidades del programa.
- **createToolBox**: Método para crear el dock widget que contiene los botones de selección de imágenes.
- **createToolButton**: Método para crear los botones de selección de imágenes.
- **mousePressEventHandler**: Método para manejar los clics del ratón en la ventana.
- **handleLineButton**: Método para manejar el clic del botón "Linea" y activar/desactivar el modo de dibujo de líneas.
- **handleSelectionChanged**: Método para manejar el cambio de selección de las imágenes en la escena.
- **drawLine**: Método para dibujar una línea entre dos imágenes seleccionadas.

## Autor

Este programa fue desarrollado por [Cesar Fernando Flores Bautista](https://github.com/fernandoflores2002).
