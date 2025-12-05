from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from yt_transcriber import start_transcription
from PySide6.QtWidgets import QLineEdit, QPushButton
def on_transcribe_clicked():
    url = window.findChild(QLineEdit, "input_url").text()
    start_transcription(url)

app = QApplication([])

loader = QUiLoader()
file = QFile("main_window.ui")
file.open(QFile.ReadOnly)

window = loader.load(file)
file.close()

# connect button click
button = window.findChild(QPushButton, "transcribe")
button.clicked.connect(on_transcribe_clicked)

window.show()
app.exec()
