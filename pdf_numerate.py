from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont
import sys

class PdfNumerate(QWidget):
    def __init__(self):
        super().__init__()

        # Pencere boyutu ve başlık
        self.setFixedSize(759, 520)
        self.setWindowTitle("PDF Numaralandır")

        # Yazı
        label = QLabel("Bu sayfa henüz geliştirme aşamasındadır", self)
        label.setFont(QFont("Gotham Narrow", 16))
        label.adjustSize()
        label.move((self.width() - label.width()) // 2, (self.height() - label.height()) // 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PdfNumerate()
    window.show()
    sys.exit(app.exec_())
