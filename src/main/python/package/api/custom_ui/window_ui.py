# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_ui.ui',
# licensing of 'window_ui.ui' applies.
#
# Created: Mon Jan 20 15:27:24 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowModality(QtCore.Qt.NonModal)
        main_window.resize(500, 484)
        main_window.setMinimumSize(QtCore.QSize(500, 484))
        self.gridLayout = QtWidgets.QGridLayout(main_window)
        self.gridLayout.setObjectName("gridLayout")
        self.le_login_first = QtWidgets.QLineEdit(main_window)
        self.le_login_first.setMinimumSize(QtCore.QSize(40, 20))
        self.le_login_first.setMaxLength(50)
        self.le_login_first.setObjectName("le_login_first")
        self.gridLayout.addWidget(self.le_login_first, 1, 0, 1, 1)
        self.le_password_second = QtWidgets.QLineEdit(main_window)
        self.le_password_second.setMinimumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        self.le_password_second.setFont(font)
        self.le_password_second.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.le_password_second.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password_second.setObjectName("le_password_second")
        self.gridLayout.addWidget(self.le_password_second, 6, 1, 1, 1)
        self.cmb_choice_universe_first = QtWidgets.QComboBox(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_choice_universe_first.sizePolicy().hasHeightForWidth())
        self.cmb_choice_universe_first.setSizePolicy(sizePolicy)
        self.cmb_choice_universe_first.setObjectName("cmb_choice_universe_first")
        self.cmb_choice_universe_first.addItem("")
        self.cmb_choice_universe_first.addItem("")
        self.gridLayout.addWidget(self.cmb_choice_universe_first, 2, 0, 1, 1)
        self.btn_load_friendlist = QtWidgets.QPushButton(main_window)
        self.btn_load_friendlist.setObjectName("btn_load_friendlist")
        self.gridLayout.addWidget(self.btn_load_friendlist, 12, 0, 1, 2)
        self.le_connect_first_account = QtWidgets.QLineEdit(main_window)
        self.le_connect_first_account.setMinimumSize(QtCore.QSize(0, 20))
        self.le_connect_first_account.setReadOnly(True)
        self.le_connect_first_account.setObjectName("le_connect_first_account")
        self.gridLayout.addWidget(self.le_connect_first_account, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(main_window)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(main_window)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.btn_add_orga_second_account = QtWidgets.QPushButton(main_window)
        self.btn_add_orga_second_account.setMinimumSize(QtCore.QSize(137, 23))
        self.btn_add_orga_second_account.setObjectName("btn_add_orga_second_account")
        self.gridLayout.addWidget(self.btn_add_orga_second_account, 15, 1, 1, 1)
        self.le_connect_second_account = QtWidgets.QLineEdit(main_window)
        self.le_connect_second_account.setMinimumSize(QtCore.QSize(0, 20))
        self.le_connect_second_account.setReadOnly(True)
        self.le_connect_second_account.setObjectName("le_connect_second_account")
        self.gridLayout.addWidget(self.le_connect_second_account, 9, 1, 1, 1)
        self.le_login_second = QtWidgets.QLineEdit(main_window)
        self.le_login_second.setMinimumSize(QtCore.QSize(40, 20))
        self.le_login_second.setMaxLength(50)
        self.le_login_second.setObjectName("le_login_second")
        self.gridLayout.addWidget(self.le_login_second, 6, 0, 1, 1)
        self.btn_connection_first_account = QtWidgets.QPushButton(main_window)
        self.btn_connection_first_account.setObjectName("btn_connection_first_account")
        self.gridLayout.addWidget(self.btn_connection_first_account, 3, 0, 1, 1)
        self.btn_connection_second_account = QtWidgets.QPushButton(main_window)
        self.btn_connection_second_account.setObjectName("btn_connection_second_account")
        self.gridLayout.addWidget(self.btn_connection_second_account, 9, 0, 1, 1)
        self.cmb_choice_universe_second = QtWidgets.QComboBox(main_window)
        self.cmb_choice_universe_second.setObjectName("cmb_choice_universe_second")
        self.cmb_choice_universe_second.addItem("")
        self.cmb_choice_universe_second.addItem("")
        self.gridLayout.addWidget(self.cmb_choice_universe_second, 7, 0, 1, 1)
        self.te_log = QtWidgets.QTextEdit(main_window)
        self.te_log.setMinimumSize(QtCore.QSize(0, 100))
        self.te_log.setMaximumSize(QtCore.QSize(16777215, 400))
        self.te_log.setReadOnly(True)
        self.te_log.setObjectName("te_log")
        self.gridLayout.addWidget(self.te_log, 16, 0, 1, 2)
        self.btn_reverse_account = QtWidgets.QPushButton(main_window)
        self.btn_reverse_account.setObjectName("btn_reverse_account")
        self.gridLayout.addWidget(self.btn_reverse_account, 13, 0, 1, 2)
        self.btn_add_orga_first_account = QtWidgets.QPushButton(main_window)
        self.btn_add_orga_first_account.setMinimumSize(QtCore.QSize(137, 23))
        self.btn_add_orga_first_account.setObjectName("btn_add_orga_first_account")
        self.gridLayout.addWidget(self.btn_add_orga_first_account, 15, 0, 1, 1)
        self.le_password_first = QtWidgets.QLineEdit(main_window)
        self.le_password_first.setMinimumSize(QtCore.QSize(40, 20))
        self.le_password_first.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.le_password_first.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password_first.setObjectName("le_password_first")
        self.gridLayout.addWidget(self.le_password_first, 1, 1, 1, 1)
        self.le_add_orga = QtWidgets.QLineEdit(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_add_orga.sizePolicy().hasHeightForWidth())
        self.le_add_orga.setSizePolicy(sizePolicy)
        self.le_add_orga.setObjectName("le_add_orga")
        self.gridLayout.addWidget(self.le_add_orga, 14, 0, 1, 2)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.le_login_first, self.le_password_first)
        main_window.setTabOrder(self.le_password_first, self.cmb_choice_universe_first)
        main_window.setTabOrder(self.cmb_choice_universe_first, self.btn_connection_first_account)
        main_window.setTabOrder(self.btn_connection_first_account, self.le_login_second)
        main_window.setTabOrder(self.le_login_second, self.le_password_second)
        main_window.setTabOrder(self.le_password_second, self.cmb_choice_universe_second)
        main_window.setTabOrder(self.cmb_choice_universe_second, self.btn_connection_second_account)
        main_window.setTabOrder(self.btn_connection_second_account, self.le_connect_second_account)
        main_window.setTabOrder(self.le_connect_second_account, self.btn_load_friendlist)
        main_window.setTabOrder(self.btn_load_friendlist, self.le_connect_first_account)
        main_window.setTabOrder(self.le_connect_first_account, self.te_log)
        main_window.setTabOrder(self.te_log, self.btn_add_orga_first_account)
        main_window.setTabOrder(self.btn_add_orga_first_account, self.btn_add_orga_second_account)
        main_window.setTabOrder(self.btn_add_orga_second_account, self.le_add_orga)
        main_window.setTabOrder(self.le_add_orga, self.btn_reverse_account)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtWidgets.QApplication.translate("main_window", "Star Citizen Friendlist Management", None, -1))
        self.le_login_first.setPlaceholderText(QtWidgets.QApplication.translate("main_window", "Login premier compte", None, -1))
        self.le_password_second.setPlaceholderText(QtWidgets.QApplication.translate("main_window", "Mot de passe second compte", None, -1))
        self.cmb_choice_universe_first.setItemText(0, QtWidgets.QApplication.translate("main_window", "PU", None, -1))
        self.cmb_choice_universe_first.setItemText(1, QtWidgets.QApplication.translate("main_window", "PTU", None, -1))
        self.btn_load_friendlist.setText(QtWidgets.QApplication.translate("main_window", "--> Charge la liste d\'amis du premier au second compte -->", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("main_window", "Premier Compte", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("main_window", "Second Compte", None, -1))
        self.btn_add_orga_second_account.setText(QtWidgets.QApplication.translate("main_window", "Ajout orga au second compte", None, -1))
        self.le_login_second.setPlaceholderText(QtWidgets.QApplication.translate("main_window", "Login second compte", None, -1))
        self.btn_connection_first_account.setText(QtWidgets.QApplication.translate("main_window", "Connection premier compte", None, -1))
        self.btn_connection_second_account.setText(QtWidgets.QApplication.translate("main_window", "Connection second compte", None, -1))
        self.cmb_choice_universe_second.setItemText(0, QtWidgets.QApplication.translate("main_window", "PU", None, -1))
        self.cmb_choice_universe_second.setItemText(1, QtWidgets.QApplication.translate("main_window", "PTU", None, -1))
        self.btn_reverse_account.setText(QtWidgets.QApplication.translate("main_window", "<-- Inverser les comptes-->", None, -1))
        self.btn_add_orga_first_account.setText(QtWidgets.QApplication.translate("main_window", "Ajout orga au premier compte", None, -1))
        self.le_password_first.setPlaceholderText(QtWidgets.QApplication.translate("main_window", "Mot de passe premier compte", None, -1))
        self.le_add_orga.setPlaceholderText(QtWidgets.QApplication.translate("main_window", "TAG de l\'orga à ajouter", None, -1))

