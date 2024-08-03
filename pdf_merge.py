from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QLabel, QVBoxLayout, QScrollArea, QPushButton, QListView
from PyQt5.QtGui import QPixmap, QImage, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
import fitz  # PyMuPDF
from pdf_merge_screen import Ui_PDF_Merge
import os

class PdfMerge(QWidget, Ui_PDF_Merge):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_select.clicked.connect(self.add_files)
        self.pushButton_up.clicked.connect(self.move_up)
        self.pushButton_down.clicked.connect(self.move_down)
        self.pushButton_remove.clicked.connect(self.remove_file)
        self.pushButton_merge.clicked.connect(self.merge_pdfs)
        self.radioButton_onizle.toggled.connect(self.update_preview)
        self.pushButton_save.clicked.connect(self.save_pdf)
        self.selected_files = []

        self.model = QStandardItemModel()
        self.listView.setModel(self.model)

        # Add a scroll area for the PDF preview
        self.scroll_area = QScrollArea(self.placeholder)
        self.scroll_area.setGeometry(0, 0, 331, 491)
        self.scroll_area_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.scroll_area.setWidgetResizable(True)
        
        self.scroll_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area.setVisible(False)

    def add_files(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "PDF Dosyaları Seç", "", "PDF Files (*.pdf)", options=options)
        if files:
            self.selected_files.extend(files)
            self.update_file_list()
            self.update_status()
            self.update_preview()

    def update_file_list(self):
        self.model.clear()
        for file in self.selected_files:
            item = QStandardItem(file)
            self.model.appendRow(item)

    def move_up(self):
        current_index = self.listView.currentIndex().row()
        if current_index > 0:
            self.selected_files[current_index], self.selected_files[current_index - 1] = self.selected_files[current_index - 1], self.selected_files[current_index]
            self.update_file_list()
            self.listView.setCurrentIndex(self.model.index(current_index - 1, 0))
            self.update_status()
            self.update_preview()

    def move_down(self):
        current_index = self.listView.currentIndex().row()
        if current_index < len(self.selected_files) - 1:
            self.selected_files[current_index], self.selected_files[current_index + 1] = self.selected_files[current_index + 1], self.selected_files[current_index]
            self.update_file_list()
            self.listView.setCurrentIndex(self.model.index(current_index + 1, 0))
            self.update_status()
            self.update_preview()

    def remove_file(self):
        current_index = self.listView.currentIndex().row()
        if current_index >= 0:
            del self.selected_files[current_index]
            self.update_file_list()
            self.update_status()
            self.update_preview()

    def merge_pdfs(self):
        if not self.selected_files:
            QMessageBox.warning(self, "Uyarı", "Lütfen önce PDF dosyalarını seçin.")
            return
        
        output_file, _ = QFileDialog.getSaveFileName(self, "Kaydet", "", "PDF Files (*.pdf)")
        if output_file:
            try:
                new_doc = fitz.open()
                for file in self.selected_files:
                    doc = fitz.open(file)
                    new_doc.insert_pdf(doc)
                new_doc.save(output_file)
                self.label_status.setText(f"Birleştirilmiş PDF kaydedildi: {output_file}")
                self.update_preview()
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"PDF kaydedilemedi: {e}")

    def save_pdf(self):
        if not self.selected_files:
            QMessageBox.warning(self, "Uyarı", "Lütfen önce PDF dosyalarını seçin ve birleştirin.")
            return
        
        output_file, _ = QFileDialog.getSaveFileName(self, "Kaydet", "", "PDF Files (*.pdf)")
        if output_file:
            try:
                doc = fitz.open(self.selected_files[0])
                for file in self.selected_files[1:]:
                    doc.insert_pdf(fitz.open(file))
                doc.save(output_file)
                self.label_status.setText(f"Birleştirilmiş PDF kaydedildi: {output_file}")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"PDF kaydedilemedi: {e}")

    def update_preview(self):
        if not self.radioButton_onizle.isChecked() or not self.selected_files:
            self.scroll_area.setVisible(False)
            self.clear_layout(self.scroll_layout)
            return

        self.clear_layout(self.scroll_layout)
        self.scroll_area.setVisible(True)

        try:
            combined_doc = fitz.open()
            for file in self.selected_files:
                doc = fitz.open(file)
                combined_doc.insert_pdf(doc)
            
            for page_num in range(len(combined_doc)):
                page = combined_doc.load_page(page_num)
                pix = page.get_pixmap()
                image_format = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
                qt_img = QImage(pix.samples, pix.width, pix.height, pix.stride, image_format)
                qt_img = QPixmap.fromImage(qt_img)

                img_label = QLabel(self)
                scaled_pixmap = qt_img.scaled(self.scroll_area.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                img_label.setPixmap(scaled_pixmap)
                img_label.setAlignment(Qt.AlignCenter)

                self.scroll_layout.addWidget(img_label)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"PDF önizlemesi yapılamadı: {e}")

    def update_status(self):
        num_files = len(self.selected_files)
        self.label_status.setText(f"Seçilen dosya sayısı: {num_files}")

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PdfMerge()
    window.show()
    sys.exit(app.exec_())
