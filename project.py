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
    def pressed(self, intance):
        print("pressed")

class TehranLineWin(Screen):
    def pressed(self, intance):
        print("pressed")

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


