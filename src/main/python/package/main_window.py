from PySide2 import QtWidgets
from time import sleep
import concurrent.futures

from package.api.custom_ui.window_ui import Ui_main_window
from package.api.test_api import StarCitizenWebApi


class MainWindow(Ui_main_window, QtWidgets.QWidget):
    def __init__(self, ctx):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Star Citizen Friendlist Management")
        self.setupUi(self)
        self.ctx = ctx
        self.modify_widget()
        self.setup_connections()
        self.first_account = None
        self.second_account = None
        self.temp = StarCitizenWebApi(universe="PU")
        self.le_connect_first_account.setText("Non connecté")
        self.le_connect_first_account.setStyleSheet("color: red;")
        self.le_connect_second_account.setText("Non connecté")
        self.le_connect_second_account.setStyleSheet("color: red;")

    def setup_connections(self):
        self.btn_add_orga_first_account.clicked.connect(self.add_orga_first_account)
        self.btn_add_orga_second_account.clicked.connect(self.add_orga_second_account)
        #self.btn_reverse_account.clicked.connect(self.reverse)
        self.btn_load_friendlist.clicked.connect(self.load_friendlist)
        self.btn_connection_first_account.clicked.connect(self.login_account_first_account)
        self.btn_connection_second_account.clicked.connect(self.login_account_second_account)
        self.btn_add_list_link.clicked.connect(self.add_list_link)

    def modify_widget(self):
        css_file = self.ctx.get_resource('style.css')
        with open(css_file, 'r') as f:
            self .setStyleSheet(f.read())

    # END UI

    def add_orga_first_account(self):
        fields = [self.le_login_first, self.le_password_first, self.le_add_orga]
        if not all([field.text() for field in fields]):
            self.te_log.append("Tous les champs ne sont pas remplis...")
        else:
            response, mb = self.temp.lst_orga(self.le_add_orga.text())
            #print(response)
            #print(mb)
            if response:
                self.te_log.append(f"Vous allez ajouté les membres de {self.le_add_orga.text()} à votre "
                                   f"liste d'amis...")
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    results = [executor.submit(self.first_account.add_friend, i) for i in mb]
                    for f in concurrent.futures.as_completed(results):
                        self.te_log.append(f.result())
                '''for i in mb:
                    self.te_log.append(self.first_account.add_friend(i))'''
                #self.te_log.append(result)
                self.te_log.append("Membres ajoutés !")
            else:
                self.te_log.append(f"Le tag rentré ne corresponde à aucune orga, voici le résultat de la recherche "
                                   f"associé, rentrez le tag de l'orga que vous souhaitez suivre...\n")
                self.te_log.append(mb)

    def add_orga_second_account(self):
        fields = [self.le_login_second, self.le_password_second, self.le_add_orga]
        if not all([field.text() for field in fields]):
            self.te_log.append("Tous les champs ne sont pas remplis...")
        else:
            response, mb = self.temp.lst_orga(self.le_add_orga.text())
            #print(response)
            #print(mb)
            if response:
                self.te_log.append(f"Vous allez ajouté les membres de {self.le_add_orga.text()} à votre "
                                   f"liste d'amis...")
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    results = [executor.submit(self.second_account.add_friend, i) for i in mb]
                    for f in concurrent.futures.as_completed(results):
                        self.te_log.append(f.result())
                '''for i in mb:
                    self.te_log.append(self.second_account.add_friend(i))'''
                self.te_log.append("Membres ajoutés !")
            else:
                self.te_log.append(f"Le tag rentré ne corresponde à aucune orga, voici le résultat de la recherche "
                                   f"associé, rentrez le tag de l'orga que vous souhaitez suivre...\n")
                self.te_log.append(mb)

    def login_account_first_account(self):
        fields = [self.le_login_first, self.le_password_first]
        if not all([field.text() for field in fields]):
            self.te_log.append("Tous les champs ne sont pas remplis...")
        else:
            dev_name = dev_type = ""
            self.te_log.append("Connexion en cours...")
            self.first_account = StarCitizenWebApi(universe=self.cmb_choice_universe_first.currentText())
            response = self.first_account.login(self.le_login_first.text(), self.le_password_first.text())
            if response == 'ErrMultiStepRequired':
                code, resultat = QtWidgets.QInputDialog.getText(self,
                                                                "Entrez votre code double authentification", "Code : ")
                retour_code, dev_type, dev_name = self.first_account.multi_step(int(code))
                while not retour_code:
                    self.te_log.append("Mauvais code !!!")
                    code, resultat = QtWidgets.QInputDialog.getText(self,
                                                                    "Entrez votre code double authentification",
                                                                    "Code : ")
                    if self.first_account.multi_step(int(code), dev_type=dev_type, dev_name=dev_name)[0]:
                        break
                    else:
                        retour_code, dev_type, dev_name = self.first_account.multi_step(int(code), dev_type=dev_type,
                                                                                        dev_name=dev_name)
                self.te_log.append("Vous êtes connecté !")
                self.le_connect_first_account.setText("Connecté")
                self.le_connect_first_account.setStyleSheet("color: green;")
            elif response == 'Erreur':
                self.te_log.append("Erreur de connexion")
            elif response == "Captcha":
                self.te_log.append("Trop de tentative, logguer-vous depuis votre naviguateur et rentrer le captcha")
            elif response == "WrongPassword":
                self.te_log.append("Mauvais login ou mot de passe...")
            elif response == "OK":
                self.te_log.append("Vous êtes connecté !")
                self.le_connect_first_account.setText("Connecté")
                self.le_connect_first_account.setStyleSheet("color: green;")

    def login_account_second_account(self):
        fields = [self.le_login_second, self.le_password_second]
        if not all([field.text() for field in fields]):
            self.te_log.append("Tous les champs ne sont pas remplis...")
        else:
            self.te_log.append("Connexion en cours...")
            self.second_account = StarCitizenWebApi(universe=self.cmb_choice_universe_second.currentText())
            response = self.second_account.login(self.le_login_second.text(), self.le_password_second.text())
            if response == 'ErrMultiStepRequired':
                code, resultat = QtWidgets.QInputDialog.getText(self,
                                                                "Entrez votre code double authentification", "Code : ")
                retour_code, dev_type, dev_name = self.second_account.multi_step(int(code))
                while not retour_code:
                    self.te_log.append("Mauvais code !!!")
                    code, resultat = QtWidgets.QInputDialog.getText(self,
                                                                    "Entrez votre code double authentification",
                                                                    "Code : ")
                    if self.second_account.multi_step(int(code), dev_type=dev_type, dev_name=dev_name)[0]:
                        break
                    else:
                        retour_code, dev_type, dev_name = self.second_account.multi_step(int(code), dev_type=dev_type,
                                                                                        dev_name=dev_name)
                self.te_log.append("Vous êtes connecté !")
                self.le_connect_second_account.setText("Connecté")
                self.le_connect_second_account.setStyleSheet("color: green;")
            elif response == 'Erreur':
                self.te_log.append("Erreur de connexion")
            elif response == "Captcha":
                self.te_log.append("Trop de tentative, logguer-vous depuis votre naviguateur et rentrer le captcha")
            elif response == "WrongPassword":
                self.te_log.append("Mauvais login ou mot de passe...")
            elif response == "OK":
                self.te_log.append("Vous êtes connecté !")
                self.le_connect_second_account.setText("Connecté")
                self.le_connect_second_account.setStyleSheet("color: green;")

    def reverse(self):
        fields = [self.le_login_first, self.le_password_first, self.le_login_second, self.le_password_second]
        if not all([field.text() for field in fields]):
            self.te_log.append("Tous les champs ne sont pas remplis...")
        else:
            temp = self.le_login_first.text()
            self.le_login_first.setText(self.le_login_second.text())
            self.le_login_second.setText(temp)

            temp = self.le_password_first.text()
            self.le_password_first.setText(self.le_password_second.text())
            self.le_password_second.setText(temp)

            temp = self.cmb_choice_universe_first.currentText()
            self.cmb_choice_universe_first.setCurrentText(self.cmb_choice_universe_second.currentText())
            self.cmb_choice_universe_second.setCurrentText(temp)

            self.temp = self.first_account
            self.first_account = self.second_account
            self.second_account = self.temp
            self.temp = StarCitizenWebApi(universe="PU")

    def load_friendlist(self):
        fields = [self.le_login_first, self.le_password_first, self.le_login_second, self.le_password_second]
        if not all([field.text() for field in fields]):
            self.te_log.append("Tous les champs ne sont pas remplis...")
        else:
            self.te_log.append("Chargement de la liste d'amis...")
            sleep(0.5)
            leninist, friendlist = self.first_account.listed_ami()
            self.te_log.append(f"Vous allez ajouter potentiellement {leninist} amis à la liste d'amis du second "
                               f"compte.")
            print(friendlist)
            '''for i in friendlist:
                self.te_log.append(self.second_account.add_friend(i))
                sleep(0.2)
            self.te_log.append("Membres ajoutés !")'''
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = [executor.submit(self.second_account.add_friend, i) for i in friendlist]
                for f in concurrent.futures.as_completed(results):
                    self.te_log.append(f.result())

    def add_list_link(self):
        fields = [self.le_login_first, self.le_password_first]
        if not all([field.text() for field in fields]):
            self.te_log.append("Tous les champs ne sont pas remplis...")
        elif self.le_connect_first_account.text() != "Connecté":
            self.te_log.append("Merci de vous connecter avant d'ajouter la liste de liens...")
        else:
            liste = []
            link = self.te_link.toPlainText()
            for i in link.split("\n"):
                name = i.replace("https://robertsspaceindustries.com/citizens/",'')
                if i != '':
                    liste.append(name)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = [executor.submit(self.first_account.add_friend, i) for i in liste]
                for f in concurrent.futures.as_completed(results):
                    self.te_log.append(f.result())
            self.te_link.clear()