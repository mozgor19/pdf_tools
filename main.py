import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets

from main_screen import Ui_Main  # Ana arayüz için içe aktarım
from pdf_divider import PdfDivider # PDF bölme arayüzü için içe aktarım
from pdf_merge import PdfMerge # PDF Birleştirme arayüzü için içe aktarım
from pdf_converter import PdfConverter # PDF dönüştürme arayüzü için içe aktarım
from pdf_watermark import PDFWatermarkApp
from pdf_numerate import PdfNumerate
from pdf_edit import PdfEdit

class MainWindow(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_merge.clicked.connect(self.open_pdf_merge)
        self.pushButton_split.clicked.connect(self.open_pdf_divider)
        self.pushButton_convert.clicked.connect(self.open_pdf_converter)
        self.pushButton_filigran.clicked.connect(self.open_pdf_watermark)
        self.pushButton_numarate.clicked.connect(self.open_pdf_numerator)
        self.pushButton_edit.clicked.connect(self.open_pdf_editor)
        self.pushButton_communicate.clicked.connect(self.open_website)

    def open_pdf_merge(self):
        self.pdf_merge_window = PdfMerge()
        self.pdf_merge_window.show()

    def open_pdf_divider(self):
        self.pdf_divider_window = PdfDivider()
        self.pdf_divider_window.show()
    
    def open_pdf_converter(self):
        self.pdf_converter_window = PdfConverter()
        self.pdf_converter_window.show()
    
    def open_pdf_watermark(self):
        self.pdf_watermark_window = PDFWatermarkApp()
        self.pdf_watermark_window.show()

    def open_pdf_numerator(self):
        self.pdf_numerator_window = PdfNumerate()
        self.pdf_numerator_window.show()
    
    def open_pdf_editor(self):
        self.pdf_editor_window = PdfEdit()
        self.pdf_editor_window.show()

    def open_website(self):
        webbrowser.open('https://web.itu.edu.tr/ozgor22/about/')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
