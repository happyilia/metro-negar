from imports import *



script_dir = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file("my.kv")
Window.clearcolor = (1, 1, 1, 1)
tehlinecolors = [(1,0,0,1),(0,0,1,1),(0,0.8,1,1),(1,0.89,0,1),(0,0.5,0,1),(1,0.45,0.85,1),(0.65,0,1,1)]

def fa(txt):
    return txt
def fa2(txt):
    return get_display(arabic_reshaper.reshape(txt))
config = Config()
config.change(
    direction='ltr',
    font_name='Vazir',
    # file_regular='{path}.ttf',
    # file_bold='{path}.ttf',
    # file_italic='{path}.ttf',
    # file_bolditalic='{path}.ttf'
)


def dijkstra_with_total_weight(graph, start, end):
    # Create a priority queue and hash set to store visited nodes
    queue = [(0, start)]
    visited = set()
    distances = {start: 0}
    parents = {start: None}

    while queue:
        (current_distance, current_node) = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                parents[neighbor] = current_node

    path = []
    total_weight = 0
    while end is not None:
        path.append(end)
        parent = parents[end]
        if parent is not None:
            total_weight += graph[parent][end]
        end = parent
    path.reverse()
    return path, total_weight

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


def line_finder(pot):
    lines=[]
    for i in range(1,8):
        file_path = os.path.join(script_dir, "tehran\\line"+str(i)+".txt")
        linetxt= open(file_path,'r', encoding='utf-8')
        linetxt=linetxt.read()
        linetxt = linetxt.split('\n')
        for j in pot:
            if j in linetxt and i not in lines:
                lines.append(i)
    return lines

#tehran_graph
teh_graph={}
teh_stations=[]
o=0
for i in range(1,8):
    file_path = os.path.join(script_dir, "tehran\\line"+str(i)+".txt")
    linetxt= open(file_path,'r', encoding='utf-8')
    linetxt=linetxt.read()
    linetxt = linetxt.split('\n')
    for j in range(len(linetxt)):
        if linetxt[j] not in teh_stations and j!=0 and j!=len(linetxt)-1:
            teh_graph[linetxt[j]] = {}
            teh_graph[linetxt[j]][linetxt[j+1]]=5
            teh_graph[linetxt[j]][linetxt[j-1]]=5
            teh_stations.append(linetxt[j])
        elif j==0:
            teh_graph[linetxt[j]] = {}
            teh_graph[linetxt[j]][linetxt[j + 1]] = 5
            teh_stations.append(linetxt[j])
        elif j==len(linetxt)-1:
            teh_graph[linetxt[j]] = {}
            teh_graph[linetxt[j]][linetxt[j-1]]=5
            
            teh_stations.append(linetxt[j])
        elif linetxt[j] in teh_stations:
            teh_graph[linetxt[j]].update({linetxt[j+1]:5,linetxt[j-1]:5})

class Node:
  def __init__(self,x_coord,y_coord):
      self.d=float('inf') #current distance from source node
      self.parent=None
      self.finished=False





class WindowManager(ScreenManager):
    pass
sm = WindowManager()
screens = []

class TouchLabel(ButtonBehavior, Label):
    pass

class WelcomeWindow(Screen):
    def __init__(self,**kwargs):
        super(WelcomeWindow,self).__init__(**kwargs)
        self.rows = 3
        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.top_rect = Rectangle()
            Color(0.5, 0.5, 0.5, 1)
            self.circle=Ellipse(radius=1000)
        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        headerLabel = Label(text=fa("خوش آمدید! "), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)
        self.bind(size=self.update_rect, pos=self.update_rect)
        self.inside = GridLayout()
        self.inside.cols = 1
        self.inside.rows = 2
        self.inside2 = GridLayout()
        self.inside2.cols = 1
        self.inside2.rows = 1
        self.insidebtn = MDCircularLayout(degree_spacing=60,start_from=90,pos_hint={'center_x':.5,'center_y':.5},circular_radius=300)

        
        self.inside2.add_widget(Label(text=fa("لطفا شهر خود را انتخاب کنید: "),font_size = 60, font_name='Vazir',color="black") )

        self.tehran_btn = MDIconButton(icon="tehranlogo.png",icon_size="55sp")
        self.tehran_btn.bind(on_press=self.pressedtbtn)
        self.insidebtn.add_widget(self.tehran_btn)

        self.mashhad_btn = MDIconButton(icon="mashhadlogo.png",icon_size="55sp")
        self.mashhad_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.mashhad_btn)

        self.isfahan_btn = MDIconButton(icon="isfahanlogo.png",icon_size="55sp")
        self.isfahan_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.isfahan_btn)

        self.shiraz_btn = MDIconButton(icon="shirazlogo.png",icon_size="55sp")
        self.shiraz_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.shiraz_btn)

        self.tabriz_btn = MDIconButton(icon="tabrizlogo.png",icon_size="55sp")
        self.tabriz_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.tabriz_btn)

        self.karaj_btn = MDIconButton(icon="karajlogo.png",icon_size="55sp")
        self.karaj_btn.bind(on_press=self.pressed)
        self.insidebtn.add_widget(self.karaj_btn)

        self.inside.add_widget(self.inside2)
        self.inside.add_widget(self.insidebtn)
        self.add_widget(self.inside)

    def pressedtbtn(self, intance):
        sm.current = "tehranline"
    def pressed(self, intance):
        print("pressed")

    def update_rect(self, *args): 
        self.top_rect.pos = (0, self.height * 0.9) 
        self.top_rect.size = (self.width, self.height * 0.1)
        self.circle.pos= (self.width*0.5-450,self.height*0.01)
        
        self.circle.size=(900,900)
class TehranLineWin(Screen):
    def __init__(self, **kwargs):
        super(TehranLineWin, self).__init__(**kwargs)
        
    def on_kv_post(self, base_widget):

        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.top_rect = Rectangle()
        
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
        
        self.searchbox=TextInput(pos_hint={'x':0.01,'y':0.8},size_hint=(0.3,0.08),hint_text=fa("نام ایستگاه/مکان"),hint_text_color=(0.4, 0.4, 0.4, 1),font_name='Vazir',background_color="white",border=(4,4,4,4),base_direction='rtl',font_context='Vazir',text_language='fa',font_size=30)
        self.add_widget(self.searchbox)
        self.searchBtn=MDIconButton(pos_hint={'x':0.35,'y':0.8},size_hint=(0.08,0.08),icon="magnify",line_width=5,line_color=(0,0,0,1),rounded_button=True,md_bg_color=(0.75, 0.75, 0.75, 1))
        self.add_widget(self.searchBtn)
        self.search_results_scroll = ScrollView(size_hint=(0.3, 0), pos_hint={'x':0.01, 'y':0.61})
        with self.search_results_scroll.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(size=self.search_results_scroll.size, pos=self.search_results_scroll.pos)
            self.search_results_scroll.bind(size=self.update_scroll_rect, pos=self.update_scroll_rect)
        
        self.search_results_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=40, padding=(10, 10))
        self.search_results_box.bind(minimum_height=self.search_results_box.setter('height'))
        self.search_results_scroll.add_widget(self.search_results_box)
        self.add_widget(self.search_results_scroll)


        self.searchbox.bind(text=self.on_text)
        self.searchBtn.bind(on_press=self.searchBtn_pressed)

        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(icon="icons8-settings-480.png",pos_hint={'center_x':0.1},icon_size="55sp")
        apiMapBtn = MDIconButton(icon="mapapiicon.png",pos_hint={'center_x':0.3},icon_size="55sp")
        mapBtn = MDIconButton(icon="mapicon.png",pos_hint={'center_x':0.9},icon_size="55sp")
        navBtn = MDIconButton(icon="navicon.png",pos_hint={'center_x':0.7},icon_size="55sp")
        lineBtn = MDIconButton(disabled=True, icon="lineicon2.png",pos_hint={'center_x':0.5},icon_size="55sp")
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        
        self.add_widget(self.footer)

        mapBtn.bind(on_press=self.map_pressed)
        apiMapBtn.bind(on_press=self.apimap_pressed)
        navBtn.bind(on_press=self.nav_pressed)
        settingBtn.bind(on_press=self.setting_pressed)

        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        headerLabel = Label(text=fa("فهرست خطوط"), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)
        

   
        
        
        
    def update_scroll_size(self, instance, value):
        self.search_results_scroll.height = self.searchbox.height * 2

    def update_rect(self, *args): 
        self.top_rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.top_rect.size = (self.width, self.height * 0.1)

    def update_scroll_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def update_line_position(self, *args):
        self.line.points = [self.children[1].center_x, self.children[25].center_y, self.width, self.children[25].center_y]
        self.line2.points = [self.children[1].center_x, self.children[24].center_y, 0, self.children[24].center_y]
        self.line3.points = [self.children[1].center_x, self.children[23].center_y, self.width, self.children[23].center_y]
        self.line4.points = [self.children[1].center_x, self.children[22].center_y, 0, self.children[22].center_y]
        self.line5.points = [self.children[1].center_x, self.children[21].center_y, self.width, self.children[21].center_y]
        self.line6.points = [self.children[1].center_x, self.children[20].center_y, 0, self.children[20].center_y]
        self.line7.points = [self.children[1].center_x, self.children[19].center_y, self.width, self.children[19].center_y]
        
        
        

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
    # def on_label_touch_down(self, instance, touch, match):
    #     print(instance)
    #     self.searchbox.text = self.ser_labels[instance].text
    def on_label_touch_down(self, instance, touch, match):
        
        if touch.collide_point(*touch.pos):  # Ensure touch is on the label
            print(f"Label clicked with text: {instance}")   
            return True
        return False 

    
    def on_text(self, instance, value):
        self.search_results_box.clear_widgets()
        self.ser_labels = []
        
        if value.strip(): 
            matches = self.search_names(value)
            for match in matches:
                label = Label(text=fa(match), font_size=30, font_name='Vazir-Bold', color="black")
                
                # Bind the touch event properly using partial
                label.bind(on_touch_down=partial(self.on_label_touch_down, match))
                self.ser_labels.append(label)
                self.search_results_box.add_widget(label)

            self.search_results_scroll.size_hint_y = None  
            self.search_results_scroll.height = self.searchbox.height * 2 
        else:
            self.search_results_scroll.size_hint_y = 0


        


    def search_names(self, query):
        script_dir = os.path.dirname(__file__)
        names = []
        for i in range(1, 8):
            file_path = os.path.join(script_dir, "tehran", f"line{i}.txt")
            with open(file_path, 'r', encoding='utf-8') as file:
                names.extend([line.strip() for line in file])
            
        pattern = re.compile(query, re.IGNORECASE)
        for i in range(1, 8):
            file_path = os.path.join(script_dir, "tehran", f"line{i}infoplacescut.txt")
            with open(file_path, 'r', encoding='utf-8') as file:
                names.extend([line.strip("، ") for line in file])
            
        
            
        pattern = re.compile(query, re.IGNORECASE)
        return [name for name in names if pattern.search(name)]
    
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
    def __init__(self, **kwargs):
        super(Setting, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(disabled=True,icon="icons8-settings-4802.png",pos_hint={'center_x':0.1},icon_size="55sp")
        apiMapBtn = MDIconButton(icon="mapapiicon.png",pos_hint={'center_x':0.3},icon_size="55sp")
        mapBtn = MDIconButton(icon="mapicon.png",pos_hint={'center_x':0.9},icon_size="55sp")
        navBtn = MDIconButton(icon="navicon.png",pos_hint={'center_x':0.7},icon_size="55sp")
        lineBtn = MDIconButton(icon="lineicon.png",pos_hint={'center_x':0.5},icon_size="55sp")
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        
        self.add_widget(self.footer)

        mapBtn.bind(on_press=self.map_pressed)
        lineBtn.bind(on_press=self.line_pressed)
        navBtn.bind(on_press=self.nav_pressed)
        apiMapBtn.bind(on_press=self.apimap_pressed)

        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        headerLabel = Label(text=fa("تنظیمات"), font_size=50, font_name='Vazir-Bold', color="white", pos_hint={'x': 0, 'y': 0})
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
    def apimap_pressed(self, instance):
        sm.current = "tehranapimap"
class TehranAPIMap(Screen):
    def __init__(self, **kwargs):
        super(TehranAPIMap, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        map_layout=FloatLayout( size_hint=(1, 0.8))

        self.map=MapView(zoom=11, lat=35.715298, lon= 51.404343,pos=(0,Window.height*0.1))
        
        self.map.map_source="osm"
        map_layout.add_widget(self.map)
        self.add_widget(map_layout)





        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(icon="icons8-settings-480.png",pos_hint={'center_x':0.1},icon_size="55sp")
        apiMapBtn = MDIconButton(disabled=True,icon="mapapiicon2.png",pos_hint={'center_x':0.3},icon_size="55sp")
        mapBtn = MDIconButton(icon="mapicon.png",pos_hint={'center_x':0.9},icon_size="55sp")
        navBtn = MDIconButton(icon="navicon.png",pos_hint={'center_x':0.7},icon_size="55sp")
        lineBtn = MDIconButton(icon="lineicon.png",pos_hint={'center_x':0.5},icon_size="55sp")
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        
        self.add_widget(self.footer)

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
        
        
        file_path = os.path.join(script_dir, "tehran\\map.png")
        self.Grid=FloatLayout(size_hint=(1,.8))
        self.add_widget(self.Grid)
        self.stencil=StencilView(pos=(0,Window.height*0.1))
        self.Grid.add_widget(self.stencil)
        self.scatter=Scatter(do_translation=True,do_rotation=False,size=(Window.width,Window.height*0.8),pos=(0,Window.height*0.1),scale_min=1)
        self.stencil.add_widget(self.scatter)
        self.image=AsyncImage(source=file_path,size=(Window.width,Window.height*0.8))
        self.scatter.add_widget(self.image)

        self.bind(size=self.update_img, pos=self.update_img)
        


        with self.canvas.before:
            self.rect_color = Color(0.4, 0.4, 0.4, 1)
            self.rect = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(icon="icons8-settings-480.png",pos_hint={'center_x':0.1},icon_size="55sp")
        apiMapBtn = MDIconButton(icon="mapapiicon.png",pos_hint={'center_x':0.3},icon_size="55sp")
        mapBtn = MDIconButton(disabled=True,icon="mapicon2.png",pos_hint={'center_x':0.9},icon_size="55sp")
        navBtn = MDIconButton( icon="navicon.png",pos_hint={'center_x':0.7},icon_size="55sp")
        lineBtn = MDIconButton(icon="lineicon.png",pos_hint={'center_x':0.5},icon_size="55sp")
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        
        self.add_widget(self.footer)

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

    def update_img(self, *args): 
        self.Grid.size_hint=(1,.8)
        self.stencil.pos=(0,Window.height*0.1)
        self.scatter.size=(Window.width,Window.height*0.8)
        self.scatter.pos=(0,Window.height*0.1)
        self.image.size=(Window.width,Window.height*0.8)


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
        
        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(icon="icons8-settings-480.png",pos_hint={'center_x':0.1},icon_size="55sp")
        apiMapBtn = MDIconButton(icon="mapapiicon.png",pos_hint={'center_x':0.3},icon_size="55sp")
        mapBtn = MDIconButton(icon="mapicon.png",pos_hint={'center_x':0.9},icon_size="55sp")
        navBtn = MDIconButton(disabled=True, icon="navicon2.png",pos_hint={'center_x':0.7},icon_size="55sp")
        lineBtn = MDIconButton(icon="lineicon.png",pos_hint={'center_x':0.5},icon_size="55sp")
        
        self.footer.rows = 1
        self.footer.cols = 5

        self.footer.add_widget(settingBtn)
        self.footer.add_widget(apiMapBtn)
        self.footer.add_widget(lineBtn)
        self.footer.add_widget(navBtn)
        self.footer.add_widget(mapBtn)
        
        self.add_widget(self.footer)

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
        self.mabdaTextinp=TextInput(size_hint=(1,0.4),pos=(0.4,0),hint_text=fa("مبدا"),hint_text_color=(0.4, 0.4, 0.4, 1),font_name='Vazir',background_color="white",border=(4,4,4,4),base_direction='rtl',font_context='Vazir',text_language='fa')
        self.maghsadTextinp=TextInput(size_hint=(1,0.4),pos=(0.4,0),hint_text=fa("مقصد"),hint_text_color=(0.4, 0.4, 0.4, 1),font_name='Vazir',background_color="white",border=(4,4,4,4),base_direction='rtl',font_context='Vazir',text_language='fa')
        searchBtn=Button(size_hint=(1,0.2),text=fa('جستجو'), font_size=40,font_name='Vazir',background_color=(0,0,0.75,1))
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
        if self.mabdaTextinp.text!='' and self.maghsadTextinp.text!='' and finder(self.mabdaTextinp.text)!=False and finder(self.maghsadTextinp.text)!=False:
            path,total_weight=dijkstra_with_total_weight(teh_graph, self.mabdaTextinp.text, self.maghsadTextinp.text)
            
            adads=line_finder(path)
            
            
            screens.append(LineWin(name="search", esm="tehran\\line" + str(1) + ".txt", adad=adads,rang=(1,1,1,1), t=True,stations=path))

            sm.add_widget(screens[len(screens)-1])
            sm.current="search"
            self.mabdaTextinp.text=''
            self.maghsadTextinp.text=''

class LineWin(Screen):
    def __init__(self, esm,adad,rang,t,stations, **kwargs):
        super(LineWin, self).__init__(**kwargs)
        self.esm = esm
        self.t=t
        self.stations=stations
        
        if self.t:
            self.adad = adad
            self.rang = rang
            besamt=[]
            start=0
            for i in range(1,8):
                file_path = os.path.join(script_dir, "tehran\\line"+str(i)+".txt")
                linetxt= open(file_path,'r', encoding='utf-8')
                linetxt=linetxt.read()
                linetxt = linetxt.split('\n')
                for j in range(start,len(self.stations)-1):
                    if self.stations[j+1] in linetxt and self.stations[j] in linetxt:
                        
                        if linetxt.index(self.stations[j])>linetxt.index(self.stations[j+1])and linetxt[0] not in besamt:
                            besamt.append(linetxt[0])
                            
                        elif linetxt.index(self.stations[j])<linetxt.index(self.stations[j+1]) and linetxt[len(linetxt)-1] not in besamt:
                            besamt.append(linetxt[len(linetxt)-1])
                        start+=1
            lines = self.stations
            rangs=[]
            for i in range(len(self.stations)):
                rangs.append(tehlinecolors[int(finder(self.stations[i])[0])-1])
        else:
            self.adad = adad
            self.rang = rang
            line = open(os.path.join(script_dir, self.esm), "r", encoding='utf-8')
            lines = line.readlines()
            rangs=[tehlinecolors[int(self.adad)-1]]*len(lines)
            besamt=lines[len(lines)-1]
                
        layoutscroll = GridLayout(cols=1, spacing=70, size_hint=(1,None))
        self.root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.885))
        self.bind(size=self.update_rect, pos=self.update_rect)
        StationBtns=[]
        r=0
        file_path_intersecs = os.path.join(script_dir, "tehran\\intersections.txt")
        open_intersecs=open(file_path_intersecs,'r',encoding='utf-8')
        intersecs=open_intersecs.read().split('\n')
        k=0
        self.inters=[]
        for i in lines:
            if i in intersecs :
                
                StationBtns.append(MDIconButton(rounded_button=False,icon=os.path.join(script_dir, "tehran\\intersecs_pics\\"+str(intersecs.index(i)+1)+".png"),pos_hint={'center_x':0.7},icon_size="42sp"))
                StationBtns[-1].pos_hint = {'center_x': 0.505, 'center_y': 0.5}
                self.inters.append(i)
                
            elif self.t:
                StationBtns.append( BaseButton(line_width = 10,line_color=rangs[r],rounded_button=True,md_bg_color=(1,1,1,1)))
                StationBtns[-1].pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            else:
                StationBtns.append( BaseButton(line_width = 10,line_color=self.rang,rounded_button=True,md_bg_color=(1,1,1,1)))
                StationBtns[-1].pos_hint = {'center_x': 0.5, 'center_y': 0.5}

            label = Label(text=i, size_hint=(None, None), color="black", font_name="Vazir", font_size=47)

            float_layout = FloatLayout(size_hint_y=None, height=StationBtns[len(StationBtns)-1].height)
            if lines.index(i) % 2 == 0:
                xlabel = 0.7
            else:
                xlabel = 0.2
            
            
            label.pos_hint = {'x': xlabel, 'center_y': 0.1}
            float_layout.add_widget(StationBtns[-1])
            float_layout.add_widget(label)
            layoutscroll.add_widget(float_layout)
            if not self.t:
                StationBtns[len(StationBtns)-1].bind(on_press=lambda instance, idx=len(StationBtns)-1: self.stationBtn_pressed(idx, self.adad))
            else:
                StationBtns[len(StationBtns)-1].bind(on_press=lambda instance, idx=int(finder(lines[len(StationBtns)-1])[2:])-1, idx2= int(finder(lines[len(StationBtns)-1])[0]) : self.stationBtn_pressed(idx, idx2))
            self.bind(size=lambda instance, value: self.update_label_size(label, self.width, self.height))
            r+=1
        
        
        if not self.t:
            with self.canvas.before:
                self.rect_color = Color(*self.rang)
                self.rect = Rectangle()
        else:
            with self.canvas.before:
                self.rect_color = Color(0.5,0.5,0.5,1)
                self.rect = Rectangle()
        self.root.add_widget(layoutscroll)
        self.add_widget(self.root)

        inside_header = RelativeLayout(size_hint=(1, 0.1), pos_hint={'top': 1})
        if self.t:
            adads=''
            self.besamts=''
            for i in self.adad:
                adads+=str(i)+' و '
            for i in besamt:
                self.besamts+=i+' ، '
            headertext="خطوط "+ adads[:len(adads)-3] 
        else:
            headertext="خط "+str(self.adad) +" به سمت: "+besamt
        headerLabel = Label(text=headertext, font_size=50, font_name='Vazir-Bold', 
                            color="white", pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(headerLabel)
        self.add_widget(inside_header)
        self.info_layout = FloatLayout(size_hint=(0.2, 0.1), pos_hint={'x': 0.8, 'y':0.1})
        self.infoBtn = MDIconButton(rounded_button=False,icon=os.path.join(script_dir, "more-info-icon.png"),icon_size="42sp",pos_hint={'center_x':0.5})
        self.info_layout.add_widget(self.infoBtn)
        self.infoBtn.bind(on_press=self.info_pressed)
        self.add_widget(self.info_layout)

        self.back_layout = FloatLayout(size_hint=(0.2, 0.1), pos_hint={'x': 0.05, 'top': 1}) 
        backBtn = MDIconButton(icon="back.png", icon_size="42sp") 
        self.back_layout.add_widget(backBtn) 
        self.add_widget(self.back_layout)
        backBtn.bind(on_press=self.back_pressed)
        layoutscroll.bind(minimum_height=layoutscroll.setter('height'))
        self.bind(size=self.layout_update)
        self.StationBtns = StationBtns
        self.layoutscroll = layoutscroll
        self.rangs = rangs
        self.bind(size=lambda instance,idx=self.layoutscroll: self.clearing_canvas_2(idx))
        Clock.schedule_interval(self.line_update, 0.1)
        
        
    

    def clearing_canvas_2(self,layoutscroll,*args):
        self.clearing_canvas(self.layoutscroll)
    def clearing_canvas(self,layoutscroll,*args):
        layoutscroll.canvas.before.clear()


    def update_lines_colors(self, layoutscroll, StationBtns, rangs):
        
        
        layoutscroll.canvas.before.clear()
        # Now, draw the lines between the buttons
        with layoutscroll.canvas.before:
            Color(*rangs[0])
            Line(points=[self.center_x, StationBtns[1].center_y+StationBtns[1].center_y/10, self.center_x, StationBtns[1].center_y], width=10)
            
            for i in range(1,len(StationBtns) - 1):
                btn1 = StationBtns[i]
                btn2 = StationBtns[i + 1]
                Color(*rangs[i])
                Line(points=[self.center_x, btn1.center_y, self.center_x, btn2.center_y], width=10)
                

    def line_update(self,*args):
        self.StationBtns = [[self.width*0.5,self.height*2.25]]+self.StationBtns[1:]
        
        self.update_positions_and_draw_lines()

    def update_label_size(self, label, width, height):
        label.font_size = height * 0.02  # Adjust font size based on the height of the window
        label.size_hint = (None, None)   # Ensure size_hint is None to manually set size
        label.size = (width * 0.2, height * 0.05)  # Adjust the size based on the width and height of the window
    def update_rect(self, *args):
        self.rect.pos = (0, self.height * 0.9)
        self.rect.size = (self.width, self.height * 0.1)

    def layout_update(self,*args):
        self.root.height=self.height*0.885

    def update_positions_and_draw_lines(self, *args):
        self.layoutscroll.do_layout()

        # Explicitly update button positions (ensure they are fully laid out)
        
        self.update_lines_colors(self.layoutscroll, self.StationBtns, self.rangs)


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
            
    def info_pressed(self,*args):
        if self.t:
            s=""
            for i in self.inters[:len(self.inters)-1]:
                s+=i + "، "
            if self.inters==[]:
                txt=''
            else:
                txt="در ایستگاه های "+s+self.inters[-1]+" به سمت "+self.besamts[:len(self.besamts)-3]+ " خط عوض کنید."
            popup=Popup(title=fa(txt),size_hint=(1,0.2),pos_hint={'center_x':0.5,'center_y':0.5})
            popup.open()
        else:
            popup=Popup(title=fa("زمانبندی حرکت قطار ها"),size_hint=(1,0.6),pos_hint={'center_x':0.5,'center_y':0.5})
            popup.add_widget(Image(source=os.path.join(script_dir, "tehran\\headway_pics\\"+self.adad+".jpg")))
            popup.open()




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


