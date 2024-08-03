from pdf_divider_screen import Ui_PDF_Divider

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QLabel, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import fitz  # PyMuPDF

class PdfDivider(QWidget, Ui_PDF_Divider):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_select.clicked.connect(self.select_pdf)
        self.pushButton_divide.clicked.connect(self.divide_pdf)
        self.pushButton_save.clicked.connect(self.save_pdf)
        self.lineEdit.textChanged.connect(self.update_preview)
        self.radioButton_onizle.toggled.connect(self.toggle_preview)
        self.selected_file = None
        self.pages_to_split = []

        # PDF görüntüleme için scroll area ekliyoruz
        self.scroll_area = QScrollArea(self.placeholder)
        self.scroll_area.setGeometry(0, 0, 331, 491)
        self.scroll_area_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.scroll_area.setWidgetResizable(True)
        
        self.scroll_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area.setVisible(False)

    def select_pdf(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "PDF Seç", "", "PDF Files (*.pdf)", options=options)
        if file_name:
            self.selected_file = file_name
            self.label_status.setText(f"Seçilen dosya: {file_name}")
            self.update_preview()  # Dosya seçildiğinde önizlemeyi güncelleyelim

    def divide_pdf(self):
        if not self.selected_file:
            QMessageBox.warning(self, "Uyarı", "Lütfen önce bir PDF dosyası seçin.")
            return
        
        pages_input = self.lineEdit.text()
        if not pages_input:
            QMessageBox.warning(self, "Uyarı", "Lütfen bölünecek sayfa aralıklarını girin.")
            return

        try:
            ranges = pages_input.split(',')
            self.pages_to_split = []
            for r in ranges:
                try:
                    if '-' in r:
                        start, end = r.split('-')
                        start = int(start) if start else 1
                        end = int(end) if end else len(fitz.open(self.selected_file))
                        self.pages_to_split.append((start, end))
                    else:
                        page = int(r)
                        self.pages_to_split.append((page, page))
                except ValueError:
                    pass  # Geçersiz girişleri görmezden gel
            self.label_status.setText("Bölme işlemi tamamlandı.")
            self.update_preview()  # Sayfa aralıkları girildikten hemen sonra önizleme güncelleniyor
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Geçersiz giriş: {e}")

    def save_pdf(self):
        if not self.pages_to_split:
            QMessageBox.warning(self, "Uyarı", "Lütfen önce sayfa aralıklarını girin ve bölme işlemini yapın.")
            return
        
        output_file, _ = QFileDialog.getSaveFileName(self, "Kaydet", "", "PDF Files (*.pdf)")
        if output_file:
            try:
                doc = fitz.open(self.selected_file)
                new_doc = fitz.open()
                for start, end in self.pages_to_split:
                    for page_num in range(start-1, end):
                        new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
                new_doc.save(output_file)
                self.label_status.setText(f"Yeni PDF kaydedildi: {output_file}")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"PDF kaydedilemedi: {e}")

    def toggle_preview(self):
        if self.radioButton_onizle.isChecked() and self.selected_file:
            self.scroll_area.setVisible(True)
            self.update_preview()
        else:
            self.scroll_area.setVisible(False)

    def update_preview(self):
        if not self.radioButton_onizle.isChecked() or not self.selected_file:
            return
        try:
            self.clear_layout(self.scroll_layout)  # Mevcut önizlemeleri temizle
            doc = fitz.open(self.selected_file)
            pages_input = self.lineEdit.text()
            if not pages_input:  # Eğer giriş yoksa tüm PDF'yi göster
                self.pages_to_split = [(1, len(doc))]
            else:
                ranges = pages_input.split(',')
                self.pages_to_split = []
                for r in ranges:
                    try:
                        if '-' in r:
                            start, end = r.split('-')
                            start = int(start) if start else 1
                            end = int(end) if end else len(doc)
                            self.pages_to_split.append((start, end))
                        else:
                            page = int(r)
                            self.pages_to_split.append((page, page))
                    except ValueError:
                        pass  # Geçersiz girişleri görmezden gel

            for start, end in self.pages_to_split:
                for page_num in range(start-1, end):
                    page = doc.load_page(page_num)
                    pix = page.get_pixmap()

                    image_format = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
                    qt_img = QImage(pix.samples, pix.width, pix.height, pix.stride, image_format)
                    qt_img = QPixmap.fromImage(qt_img)

                    img_label = QLabel(self)
                    scaled_pixmap = qt_img.scaled(self.placeholder.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    img_label.setPixmap(scaled_pixmap)
                    img_label.setAlignment(Qt.AlignCenter)

                    self.scroll_layout.addWidget(img_label)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"PDF önizlemesi yapılamadı: {e}")

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PdfDivider()
    window.show()
    sys.exit(app.exec_())
