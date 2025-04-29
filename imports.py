import kivy
import os
import arabic_reshaper
import re
from kivy.uix.boxlayout import BoxLayout
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
from kivy.graphics import StencilPush, StencilUse, StencilUnUse, StencilPop, Ellipse, Color
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
from kivy.uix.image import Image, AsyncImage
from kivy.uix.scatter import Scatter
from kivymd.uix.circularlayout import MDCircularLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.label.label import MDLabel
import heapq
from functools import partial
from kivy.garden.mapview import MapView,MapSource,MapMarker
from kivy.uix.stencilview import StencilView
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.event import EventDispatcher 
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button.button import MDRaisedButton
from kivy.graphics import Rotate
from kivy.animation import Animation
