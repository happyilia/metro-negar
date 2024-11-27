from imports import *


script_dir = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file("my.kv")
Window.clearcolor = (1, 1, 1, 1)

def fa(txt):
    return get_display(arabic_reshaper.reshape(txt))


        
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

        self.inside.add_widget(Label(text=fa("خوش آمدید! "),font_size = 50, font_name='Vazir-Bold' ,color="black"))
        self.inside.add_widget(Label(text=fa("لطفا شهر خود را انتخاب کنید: "),font_size = 40, font_name='Vazir',color="black") )

        self.tehran_btn = Button(text=fa('تهران'), font_size=40,font_name='Vazir',background_color="red")
        self.tehran_btn.bind(on_press=self.pressedtbtn)
        self.insidebtn.add_widget(self.tehran_btn)

        self.mashhad_btn = Button(text=fa('مشهد'), font_size=40,font_name='Vazir',background_color="green")
        self.mashhad_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.mashhad_btn)

        self.isfahan_btn = Button(text=fa('اصفهان'), font_size=40,font_name='Vazir',background_color="yellow")
        self.isfahan_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.isfahan_btn)

        self.shiraz_btn = Button(text=fa('شیراز'), font_size=40,font_name='Vazir',background_color="blue")
        self.shiraz_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.shiraz_btn)

        self.tabriz_btn = Button(text=fa('تبریز'), font_size=40,font_name='Vazir',background_color="pink")
        self.tabriz_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.tabriz_btn)

        self.karaj_btn = Button(text=fa('کرج'), font_size=40,font_name='Vazir',background_color="gray")
        self.karaj_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.karaj_btn)

        self.inside.add_widget(self.insidebtn)
        self.add_widget(self.inside)

    def pressedtbtn(self, intance):
        sm.current = "tehranline"
    def pressed(self, intance):
        print("pressed")

class TehranLinesWin(Screen):
    def __init__(self, **kwargs):
        super(TehranLinesWin, self).__init__(**kwargs)
        
    def on_kv_post(self, base_widget):

        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle()
        
        with self.canvas:
            Color(1, 0, 0, 1) 
            self.line = Line(width=10)
        with self.canvas:
            Color(0, 0, 1, 1) 
            self.line2 = Line(width=10)
        with self.canvas:
            Color(0,0.8,1,1) 
            self.line3 = Line(width=10)
        with self.canvas:
            Color(1,0.89,0,1)
            self.line4 = Line(width=10)
        with self.canvas:
            Color(0,0.5,0,1)
            self.line5 = Line(width=10)
        with self.canvas:
            Color(1,0.45,0.85,1)
            self.line6 = Line(width=10)
        with self.canvas:
            Color(0.65,0,1,1)
            self.line7 = Line(width=10)
        
        line1Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.8},line_width = 10,line_color=(1,0,0,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line1Btn.bind(on_press=self.line1_pressed)
        self.add_widget(line1Btn)

        line2Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.6875},line_width = 10,line_color=(0,0,1,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line2Btn.bind(on_press=self.line1_pressed)
        self.add_widget(line2Btn)

        line3Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.5750},line_width = 10,line_color=(0,0.8,1,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line3Btn.bind(on_press=self.line1_pressed)
        self.add_widget(line3Btn)

        line4Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.4625},line_width = 10,line_color=(1,0.89,0,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line4Btn.bind(on_press=self.line1_pressed)
        self.add_widget(line4Btn)

        line5Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.3500},line_width = 10,line_color=(0,0.5,0,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line5Btn.bind(on_press=self.line1_pressed)
        self.add_widget(line5Btn)

        line6Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.2375},line_width = 10,line_color=(1,0.45,0.85,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line6Btn.bind(on_press=self.line1_pressed)
        self.add_widget(line6Btn)

        line7Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.1250},line_width = 10,line_color=(0.65,0,1,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line7Btn.bind(on_press=self.line1_pressed)
        self.add_widget(line7Btn)
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        self.bind(size=self.update_line_position, pos=self.update_line_position) 
        line1Btn.bind(pos=self.update_line_position)
        
        j=0
        for i in (0.8,0.6875,0.5750,0.4625,0.35,0.2375,0.125):
            j+=1
            if j%2!=0:
                xlabel=0.8
            else:
                xlabel=0.3
            file_path = os.path.join(script_dir, "tehran\\line"+str(j)+".txt")
            linetxt= open(file_path,'r', encoding='utf-8')
            self.linelabel = Label(text=fa("خط "+str(j)),font_size = 40, font_name='Vazir-Bold' ,color="black",pos_hint = {'center_x':xlabel , 'y':i-0.45})
            self.add_widget(self.linelabel)
            taj=linetxt.readlines()[0]+' '
            linetxt= open(file_path,'r', encoding='utf-8')
            text=taj+"- "+linetxt.readlines()[len(linetxt.readlines())-1]
            clean_text = text.replace("\n","")
            self.linelabel2 = Label(text=fa(clean_text),font_size = 40, font_name='Vazir-Bold' ,color="black",pos_hint = {'center_x':xlabel , 'y':i-0.5})
            self.add_widget(self.linelabel2)
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
        headerLabel = Label(text=fa("فهرست خطوط"), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)

        
        
        


    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)
    def update_line_position(self, *args):
        self.line.points = [self.children[1].center_x, self.children[22].center_y, self.width, self.children[22].center_y]
        self.line2.points = [self.children[1].center_x, self.children[21].center_y, 0, self.children[21].center_y]
        self.line3.points = [self.children[1].center_x, self.children[20].center_y, self.width, self.children[20].center_y]
        self.line4.points = [self.children[1].center_x, self.children[19].center_y, 0, self.children[19].center_y]
        self.line5.points = [self.children[1].center_x, self.children[18].center_y, self.width, self.children[18].center_y]
        self.line6.points = [self.children[1].center_x, self.children[17].center_y, 0, self.children[17].center_y]
        self.line7.points = [self.children[1].center_x, self.children[16].center_y, self.width, self.children[16].center_y]
        
        
        

    def map_pressed(self, instance):
        sm.current = "tehranmap"
    def apimap_pressed(self, instance):
        sm.current = "tehranapimap"
    def nav_pressed(self, instance):
        sm.current = "tehrannav"
    def setting_pressed(self, instance):
        sm.current = "setting"
    def line1_pressed(self, instance):
        sm.current="linewin"

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
        headerLabel = Label(text=fa("نقشه متحرک"), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
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
        headerLabel = Label(text=fa("نقشه رسمی"), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
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
        headerLabel = Label(text=fa("مسیریاب"), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
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


class LineWin(Screen):
    def __init__(self, **kwargs):
        super(LineWin, self).__init__(**kwargs)
        line = open(os.path.join(script_dir, direc),"r",encoding='utf-8')
        lines=line.readlines()
        layoutscroll = GridLayout(cols=1, spacing=100, size_hint_y=None)
        layoutscroll.bind(minimum_height=layoutscroll.setter('height'))
        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        headerLabel = Label(text=fa("خط 1"), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)
        root = ScrollView(
         size_hint=(1, 0.9)
        )
        with root.canvas.before:
            Color(1, 0, 0, 1)
            self.line = Line(points=[Window.width / 2, 0, Window.width / 2, layoutscroll.height],width=10)

        with self.canvas.before:
            self.rect_color = Color(1,0,0, 1)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        for i in lines:
            StationBtn= BaseButton(line_width = 10,line_color=(1,0,0,1),rounded_button=True,md_bg_color=(1,1,1,1),pos_hint={"x":0.5})
            
            label = Label(text=fa(i), size_hint=(None, None),color="black",font_name="Vazir",font_size=47)
            float_layout = FloatLayout(size_hint_y=None, height=StationBtn.height) 
            if lines.index(i)%2==0:
                xlabel=0.7
            else:
                xlabel=0.2
            StationBtn.pos_hint = {'center_x': 0.5, 'center_y': 0.5} # Position button to the left
            label.pos_hint = {'x': xlabel, 'center_y': 0.1 }
            float_layout.add_widget(StationBtn)
            float_layout.add_widget(label)
            layoutscroll.add_widget(float_layout)
        layoutscroll.bind(minimum_height=self.update_line)
        self.bind(size=self.update_line_position)
        root.add_widget(layoutscroll)
        self.add_widget(root)
    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)
    def update_line(self, instance, value):
        self.line.points = [Window.width / 2, 0, Window.width / 2, instance.height]
    def update_line_position(self, *args):
        self.line.points = [self.width / 2, 0, self.width / 2, self.line.points[3]]


class WindowManager(ScreenManager):
    pass

sm = WindowManager()

class MyApp(MDApp):
    def build(self): 
        screens = [ WelcomeWindow(name="welcome"),
            TehranLinesWin(name="tehranline"),
            TehranMap(name="tehranmap"),
            TehranAPIMap(name="tehranapimap"),
            TehranNav(name="tehrannav"), 
            Setting(name="setting")]
        j=0
        for i in ("tehran\\line1.txt","tehran\\line1.txt","tehran\\line1.txt","tehran\\line1.txt","tehran\\line1.txt","tehran\\line1.txt","tehran\\line1.txt"):
            j+=1
            screens.append(LineWin(name="tehranline"+str(j)+"win",direc=i))

        for screen in screens:
            sm.add_widget(screen)
        sm.current = "welcome"
        return sm
        
        
if __name__=="__main__":
    MyApp().run()


