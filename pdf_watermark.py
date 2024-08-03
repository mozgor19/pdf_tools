import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLineEdit, QColorDialog, QComboBox, QSlider, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color

class PDFWatermarkApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('PDF Filigran Ekle')
        self.setFixedSize(759, 520)
        self.setStyleSheet("QWidget { font-family: 'Gotham Narrow'; font-size: 14px; }")

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(20, 20, 20, 20)
        mainLayout.setSpacing(10)

        header = QLabel('PDF Filigran Ekle', self)
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(header)

        fileLayout = QHBoxLayout()
        self.pdfPathLineEdit = QLineEdit(self)
        self.pdfPathLineEdit.setPlaceholderText('PDF dosyasını seçin...')
        fileLayout.addWidget(self.pdfPathLineEdit)
        
        self.selectPDFButton = QPushButton('PDF Seç', self)
        self.selectPDFButton.setStyleSheet("padding: 10px;")
        self.selectPDFButton.clicked.connect(self.selectPDF)
        fileLayout.addWidget(self.selectPDFButton)
        
        mainLayout.addLayout(fileLayout)
        
        self.textLineEdit = QLineEdit(self)
        self.textLineEdit.setPlaceholderText('Filigran metni girin...')
        mainLayout.addWidget(self.textLineEdit)

        fontLayout = QHBoxLayout()
        fontLabel = QLabel('Yazı Tipi:')
        fontLayout.addWidget(fontLabel)
        fontLayout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.fontComboBox = QComboBox(self)
        self.fontComboBox.addItems(['Courier', 'Helvetica', 'Times-Roman'])
        self.fontComboBox.setStyleSheet("padding: 5px;")
        fontLayout.addWidget(self.fontComboBox)
        mainLayout.addLayout(fontLayout)
        
        positionLayout = QHBoxLayout()
        positionLabel = QLabel('Konum:')
        positionLayout.addWidget(positionLabel)
        positionLayout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.positionComboBox = QComboBox(self)
        self.positionComboBox.addItems(['Üst Sol', 'Üst Orta', 'Üst Sağ', 'Orta Sol', 'Orta Orta', 'Orta Sağ', 'Alt Sol', 'Alt Orta', 'Alt Sağ'])
        self.positionComboBox.setStyleSheet("padding: 5px;")
        positionLayout.addWidget(self.positionComboBox)
        mainLayout.addLayout(positionLayout)
        
        opacityLayout = QHBoxLayout()
        opacityLabel = QLabel('Saydamlık:')
        opacityLayout.addWidget(opacityLabel)
        opacityLayout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.opacitySlider = QSlider(Qt.Horizontal, self)
        self.opacitySlider.setRange(0, 100)
        self.opacitySlider.setValue(50)
        opacityLayout.addWidget(self.opacitySlider)
        mainLayout.addLayout(opacityLayout)
        
        colorLayout = QHBoxLayout()
        self.selectColorButton = QPushButton('Renk Seç', self)
        self.selectColorButton.setStyleSheet("padding: 10px;")
        self.selectColorButton.clicked.connect(self.selectColor)
        colorLayout.addWidget(self.selectColorButton)
        mainLayout.addLayout(colorLayout)
        
        self.addWatermarkButton = QPushButton('Filigran Ekle', self)
        self.addWatermarkButton.setStyleSheet("padding: 10px; font-weight: bold;")
        self.addWatermarkButton.clicked.connect(self.addWatermark)
        mainLayout.addWidget(self.addWatermarkButton)
        
        self.setLayout(mainLayout)
        self.show()
        
    def selectPDF(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, 'PDF Seç', '', 'PDF Files (*.pdf)', options=options)
        if filePath:
            self.pdfPathLineEdit.setText(filePath)
    
    def selectColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.selectedColor = color
    
    def create_watermark(self, text, font, position, opacity, color, width, height):
        c = canvas.Canvas("watermark.pdf", pagesize=(width, height))
        c.setFont(font, 40)
        c.setFillColor(Color(color.redF(), color.greenF(), color.blueF(), alpha=opacity))
        
        text_width = c.stringWidth(text, font, 40)
        x, y = 0, 0
        
        if position == 'Üst Sol':
            x, y = 10, height - 50
        elif position == 'Üst Orta':
            x, y = (width - text_width) / 2, height - 50
        elif position == 'Üst Sağ':
            x, y = width - text_width - 10, height - 50
        elif position == 'Orta Sol':
            x, y = 10, height / 2
        elif position == 'Orta Orta':
            x, y = (width - text_width) / 2, height / 2
        elif position == 'Orta Sağ':
            x, y = width - text_width - 10, height / 2
        elif position == 'Alt Sol':
            x, y = 10, 50
        elif position == 'Alt Orta':
            x, y = (width - text_width) / 2, 50
        elif position == 'Alt Sağ':
            x, y = width - text_width - 10, 50
        
        c.drawString(x, y, text)
        c.save()
    
    def addWatermark(self):
        pdfPath = self.pdfPathLineEdit.text()
        text = self.textLineEdit.text()
        font = self.fontComboBox.currentText()
        position = self.positionComboBox.currentText()
        opacity = self.opacitySlider.value() / 100.0
        color = self.selectedColor
        
        reader = PdfReader(pdfPath)
        writer = PdfWriter()
        
        for pageNum in range(len(reader.pages)):
            page = reader.pages[pageNum]
            width = page.mediabox.width
            height = page.mediabox.height
            
            self.create_watermark(text, font, position, opacity, color, width, height)
            
            watermark_reader = PdfReader("watermark.pdf")
            watermark_page = watermark_reader.pages[0]
            page.merge_page(watermark_page)
            
            writer.add_page(page)
        
        outputPath = pdfPath.replace('.pdf', '_watermarked.pdf')
        with open(outputPath, 'wb') as outputStream:
            writer.write(outputStream)

        print(f"Filigran eklenmiş PDF oluşturuldu: {outputPath}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PDFWatermarkApp()
    sys.exit(app.exec_())
