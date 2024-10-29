import kivy
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.rows = 3

        self.inside = GridLayout()
        self.inside.cols = 3
        self.inside.rows = 3

        self.add_widget(Label(text=get_display(arabic_reshaper.reshape("خوش آمدید! ")),font_size = 50, font_name='arial' ))
        self.add_widget(Label(text=get_display(arabic_reshaper.reshape("لطفا شهر خود را انتخاب کنید: ")),font_size = 40, font_name='arial') )

        self.tehran_btn = Button(text=get_display(arabic_reshaper.reshape('تهران')), font_size=40,font_name='arial')
        self.tehran_btn.bind(on_press=self.pressed)
        self.inside.add_widget(self.tehran_btn)

        self.mashhad_btn = Button(text=get_display(arabic_reshaper.reshape('مشهد')), font_size=40,font_name='arial')
        self.mashhad_btn.bind(on_press=self.pressed)
        self.inside.add_widget(self.mashhad_btn)

        self.isfahan_btn = Button(text=get_display(arabic_reshaper.reshape('اصفهان')), font_size=40,font_name='arial')
        self.isfahan_btn.bind(on_press=self.pressed)
        self.inside.add_widget(self.isfahan_btn)

        self.shiraz_btn = Button(text=get_display(arabic_reshaper.reshape('شیراز')), font_size=40,font_name='arial')
        self.shiraz_btn.bind(on_press=self.pressed)
        self.inside.add_widget(self.shiraz_btn)

        self.tabriz_btn = Button(text=get_display(arabic_reshaper.reshape('تبریز')), font_size=40,font_name='arial')
        self.tabriz_btn.bind(on_press=self.pressed)
        self.inside.add_widget(self.tabriz_btn)

        self.karaj_btn = Button(text=get_display(arabic_reshaper.reshape('کرج')), font_size=40,font_name='arial')
        self.karaj_btn.bind(on_press=self.pressed)
        self.inside.add_widget(self.karaj_btn)

        self.add_widget(self.inside)


    def pressed(self, intance):
        print("pressed")
class MyApp (App):
    def build(self): 
        return MyGrid()
        
        
if __name__=="__main__":
    MyApp().run()


print("metro-negar")