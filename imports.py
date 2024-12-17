import kivy
import os
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
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Ellipse, Color
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.button import BaseButton
from kivy.graphics import Line
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivyir import *
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
