'''
Drivers para uso do Selenium -- conecta o script com o navegador
Chrome:	https://chromedriver.chromium.org/downloads
Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:	https://github.com/mozilla/geckodriver/releases
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/
'''

from selenium import webdriver
from time import sleep  # usado para dar pausa em cada acontecimento do script
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FirefoxAuto:  # caso firefox não esteja atualizado, pode dar erro
    def __init__(self):
        self.driver = webdriver.Firefox()

    # classe para acessar o site
    def acessa(self, site):
        self.driver.get(site)

    def sair(self):  # sair do site
        self.driver.quit()

    def clica_sign_in(self):
        try:
            # para usar o find_element nessa versão é necessário definir o que quer procurar no site:
            # se vai ser por texto -- By.LINK_TEXT, "Texto para procurar", também tem o PARTIAL_LINK_TEXT
            # se vai ser por cssSelector -- By.CSS_SELECTOR, "td.subtabTxtNsel>a.subtabTxtNsel[tag='a']"
            # se vai ser pelo xPath -- By.XPATH, "//td[@class='subtabTxtNsel']/a[@class='subtabTxtNsel' and contains(.,'Specifications')]"
            btn_sign_in = self.driver.find_element(By.LINK_TEXT, "Sign in")
            btn_sign_in.click()
        except Exception as e:
            print("Erro:", e)

    def faz_login(self):
        try:
            input_login = self.driver.find_element(By.ID, 'login_field')
            input_password = self.driver.find_element(By.ID, 'password')
            btn_login = self.driver.find_element(By.NAME, 'commit')  # botão de fazer login

            input_login.send_keys('___USER LOGIN___')
            input_password.send_keys('___PASSWORD___')
            sleep(5)
            btn_login.click()

        except Exception as e:
            print("Erro ao fazer Login:", e)

    def clica_perfil(self):
        try:
            perfil = self.driver.find_element(By.CSS_SELECTOR, "body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details")
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            perfil = self.driver.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro ao fazer Log Out:', e)

    def verifica_usuario(self, usuario):
        profile_link = self.driver.find_element(By.CLASS_NAME, 'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html  # para verificar se o usuário passado como atributo está certo
        print('Usuário Correto')


class ChromeAuto:
    def __init__(self):  # construtor
        # self.driver = driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome()
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')  # Criar um perfil padrão para não ter erro na execução
        # self.chrome = webdriver.Chrome(  # Selenium < 3.x
        #     self.driver_path,
        #     options=self.options
        # )

    # classe para acessar o site
    def acessa(self, site):
        self.driver.get(site)

    def sair(self):  # sair do site
        self.driver.quit()

    def clica_sign_in(self):
        try:
            # para usar o find_element nessa versão é necessário definir o que quer procurar no site:
            # se vai ser por texto -- By.LINK_TEXT, "Texto para procurar", também tem o PARTIAL_LINK_TEXT
            # se vai ser por cssSelector -- By.CSS_SELECTOR, "td.subtabTxtNsel>a.subtabTxtNsel[tag='a']"
            # se vai ser pelo xPath -- By.XPATH, "//td[@class='subtabTxtNsel']/a[@class='subtabTxtNsel' and contains(.,'Specifications')]"
            btn_sign_in = self.driver.find_element(By.LINK_TEXT, "Sign in")
            btn_sign_in.click()
        except Exception as e:
            print("Erro:", e)

    def faz_login(self):
        try:
            input_login = self.driver.find_element(By.ID, 'login_field')
            input_password = self.driver.find_element(By.ID, 'password')
            btn_login = self.driver.find_element(By.NAME, 'commit')  # botão de fazer login

            input_login.send_keys('___USER LOGIN___')
            input_password.send_keys('___PASSWORD___')
            sleep(5)
            btn_login.click()

        except Exception as e:
            print("Erro ao fazer Login:", e)

    def clica_perfil(self):
        try:
            perfil = self.driver.find_element(By.CSS_SELECTOR,
                                              "body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details")
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            perfil = self.driver.find_element(By.CSS_SELECTOR,
                                              'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro ao fazer Log Out:', e)

    def verifica_usuario(self, usuario):
        profile_link = self.driver.find_element(By.CLASS_NAME, 'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html  # para verificar se o usuário passado como atributo está certo
        print('Usuário Correto')


if __name__ == '__main__':
    firefox = FirefoxAuto()  # Do Chrome para o Firefox muda apenas o driver.
    firefox.acessa('https://github.com/')
    firefox.clica_sign_in()
    sleep(2)
    firefox.faz_login()  # Necessário definir login e senha no método para fazer acesso!
    sleep(5)
    firefox.clica_perfil()
    sleep(5)
    firefox.verifica_usuario('___NOME DO USUARIO LOGADO___')
    sleep(5)
    firefox.faz_logout()
    sleep(10)
    firefox.sair()
