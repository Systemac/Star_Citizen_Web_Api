# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_main_window(object):
    def setupUi(self, main_window):
        if main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.setWindowModality(Qt.NonModal)
        main_window.resize(500, 554)
        main_window.setMinimumSize(QSize(500, 554))
        self.gridLayout = QGridLayout(main_window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_load_friendlist = QPushButton(main_window)
        self.btn_load_friendlist.setObjectName(u"btn_load_friendlist")

        self.gridLayout.addWidget(self.btn_load_friendlist, 12, 0, 1, 2)

        self.te_log = QTextEdit(main_window)
        self.te_log.setObjectName(u"te_log")
        self.te_log.setMinimumSize(QSize(0, 100))
        self.te_log.setMaximumSize(QSize(16777215, 400))
        self.te_log.setReadOnly(True)

        self.gridLayout.addWidget(self.te_log, 17, 0, 1, 2)

        self.label_2 = QLabel(main_window)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 15, 0, 1, 1)

        self.le_password_second = QLineEdit(main_window)
        self.le_password_second.setObjectName(u"le_password_second")
        self.le_password_second.setMinimumSize(QSize(40, 20))
        font = QFont()
        font.setKerning(True)
        self.le_password_second.setFont(font)
        self.le_password_second.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.le_password_second.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.le_password_second, 6, 1, 1, 1)

        self.btn_add_orga_first_account = QPushButton(main_window)
        self.btn_add_orga_first_account.setObjectName(u"btn_add_orga_first_account")
        self.btn_add_orga_first_account.setMinimumSize(QSize(137, 23))

        self.gridLayout.addWidget(self.btn_add_orga_first_account, 14, 0, 1, 1)

        self.btn_connection_second_account = QPushButton(main_window)
        self.btn_connection_second_account.setObjectName(u"btn_connection_second_account")

        self.gridLayout.addWidget(self.btn_connection_second_account, 9, 0, 1, 1)

        self.le_password_first = QLineEdit(main_window)
        self.le_password_first.setObjectName(u"le_password_first")
        self.le_password_first.setMinimumSize(QSize(40, 20))
        self.le_password_first.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.le_password_first.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.le_password_first, 1, 1, 1, 1)

        self.le_login_second = QLineEdit(main_window)
        self.le_login_second.setObjectName(u"le_login_second")
        self.le_login_second.setMinimumSize(QSize(40, 20))
        self.le_login_second.setMaxLength(50)

        self.gridLayout.addWidget(self.le_login_second, 6, 0, 1, 1)

        self.btn_add_list_link = QPushButton(main_window)
        self.btn_add_list_link.setObjectName(u"btn_add_list_link")

        self.gridLayout.addWidget(self.btn_add_list_link, 15, 1, 1, 1)

        self.label = QLabel(main_window)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btn_connection_first_account = QPushButton(main_window)
        self.btn_connection_first_account.setObjectName(u"btn_connection_first_account")

        self.gridLayout.addWidget(self.btn_connection_first_account, 3, 0, 1, 1)

        self.cmb_choice_universe_second = QComboBox(main_window)
        self.cmb_choice_universe_second.addItem("PU")
        self.cmb_choice_universe_second.addItem("PTU")
        self.cmb_choice_universe_second.setObjectName(u"cmb_choice_universe_second")

        self.gridLayout.addWidget(self.cmb_choice_universe_second, 7, 0, 1, 1)

        self.le_add_orga = QLineEdit(main_window)
        self.le_add_orga.setObjectName(u"le_add_orga")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_add_orga.sizePolicy().hasHeightForWidth())
        self.le_add_orga.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_add_orga, 13, 0, 1, 2)

        self.le_connect_first_account = QLineEdit(main_window)
        self.le_connect_first_account.setObjectName(u"le_connect_first_account")
        self.le_connect_first_account.setMinimumSize(QSize(0, 20))
        self.le_connect_first_account.setReadOnly(True)

        self.gridLayout.addWidget(self.le_connect_first_account, 3, 1, 1, 1)

        self.cmb_choice_universe_first = QComboBox(main_window)
        self.cmb_choice_universe_first.addItem("PU")
        self.cmb_choice_universe_first.addItem("PTU")
        self.cmb_choice_universe_first.setObjectName(u"cmb_choice_universe_first")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cmb_choice_universe_first.sizePolicy().hasHeightForWidth())
        self.cmb_choice_universe_first.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.cmb_choice_universe_first, 2, 0, 1, 1)

        self.te_link = QTextEdit(main_window)
        self.te_link.setObjectName(u"te_link")
        self.te_link.setAcceptRichText(False)

        self.gridLayout.addWidget(self.te_link, 16, 0, 1, 2)

        self.btn_add_orga_second_account = QPushButton(main_window)
        self.btn_add_orga_second_account.setObjectName(u"btn_add_orga_second_account")
        self.btn_add_orga_second_account.setMinimumSize(QSize(137, 23))

        self.gridLayout.addWidget(self.btn_add_orga_second_account, 14, 1, 1, 1)

        self.label_3 = QLabel(main_window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.le_connect_second_account = QLineEdit(main_window)
        self.le_connect_second_account.setObjectName(u"le_connect_second_account")
        self.le_connect_second_account.setMinimumSize(QSize(0, 20))
        self.le_connect_second_account.setReadOnly(True)

        self.gridLayout.addWidget(self.le_connect_second_account, 9, 1, 1, 1)

        self.le_login_first = QLineEdit(main_window)
        self.le_login_first.setObjectName(u"le_login_first")
        self.le_login_first.setMinimumSize(QSize(40, 20))
        self.le_login_first.setMaxLength(50)

        self.gridLayout.addWidget(self.le_login_first, 1, 0, 1, 1)

        QWidget.setTabOrder(self.le_login_first, self.le_password_first)
        QWidget.setTabOrder(self.le_password_first, self.cmb_choice_universe_first)
        QWidget.setTabOrder(self.cmb_choice_universe_first, self.btn_connection_first_account)
        QWidget.setTabOrder(self.btn_connection_first_account, self.le_login_second)
        QWidget.setTabOrder(self.le_login_second, self.le_password_second)
        QWidget.setTabOrder(self.le_password_second, self.cmb_choice_universe_second)
        QWidget.setTabOrder(self.cmb_choice_universe_second, self.btn_connection_second_account)
        QWidget.setTabOrder(self.btn_connection_second_account, self.le_connect_second_account)
        QWidget.setTabOrder(self.le_connect_second_account, self.btn_load_friendlist)
        QWidget.setTabOrder(self.btn_load_friendlist, self.le_connect_first_account)
        QWidget.setTabOrder(self.le_connect_first_account, self.te_log)
        QWidget.setTabOrder(self.te_log, self.btn_add_orga_first_account)
        QWidget.setTabOrder(self.btn_add_orga_first_account, self.btn_add_orga_second_account)
        QWidget.setTabOrder(self.btn_add_orga_second_account, self.le_add_orga)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Star Citizen Friendlist Management", None))
        self.btn_load_friendlist.setText(QCoreApplication.translate("main_window", u"--> Charge la liste d'amis du premier au second compte -->", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"Liste lien RSI des amis \u00e0 ajouter \u00e0 la friendlist", None))
        self.le_password_second.setPlaceholderText(QCoreApplication.translate("main_window", u"Mot de passe second compte", None))
        self.btn_add_orga_first_account.setText(QCoreApplication.translate("main_window", u"Ajout orga au premier compte", None))
        self.btn_connection_second_account.setText(QCoreApplication.translate("main_window", u"Connection second compte", None))
        self.le_password_first.setPlaceholderText(QCoreApplication.translate("main_window", u"Mot de passe premier compte", None))
        self.le_login_second.setPlaceholderText(QCoreApplication.translate("main_window", u"Login second compte", None))
        self.btn_add_list_link.setText(QCoreApplication.translate("main_window", u"Ajouter la liste de lien RSI", None))
        self.label.setText(QCoreApplication.translate("main_window", u"Premier Compte", None))
        self.btn_connection_first_account.setText(QCoreApplication.translate("main_window", u"Connection premier compte", None))
        self.cmb_choice_universe_second.setItemText(0, QCoreApplication.translate("main_window", u"PU", None))
        self.cmb_choice_universe_second.setItemText(1, QCoreApplication.translate("main_window", u"PTU", None))

        self.le_add_orga.setPlaceholderText(QCoreApplication.translate("main_window", u"TAG de l'orga \u00e0 ajouter", None))
        self.cmb_choice_universe_first.setItemText(0, QCoreApplication.translate("main_window", u"PU", None))
        self.cmb_choice_universe_first.setItemText(1, QCoreApplication.translate("main_window", u"PTU", None))

        self.te_link.setPlaceholderText(QCoreApplication.translate("main_window", u"Coller ici la liste de lien que vous avez copi\u00e9...", None))
        self.btn_add_orga_second_account.setText(QCoreApplication.translate("main_window", u"Ajout orga au second compte", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"Second Compte", None))
        self.le_login_first.setPlaceholderText(QCoreApplication.translate("main_window", u"Login premier compte", None))
    # retranslateUi

