from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox
import urllib.request
import os
import sys


def update():
    version_url = "https://uyounggong.github.io/20230707/version.txt"  # URL of your app's latest version number
    response = urllib.request.urlopen(version_url)
    latest_version = response.read().decode('utf-8').strip()

    with open('version.txt', 'r') as file:
        current_version = file.read().replace('\n', '')

    print(current_version)
    print(latest_version)
    if current_version != latest_version:
        print("New update available! Updating...")
        exe_url = f"https://github.com/uyounggong/20230707/releases/download/v{latest_version}/main.exe"
        urllib.request.urlretrieve(exe_url, 'new_main.exe')

        # Rename the current exe file (this will be our backup)
        os.rename('main.exe', f'main_{current_version}.exe')

        # Rename the new exe file to main.exe
        os.rename('new_main.exe', 'main.exe')

        # Update version file locally
        with open('version.txt', 'w') as file:
            file.write(latest_version)

        # The following part might not work as expected as we discussed earlier.
        # Restart the program
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        print("No update available")
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
        self.combo_box.addItem("please")

        # Create a QVBoxLayout
        layout = QVBoxLayout(self)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.combo_box)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    update()
    window = MyWindow()
    window.show()

    app.exec()
