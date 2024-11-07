import kivy
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kv = Builder.load_file("my.kv")
Window.clearcolor = (1, 1, 1, 1)


class WelcomeWindow(Screen):
    def __init__(self,**kwargs):
        super(WelcomeWindow,self).__init__(**kwargs)
        self.rows = 3

        self.inside = GridLayout()
        self.inside.cols = 1
        self.inside.rows = 3
        self.insidebtn = GridLayout()
        self.insidebtn.cols = 3
        self.insidebtn.rows = 2

        self.inside.add_widget(Label(text=get_display(arabic_reshaper.reshape("خوش آمدید! ")),font_size = 50, font_name='Vazir-Bold' ,color="black"))
        self.inside.add_widget(Label(text=get_display(arabic_reshaper.reshape("لطفا شهر خود را انتخاب کنید: ")),font_size = 40, font_name='Vazir',color="black") )

        self.tehran_btn = Button(text=get_display(arabic_reshaper.reshape('تهران')), font_size=40,font_name='Vazir',background_color="red")
        self.tehran_btn.bind(on_press=self.pressedtbtn)
        self.insidebtn.add_widget(self.tehran_btn)

        self.mashhad_btn = Button(text=get_display(arabic_reshaper.reshape('مشهد')), font_size=40,font_name='Vazir',background_color="green")
        self.mashhad_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.mashhad_btn)

        self.isfahan_btn = Button(text=get_display(arabic_reshaper.reshape('اصفهان')), font_size=40,font_name='Vazir',background_color="yellow")
        self.isfahan_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.isfahan_btn)

        self.shiraz_btn = Button(text=get_display(arabic_reshaper.reshape('شیراز')), font_size=40,font_name='Vazir',background_color="blue")
        self.shiraz_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.shiraz_btn)

        self.tabriz_btn = Button(text=get_display(arabic_reshaper.reshape('تبریز')), font_size=40,font_name='Vazir',background_color="pink")
        self.tabriz_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.tabriz_btn)

        self.karaj_btn = Button(text=get_display(arabic_reshaper.reshape('کرج')), font_size=40,font_name='Vazir',background_color="gray")
        self.karaj_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.karaj_btn)

        self.inside.add_widget(self.insidebtn)
        self.add_widget(self.inside)

    def pressedtbtn(self, intance):
        sm.current = "tehranline"
    def pressed(self, intance):
        print("pressed")
class TehranLineWin(Screen):
    def __init__(self,**kwargs):
        super(TehranLineWin,self).__init__(**kwargs)
        self.inside = FloatLayout(pos_hint={'x':0,'y':0},size_hint = (1, 0.1))
        self.footer = GridLayout()
        settingBtn = Button(background_normal="icons8-settings-480.png")
        apiMapBtn = Button(background_normal="mapapiicon.png")
        mapBtn = Button(background_normal="mapicon.png")
        navBtn = Button(background_normal="navicon.png")
        lineBtn = Button(background_normal="lineicon.png")
        self.footer.rows =1
        self.footer.cols = 5
        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        self.inside.add_widget(self.footer)
        self.add_widget(self.inside)

class TehranSetting(Screen):
    pass
class TehranAPIMap(Screen):
    pass
class TehranMap(Screen):
    pass
class TehranNav(Screen):
    pass
class WindowManager(ScreenManager):
    pass

screens = [WelcomeWindow(name="welcome"),TehranLineWin(name="tehranline")]
sm = WindowManager()
for screen in screens:
    sm.add_widget(screen)

sm.current = "welcome"
class MyApp (App):
    def build(self): 
        return sm
        
        
if __name__=="__main__":
    MyApp().run()


