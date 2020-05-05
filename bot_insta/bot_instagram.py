#[PT]Importes necessários!
#[EN]Imports required!
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
import getpass_ak

class InstagramBot:
    def __init__(self, username, password, usernameProfile):
        self.username = username
        self.password = password
        self.usernameProfile = usernameProfile
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.bot = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    #[PT]Script para pegar Instagram e seguir referências
    #[EN]Script to get Instagram and follow reference
    def getProfile(self):
        bot = self.bot
        #[PT]Navega \pela página do Instagram
        #[EN]Browse the Instagram page
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)

        #[PT]Busca pelo inputs do email e senha
        #[EN]Search for email and password inputs
        username = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)

        #[PT]Espero 1 minuto para pressionar o ENTER
        #[EN]I wait 1 minute to press ENTER
        time.sleep(1)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)

        #[PT]Espero mais 3 minutos para entrar
        #[EN]I wait more 3 minute to for login
        time.sleep(3)
        #[PT]Navega pela paginá do Instagram
        #[EN]Browse the Instagram page
        bot.get('https://instagram.com/' + self.usernameProfile)
        time.sleep(3)

        #[PT]Pego o numero de seguidores atual
        #[EN]I take the current number of followers
        numberFollows = bot.find_elements_by_class_name('g47SY')
        time.sleep(3)

        #[PT]Transformo em texto e depois em inteiro
        #[EN]I convert it into text and then in int
        numberFollows = numberFollows[1].text
        if '.' in numberFollows:
            numberFollows = int(numberFollows.replace('.',''))
        else:
            numberFollows = int(numberFollows.replace(',',''))


        #[PT]Clico nos seguidores
        #[EN]Click in followes
        bot.find_element_by_xpath('//a[@href="/' + self.usernameProfile + '/followers/"]').click()
        time.sleep(3)

        #[PT]Pego o numero de botões que contém seguir
        #[EN]I take the number of buttons that contains follow

        follow = bot.find_elements_by_xpath("//button[contains(text(), 'Follow')]")

        time.sleep(2)

        #[PT]Pego a janela onde contém os seguidores para depois rolar o scroll
        #[EN]I take the window containing the followers and then scroll down
        popup = bot.find_element_by_class_name('isgrP')
        time.sleep(2)

        #[PT]O codigo abaixo é para o robor não seguir todos e evitar bloqueios.
        #[EN]The code below is for the robot not to follow all and avoid blocking.
        if(numberFollows > 400 and numberFollows < 1000):
            numberFollows = int(numberFollows * 0.10)
        elif(numberFollows > 1000):
            numberFollows = int(numberFollows * 0.02)
        elif(numberFollows > 100 and numberFollows < 400):
            numberFollows = int(numberFollows * 0.2)

        #[PT]Os controladores para terminar o laço e retonar a quantidade de Clicks
        #[EN]The controllers to end the loop and return the number of Clicks
        i = 0
        index = 0
        quantClick=0


        while index < numberFollows:
            #[PT]Executa script para rola a página.
            #[EN]Run script to scroll the page.
            bot.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', popup)
            time.sleep(2)

            #[PT]Pega todos os botões que contém o nome seguir novamente
            #[EN]Get all the buttons that contain the name follow again
            followIn = bot.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")
            time.sleep(2)

            #[PT]Se houver alguém para seguir ele entra no "for"
            #[EN]If there is someone to follow he enters the "for"
            if(len(followIn) != 0):
                for follower in followIn:
                    #[PT]Executa a ação do click no botão seguir
                    #[EN]Performs the click action on the follow button
                    bot.execute_script("arguments[0].click();", follower)
                    time.sleep(1)
                    quantClick += 1
            #[PT]"follow" recene mais novos botões ao rolar o caixa
            #[EN]"follow" receive more new buttons when rolling the cashier
            follow += bot.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")

            #[PT]Se o index chegar a quantidade de seguidores o laço para
            #[EN]If the index reaches the number of followers, the loop for
            index += len(follow)
        bot.quit()
        #[PT]Retorna a quantidade de clicks
        #[EN]Returns the number of clicks
        return "Finalizado. O robo seguiu {}".format(quantClick)

    #[PT]Script para comentar em cadeia
    #[EN]String comment script
    def commentPost(self, comment, limit):
        bot = self.bot
        #[PT]Navega \pela página do Instagram
        #[EN]Browse the Instagram page
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)

        #[PT]Busca pelo inputs do email e senha
        #[EN]Search for email and password inputs
        username = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)

        #[PT]Espero 1 minuto para pressionar o ENTER
        #[EN]I wait 1 minute to press ENTER
        time.sleep(1)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)

        #[PT]Espero mais 3 minutos para entrar
        #[EN]I wait more 3 minute to for login
        time.sleep(3)

        #[PT]Entra na página do usuário
        #[EN]Enter user page
        bot.get('https://instagram.com/' + self.usernameProfile)
        time.sleep(3)

        #[PT]Pega todas as fotos do feed
        #[EN]Get all photos from the feed
        divPhotos = bot.execute_script("return document.getElementsByClassName('KL4Bh')")
        quantComment = 0

        #[PT]Passeia pelas fotos do feed
        #[EN]Stroll through the photos in the feed
        for photos in range(limit):

            #[PT]Clica na foto
            #[EN]Click in photo
            bot.execute_script('arguments[0].click()', divPhotos[photos])
            time.sleep(2)

            #[PT]Clica no botão do gostei!
            #[EN]Click in button like
            bot.execute_script('var buttom = document.getElementsByClassName("wpO6b"); buttom[1].click()')
            time.sleep(2)

            #[PT]Pego o textarea responsável pelo comentário and click
            #[EN]I take the textarea responsible for the comment
            commentArea = bot.find_element_by_class_name('Ypffh')
            commentArea.click()
            time.sleep(3)
            commentArea = bot.find_element_by_class_name('Ypffh')
            commentArea.click()
            time.sleep(3)

            #[PT]Passo o comentário para o textarea e clico em enviar
            #[EN]I pass the comment to textarea and click send
            commentArea.send_keys(comment)
            time.sleep(0.6)
            bot.find_element_by_xpath('//button[@type="submit"]').click()
            time.sleep(3)

            quantComment+=1
        bot.close()
        time.sleep(0.5)
        #[PT]Retorno a quantidade de comentários eventualmente feitos
        #[EN]Return the amount of comments eventually made
        return 'Você comentou em {}'.format(quantComment)
