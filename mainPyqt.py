import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget


class ListaTareasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tareas")
        self.setGeometry(100, 100, 400, 300)

        self.lista_tareas = []

        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        self.lista_tareas_widget = QListWidget()
        self.layout_principal.addWidget(self.lista_tareas_widget)

        self.layout_botones = QHBoxLayout()
        self.layout_principal.addLayout(self.layout_botones)

        self.input_tarea = QLineEdit()
        self.layout_botones.addWidget(self.input_tarea)

        self.btn_agregar = QPushButton("Agregar")
        self.btn_agregar.clicked.connect(self.agregar_tarea)
        self.layout_botones.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_tarea)
        self.layout_botones.addWidget(self.btn_eliminar)

        self.btn_completar = QPushButton("Completar")
        self.btn_completar.clicked.connect(self.marcar_completada)
        self.layout_botones.addWidget(self.btn_completar)

        self.actualizar_lista_tareas()

    def agregar_tarea(self):
        tarea = self.input_tarea.text()
        if tarea:
            self.lista_tareas.append({'tarea': tarea, 'completada': False})
            self.actualizar_lista_tareas()
            self.input_tarea.clear()

    def eliminar_tarea(self):
        indice = self.lista_tareas_widget.currentRow()
        if indice != -1:
            del self.lista_tareas[indice]
            self.actualizar_lista_tareas()

    def marcar_completada(self):
        indice = self.lista_tareas_widget.currentRow()
        if indice != -1:
            self.lista_tareas[indice]['completada'] = True
            self.actualizar_lista_tareas()

    def actualizar_lista_tareas(self):
        self.lista_tareas_widget.clear()
        for tarea in self.lista_tareas:
            tarea_texto = f"{tarea['tarea']} - {'Completada' if tarea['completada'] else 'Pendiente'}"
            self.lista_tareas_widget.addItem(tarea_texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ListaTareasApp()
    ventana.show()
    sys.exit(app.exec_())
