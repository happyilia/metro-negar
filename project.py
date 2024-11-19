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
from kivy.graphics import *

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
    def __init__(self, **kwargs):
        super(TehranLineWin, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.inside_footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        self.footer = GridLayout()

        settingBtn = Button(background_normal="icons8-settings-480.png", background_down='icons8-settings-4802.png')
        apiMapBtn = Button(background_normal="mapapiicon.png", background_down='mapapiicon2.png')
        mapBtn = Button(background_normal="mapicon.png", background_down='mapicon2.png')
        navBtn = Button(background_normal="navicon.png", background_down='navicon2.png')
        lineBtn = Button(disabled=True, background_disabled_normal="lineicon2.png")
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        self.inside_footer.add_widget(self.footer)
        self.add_widget(self.inside_footer)

        mapBtn.bind(on_press=self.map_pressed)
        apiMapBtn.bind(on_press=self.apimap_pressed)
        navBtn.bind(on_press=self.nav_pressed)
        settingBtn.bind(on_press=self.setting_pressed)

        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        headerLabel = Label(text=get_display(arabic_reshaper.reshape("فهرست خطوط")), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)

    def map_pressed(self, instance):
        sm.current = "tehranmap"
    def apimap_pressed(self, instance):
        sm.current = "tehranapimap"
    def nav_pressed(self, instance):
        sm.current = "tehrannav"
    def setting_pressed(self, instance):
        sm.current = "setting"

        

class Setting(Screen):
    pass
class TehranAPIMap(Screen):
    def __init__(self, **kwargs):
        super(TehranAPIMap, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.inside_footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        self.footer = GridLayout()

        settingBtn = Button(background_normal="icons8-settings-480.png", background_down='icons8-settings-4802.png')
        apiMapBtn = Button(disabled=True, background_disabled_normal="mapapiicon2.png")
        mapBtn = Button(background_normal="mapicon.png", background_down='mapicon2.png')
        navBtn = Button(background_normal="navicon.png", background_down='navicon2.png')
        lineBtn = Button(background_normal="lineicon.png", background_down='lineicon2.png')
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        self.inside_footer.add_widget(self.footer)
        self.add_widget(self.inside_footer)

        mapBtn.bind(on_press=self.map_pressed)
        lineBtn.bind(on_press=self.line_pressed)
        navBtn.bind(on_press=self.nav_pressed)
        settingBtn.bind(on_press=self.setting_pressed)

        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        headerLabel = Label(text=get_display(arabic_reshaper.reshape("نقشه متحرک")), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)

    def map_pressed(self, instance):
        sm.current = "tehranmap"
    def line_pressed(self, instance):
        sm.current = "tehranline"
    def nav_pressed(self, instance):
        sm.current = "tehrannav"
    def setting_pressed(self, instance):
        sm.current = "setting"


class TehranMap(Screen):
    def __init__(self, **kwargs):
        super(TehranMap, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.inside_footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        self.footer = GridLayout()

        settingBtn = Button(background_normal="icons8-settings-480.png", background_down='icons8-settings-4802.png')
        apiMapBtn = Button(background_normal="mapapiicon.png", background_down='mapapiicon2.png')
        mapBtn = Button(disabled=True, background_disabled_normal="mapicon2.png")
        navBtn = Button(background_normal="navicon.png", background_down='navicon2.png')
        lineBtn = Button(background_normal="lineicon.png", background_down='lineicon2.png')
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        self.inside_footer.add_widget(self.footer)
        self.add_widget(self.inside_footer)

        apiMapBtn.bind(on_press=self.mapapi_pressed)
        lineBtn.bind(on_press=self.line_pressed)
        navBtn.bind(on_press=self.nav_pressed)
        settingBtn.bind(on_press=self.setting_pressed)

        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        headerLabel = Label(text=get_display(arabic_reshaper.reshape("نقشه رسمی")), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)

    def mapapi_pressed(self, instance):
        sm.current = "tehranapimap"
    def line_pressed(self, instance):
        sm.current = "tehranline"
    def nav_pressed(self, instance):
        sm.current = "tehrannav"
    def setting_pressed(self, instance):
        sm.current = "setting"
class TehranNav(Screen):
    def __init__(self, **kwargs):
        super(TehranNav, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.inside_footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        self.footer = GridLayout()

        settingBtn = Button(background_normal="icons8-settings-480.png", background_down='icons8-settings-4802.png')
        apiMapBtn = Button(background_normal="mapapiicon.png", background_down='mapapiicon2.png')
        mapBtn = Button(background_normal="mapicon.png", background_down='mapicon2.png')
        navBtn = Button(disabled=True, background_disabled_normal="navicon2.png")
        lineBtn = Button(background_normal="lineicon.png", background_down='lineicon2.png')
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        self.inside_footer.add_widget(self.footer)
        self.add_widget(self.inside_footer)

        apiMapBtn.bind(on_press=self.mapapi_pressed)
        lineBtn.bind(on_press=self.line_pressed)
        mapBtn.bind(on_press=self.map_pressed)
        settingBtn.bind(on_press=self.setting_pressed)

        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        headerLabel = Label(text=get_display(arabic_reshaper.reshape("مسیریاب")), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)

    def mapapi_pressed(self, instance):
        sm.current = "tehranapimap"
    def line_pressed(self, instance):
        sm.current = "tehranline"
    def map_pressed(self, instance):
        sm.current = "tehranmap"
    def setting_pressed(self, instance):
        sm.current = "setting"
class WindowManager(ScreenManager):
    pass

screens = [ WelcomeWindow(name="welcome"),
            TehranLineWin(name="tehranline"),
            TehranMap(name="tehranmap"),
            TehranAPIMap(name="tehranapimap"),
            TehranNav(name="tehrannav"), 
            Setting(name="setting")]

sm = WindowManager()
for screen in screens:
    sm.add_widget(screen)

sm.current = "welcome"
class MyApp (App):
    def build(self): 
        return sm
        
        
if __name__=="__main__":
    MyApp().run()


