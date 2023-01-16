import sys

from PyQt5.QtGui import QPixmap, QIcon, QClipboard
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QMainWindow, QComboBox, QRadioButton, QLineEdit, QCheckBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        layout = QVBoxLayout()
        # Add widgets to the layout
        # first widget
        first_block = QHBoxLayout()
        self.length_combo = QComboBox()
        self.length_combo.setEditable(True)
        self.length_combo.addItems([str(i) for i in range(4, 32, 2)])
        first_block.addWidget(QLabel("Enter password length: "))
        first_block.addWidget(self.length_combo)
        layout.addLayout(first_block)

        # second widget
        second_block = QVBoxLayout()
        second_block.addWidget(QLabel("Password Type: "))
        type_layout = QHBoxLayout()
        r_pin = QRadioButton()
        r_pin.setText("Pin")
        r_pin.setToolTip("Only includes digit")
        type_layout.addWidget(r_pin)
        r_memorable = QRadioButton()
        r_memorable.setText("Memorable(medium)")
        r_memorable.setToolTip("Only includes letters(uppercase and lower case)")
        type_layout.addWidget(r_memorable)
        r_strong = QRadioButton()
        r_strong.setText("Strong")
        r_strong.setToolTip("includes letters, digits, special character")
        type_layout.addWidget(r_strong)
        r_default = QRadioButton()
        r_default.setText("Default")
        r_default.setToolTip("Same as strong")
        type_layout.addWidget(r_default)
        second_block.addLayout(type_layout)
        layout.addLayout(second_block)

        third_block = QHBoxLayout()
        self.generated_pass = QLineEdit()
        self.generated_pass.setModified(False)
        self.generated_pass.setReadOnly(True)
        self.editable_toggle = QCheckBox()
        self.editable_toggle.setChecked(False)
        self.editable_toggle.stateChanged.connect(self.modified_generated_pass)
        self.copy_btn = QPushButton()
        self.copy_btn.clicked.connect(self.copy_pass)
        # set icon for copy btn
        pixmap = QPixmap("copy_iconpng.png")
        icon = QIcon(pixmap)
        self.copy_btn.setIcon(icon)
        third_block.addWidget(self.generated_pass)
        third_block.addWidget(self.editable_toggle)
        third_block.addWidget(self.copy_btn)
        layout.addLayout(third_block)

        self.generate_pass_btn = QPushButton("Generate Password")
        self.generate_pass_btn.clicked.connect(self.generate_pass)
        layout.addWidget(self.generate_pass_btn)
        # Set the layout on the application's window
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(layout)
        self.setCentralWidget(self.centralWidget)
        print(self.children())

    def modified_generated_pass(self):
        if self.editable_toggle.isChecked():
            self.generated_pass.setModified(True)
            self.generated_pass.setReadOnly(False)
        else:
            self.generated_pass.setModified(False)
            self.generated_pass.setReadOnly(True)

    def copy_pass(self):
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText("Clipboard Text", mode=cb.Clipboard)

    def generate_pass(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())