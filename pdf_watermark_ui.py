from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(759, 520)
        Form.setMinimumSize(QtCore.QSize(759, 520))
        Form.setMaximumSize(QtCore.QSize(759, 520))
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(350, 210, 401, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_aralk = QtWidgets.QLabel(Form)
        self.label_aralk.setGeometry(QtCore.QRect(360, 150, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.label_aralk.setFont(font)
        self.label_aralk.setObjectName("label_aralk")
        self.pushButton_select = QtWidgets.QPushButton(Form)
        self.pushButton_select.setGeometry(QtCore.QRect(650, 60, 100, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.pushButton_select.setFont(font)
        self.pushButton_select.setObjectName("pushButton_select")
        self.label_select_file = QtWidgets.QLabel(Form)
        self.label_select_file.setGeometry(QtCore.QRect(360, 80, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.label_select_file.setFont(font)
        self.label_select_file.setObjectName("label_select_file")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(350, 40, 611, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_label = QtWidgets.QLabel(Form)
        self.main_label.setGeometry(QtCore.QRect(350, 10, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(24)
        self.main_label.setFont(font)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(350, 110, 611, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_filigranMetni = QtWidgets.QLineEdit(Form)
        self.lineEdit_filigranMetni.setGeometry(QtCore.QRect(360, 170, 391, 31))
        self.lineEdit_filigranMetni.setObjectName("lineEdit_filigranMetni")
        self.placeholder = QtWidgets.QLabel(Form)
        self.placeholder.setGeometry(QtCore.QRect(10, 10, 331, 491))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(12)
        self.placeholder.setFont(font)
        self.placeholder.setFrameShape(QtWidgets.QFrame.Box)
        self.placeholder.setAlignment(QtCore.Qt.AlignCenter)
        self.placeholder.setObjectName("placeholder")
        self.radioButton_onizle = QtWidgets.QRadioButton(Form)
        self.radioButton_onizle.setGeometry(QtCore.QRect(360, 480, 99, 20))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.radioButton_onizle.setFont(font)
        self.radioButton_onizle.setObjectName("radioButton_onizle")
        self.label_aralk_2 = QtWidgets.QLabel(Form)
        self.label_aralk_2.setGeometry(QtCore.QRect(360, 240, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.label_aralk_2.setFont(font)
        self.label_aralk_2.setObjectName("label_aralk_2")
        self.spinBox_fontsize = QtWidgets.QSpinBox(Form)
        self.spinBox_fontsize.setGeometry(QtCore.QRect(530, 270, 51, 32))
        self.spinBox_fontsize.setObjectName("spinBox_fontsize")
        self.checkBox_isBold = QtWidgets.QCheckBox(Form)
        self.checkBox_isBold.setGeometry(QtCore.QRect(600, 270, 71, 31))
        self.checkBox_isBold.setObjectName("checkBox_isBold")
        self.checkBox_isItalic = QtWidgets.QCheckBox(Form)
        self.checkBox_isItalic.setGeometry(QtCore.QRect(670, 270, 71, 31))
        self.checkBox_isItalic.setObjectName("checkBox_isItalic")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(350, 320, 401, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_aralk_3 = QtWidgets.QLabel(Form)
        self.label_aralk_3.setGeometry(QtCore.QRect(360, 350, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.label_aralk_3.setFont(font)
        self.label_aralk_3.setObjectName("label_aralk_3")
        self.label_aralk_4 = QtWidgets.QLabel(Form)
        self.label_aralk_4.setGeometry(QtCore.QRect(470, 350, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.label_aralk_4.setFont(font)
        self.label_aralk_4.setObjectName("label_aralk_4")
        self.label_aralk_5 = QtWidgets.QLabel(Form)
        self.label_aralk_5.setGeometry(QtCore.QRect(570, 350, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.label_aralk_5.setFont(font)
        self.label_aralk_5.setObjectName("label_aralk_5")
        self.label_aralk_6 = QtWidgets.QLabel(Form)
        self.label_aralk_6.setGeometry(QtCore.QRect(670, 350, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.label_aralk_6.setFont(font)
        self.label_aralk_6.setObjectName("label_aralk_6")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(445, 330, 20, 71))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.comboBox_place = QtWidgets.QComboBox(Form)
        self.comboBox_place.setGeometry(QtCore.QRect(350, 370, 103, 32))
        self.comboBox_place.setObjectName("comboBox_place")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.spinBox_opacity = QtWidgets.QSpinBox(Form)
        self.spinBox_opacity.setGeometry(QtCore.QRect(480, 370, 51, 32))
        self.spinBox_opacity.setMinimum(0)
        self.spinBox_opacity.setMaximum(100)
        self.spinBox_opacity.setSingleStep(1)
        self.spinBox_opacity.setObjectName("spinBox_opacity")
        self.spinBox_rotation = QtWidgets.QSpinBox(Form)
        self.spinBox_rotation.setGeometry(QtCore.QRect(580, 370, 51, 32))
        self.spinBox_rotation.setMinimum(90)
        self.spinBox_rotation.setMaximum(360)
        self.spinBox_rotation.setSingleStep(90)
        self.spinBox_rotation.setObjectName("spinBox_rotation")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(540, 330, 20, 71))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(640, 330, 20, 71))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.spinBox_startPage = QtWidgets.QSpinBox(Form)
        self.spinBox_startPage.setGeometry(QtCore.QRect(660, 370, 41, 32))
        self.spinBox_startPage.setMaximum(100)
        self.spinBox_startPage.setObjectName("spinBox_startPage")
        self.spinBox_endPage = QtWidgets.QSpinBox(Form)
        self.spinBox_endPage.setGeometry(QtCore.QRect(710, 370, 41, 32))
        self.spinBox_endPage.setMaximum(100)
        self.spinBox_endPage.setObjectName("spinBox_endPage")
        self.pushButton_addFiligran = QtWidgets.QPushButton(Form)
        self.pushButton_addFiligran.setGeometry(QtCore.QRect(520, 460, 100, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.pushButton_addFiligran.setFont(font)
        self.pushButton_addFiligran.setObjectName("pushButton_addFiligran")
        self.pushButton_save = QtWidgets.QPushButton(Form)
        self.pushButton_save.setGeometry(QtCore.QRect(650, 460, 100, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.comboBox_font = QtWidgets.QComboBox(Form)
        self.comboBox_font.setGeometry(QtCore.QRect(350, 270, 161, 32))
        self.comboBox_font.setObjectName("comboBox_font")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.pushButton_selectColor = QtWidgets.QPushButton(Form)
        self.pushButton_selectColor.setGeometry(QtCore.QRect(360, 410, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Narrow")
        font.setPointSize(14)
        self.pushButton_selectColor.setFont(font)
        self.pushButton_selectColor.setObjectName("pushButton_selectColor")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_aralk.setText(_translate("Form", "Filigran metnini giriniz:"))
        self.pushButton_select.setText(_translate("Form", "PDF Seç"))
        self.label_select_file.setText(_translate("Form", "Lütfen dosyanızı seçiniz:"))
        self.main_label.setText(_translate("Form", "PDF Filigran Ekle"))
        self.placeholder.setText(_translate("Form", "Önizleme için sağ alttaki butonu aktif hale getiriniz."))
        self.radioButton_onizle.setText(_translate("Form", "Önizle"))
        self.label_aralk_2.setText(_translate("Form", "Metin biçimi:"))
        self.checkBox_isBold.setText(_translate("Form", "Bold"))
        self.checkBox_isItalic.setText(_translate("Form", "Italic"))
        self.label_aralk_3.setText(_translate("Form", "Konum:"))
        self.label_aralk_4.setText(_translate("Form", "Saydamlık:"))
        self.label_aralk_5.setText(_translate("Form", "Döndürme:"))
        self.label_aralk_6.setText(_translate("Form", "Sayfalar:"))
        self.comboBox_place.setItemText(0, _translate("Form", "Üst Sol"))
        self.comboBox_place.setItemText(1, _translate("Form", "Üst Sağ"))
        self.comboBox_place.setItemText(2, _translate("Form", "Üst Orta"))
        self.comboBox_place.setItemText(3, _translate("Form", "Orta Sol"))
        self.comboBox_place.setItemText(4, _translate("Form", "Orta Sağ"))
        self.comboBox_place.setItemText(5, _translate("Form", "Orta Orta"))
        self.comboBox_place.setItemText(6, _translate("Form", "Alt Sol"))
        self.comboBox_place.setItemText(7, _translate("Form", "Alt Sağ"))
        self.comboBox_place.setItemText(8, _translate("Form", "Alt Orta"))
        self.pushButton_addFiligran.setText(_translate("Form", "Filigran Ekle"))
        self.pushButton_save.setText(_translate("Form", "Kaydet"))
        self.comboBox_font.setItemText(0, _translate("Form", "Times-Roman"))
        self.comboBox_font.setItemText(1, _translate("Form", "Courier"))
        self.comboBox_font.setItemText(2, _translate("Form", "Helvetica"))
        self.pushButton_selectColor.setText(_translate("Form", "Renk Seç"))
