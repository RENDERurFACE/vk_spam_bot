from kivy.app import App 
from kivy.uix.button import Button 
import vk_api
import time 
import random 

class MyApp(App):
    def build(self):
        return Button(text = "СПАМИТЬ!",on_press = self.btn_press)

    def btn_press(self,instance):
        spambot_activate()






session = vk_api.VkApi(token = "vk1.a.F_IoO0x2JIz7H2QB5o2BiqLbLCbhXKR5rbzv_v9x1W7V31DAsMGln0-5SOERhtmdbvPmo8VxpDPTulO27B6ZsVSEwUgIF7QB3Hikuv3iCM5CrA1G4FLFTd9FmvGU7aOfwTx1qQTXuEung8tFAesM57pDgjCO5RYzWuJJOtww2bRLWZc7res8qkahushpCGAe")
vk =  session.get_api()


def spambot_activate():   
    nikita_lol =('Как у нашего Никиты ноги пахнут общепитом.\nКак у нашего Никиты всё болеет простатитом.\n Как у нашего Никиты Все черты лица размыты.\nКак из нашего Никиты Раздаётся: «Да иди ты!»\nКак у нашего Никиты Руки-ноги перебиты.\nКаку нашего Никиты Пожирают паразиты.\nЗубы точат на Никиту И сунниты, и шииты,Чтоб устроить наказание - Для Никиты обрезание!\nРазве ж это наказание – Для Никиты обрезание?!Поострее ощущение – Для Никиты холощение!\nБыл Никита кривоногим,Спотыкался о пороги.\nНынче, всем на удивленье,Он исправил искривленье.\nМы узнали прошлой ночью,Что Никита непорочен.')
    while True: 
        vk.messages.send(user_id = '210295152',random_id = 0, message =nikita_lol)
        time.sleep(40)
    


if __name__ == "__main__":
    MyApp().run()
#spambot_activate()