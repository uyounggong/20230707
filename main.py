from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QLineEdit
        self.line_edit = QLineEdit(self)

        # Create a QComboBox
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Option 1")
        self.combo_box.addItem("Option 2")
        self.combo_box.addItem("Option 3")

        # Create a QVBoxLayout
        layout = QVBoxLayout(self)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.combo_box)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])

    window = MyWindow()
    window.show()

    app.exec()
