import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # VENTANA GENERAL
        self.setWindowTitle("Programa - CODEAUNI")
        self.setGeometry(100, 100, 800, 600)
        # ESCENA
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(QRectF(0, 0, 600, 400))  # Establecer un tamaño máximo para la escena
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)
        # BOTONES
        self.last_image_path = None
        self.line_button = QPushButton("Linea")  # Crear el botón "line_button"
        self.line_button.setCheckable(True)  # Hacer el botón verificable
        self.line_button.clicked.connect(self.handleLineButton)  # Conectar el clic del botón a una función
        self.selected_items = []

        # TOOLBOX
        self.createToolBox()  # Llamar a createToolBox después de crear el botón "Linea"
        
        # LAYOUT PRINCIPAL
        #Diseño Vertical en la MainWindow
        main_layout = QVBoxLayout()
        #Escena
        main_layout.addWidget(self.view)
        #Boton de linea
        main_layout.addWidget(self.line_button, alignment=Qt.AlignTop | Qt.AlignLeft)  # Alineación del botón
        #Diseño principal
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    
    #Definimos el toolbox
    def createToolBox(self):
        toolbox = QDockWidget("Images", self)
        toolbox.setFeatures(QDockWidget.DockWidgetMovable)

        tool_contents = QWidget()
        layout = QVBoxLayout()

        tool1 = self.createToolButton("", "src/carritodecompras.png")
        tool2 = self.createToolButton("", "src/carteldecerrado.png")
        tool3 = self.createToolButton("", "src/cajaderegalos.png")

        layout.addWidget(tool1)
        layout.addWidget(tool2)
        layout.addWidget(tool3)

        tool_contents.setLayout(layout)
        toolbox.setWidget(tool_contents)

        self.addDockWidget(Qt.LeftDockWidgetArea, toolbox)

    #Botones del ToolBox
    def createToolButton(self, name, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        button = QPushButton(name)
        button.setIcon(QIcon(scaled_pixmap))
        button.setIconSize(QSize(50, 50))
        button.setMaximumSize(60, 60)
        button.clicked.connect(lambda checked, path=image_path: self.mousePressEventHandler(path))
        return button

    # Cualquier parte donde haga clic en la ventana
    def mousePressEventHandler(self, image_path):
        self.last_image_path = image_path

    # Acciones específicas del clic
    def mousePressEvent(self, event):
        if self.last_image_path is not None and not self.line_button.isChecked():
            scene_pos = self.view.mapToScene(event.pos())
            if scene_pos is not None:
                if self.scene.sceneRect().contains(scene_pos):
                    pixmap = QPixmap(self.last_image_path)
                    scaled_pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    item = QGraphicsPixmapItem(scaled_pixmap)
                    self.scene.addItem(item)
                    item.setPos(scene_pos - QPointF(2*scaled_pixmap.width(), 1*scaled_pixmap.height() ))
                    item.setFlag(QGraphicsPixmapItem.ItemIsSelectable)
                    item.setFlag(QGraphicsPixmapItem.ItemIsMovable)
                    #self.selected_items.append(item)  # Agregar la imagen seleccionada a la lista
                else:
                    QMessageBox.warning(self, "Espacio no adecuado",
                                        "No hay espacio suficiente para colocar la imagen.")
                self.last_image_path = None

        else:
            super().mousePressEvent(event)

    #Manipulación del boton linea
    def handleLineButton(self, event):
        # Verificar si el botón de línea está activado
        if self.line_button.isChecked():
            print("Botón Linea activado")
            self.setCursor(Qt.CrossCursor)
            self.scene.selectionChanged.connect(self.handleSelectionChanged)  # Conectar la señal de cambio de selección
        else:
            print("Botón Linea desactivado")
            self.setCursor(Qt.ArrowCursor)
            self.selected_items = []
            self.scene.selectionChanged.disconnect(self.handleSelectionChanged)  # Desconectar la señal de cambio de selección
            self.selected_items.clear()

    #Cambio de selección de copias
    def handleSelectionChanged(self):
        if len(self.selected_items) < 2:
            selected = self.scene.selectedItems()
            for item in selected:
                if item in self.selected_items:
                    continue
                else:
                    self.selected_items.append(item)
                    if len(self.selected_items) == 2:
                        self.drawLine()
    
    #Dibujar la linea
    def drawLine(self):
        # Obtener las posiciones de las imágenes seleccionadas para dibujar la línea
        pos1 = self.selected_items[0].pos() + QPointF(self.selected_items[0].pixmap().width() / 2, self.selected_items[0].pixmap().height() / 2)
        pos2 = self.selected_items[1].pos() + QPointF(self.selected_items[1].pixmap().width() / 2, self.selected_items[1].pixmap().height() / 2)
        line = QGraphicsLineItem(pos1.x(), pos1.y(), pos2.x(), pos2.y())  # Crear un elemento de línea con las coordenada x1,y1,x2,y2
        line.setPen(QPen(Qt.black))  # Configuraciones de la linea
        self.scene.addItem(line)  # Agregar la línea a la escena

#Correr el programa
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
