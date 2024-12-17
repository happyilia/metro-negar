from imports import *


script_dir = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file("my.kv")
Window.clearcolor = (1, 1, 1, 1)
tehlinecolors = [(1,0,0,1),(0,0,1,1),(0,0.8,1,1),(1,0.89,0,1),(0,0.5,0,1),(1,0.45,0.85,1),(0.65,0,1,1)]
def fa(txt):
    return txt
config = Config()
config.change(
    direction='ltr',
    font_name='Vazir',
    # file_regular='{path}.ttf',
    # file_bold='{path}.ttf',
    # file_italic='{path}.ttf',
    # file_bolditalic='{path}.ttf'
)

def finder(txt):
    
    for i in range(1,8):
        file_path = os.path.join(script_dir, "tehran\\line"+str(i)+".txt")
        linetxt= open(file_path,'r', encoding='utf-8')
        linetxt=linetxt.read()
        linetxt = linetxt.split('\n')
        if txt in linetxt:
            
            return str(i)+','+str(linetxt.index(txt)+1)
    return False

def nearplacesfinder(txt):
    
    for i in range(1,8):
        file_path = os.path.join(script_dir, "tehran\\line"+str(i)+"infoplaces.txt")
        linetxt= open(file_path,'r', encoding='utf-8')
        linetxt=linetxt.read()
        linetxt = linetxt.split('\n')
        for j in linetxt:
            if txt in j:
                
                return str(i)+','+str(linetxt.index(j)+1)
    return False

class WindowManager(ScreenManager):
    pass
sm = WindowManager()
screens = []
        
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
class TehranLineWin(Screen):
    def __init__(self, **kwargs):
        super(TehranLineWin, self).__init__(**kwargs)
        
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
        line2Btn.bind(on_press=self.line2_pressed)
        self.add_widget(line2Btn)

        line3Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.5750},line_width = 10,line_color=(0,0.8,1,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line3Btn.bind(on_press=self.line3_pressed)
        self.add_widget(line3Btn)

        line4Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.4625},line_width = 10,line_color=(1,0.89,0,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line4Btn.bind(on_press=self.line4_pressed)
        self.add_widget(line4Btn)

        line5Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.3500},line_width = 10,line_color=(0,0.5,0,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line5Btn.bind(on_press=self.line5_pressed)
        self.add_widget(line5Btn)

        line6Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.2375},line_width = 10,line_color=(1,0.45,0.85,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line6Btn.bind(on_press=self.line6_pressed)
        self.add_widget(line6Btn)

        line7Btn= BaseButton(pos_hint = {'center_x':.5 , 'y':0.1250},line_width = 10,line_color=(0.65,0,1,1),rounded_button=True,md_bg_color=(1,1,1,1))
        line7Btn.bind(on_press=self.line7_pressed)
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

        self.searchbox=TextInput(pos_hint={'x':0.05,'y':0.8},size_hint=(0.3,0.08),hint_text=fa("نام ایستگاه/مکان"),hint_text_color=(0.4, 0.4, 0.4, 1),font_name='Vazir',background_color="white",border=(4,4,4,4),base_direction='rtl',font_context='Vazir',text_language='fa')
        self.add_widget(self.searchbox)
        self.searchBtn=MDIconButton(pos_hint={'x':0.37,'y':0.8},size_hint=(0.08,0.08),icon="magnify",line_width=5,line_color=(0,0,0,1),rounded_button=True,md_bg_color=(0.75, 0.75, 0.75, 1))
        self.add_widget(self.searchBtn)
        self.searchBtn.bind(on_press=self.searchBtn_pressed)

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
        self.line.points = [self.children[1].center_x, self.children[24].center_y, self.width, self.children[24].center_y]
        self.line2.points = [self.children[1].center_x, self.children[23].center_y, 0, self.children[23].center_y]
        self.line3.points = [self.children[1].center_x, self.children[22].center_y, self.width, self.children[22].center_y]
        self.line4.points = [self.children[1].center_x, self.children[21].center_y, 0, self.children[21].center_y]
        self.line5.points = [self.children[1].center_x, self.children[20].center_y, self.width, self.children[20].center_y]
        self.line6.points = [self.children[1].center_x, self.children[19].center_y, 0, self.children[19].center_y]
        self.line7.points = [self.children[1].center_x, self.children[18].center_y, self.width, self.children[18].center_y]
        
        
        

    def map_pressed(self, instance):
        sm.current = "tehranmap"
    def apimap_pressed(self, instance):
        sm.current = "tehranapimap"
    def nav_pressed(self, instance):
        sm.current = "tehrannav"
    def setting_pressed(self, instance):
        sm.current = "setting"
    def line1_pressed(self, instance):
        sm.current="tehline1"
    def line2_pressed(self, instance):
        sm.current="tehline2"
    def line3_pressed(self, instance):
        sm.current="tehline3"

    def line4_pressed(self, instance):
        sm.current="tehline4"
    def line5_pressed(self, instance):
        sm.current="tehline5"

    def line6_pressed(self, instance):
        sm.current="tehline6"
    def line7_pressed(self, instance):
        sm.current="tehline7"
        
    def searchBtn_pressed(self,instance):
        k=finder(self.searchbox.text)
        if k!=False:
            sm.current=k
        else:
            k=nearplacesfinder(self.searchbox.text)
            if k!=False:
                sm.current=k
        self.searchbox.text = ''

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
        global screens
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


        self.layout=GridLayout(pos_hint={'x': 0.25, 'y':0.3},size_hint=(0.5,0.45))
        self.layout.rows=3
        self.layout.cols=1
        self.mabdaTextinp=TextInput(pos=(0.4,0),hint_text=fa("مبدا"),hint_text_color=(0.4, 0.4, 0.4, 1),font_name='Vazir',background_color="white",border=(4,4,4,4),base_direction='rtl',font_context='Vazir',text_language='fa')
        self.maghsadTextinp=TextInput(pos=(0.4,0),hint_text=fa("مقصد"),hint_text_color=(0.4, 0.4, 0.4, 1),font_name='Vazir',background_color="white",border=(4,4,4,4),base_direction='rtl',font_context='Vazir',text_language='fa')
        searchBtn=Button(text=fa('جستجو'), font_size=40,font_name='Vazir',background_color=(0,0,0.75,1))
        self.btnlayout=GridLayout(size_hint=(0.5,0.5),rows=1,cols=1)
        self.layout.add_widget(self.mabdaTextinp)
        self.layout.add_widget(self.maghsadTextinp)
        self.btnlayout.add_widget(searchBtn)
        self.layout.add_widget(self.btnlayout)
        self.add_widget(self.layout)
        searchBtn.bind(on_press=lambda instance: self.search_pressed(screens,instance))
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
    def search_pressed(self,screens, instance):
        
        
        mab=finder(self.mabdaTextinp.text)
        magh=finder(self.maghsadTextinp.text)
        if  mab!=False and  magh!=False:
            global tehlinecolors
            file_path = os.path.join(script_dir, "tehran\\line"+mab[0]+".txt")
            linetxt= open(file_path,'r', encoding='utf-8')
            linetxt=linetxt.read().split('\n')
            if int(magh[2:])>int(mab[2:]):
                screens.append(LineWin(name="search", esm="tehran\\line" + mab[0] + ".txt", adad=mab[0], rang=tehlinecolors[int(mab[0])-1],t=True,stations=linetxt[min(int(mab[2:]),int(magh[2:]))-1:max(int(mab[2:]),int(magh[2:]))]))
            else:
                tline=linetxt[min(int(mab[2:]),int(magh[2:]))-1:max(int(mab[2:]),int(magh[2:]))]
                tline.reverse()
                screens.append(LineWin(name="search", esm="tehran\\line" + mab[0] + ".txt", adad=mab[0], rang=tehlinecolors[int(mab[0])-1],t=True,stations=tline))

            sm.add_widget(screens[len(screens)-1])
            sm.current="search"
        self.mabdaTextinp.text=''
        self.maghsadTextinp.text=''

class LineWin(Screen):
    def __init__(self, esm,adad,rang,t,stations, **kwargs):
        super(LineWin, self).__init__(**kwargs)
        self.esm = esm
        self.adad = adad
        self.rang = rang
        self.t=t
        self.stations=stations
        
        # Ensure 'esm' is passed correctly and used to open the file
        if not self.t:
            line = open(os.path.join(script_dir, self.esm), "r", encoding='utf-8')
            lines = line.readlines()
        else:
            lines = self.stations
        layoutscroll = GridLayout(cols=1, spacing=70, size_hint=(1,None))


        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.885))

        # Draw the red line on the canvas
        with root.canvas.before:
            Color( *self.rang)
            self.line = Line(points=[Window.width / 2, 0, Window.width / 2, layoutscroll.height],width=10)

        with self.canvas.before:
            self.rect_color = Color(*self.rang)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        StationBtns=[]
        for i in lines:
            StationBtns.append( BaseButton(line_width = 10,line_color=self.rang,rounded_button=True,md_bg_color=(1,1,1,1),pos_hint={"x":0.5}))

            label = Label(text=i, size_hint=(None, None), color="black", 
                          font_name="Vazir", font_size=47)

            float_layout = FloatLayout(size_hint_y=None, height=StationBtns[len(StationBtns)-1].height)
            if lines.index(i) % 2 == 0:
                xlabel = 0.7
            else:
                xlabel = 0.2

            StationBtns[len(StationBtns)-1].pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            label.pos_hint = {'x': xlabel, 'center_y': 0.1}
            float_layout.add_widget(StationBtns[len(StationBtns)-1])
            float_layout.add_widget(label)
            layoutscroll.add_widget(float_layout)
            if not self.t:
                StationBtns[len(StationBtns)-1].bind(on_press=lambda instance, idx=len(StationBtns)-1: self.stationBtn_pressed(idx, self.adad))
            else:
                StationBtns[len(StationBtns)-1].bind(on_press=lambda instance, idx=int(finder(lines[len(StationBtns)-1])[2:])-1 : self.stationBtn_pressed(idx, self.adad))
            self.bind(size=lambda instance, value: self.update_label_size(label, self.width, self.height))

        root.add_widget(layoutscroll)
        self.add_widget(root)
        layoutscroll.bind(minimum_height=lambda instance, value: self.update_line(layoutscroll, max(value, Window.height * 0.885)))

        inside_header = RelativeLayout(size_hint=(1, 0.1), pos_hint={'top': 1})
        headerLabel = Label(text="خط "+self.adad, font_size=50, font_name='Vazir-Bold', 
                            color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)

        self.back_layout = FloatLayout(size_hint=(0.2, 0.1), pos_hint={'x': 0.05, 'top': 1}) 
        backBtn = Button(background_normal="back.png", background_down="back.png") 
        self.back_layout.add_widget(backBtn) 
        self.add_widget(self.back_layout)
        backBtn.bind(on_press=self.back_pressed)
        layoutscroll.bind(minimum_height=layoutscroll.setter('height'))

        self.bind(size=self.update_line_position)

    def update_label_size(self, label, width, height):
        label.font_size = height * 0.02  # Adjust font size based on the height of the window
        label.size_hint = (None, None)   # Ensure size_hint is None to manually set size
        label.size = (width * 0.2, height * 0.05)  # Adjust the size based on the width and height of the window
    def update_rect(self, *args):
        self.rect.pos = (0, self.height * 0.9)
        self.rect.size = (self.width, self.height * 0.1)

    def update_line(self, instance, value):
        scroll_y = self.ids.scroll_view.scroll_y if 'scroll_view' in self.ids else 0
        self.line.points = [Window.width / 2, 0, Window.width / 2, max(instance.height, Window.height * 0.885)]
        if 'scroll_view' in self.ids:
            self.ids.scroll_view.scroll_y = scroll_y

    def update_line_position(self, *args):
        scroll_y = self.ids.scroll_view.scroll_y if 'scroll_view' in self.ids else 0
        self.line.points = [self.width / 2, 0, self.width / 2, max(self.line.points[3], self.height)]
        if 'scroll_view' in self.ids:
            self.ids.scroll_view.scroll_y = scroll_y



    def back_pressed(self,*args):
        sm.current="tehranline"
        if self.t:
            sm.remove_widget(screens[len(screens)-1])
            
            screens.pop()

    def stationBtn_pressed(self,namd,adadd,*args):
        sm.current=str(adadd)+','+str(namd+1)
        if self.t:
            sm.remove_widget(screens[len(screens)-1])
            screens.pop()
            

class StationWin(Screen):
    def __init__(self,nam,rang,adad,esm,**kwargs):
        super(StationWin, self).__init__(**kwargs)
        self.rang = rang
        self.adad = adad
        self.esm = esm
        self.nam = nam
        with self.canvas.before:
            self.rect_color = Color(*self.rang)
            self.rect = Rectangle()
        self.bind(size=self.update_rect, pos=self.update_rect)
        line = open(os.path.join(script_dir, self.esm), "r", encoding='utf-8')
        lines = line.readlines()
        staLine=lines[adad-1].split(" - ")
        
        staName=staLine[0]
        inside_header = RelativeLayout(size_hint=(1, 0.1), pos_hint={'top': 1})
        headerLabel = Label(text=fa(staName), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)

        staEnters=staLine[1]
        staATMs=staLine[2]
        staPlaces=staLine[3]
        self.layout = GridLayout(size_hint=(1,.9))
        self.layout.rows=6
        self.layout.cols=1
        lblenters=Label(text=fa("تعداد ورودی ها :"),color="black", font_name="Vazir-Bold", font_size=50)
        self.layout.add_widget(lblenters)
        enters=Label(text=fa(staEnters),color="black", font_name="Vazir", font_size=45)
        self.layout.add_widget(enters)
        lblatms=Label(text=fa("تعداد خودپرداز ها :"),color="black", font_name="Vazir-Bold", font_size=50)
        self.layout.add_widget(lblatms)
        atms=Label(text=fa(staATMs),color="black", font_name="Vazir", font_size=45)
        self.layout.add_widget(atms)
        lblplaces=Label(text=fa("مکان های مهم اطراف :"),color="black", font_name="Vazir-Bold", font_size=50)
        self.layout.add_widget(lblplaces)
        places=Label(text=fa(staPlaces),color="black", font_name="Vazir", font_size=45)
        self.layout.add_widget(places)

        self.add_widget(self.layout)

        self.back_layout = FloatLayout(size_hint=(0.2, 0.1), pos_hint={'x': 0.05, 'top': 1}) 
        backBtn = Button(background_normal="back.png", background_down="back.png") 
        self.back_layout.add_widget(backBtn) 
        self.add_widget(self.back_layout)
        backBtn.bind(on_press=lambda instance,idx=self.nam: self.back_pressed(idx))

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)

    def back_pressed(self,namd,*args):
        sm.current="tehline"+str(namd)
    



class MyApp(MDApp):
    def build(self):
        global screens
        tehlinecolors = [(1,0,0,1),(0,0,1,1),(0,0.8,1,1),(1,0.89,0,1),(0,0.5,0,1),(1,0.45,0.85,1),(0.65,0,1,1)]
        
        # Adding LineWin screens
        for i in range(1, 8):
            screens.append(LineWin(name="tehline" + str(i), esm="tehran\\line" + str(i) + ".txt", adad=str(i), rang=tehlinecolors[i - 1],t=False,stations=[]))
        
        # Adding StationWin screens
        for i in range(1, 8):
            line = open(os.path.join(script_dir, "tehran\\line" + str(i) + ".txt"), "r", encoding='utf-8')
            lines = line.readlines()
            for j in range(1, len(lines) + 1):
                screens.append(StationWin(name=str(i) + ',' + str(j), nam=i, adad=j, rang=tehlinecolors[i - 1], esm="tehran\\line" + str(i) + "info.txt"))
        
        # Adding other screens
        screens += [
            WelcomeWindow(name="welcome"),
            TehranLineWin(name="tehranline"),
            TehranMap(name="tehranmap"),
            TehranAPIMap(name="tehranapimap"),
            TehranNav(name="tehrannav"), 
            Setting(name="setting")
        ]
        
        # Adding all screens to the ScreenManager
        for screen in screens:
            sm.add_widget(screen)
        
        sm.current = "welcome"
        return sm

        
        
if __name__=="__main__":
    MyApp().run()


