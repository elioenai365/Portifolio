import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]
black = [0,0,0,1]

class HBoxLayoutExemple(App):

    def build(self):
        #Criação do layout principal
        layout = BoxLayout(padding=10)#argumento padding singular existem outras duas maneiras
        colors = [red,green,blue,purple,black]

        #criação dos 5botoes com cores aleatórias e eventos de clique
        for i in range(5):

            btn = Button(text= f"Button {i+1}", background_color = random.choice(colors))

            layout.add_widget(btn)
            btn.bind(on_press=self.on_press_button)


        return layout

    #Função chamada quando QUALQUER botão for pressionado
    def on_press_button(self, instance):
        #'instance' é o própio botão que foi clicado
        print (f'Você apertou o {instance.text}')

if __name__ == '__main__':
    app = HBoxLayoutExemple()
    app.run()
