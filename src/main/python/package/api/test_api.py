import time

import requests
from bs4 import BeautifulSoup as bs
from package.api.constants import SC_DIR


class StarCitizenWebApi:

    def __init__(self, universe):
        self.token_rsi = ''
        self.nickname = ''
        self.cookie = None
        self.URL_PU_BASE = 'https://robertsspaceindustries.com/'
        self.URL_PTU_BASE = 'https://ptu.cloudimperiumgames.com/'
        self.URL_SIGNIN = 'api/account/signin'
        self.URL_ADD = 'api/contacts/add'
        self.URL_ERASE = 'api/contacts/erase'
        self.URL_ORGA = 'api/orgs/getOrgMembers'
        self.URL_MULTISTEP = 'api/account/signinMultiStep'
        self.URL_LIST = 'api/contacts/list'
        self.URL_FIND_ORGA = 'api/orgs/getOrgs'
        self.response = None
        if universe == 'PU':
            self.url_base = self.URL_PU_BASE
            self.key_token_rsi = 'X-Rsi-Token'
            self.key_login_token_rsi = 'Rsi-Token'
        elif universe == 'PTU':
            self.url_base = self.URL_PTU_BASE
            self.key_token_rsi = 'X-Rsi-PTU-Token'
            self.key_login_token_rsi = 'Rsi-PTU-Token'

    def login(self, username, mdp):
        print(self.url_base)
        params = {
            'username': username,
            'password': mdp,
            'remember': 'null'
        }
        self.response = requests.post(self.url_base + self.URL_SIGNIN, params=params)
        print(self.response.cookies.get_dict())
        self.token_rsi = self.response.cookies.get_dict()[self.key_login_token_rsi]
        self.cookie = self.response.cookies
        print(self.response.json())
        if self.response.json()['msg'] == "OK":
            self.nickname = self.response.json()['data']['nickname']
            print("Vous etes connecté")
            return "OK"
            # print(response.cookies)
            # print(self.cookie)
        elif self.response.json()['code'] == 'ErrMultiStepRequired':
            print('ErrMultiStepRequired')
            return 'ErrMultiStepRequired'
        elif self.response.json()['code'] == 'ErrCaptchaRequired':
            return 'Captcha'
        elif self.response.json()['code'] == 'ErrWrongPassword_username':
            return 'WrongPassword'
        elif self.response.json()['success'] == 0:
            print("Erreur de connexion")
            return 'Erreur'
        # print(response.cookies.get_dict())
        print(f'Token RSI : {self.token_rsi}')

    def multi_step(self, factor, dev_type=None, dev_name=None):
        if dev_name is None and dev_type is None:
            dev_type = self.response.json()['data']['device_type']
            dev_name = self.response.json()['data']['device_name']
        print("Double authentification requise : ")
        # factor = input('Code 2 facteur : ')
        params = {
            'code': factor,
            'device_name': dev_name,
            'device_type': dev_type,
            'duration': 'month'
        }
        headers = {
            self.key_token_rsi: self.token_rsi}
        self.response = requests.post(self.url_base + self.URL_MULTISTEP,
                                      params=params, headers=headers, cookies=self.cookie)
        print(self.response.json())
        # print(response.cookies.get_dict())
        if self.response.json()['code'] == "OK":
            self.nickname = self.response.json()['data']['nickname']
            print("Vous etes connecté")
            return True, dev_type, dev_name
        elif self.response.json()['code'] == 'ErrMultiStepWrongCode':
            return False, dev_type, dev_name

    def listed_ami(self):
        friend_list = []
        headers = {
            'Referer': self.url_base,
            self.key_token_rsi: self.token_rsi,
        }
        self.response = requests.post(self.url_base + self.URL_LIST, headers=headers, cookies=self.cookie)
        print(self.response.json())
        long_page = self.response.json()['data']['pagecount']
        cursor = self.response.json()['data']['cursor']

        for page in range(long_page + 1):
            print(f'{cursor}')
            print(f'Page {page}')
            headers = {
                self.key_token_rsi: self.token_rsi,
                "page": str(page)
            }
            payload = {
                "page": str(page),
                "cursor": cursor
            }
            self.response = requests.post(self.url_base + self.URL_LIST, headers=headers,
                                          params=payload, cookies=self.cookie)
            cursor = self.response.json()['data']['cursor']
            nb_listed = len(self.response.json()['data']['resultset'])
            # friend_list.append(f'page {i}')
            print(f'Nombre de resultat : {nb_listed}')
            for pages in range(len(self.response.json()['data']['resultset'])):
                time.sleep(0.1)
                friend = self.response.json()['data']['resultset'][pages]['nickname']
                # print(f'{friend} est dans la liste ? {friend in friend_list}')
                if friend not in friend_list:
                    if friend is not self.nickname:
                        friend_list.append(friend)
        print(f'Vous avez {len(friend_list)} amis.')
        # print(friend_list)
        return len(friend_list), friend_list

    def add_friend(self, name_friend):
        headers = {
            'Origin': self.url_base,
            self.key_token_rsi: self.token_rsi,
            'Referer': f'{self.url_base}citizens/{name_friend}'
        }

        payload = {
            'nickname': name_friend,
        }

        response = requests.post(self.url_base + self.URL_ADD, headers=headers, cookies=self.cookie, params=payload)
        # print(response.json())
        if response.json()['success'] == 0:
            if response.json()['code'] == 'ErrCannotAddItself':
                return 'Vous ne pouvez pas vous ajouter...'
            elif response.json()['code'] == 'ErrNoAccountForNickname':
                return f'{name_friend} n\'est pas sur le serveur'
            elif response.json()['code'] == 'ErrValidationFailed':
                if response.json()['data']['properties']['contact_account_id'] == 'You already have this account ' \
                                                                                  'as a contact':
                    return f'{name_friend} est déjà dans vos contact'
        else:
            return f'{name_friend} ajouté avec succes !'

    def suppression_amis(self, name_friend):
        headers = {
            self.key_token_rsi: self.token_rsi,
            'Referer': f'{self.url_base}citizens/{name_friend}'
        }
        payload = {
            'nickname': name_friend,
        }
        response = requests.post(self.URL_ERASE, headers=headers, cookies=self.cookie, params=payload)
        if response.json()['code'] == 'ErrContactRelationNotFound':
            print(f'{name_friend} n\'était pas dans votre liste d\'amis. ')
        else:
            print(f'{name_friend} supprimé avec succès. ')

    def listing_orga(self, tag_orga):
        headers = {
            self.key_token_rsi: self.token_rsi,
            'Referer': f'{self.url_base}orgs/{tag_orga}/members'
        }
        payload = {
            'page': '1',
            'symbol': tag_orga
        }
        response = requests.post(self.URL_ORGA, headers=headers, params=payload)
        print(response.json())

    def lst_orga(self, tag_orga):
        p = 1
        nom_orga = ""
        list_membres = []
        headers = {
            'Referer': f'{self.URL_PU_BASE}orgs/{tag_orga}/members'
        }
        payload = {
            'page': p,
            'symbol': tag_orga
        }
        response = requests.post(self.URL_PU_BASE + self.URL_ORGA, headers=headers, params=payload)
        if response.json()['code'] == 'ErrInvalidOrganization':
            payload = {
                'search': tag_orga
            }
            response = requests.post(self.URL_PU_BASE + self.URL_FIND_ORGA, params=payload)
            soup = bs(response.json()['data']['html'], 'html.parser')
            for item in soup.find_all('a'):
                # print(f"{item}")
                nom_orga += f"Nom de l'orga : {item.h3.text}\n"
                tag = item.get("href").replace('/orgs/', '')
                nom_orga += f'TAG : {tag} \n\n'
            return False, nom_orga
        nb_membres = response.json()['data']['totalrows']
        while len(list_membres) < nb_membres:
            headers = {
                'Referer': f'{self.URL_PU_BASE}orgs/{tag_orga}/members'
            }
            payload = {
                'page': p,
                'symbol': tag_orga
            }
            response = requests.post(self.URL_PU_BASE + self.URL_ORGA, headers=headers, params=payload)
            soup = bs(response.json()['data']['html'], 'html.parser')
            for link in soup.find_all('a'):
                t = link.get('href').replace('/citizens/', '')
                if t not in list_membres:
                    if t != self.nickname:
                        list_membres.append(t)
            p += 1
        # print(list_membres)
        #print(len(list_membres))
        return True, list_membres
