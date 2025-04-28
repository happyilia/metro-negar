from imports import *



script_dir = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file("my.kv")
Window.clearcolor = (1, 1, 1, 1)
tehlinecolors = [(1,0,0,1),(0,0,1,1),(0,0.8,1,1),(1,0.89,0,1),(0,0.5,0,1),(1,0.45,0.85,1),(0.65,0,1,1)]
theme=(1,1,1,1)
tehranlinecolors = [(1,0,0,1),(0,0,1,1),(0,0.8,1,1),(1,0.89,0,1),(0,0.5,0,1),(1,0.45,0.85,1),(0.65,0,1,1),7]
mashhadlinecolors= [(0,0.5,0,1),(0,0,1,1),(1,0,0,1),3]
isfahanlinecolors=[(1,0,0,1),1]
shirazlinecolors=[(1,0,0,1),(0,0.5,0,1),2]
tabrizlinecolors=[(0.016, 0.686, 0.769,1),1]
karajlinecolors=[(0.78, 0.8, 0.075,1),(0.016, 0.686, 0.769,1),2]

towncolors={
    "tehran":tehranlinecolors,"mashhad":mashhadlinecolors,"isfahan":isfahanlinecolors,"shiraz":shirazlinecolors,"tabriz":tabrizlinecolors,"karaj":karajlinecolors
    }
townnumlines={
    "tehran":7,
    "mashhad":3,
    "isfahan":1,
    "shiraz":2,
    "tabriz":1,
    "karaj":2
}

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

def finder(txt,town):
    
    for i in range(1,townnumlines[town]+1):
        file_path = os.path.join(script_dir, str(town)+"\\line"+str(i)+".txt")
        linetxt= open(file_path,'r', encoding='utf-8')
        linetxt=linetxt.read()
        linetxt = linetxt.split('\n')
        if txt in linetxt:
            
            return str(i)+','+str(linetxt.index(txt)+1)+town
    return False

def nearplacesfinder(txt,town):
    
    for i in range(1,townnumlines[town]+1):
        file_path = os.path.join(script_dir, str(town)+"\\line"+str(i)+"infoplaces.txt")
        linetxt= open(file_path,'r', encoding='utf-8')
        linetxt=linetxt.read()
        linetxt = linetxt.split('\n')
        for j in linetxt:
            if txt in j:
                
                return str(i)+','+str(linetxt.index(j)+1)+town
    return False


def line_finder(pot,town):
    lines=[]
    for i in range(1,townnumlines[town]+1):
        file_path = os.path.join(script_dir, str(town)+"\\line"+str(i)+".txt")
        linetxt= open(file_path,'r', encoding='utf-8')
        linetxt=linetxt.read()
        linetxt = linetxt.split('\n')
        for j in pot:
            if j in linetxt and i not in lines:
                lines.append(i)
    return lines
def towncolor(town):
    tehranlinecolors = [(1,0,0,1),(0,0,1,1),(0,0.8,1,1),(1,0.89,0,1),(0,0.5,0,1),(1,0.45,0.85,1),(0.65,0,1,1),7]
    mashhadlinecolors= [(0,0.5,0,1),(0,0,1,1),(1,0,0,1),3]
    isfahanlinecolors=[(1,0,0,1),1]
    shirazlinecolors=[(1,0,0,1),(0,0.5,0,1),2]
    tabrizlinecolors=[(0.016, 0.686, 0.769,1),1]
    karajlinecolors=[(0.78, 0.8, 0.075,1),(0.016, 0.686, 0.769,1),2]
    towns=["tehran","mashhad","isfahan","shiraz","tabriz","karaj"]
    towncolors={
        "tehran":tehranlinecolors,"mashhad":mashhadlinecolors,"isfahan":isfahanlinecolors,"shiraz":shirazlinecolors,"tabriz":tabrizlinecolors,"karaj":karajlinecolors
    }
    return towncolors[town]

def townbtnspos(town):
    return [0.8,0.6875,0.575,0.4625,0.35,0.2375,0.1250]

townlatslons={
    "tehran":(35.715298,51.404343),
    "mashhad":(36.310699,59.599457),
    "isfahan":(32.661343,51.680374),
    "shiraz":(29.591768,52.583698),
    "tabriz":(38.066666,46.299999),
    "karaj":(35.855938,50.961750)
}

def townLatLon(town):
    
    return townlatslons[town]
    

#tehran_graph
tehran_graph={}
tehran_stations=[]
o=0
for i in range(1,8):
    file_path = os.path.join(script_dir, "tehran\\line"+str(i)+".txt")
    linetxt= open(file_path,'r', encoding='utf-8')
    linetxt=linetxt.read()
    linetxt = linetxt.split('\n')
    for j in range(len(linetxt)):
        if linetxt[j] not in tehran_stations and j!=0 and j!=len(linetxt)-1:
            tehran_graph[linetxt[j]] = {}
            tehran_graph[linetxt[j]][linetxt[j+1]]=5
            tehran_graph[linetxt[j]][linetxt[j-1]]=5
            tehran_stations.append(linetxt[j])
        elif j==0:
            tehran_graph[linetxt[j]] = {}
            tehran_graph[linetxt[j]][linetxt[j + 1]] = 5
            tehran_stations.append(linetxt[j])
        elif j==len(linetxt)-1:
            tehran_graph[linetxt[j]] = {}
            tehran_graph[linetxt[j]][linetxt[j-1]]=5
            
            tehran_stations.append(linetxt[j])
        elif linetxt[j] in tehran_stations:
            tehran_graph[linetxt[j]].update({linetxt[j+1]:5,linetxt[j-1]:5})

#mashhad_graph
mashhad_graph={}
mashhad_stations=[]
o=0
for i in range(1,3):
    file_path = os.path.join(script_dir, "mashhad\\line"+str(i)+".txt")
    linetxt= open(file_path,'r', encoding='utf-8')
    linetxt=linetxt.read()
    linetxt = linetxt.split('\n')
    for j in range(len(linetxt)):
        if linetxt[j] not in mashhad_stations and j!=0 and j!=len(linetxt)-1:
            mashhad_graph[linetxt[j]] = {}
            mashhad_graph[linetxt[j]][linetxt[j+1]]=5
            mashhad_graph[linetxt[j]][linetxt[j-1]]=5
            mashhad_stations.append(linetxt[j])
        elif j==0:
            mashhad_graph[linetxt[j]] = {}
            mashhad_graph[linetxt[j]][linetxt[j + 1]] = 5
            mashhad_stations.append(linetxt[j])
        elif j==len(linetxt)-1:
            mashhad_graph[linetxt[j]] = {}
            mashhad_graph[linetxt[j]][linetxt[j-1]]=5
            
            mashhad_stations.append(linetxt[j])
        elif linetxt[j] in mashhad_stations:
            mashhad_graph[linetxt[j]].update({linetxt[j+1]:5,linetxt[j-1]:5})

#mashhad_graph
isfahan_graph={}
isfahan_stations=[]
o=0
for i in range(1,1):
    file_path = os.path.join(script_dir, "isfahan\\line"+str(i)+".txt")
    linetxt= open(file_path,'r', encoding='utf-8')
    linetxt=linetxt.read()
    linetxt = linetxt.split('\n')
    for j in range(len(linetxt)):
        if linetxt[j] not in isfahan_stations and j!=0 and j!=len(linetxt)-1:
            isfahan_graph[linetxt[j]] = {}
            isfahan_graph[linetxt[j]][linetxt[j+1]]=5
            isfahan_graph[linetxt[j]][linetxt[j-1]]=5
            isfahan_stations.append(linetxt[j])
        elif j==0:
            isfahan_graph[linetxt[j]] = {}
            isfahan_graph[linetxt[j]][linetxt[j + 1]] = 5
            isfahan_stations.append(linetxt[j])
        elif j==len(linetxt)-1:
            isfahan_graph[linetxt[j]] = {}
            isfahan_graph[linetxt[j]][linetxt[j-1]]=5
            
            isfahan_stations.append(linetxt[j])
        elif linetxt[j] in isfahan_stations:
            isfahan_graph[linetxt[j]].update({linetxt[j+1]:5,linetxt[j-1]:5})

shiraz_graph={}
shiraz_stations=[]
o=0
for i in range(1,2):
    file_path = os.path.join(script_dir, "shiraz\\line"+str(i)+".txt")
    linetxt= open(file_path,'r', encoding='utf-8')
    linetxt=linetxt.read()
    linetxt = linetxt.split('\n')
    for j in range(len(linetxt)):
        if linetxt[j] not in shiraz_stations and j!=0 and j!=len(linetxt)-1:
            shiraz_graph[linetxt[j]] = {}
            shiraz_graph[linetxt[j]][linetxt[j+1]]=5
            shiraz_graph[linetxt[j]][linetxt[j-1]]=5
            shiraz_stations.append(linetxt[j])
        elif j==0:
            shiraz_graph[linetxt[j]] = {}
            shiraz_graph[linetxt[j]][linetxt[j + 1]] = 5
            shiraz_stations.append(linetxt[j])
        elif j==len(linetxt)-1:
            shiraz_graph[linetxt[j]] = {}
            shiraz_graph[linetxt[j]][linetxt[j-1]]=5
            
            shiraz_stations.append(linetxt[j])
        elif linetxt[j] in shiraz_stations:
            shiraz_graph[linetxt[j]].update({linetxt[j+1]:5,linetxt[j-1]:5})

tabriz_graph={}
tabriz_stations=[]
o=0
for i in range(1,1):
    file_path = os.path.join(script_dir, "tabriz\\line"+str(i)+".txt")
    linetxt= open(file_path,'r', encoding='utf-8')
    linetxt=linetxt.read()
    linetxt = linetxt.split('\n')
    for j in range(len(linetxt)):
        if linetxt[j] not in tabriz_stations and j!=0 and j!=len(linetxt)-1:
            tabriz_graph[linetxt[j]] = {}
            tabriz_graph[linetxt[j]][linetxt[j+1]]=5
            tabriz_graph[linetxt[j]][linetxt[j-1]]=5
            tabriz_stations.append(linetxt[j])
        elif j==0:
            tabriz_graph[linetxt[j]] = {}
            tabriz_graph[linetxt[j]][linetxt[j + 1]] = 5
            tabriz_stations.append(linetxt[j])
        elif j==len(linetxt)-1:
            tabriz_graph[linetxt[j]] = {}
            tabriz_graph[linetxt[j]][linetxt[j-1]]=5
            
            tabriz_stations.append(linetxt[j])
        elif linetxt[j] in tabriz_stations:
            tabriz_graph[linetxt[j]].update({linetxt[j+1]:5,linetxt[j-1]:5})

karaj_graph={}
karaj_stations=[]
o=0
for i in range(1,1):
    file_path = os.path.join(script_dir, "karaj\\line"+str(i)+".txt")
    linetxt= open(file_path,'r', encoding='utf-8')
    linetxt=linetxt.read()
    linetxt = linetxt.split('\n')
    for j in range(len(linetxt)):
        if linetxt[j] not in karaj_stations and j!=0 and j!=len(linetxt)-1:
            karaj_graph[linetxt[j]] = {}
            karaj_graph[linetxt[j]][linetxt[j+1]]=5
            karaj_graph[linetxt[j]][linetxt[j-1]]=5
            karaj_stations.append(linetxt[j])
        elif j==0:
            karaj_graph[linetxt[j]] = {}
            karaj_graph[linetxt[j]][linetxt[j + 1]] = 5
            karaj_stations.append(linetxt[j])
        elif j==len(linetxt)-1:
            karaj_graph[linetxt[j]] = {}
            karaj_graph[linetxt[j]][linetxt[j-1]]=5
            
            karaj_stations.append(linetxt[j])
        elif linetxt[j] in karaj_stations:
            karaj_graph[linetxt[j]].update({linetxt[j+1]:5,linetxt[j-1]:5})


all_town_graphs={
    "tehran":tehran_graph,
    "mashhad":mashhad_graph,
    "isfahan":isfahan_graph,
    "shiraz":shiraz_graph,
    "tabriz":tabriz_graph,
    "karaj":karaj_graph
}
class Node:
  def __init__(self,x_coord,y_coord):
      self.d=float('inf') #current distance from source node
      self.parent=None
      self.finished=False

class SettingManager(EventDispatcher):
    color = ListProperty([0, 0, 0, 1])
    colorhead= ListProperty([1,1,1,1])
    best_route = StringProperty("time")
    fonthead=StringProperty('Vazir-Bold')
    font=StringProperty('Vazir')
    icon=StringProperty("")
    city=StringProperty("tehran")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

setting_manager = SettingManager()



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
            self.rect_color = Color(0.5, 0.5, 0.5, 1)
            self.top_rect = Rectangle()
            self.rect_color2 = Color(0.7, 0.7, 0.7,1)
            self.rect2 = Rectangle()
            Color(0.5, 0.5, 0.5, 1)
            self.circle=Ellipse(radius=1000)
        inside_header = FloatLayout(pos_hint={'x': 0, 'y': 0.9}, size_hint=(1, 0.1))
        self.headerLabel = Label(text=fa("خوش آمدید! "), font_size=50, font_name=setting_manager.fonthead, color=setting_manager.colorhead, pos_hint={'x': 0, 'y': 0})
        
        inside_header.add_widget(self.headerLabel)
        self.add_widget(inside_header)
        self.bind(size=self.update_rect, pos=self.update_rect)
        self.inside = GridLayout()
        self.inside.cols = 1
        self.inside.rows = 2
        self.inside2 = GridLayout()
        self.inside2.cols = 1
        self.inside2.rows = 1
        self.insidebtn = MDCircularLayout(degree_spacing=60,start_from=90,pos_hint={'center_x':.5,'center_y':.5},circular_radius=300)

        self.label1=Label(text=fa("لطفا شهر خود را انتخاب کنید: "),font_size = 60, font_name=setting_manager.font,color=setting_manager.color)
        self.inside2.add_widget(self.label1)
        setting_manager.bind(color=self.update_color)
        setting_manager.bind(font=self.update_font)
        setting_manager.bind(fonthead=self.update_fonthead)

        self.tehran_btn = MDIconButton(icon="tehranlogo.png",icon_size="55sp")
        self.tehran_btn.bind(on_press=lambda instance,idx="tehran": self.pressed(idx))
        self.insidebtn.add_widget(self.tehran_btn)

        self.mashhad_btn = MDIconButton(icon="mashhadlogo.png",icon_size="55sp")
        self.mashhad_btn.bind(on_press=lambda instance,idx="mashhad": self.pressed(idx))
        self.insidebtn.add_widget(self.mashhad_btn)

        self.isfahan_btn = MDIconButton(icon="isfahanlogo.png",icon_size="55sp")
        self.isfahan_btn.bind(on_press=lambda instance,idx="isfahan": self.pressed(idx))
        self.insidebtn.add_widget(self.isfahan_btn)

        self.shiraz_btn = MDIconButton(icon="shirazlogo.png",icon_size="55sp")
        self.shiraz_btn.bind(on_press=lambda instance,idx="shiraz": self.pressed(idx))
        self.insidebtn.add_widget(self.shiraz_btn)

        self.tabriz_btn = MDIconButton(icon="tabrizlogo.png",icon_size="55sp")
        self.tabriz_btn.bind(on_press=lambda instance,idx="tabriz": self.pressed(idx))
        self.insidebtn.add_widget(self.tabriz_btn)

        self.karaj_btn = MDIconButton(icon="karajlogo.png",icon_size="55sp")
        self.karaj_btn.bind(on_press=lambda instance,idx="karaj": self.pressed(idx))
        self.insidebtn.add_widget(self.karaj_btn)

        self.inside.add_widget(self.inside2)
        self.inside.add_widget(self.insidebtn)
        self.add_widget(self.inside)

    
        
    
    def pressed(self,town, *kwargs):
        sm.current = town+"line"
        setting_manager.city=town

    def update_rect(self, *args): 
        self.top_rect.pos = (0, self.height * 0.9) 
        self.top_rect.size = (self.width, self.height * 0.1)
        self.rect2.pos = (0, 0) # Adjust position to be 90% down the screen 
        self.rect2.size = (self.width, self.height * 0.1)
        self.circle.pos= (self.width*0.5-450,self.height*0.01)
        
        self.circle.size=(900,900)

    def update_color(self, instance, value):
        self.label1.color = value
    def update_colorhead(self, instance, value):
        self.headerLabel.color = value
    def update_fonthead(self, instance, value):
        self.headerLabel.font_name = value
    def update_font(self, instance, value):
        self.label1.font_name = value
class LinesPage(Screen):
    def __init__(self,town, **kwargs):
        self.town=town
        super(LinesPage, self).__init__(**kwargs)
    
    def line1_pressed(self, instance):
        sm.current=self.town+"line1"
    def line2_pressed(self, instance):
        sm.current=self.town+"line2"
    def line3_pressed(self, instance):
        sm.current=self.town+"line3"

    def line4_pressed(self, instance):
        sm.current=self.town+"line4"
    def line5_pressed(self, instance):
        sm.current=self.town+"line5"

    def line6_pressed(self, instance):
        sm.current=self.town+"line6"
    def line7_pressed(self, instance):
        sm.current=self.town+"line7"

    def on_kv_post(self, base_widget):
        
        self.towncolor=towncolor(self.town)
        self.townbtnspos=townbtnspos(self.town)
        self.num_line=self.towncolor[-1]
        with self.canvas.before:
            self.toprect_color = Color(0.5, 0.5, 0.5, 1)
            self.top_rect = Rectangle()
            self.rect_color2 = Color(0.7, 0.7, 0.7,1)
            self.rect2 = Rectangle()
        self.lines=[]
        with self.canvas:
            for i in range(self.num_line):
                Color(*self.towncolor[i])
                self.lines.append(Line(width=10))
        self.lineBtns=[]
        for i in range(self.num_line):
            self.lineBtns.append(BaseButton(pos_hint = {'center_x':.5 , 'y':self.townbtnspos[i]},line_width = 10,line_color=self.towncolor[i],rounded_button=True,md_bg_color=(1,1,1,1)))
            self.add_widget(self.lineBtns[-1])
            function_name = f"line{i+1}_pressed"
            function_to_call = getattr(self, function_name)
            self.lineBtns[i].bind(on_press=function_to_call)
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        self.bind(size=self.update_line_position, pos=self.update_line_position) 
        self.lineBtns[0].bind(pos=self.update_line_position)
        self.linelabels1=[]
        self.linelabels2=[]
        j=0
        for i in self.townbtnspos[:self.num_line]:
            j+=1
            if j%2!=0:
                xlabel=0.8
            else:
                xlabel=0.3
            file_path = os.path.join(script_dir, str(self.town)+"\\line"+str(j)+".txt")
            linetxt= open(file_path,'r', encoding='utf-8')
            self.linelabel = Label(text=fa("خط "+str(j)),font_size = 40, font_name=setting_manager.fonthead ,color=setting_manager.color,pos_hint = {'center_x':xlabel , 'y':i-0.45})
            self.linelabels1.append(self.linelabel)
            self.add_widget(self.linelabel)
            taj=linetxt.readlines()[0]+' '
            linetxt= open(file_path,'r', encoding='utf-8')
            text=taj+"- "+linetxt.readlines()[len(linetxt.readlines())-1]
            clean_text = text.replace("\n","")
            self.linelabel2 = Label(text=fa(clean_text),font_size = 40, font_name=setting_manager.fonthead ,color=setting_manager.color,pos_hint = {'center_x':xlabel , 'y':i-0.5})
            self.linelabels2.append(self.linelabel2)
            self.add_widget(self.linelabel2)
        


        
        


        self.searchbox=TextInput(pos_hint={'x':0.01,'y':0.8},size_hint=(0.3,0.08),hint_text=fa("نام ایستگاه/مکان"),hint_text_color=(0.4, 0.4, 0.4, 1),font_name=setting_manager.font,background_color="white",border=(4,4,4,4),base_direction='rtl',font_context=setting_manager.font,text_language='fa',font_size=30)
        
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
        

        settingBtn = MDIconButton(icon="icons8-settings-480.png",pos_hint={'center_x':0.1,'center_y':.5},icon_size="50sp")
        apiMapBtn = MDIconButton(icon="mapapiicon.png",pos_hint={'center_x':0.3,'center_y':.5},icon_size="50sp")
        mapBtn = MDIconButton(icon="mapicon.png",pos_hint={'center_x':0.9,'center_y':.5},icon_size="50sp")
        navBtn = MDIconButton(icon="navicon.png",pos_hint={'center_x':0.7,'center_y':.5},icon_size="50sp")
        lineBtn = MDIconButton(disabled=True, icon="lineicon2.png",pos_hint={'center_x':0.5,'center_y':.5},icon_size="50sp")
        
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
        self.headerLabel = Label(text=fa("فهرست خطوط"), font_size=50, font_name=setting_manager.fonthead, color=setting_manager.colorhead, pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(self.headerLabel)
        self.add_widget(inside_header)

        setting_manager.bind(color=self.update_color)
        setting_manager.bind(fonthead=self.update_fonthead)
        setting_manager.bind(colorhead=self.update_colorhead)
        setting_manager.bind(fonthead=self.update_font)
        setting_manager.bind(city=self.update_city)
        

   
        
        
    def update_color(self, instance, value):
        for i in range(self.num_line):
            self.linelabels1[i].color=value
            self.linelabels2[i].color=value

    def update_city(self, instance, value):
        pass
        
    def update_colorhead(self, instance, value):
        self.headerLabel.color = value
        for i in range(self.num_line):
            self.lineBtns[i].md_bg_color=value
        
    def update_fonthead(self, instance, value):
        self.headerLabel.font_name = value
        for i in range(self.num_line):
            self.linelabels1[i].font_name=value
            self.linelabels2[i].font_name=value
        
    def update_font(self, instance, value):
        return 


    def update_scroll_size(self, instance, value):
        self.search_results_scroll.height = self.searchbox.height * 2

    def update_rect(self, *args): 
        self.top_rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.top_rect.size = (self.width, self.height * 0.1)
        self.rect2.pos = (0, 0) # Adjust position to be 90% down the screen 
        self.rect2.size = (self.width, self.height * 0.1)

    def update_scroll_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def update_line_position(self, *args):
        for i in range(self.num_line):
            if i%2==0:
                self.lines[i].points = [self.children[1].center_x, self.children[len(self.children)-i-1].center_y, self.width, self.children[len(self.children)-i-1].center_y]
            else:
                 self.lines[i].points = [self.children[1].center_x, self.children[len(self.children)-i-1].center_y, 0, self.children[len(self.children)-i-1].center_y]
        
        
        

    def map_pressed(self, instance):
        sm.current = self.town+"map"
    def apimap_pressed(self, instance):
        sm.current = self.town+"apimap"
    def nav_pressed(self, instance):
        sm.current = self.town+"nav"
    def setting_pressed(self, instance):
        sm.current = "setting"
    
    
    def on_label_touch_down(self, instance, touch, match):
        
        if touch.collide_point(*touch.pos):  # Ensure touch is on the label
               
            return True
        return False 

    
    def on_text(self, instance, value):
        self.search_results_box.clear_widgets()
        self.ser_labels = []
        
        if value.strip(): 
            matches = self.search_names(value)
            for match in matches:
                label = Label(text=fa(match), font_size=30, font_name=setting_manager.font, color="black")
                
                # Bind the touch event properly using partial
                self.ser_labels.append(label)
                self.ser_labels[-1].bind(on_touch_down=partial(self.on_label_touch_down, match))
                self.search_results_box.add_widget(self.ser_labels[-1])

            self.search_results_scroll.size_hint_y = None  
            self.search_results_scroll.height = self.searchbox.height * 2 
        else:
            self.search_results_scroll.size_hint_y = 0


        


    def search_names(self, query):
        script_dir = os.path.dirname(__file__)
        names = []
        for i in range(1, townnumlines[self.town]):
            file_path = os.path.join(script_dir, self.town, f"line{i}.txt")
            with open(file_path, 'r', encoding='utf-8') as file:
                names.extend([line.strip() for line in file])
            
        pattern = re.compile(query, re.IGNORECASE)
        for i in range(1, townnumlines[self.town]):
            file_path = os.path.join(script_dir, self.town, f"line{i}infoplacescut.txt")
            with open(file_path, 'r', encoding='utf-8') as file:
                names.extend([line.strip("، ") for line in file])
            
        
            
        pattern = re.compile(query, re.IGNORECASE)
        return [name for name in names if pattern.search(name)]
    
    def searchBtn_pressed(self,instance):
        k=finder(self.searchbox.text,self.town)
        if k!=False:
            sm.current=k
        else:
            k=nearplacesfinder(self.searchbox.text,self.town)
            if k!=False:
                sm.current=k
        self.searchbox.text = ''

class Setting(Screen):
    def __init__(self, **kwargs):
        super(Setting, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        
        with self.canvas.before:
            self.rect_color = Color(0.5, 0.5, 0.5, 1)
            self.rect = Rectangle()
            self.rect_color2 = Color(0.7, 0.7, 0.7,1)
            self.rect2 = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.sun_pic='sun1.png'
        self.sun_dis=True
        self.moon_pic='moon1.png'
        self.moon_dis=False
        self.Grid=FloatLayout(pos=(0,Window.height*0.1),size_hint=(1,0.8))
        self.theme_lbl=Label(text=fa("پوسته ی برنامه : "),font_size = 50, font_name=setting_manager.font,color=setting_manager.color,pos_hint={'center_x':0.75,'center_y':.925})
        theme_grid=GridLayout(size_hint=(0.35,0.9),cols=2,rows=1,pos_hint={'center_x':0.2,'center_y':.55})
        self.sunbtn=MDIconButton(icon=self.sun_pic,disabled=self.sun_dis,icon_size="45sp",pos_hint={'center_x':0,'center_y':.5})
        self.moonbtn=MDIconButton(icon=self.moon_pic,disabled=self.moon_dis,icon_size="45sp")
        theme_grid.add_widget(self.sunbtn)
        theme_grid.add_widget(self.moonbtn)
        self.sunbtn.bind(on_press=self.sun_press)
        self.moonbtn.bind(on_press=self.moon_press)
        self.Grid.add_widget(theme_grid)
        self.Grid.add_widget(self.theme_lbl)
        

        self.cityBtn=Button(size_hint=(0.3,0.1),text=fa('تغییر شهر'), font_size=40,font_name=setting_manager.font,pos_hint={'x':0.35,'y':0.3})
        self.cityBtn.bind(on_press=self.city_press)
        self.Grid.add_widget(self.cityBtn)

        self.listBtn=Button(text=fa("تغییر فونت"), font_size=40,font_name=setting_manager.font,pos_hint={'center_x':.5,'center_y':.6},size_hint=(0.3,0.1))
        self.Grid.add_widget(self.listBtn)
        self.listBtn.bind(on_press=self.dropdown)
        
        self.add_widget(self.Grid)
        



        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(disabled=True,icon="icons8-settings-4802.png",pos_hint={'center_x':0.1,'center_y':.5},icon_size="50sp")
        apiMapBtn = MDIconButton(icon="mapapiicon.png",pos_hint={'center_x':0.3,'center_y':.5},icon_size="50sp")
        mapBtn = MDIconButton(icon="mapicon.png",pos_hint={'center_x':0.9,'center_y':.5},icon_size="50sp")
        navBtn = MDIconButton(icon="navicon.png",pos_hint={'center_x':0.7,'center_y':.5},icon_size="50sp")
        lineBtn = MDIconButton(icon="lineicon.png",pos_hint={'center_x':0.5,'center_y':.5},icon_size="50sp")
        
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
        self.headerLabel = Label(text=fa("تنظیمات"), font_size=50, font_name=setting_manager.fonthead, color=setting_manager.colorhead, pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(self.headerLabel)
        self.add_widget(inside_header)

        setting_manager.bind(color=self.update_color)
        setting_manager.bind(fonthead=self.update_fonthead)
        setting_manager.bind(colorhead=self.update_colorhead)
        setting_manager.bind(fonthead=self.update_font)


    def dropdown(self,instance):
        self.fontlist=MDDropdownMenu(caller=self.listBtn,width_mult=4)
        self.fontlist.items.append({"viewclass": "OneLineListItem", "text": "Vazir", "on_release":lambda x="Vazir": self.menu_callback(x)})
        self.fontlist.items.append({"viewclass": "OneLineListItem", "text": "Roya", "on_release":lambda x="Roya": self.menu_callback(x)})
        self.fontlist.items.append({"viewclass": "OneLineListItem", "text": "Traffic", "on_release":lambda x="Traffic": self.menu_callback(x)})
        self.fontlist.items.append({"viewclass": "OneLineListItem", "text": "Negaar", "on_release":lambda x="Negaar": self.menu_callback(x)})
        self.fontlist.open()

    def menu_callback(self, selected_item):
        
        setting_manager.font=selected_item
        setting_manager.fonthead=selected_item+'-Bold'
        self.fontlist.dismiss()

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)
        self.rect2.pos = (0, 0) # Adjust position to be 90% down the screen 
        self.rect2.size = (self.width, self.height * 0.1)

    def sun_press(self, instance):
        setting_manager.colorhead = [1,1,1, 1]
        setting_manager.color = [0, 0, 0, 1]
        setting_manager.icon=""
        
        self.sun_dis=False
        self.sun_pic="sun2.png"
        self.moonbtn.icon="moon1.png"
        self.moonbtn.disabled=False
        self.sunbtn.icon="sun1.png"
        self.sunbtn.disabled=True
        Window.clearcolor=(1,1,1,1)
        
    def moon_press(self, instance):
        setting_manager.color = [1,1,1, 1]
        setting_manager.colorhead = [0, 0, 0, 1]
        setting_manager.icon=" light"
        self.moon_dis=False
        self.moon_pic="moon2.png"
        self.moonbtn.icon="moon2.png"
        self.moonbtn.disabled=True
        self.sunbtn.icon="sun2.png"
        self.sunbtn.disabled=False
        Window.clearcolor=(0,0,0,1)

    
        
    def city_press(self,instance):
        sm.current="welcome"


    def update_color(self, instance, value):
        self.theme_lbl.color = value
    def update_colorhead(self, instance, value):
        self.headerLabel.color = value
        self.cityBtn.color=value
        self.listBtn.color = value
    def update_fonthead(self, instance, value):
        self.headerLabel.font_name = value
    def update_font(self, instance, value):
        self.theme_lbl.font_name = value
        self.cityBtn.font_name=value
        self.listBtn.font_name = value

    def map_pressed(self, instance):
        sm.current = setting_manager.city+"map"
    def line_pressed(self, instance):
        sm.current = setting_manager.city+"line"
    def nav_pressed(self, instance):
        sm.current = setting_manager.city+"nav"
    def apimap_pressed(self, instance):
        sm.current = setting_manager.city+"apimap"
class APIMap(Screen):
    def __init__(self,town, **kwargs):
        self.town=town
        super(APIMap, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        with self.canvas.before:
            self.rect_color = Color(0.5, 0.5, 0.5, 1)
            self.rect = Rectangle()
            self.rect_color2 = Color(0.7, 0.7, 0.7,1)
            self.rect2 = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        self.linegraph={
            "tehran":["red","blue","lightblue","yellow","green","pink","purple",7],
            "mashhad": ["green","blue","red",2],
            "isfahan":["red",1],
            "shiraz":["red","green",2],
            "tabriz":["lightblue",1],
            "karaj":["gold","lightblue",2]
        }
        map_layout=FloatLayout( size_hint=(1, 0.8))
        self.lat,self.lon=townLatLon(self.town)
        self.map=MapView(zoom=11, lat=self.lat, lon= self.lon,pos=(0,Window.height*0.1))
        for i in range(1,self.linegraph[self.town][-1]+1):
            file_path = os.path.join(script_dir, self.town+"\\line"+str(i)+"cords.txt")
            line = open(file_path,'r')
            line=line.readlines()
            for j in range(len(line)):
                marker=MapMarker(lat=float(line[j][1:10]),lon=float(line[j][12:19]),source="mapmarker"+self.linegraph[self.town][i-1]+".png",size=(32,32),anchor_x=0.5,anchor_y=0)
                self.map.add_widget(marker)
        
        self.map.map_source="osm"
        map_layout.add_widget(self.map)
        self.add_widget(map_layout)

        self.user_marker = MapMarker(lat=self.lat, lon=self.lon, source="user_marker.png", size=(32, 32), anchor_x=0.5, anchor_y=0.5)
        self.map.add_widget(self.user_marker)

        with self.user_marker.canvas.before:
            self.rotation = Rotate()
            self.rotation.origin = self.user_marker.center
            self.rotation.angle = 0

        # Start compass (to get orientation)
        try:
            compass.enable()
            Clock.schedule_interval(self.update_compass, 0.1)  # Check compass every 0.1s
        except NotImplementedError:
            pass

        try:
            gps.configure(on_location=self.on_gps_location, on_status=self.on_gps_status)
            gps.start(minTime=1000, minDistance=1)  # updates every 1 second or 1 meter
        except NotImplementedError:
            pass  # GPS not available (e.g., desktop)


        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(icon="icons8-settings-480.png",pos_hint={'center_x':0.1,'center_y':.5},icon_size="50sp")
        apiMapBtn = MDIconButton(disabled=True,icon="mapapiicon2.png",pos_hint={'center_x':0.3,'center_y':.5},icon_size="50sp")
        mapBtn = MDIconButton(icon="mapicon.png",pos_hint={'center_x':0.9,'center_y':.5},icon_size="50sp")
        navBtn = MDIconButton(icon="navicon.png",pos_hint={'center_x':0.7,'center_y':.5},icon_size="50sp")
        lineBtn = MDIconButton(icon="lineicon.png",pos_hint={'center_x':0.5,'center_y':.5},icon_size="50sp")
        
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
        self.headerLabel = Label(text=fa("نقشه متحرک"), font_size=50, font_name=setting_manager.fonthead ,color=setting_manager.colorhead, pos_hint={'x': 0, 'y': 0})
        setting_manager.bind(colorhead=self.update_theme)
        
        setting_manager.bind(fonthead=self.update_fonthead)
        inside_header.add_widget(self.headerLabel)
        self.add_widget(inside_header)


        
    def on_gps_location(self, **kwargs):
        # New GPS coordinates
        new_lat = kwargs['lat']
        new_lon = kwargs['lon']
        
        # Update marker's position
        self.user_marker.lat = new_lat
        self.user_marker.lon = new_lon
        
        # Create an animation for smooth movement
        anim = Animation(
            x=self.map.lon_to_x(new_lon), 
            y=self.map.lat_to_y(new_lat), 
            duration=2  # 2 seconds for smooth movement
        )
        
        # Start the animation on the marker
        anim.start(self.user_marker)
        
        # Update the map center on the new position
        self.map.center_on(new_lat, new_lon)

    def on_gps_status(self, stype, status):
        pass  # You can ignore GPS status if you want

    def update_compass(self, dt):
        orientation = compass.orientation
        if orientation and 'azimuth' in orientation:
            azimuth = orientation['azimuth']  # degrees
            self.rotation.angle = -azimuth 

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)
        self.rect2.pos = (0, 0) # Adjust position to be 90% down the screen 
        self.rect2.size = (self.width, self.height * 0.1)

    def update_theme(self, instance, value):
        self.headerLabel.color = value
    def update_fonthead(self, instance, value):
        self.headerLabel.font_name = value
    def map_pressed(self, instance):
        sm.current = self.town+"map"
    def line_pressed(self, instance):
        sm.current = self.town+"line"
    def nav_pressed(self, instance):
        sm.current = self.town+"nav"
    def setting_pressed(self, instance):
        sm.current = "setting"



class Map(Screen):
    def __init__(self,town, **kwargs):
        self.town=town
        super(Map, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        
        
        file_path = os.path.join(script_dir, self.town+"\\map"+setting_manager.icon+".png")
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
            self.rect_color = Color(0.5, 0.5, 0.5, 1)
            self.rect = Rectangle()
            self.rect_color2 = Color(0.7, 0.7, 0.7,1)
            self.rect2 = Rectangle()
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(icon="icons8-settings-480.png",pos_hint={'center_x':0.1,'center_y':.5},icon_size="50sp")
        apiMapBtn = MDIconButton(icon="mapapiicon.png",pos_hint={'center_x':0.3,'center_y':.5},icon_size="50sp")
        mapBtn = MDIconButton(disabled=True,icon="mapicon2.png",pos_hint={'center_x':0.9,'center_y':.5},icon_size="50sp")
        navBtn = MDIconButton( icon="navicon.png",pos_hint={'center_x':0.7,'center_y':.5},icon_size="50sp")
        lineBtn = MDIconButton(icon="lineicon.png",pos_hint={'center_x':0.5,'center_y':.5},icon_size="50sp")
        
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
        self.headerLabel = Label(text=fa("نقشه رسمی"), font_size=50, font_name=setting_manager.fonthead, color=setting_manager.colorhead, pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(self.headerLabel)
        self.add_widget(inside_header)
        setting_manager.bind(colorhead=self.update_theme)
        setting_manager.bind(fonthead=self.update_fonthead)
        setting_manager.bind(icon=self.update_icon)

    def update_icon(self, instance, value):
        self.image.source = os.path.join(script_dir, self.town+"\\map"+value+".png")
    def update_theme(self, instance, value):
        self.headerLabel.color = value
    def update_fonthead(self, instance, value):
        self.headerLabel.font_name = value

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)
        self.rect2.pos = (0, 0) # Adjust position to be 90% down the screen 
        self.rect2.size = (self.width, self.height * 0.1)

    def update_img(self, *args): 
        self.Grid.size_hint=(1,.8)
        self.stencil.pos=(0,Window.height*0.1)
        self.scatter.size=(Window.width,Window.height*0.8)
        self.scatter.pos=(0,Window.height*0.1)
        self.image.size=(Window.width,Window.height*0.8)


    def mapapi_pressed(self, instance):
        sm.current = self.town+"apimap"
    def line_pressed(self, instance):
        sm.current = self.town+"line"
    def nav_pressed(self, instance):
        sm.current = self.town+"nav"
    def setting_pressed(self, instance):
        sm.current = "setting"
class Nav(Screen):
    def __init__(self,town, **kwargs):
        self.town=town
        super(Nav, self).__init__(**kwargs)
    def on_kv_post(self, base_widget):
        global screens
        with self.canvas.before:
            self.rect_color = Color(0.5, 0.5, 0.5, 1)
            self.rect = Rectangle()
            self.rect_color2 = Color(0.7, 0.7, 0.7,1)
            self.rect2 = Rectangle()

        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.footer = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.1))
        

        settingBtn = MDIconButton(icon="icons8-settings-480.png",pos_hint={'center_x':0.1,'center_y':.5},icon_size="50sp")
        apiMapBtn = MDIconButton(icon="mapapiicon.png",pos_hint={'center_x':0.3,'center_y':.5},icon_size="50sp")
        mapBtn = MDIconButton(icon="mapicon.png",pos_hint={'center_x':0.9,'center_y':.5},icon_size="50sp")
        navBtn = MDIconButton(disabled=True, icon="navicon2.png",pos_hint={'center_x':0.7,'center_y':.5},icon_size="50sp")
        lineBtn = MDIconButton(icon="lineicon.png",pos_hint={'center_x':0.5,'center_y':.5},icon_size="50sp")
        
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
        self.headerLabel = Label(text=fa("مسیریاب"), font_size=50, font_name=setting_manager.fonthead, color=setting_manager.colorhead, pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(self.headerLabel)
        self.add_widget(inside_header)


        self.layout=GridLayout(pos_hint={'x': 0.25, 'y':0.3},size_hint=(0.5,0.45))
        self.layout.rows=3
        self.layout.cols=1
        self.mabdaTextinp=TextInput(size_hint=(1,0.4),pos=(0.4,0),hint_text=fa("مبدا"),hint_text_color=setting_manager.colorhead,foreground_color=setting_manager.colorhead,font_name=setting_manager.font,background_color=(0.4, 0.4, 0.4, 1),border=(4,4,4,4),base_direction='rtl',font_context=setting_manager.font,text_language='fa')
        self.maghsadTextinp=TextInput(size_hint=(1,0.4),pos=(0.4,0),hint_text=fa("مقصد"),hint_text_color=setting_manager.colorhead,foreground_color=setting_manager.colorhead,font_name=setting_manager.font,background_color=(0.4, 0.4, 0.4, 1),border=(4,4,4,4),base_direction='rtl',font_context=setting_manager.font,text_language='fa')
        self.searchBtn=Button(size_hint=(1,0.2),text=fa('جستجو'), font_size=40,font_name=setting_manager.font,background_color=(0,0,0.75,1))
        self.btnlayout=GridLayout(size_hint=(0.5,0.5),rows=1,cols=1)
        self.layout.add_widget(self.mabdaTextinp)
        self.layout.add_widget(self.maghsadTextinp)
        self.btnlayout.add_widget(self.searchBtn)
        self.layout.add_widget(self.btnlayout)
        self.add_widget(self.layout)
        self.searchBtn.bind(on_press=lambda instance: self.search_pressed(screens,instance))
        setting_manager.bind(colorhead=self.update_theme)
        setting_manager.bind(color=self.update_color)
        setting_manager.bind(fonthead=self.update_fonthead)
        setting_manager.bind(font=self.update_font)

    def update_theme(self, instance, value):
        self.headerLabel.color = value
        self.mabdaTextinp.hint_text_color = value
        self.maghsadTextinp.hint_text_color= value
        self.mabdaTextinp.foreground_color=value
        self.maghsadTextinp.foreground_color=value
        
    
    def update_color(self,instance,value):
        pass

    def update_font(self, instance, value):
        self.searchBtn.font_name = value
        self.mabdaTextinp.font_name = value
        self.mabdaTextinp.font_context = value
        self.maghsadTextinp.font_name= value
        self.maghsadTextinp.font_context= value
    def update_fonthead(self, instance, value):
        self.headerLabel.font_name = value
    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)
        self.rect2.pos = (0, 0) # Adjust position to be 90% down the screen 
        self.rect2.size = (self.width, self.height * 0.1)

    def mapapi_pressed(self, instance):
        sm.current = self.town+"apimap"
    def line_pressed(self, instance):
        sm.current = self.town+"line"
    def map_pressed(self, instance):
        sm.current =self.town+ "map"
    def setting_pressed(self, instance):
        sm.current = "setting"
    def search_pressed(self,screens, instance):
        if self.mabdaTextinp.text!='' and self.maghsadTextinp.text!='' and finder(self.mabdaTextinp.text,self.town)!=False and finder(self.maghsadTextinp.text,self.town)!=False:
            path,total_weight=dijkstra_with_total_weight(all_town_graphs[self.town], self.mabdaTextinp.text, self.maghsadTextinp.text)
            
            adads=line_finder(path,self.town)
            
            
            screens.append(LineWin(name="search", esm=self.town+"\\line" + str(1) + ".txt", adad=adads,rang=(1,1,1,1), t=True,stations=path,town=self.town))

            sm.add_widget(screens[len(screens)-1])
            sm.current="search"
            self.mabdaTextinp.text=''
            self.maghsadTextinp.text=''

class LineWin(Screen):
    def __init__(self, esm,adad,rang,t,stations,town, **kwargs):
        super(LineWin, self).__init__(**kwargs)
        self.esm = esm
        self.t=t
        self.stations=stations
        self.town=town
        if self.t:
            self.adad = adad
            self.rang = rang
            besamt=[]
            start=0
            for i in range(1,townnumlines[self.town]+1):
                file_path = os.path.join(script_dir,self.town+"\\line"+str(i)+".txt")
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
                rangs.append(towncolors[self.town][int(finder(self.stations[i],self.town)[0])-1])
        else:
            self.adad = adad
            self.rang = rang
            line = open(os.path.join(script_dir, self.esm), "r", encoding='utf-8')
            lines = line.readlines()
            rangs=[towncolors[self.town][int(self.adad)-1]]*len(lines)
            besamt=lines[len(lines)-1]
                
        layoutscroll = GridLayout(cols=1, spacing=70, size_hint=(1,None))
        self.root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.885))
        self.bind(size=self.update_rect, pos=self.update_rect)
        self.StationBtns=[]
        r=0
        file_path_intersecs = os.path.join(script_dir, self.town+"\\intersections.txt")
        open_intersecs=open(file_path_intersecs,'r',encoding='utf-8')
        intersecs=open_intersecs.read().split('\n')
        k=0
        self.inters=[]
        self.labels=[]
        for i in lines:
            if i in intersecs :
                
                self.StationBtns.append(MDIconButton(rounded_button=False,icon=os.path.join(script_dir, self.town+"\\intersecs_pics\\"+str(setting_manager.colorhead)+" ("+str(intersecs.index(i)+1)+").png"),pos_hint={'center_x':0.7},icon_size="42sp"))
                self.StationBtns[-1].pos_hint = {'center_x': 0.505, 'center_y': 0.5}
                self.inters.append(i)
                
            elif self.t:
                self.StationBtns.append( BaseButton(line_width = 10,line_color=rangs[r],rounded_button=True,md_bg_color=setting_manager.colorhead))
                self.StationBtns[-1].pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            else:
                self.StationBtns.append( BaseButton(line_width = 10,line_color=self.rang,rounded_button=True,md_bg_color=setting_manager.colorhead))
                self.StationBtns[-1].pos_hint = {'center_x': 0.5, 'center_y': 0.5}

            label = Label(text=i, size_hint=(None, None), color=setting_manager.color, font_name=setting_manager.font, font_size=47)

            float_layout = FloatLayout(size_hint_y=None, height=self.StationBtns[len(self.StationBtns)-1].height)
            if lines.index(i) % 2 == 0:
                xlabel = 0.7
            else:
                xlabel = 0.2
            
            
            label.pos_hint = {'x': xlabel, 'center_y': 0.1}
            self.labels.append(label)
            float_layout.add_widget(self.StationBtns[-1])
            float_layout.add_widget(label)
            layoutscroll.add_widget(float_layout)
            if not self.t:
                self.StationBtns[len(self.StationBtns)-1].bind(on_press=lambda instance, idx=len(self.StationBtns)-1: self.stationBtn_pressed(idx, self.adad))
            else:
                self.StationBtns[len(self.StationBtns)-1].bind(on_press=lambda instance, idx=int(finder(lines[len(self.StationBtns)-1],self.town)[2])-1, idx2= int(finder(lines[len(self.StationBtns)-1],self.town)[0]) : self.stationBtn_pressed(idx, idx2))
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
        self.headerLabel = Label(text=headertext, font_size=50, font_name=setting_manager.fonthead, 
                            color=setting_manager.colorhead, pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(self.headerLabel)
        self.add_widget(inside_header)
        self.info_layout = FloatLayout(size_hint=(0.2, 0.1), pos_hint={'x': 0.8, 'y':0.1})
        self.infoBtn = MDIconButton(rounded_button=False,icon=os.path.join(script_dir, "more-info-icon"+setting_manager.icon+".png"),icon_size="42sp",pos_hint={'center_x':0.5})
        self.info_layout.add_widget(self.infoBtn)
        self.infoBtn.bind(on_press=self.info_pressed)
        self.add_widget(self.info_layout)

        self.back_layout = FloatLayout(size_hint=(0.2, 0.1), pos_hint={'x': 0.05, 'top': 1}) 
        self.backBtn = MDIconButton(icon="back"+setting_manager.icon+".png", icon_size="42sp") 
        self.back_layout.add_widget(self.backBtn) 
        self.add_widget(self.back_layout)
        self.backBtn.bind(on_press=self.back_pressed)
        layoutscroll.bind(minimum_height=layoutscroll.setter('height'))
        self.bind(size=self.layout_update)
        
        self.layoutscroll = layoutscroll
        self.rangs = rangs
        self.bind(size=lambda instance,idx=self.layoutscroll: self.clearing_canvas_2(idx))
        setting_manager.bind(color=self.update_color)
        setting_manager.bind(colorhead=self.update_colorhead)
        setting_manager.bind(icon=self.update_icon)
        setting_manager.bind(font=self.update_font)
        setting_manager.bind(fonthead=self.update_fonthead)
        Clock.schedule_interval(self.line_update, 0.1)
        
        
    
    def update_color(self, instance, value):
        for i in range(len(self.labels)):
            self.labels[i].color=value
        
    def update_font(self, instance, value):
        for i in range(len(self.labels)):
            self.labels[i].font_name=value
    def update_fonthead(self, instance, value):
        self.headerLabel.font_name=value
        
        
    def update_colorhead(self, instance, value):
        for i in range(0,len(self.StationBtns)):
            self.StationBtns[i].md_bg_color=value
        self.headerLabel.color=value
    def update_icon(self, instance, value):
        self.backBtn.icon="back"+value+".png"
        self.infoBtn.icon="more-info-icon"+value+".png"

    def clearing_canvas_2(self,layoutscroll,*args):
        self.clearing_canvas(self.layoutscroll)
    def clearing_canvas(self,layoutscroll,*args):
        layoutscroll.canvas.before.clear()


    def update_lines_colors(self, layoutscroll, StationBtns, rangs):
        
        
        layoutscroll.canvas.before.clear()
        
        with layoutscroll.canvas.before:
            Color(*rangs[0])
            Line(points=[self.center_x, StationBtns[1].center_y+StationBtns[1].center_y/10, self.center_x, StationBtns[1].center_y], width=10)
            
            for i in range(1,len(StationBtns) - 1):
                btn1 = StationBtns[i]
                btn2 = StationBtns[i + 1]
                Color(*rangs[i])
                Line(points=[self.center_x, btn1.center_y, self.center_x, btn2.center_y], width=10)
                

    def line_update(self,*args):
        self.StationBtns2 = [[self.width*0.5,self.height*2.25]]+self.StationBtns[1:]
        
        self.update_positions_and_draw_lines()

    def update_label_size(self, label, width, height):
        label.font_size = height * 0.02  
        label.size_hint = (None, None)   
        label.size = (width * 0.2, height * 0.05)  
    def update_rect(self, *args):
        self.rect.pos = (0, self.height * 0.9)
        self.rect.size = (self.width, self.height * 0.1)

    def layout_update(self,*args):
        self.root.height=self.height*0.885

    def update_positions_and_draw_lines(self, *args):
        self.layoutscroll.do_layout()
        self.update_lines_colors(self.layoutscroll, self.StationBtns2, self.rangs)


    def back_pressed(self,*args):
        if self.t:
            sm.current=self.town+"nav"
            sm.remove_widget(screens[len(screens)-1])
            
            screens.pop()
        else:
            sm.current=self.town+"line"
            

    def stationBtn_pressed(self,namd,adadd,*args):
        sm.current=str(adadd)+','+str(namd+1)+self.town
        if self.t:
            sm.remove_widget(screens[-1])
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
            self.popup=Popup(title=fa(txt),size_hint=(1,0.2),pos_hint={'center_x':0.5,'center_y':0.5})
            self.popup.open()
        else:
            self.popup=Popup(title=fa("زمانبندی حرکت قطار ها(ممکن است زمان ها درست نباشند)"),size_hint=(1,0.6),pos_hint={'center_x':0.5,'center_y':0.5})
            self.Grid=FloatLayout(size_hint=(1,1))
            self.stencil=StencilView(pos_hint={'center_x':0.5,'center_y':0.5})
            self.Grid.add_widget(self.stencil)
            self.scatter=Scatter(do_translation=True,do_rotation=False,size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5},scale_min=1)
            self.stencil.add_widget(self.scatter)
            self.imagepop=AsyncImage(source=os.path.join(script_dir, self.town+"\\headway_pics\\"+self.adad+".jpg"))
            self.scatter.add_widget(self.imagepop)
            self.bind(size=self.update_img, pos=self.update_img)
            self.popup.add_widget(self.Grid)
            self.popup.open()
            self.update_img()
    def update_img(self, *args): 
        self.Grid.size_hint=(1,1)
        self.stencil.pos=(0,self.popup.height*0.1)
        self.scatter.size=(self.popup.width,self.popup.height*1)
        self.scatter.pos=(0,self.popup.height*0.25)
        self.imagepop.size=(self.popup.width,self.popup.height*1)



class StationWin(Screen):
    def __init__(self,nam,rang,adad,esm,town,**kwargs):
        super(StationWin, self).__init__(**kwargs)
        self.rang = rang
        self.adad = adad
        self.esm = esm
        self.nam = nam
        self.town=town
        with self.canvas.before:
            self.rect_color = Color(*self.rang)
            self.rect = Rectangle()
        self.bind(size=self.update_rect, pos=self.update_rect)
        line = open(os.path.join(script_dir, self.esm), "r", encoding='utf-8')
        lines = line.readlines()
        staLine=lines[adad-1].split(" - ")
        
        staName=staLine[0]
        inside_header = RelativeLayout(size_hint=(1, 0.1), pos_hint={'top': 1})
        self.headerLabel = Label(text=fa(staName), font_size=50, font_name=setting_manager.fonthead, color=setting_manager.colorhead, pos_hint={'x': 0, 'y': 0})
        inside_header.add_widget(self.headerLabel)
        self.add_widget(inside_header)

        staEnters=staLine[1]
        staATMs=staLine[2]
        staPlaces=staLine[3]
        self.layout = GridLayout(size_hint=(1,.9))
        self.layout.rows=6
        self.layout.cols=1
        self.lblenters=Label(text=fa("تعداد ورودی ها :"),color=setting_manager.color, font_name=setting_manager.fonthead, font_size=50)
        self.layout.add_widget(self.lblenters)
        self.enters=Label(text=fa(staEnters),color=setting_manager.color, font_name=setting_manager.font, font_size=45)
        self.layout.add_widget(self.enters)
        self.lblatms=Label(text=fa("تعداد خودپرداز ها :"),color=setting_manager.color, font_name=setting_manager.fonthead, font_size=50)
        self.layout.add_widget(self.lblatms)
        self.atms=Label(text=fa(staATMs),color=setting_manager.color, font_name=setting_manager.font, font_size=45)
        self.layout.add_widget(self.atms)
        self.lblplaces=Label(text=fa("مکان های مهم اطراف :"),color=setting_manager.color, font_name=setting_manager.fonthead, font_size=50)
        self.layout.add_widget(self.lblplaces)
        self.places=Label(text=fa(staPlaces),color=setting_manager.color, font_name=setting_manager.font, font_size=45)
        self.layout.add_widget(self.places)

        self.add_widget(self.layout)

        self.back_layout = FloatLayout(size_hint=(0.2, 0.1), pos_hint={'x': 0.05, 'top': 1}) 
        self.backBtn = MDIconButton(icon="back"+setting_manager.icon+".png", icon_size="42sp")
        self.back_layout.add_widget(self.backBtn) 
        self.add_widget(self.back_layout)
        self.backBtn.bind(on_press=lambda instance,idx=self.nam: self.back_pressed(idx))
        setting_manager.bind(color=self.update_color)
        setting_manager.bind(colorhead=self.update_colorhead)
        setting_manager.bind(icon=self.update_icon)
        setting_manager.bind(font=self.update_font)
        setting_manager.bind(fonthead=self.update_fonthead)

    def update_fonthead(self, instance, value):
        self.lblatms.font_name = value
        self.lblenters.font_name=value
        self.lblplaces.font_name=value
        self.headerLabel.font_name = value

    def update_font(self, instance, value):
        self.atms.font_name = value
        self.enters.font_name=value
        self.places.font_name=value

    def update_rect(self, *args): 
        self.rect.pos = (0, self.height * 0.9) # Adjust position to be 90% down the screen 
        self.rect.size = (self.width, self.height * 0.1)

    def back_pressed(self,namd,*args):
        sm.current=self.town+"line"+str(namd)
    
    def update_color(self, instance, value):
        self.lblenters.color=value
        
        self.enters.color=value
        
        self.lblatms.color=value
       
        self.atms.color=value
        
        self.lblplaces.color=value

        self.places.color=value
        
    def update_icon(self, instance, value):
        self.backBtn.icon="back"+value+".png"
    
    def update_colorhead(self, instance, value):
        self.headerLabel.color=value

class MyApp(MDApp):
    def build(self):
        global screens
        tehranlinecolors = [(1,0,0,1),(0,0,1,1),(0,0.8,1,1),(1,0.89,0,1),(0,0.5,0,1),(1,0.45,0.85,1),(0.65,0,1,1),7]
        mashhadlinecolors= [(0,0.5,0,1),(0,0,1,1),(1,0,0,1),3]
        isfahanlinecolors=[(1,0,0,1),1]
        shirazlinecolors=[(1,0,0,1),(0,0.5,0,1),2]
        tabrizlinecolors=[(0.016, 0.686, 0.769,1),1]
        karajlinecolors=[(0.78, 0.8, 0.075,1),(0.016, 0.686, 0.769,1),2]
        towns=["tehran","mashhad","isfahan","shiraz","tabriz","karaj"]
        towncolors={
            1:tehranlinecolors,2:mashhadlinecolors,3:isfahanlinecolors,4:shirazlinecolors,5:tabrizlinecolors,6:karajlinecolors
        }
        t=0
        # Adding LineWin screens
        for j in (7,3,1,2,1,2):
            for i in (range(1, j+1)):
                screens.append(LineWin(name=towns[t]+"line" + str(i), esm=towns[t]+"\\line" + str(i) + ".txt", adad=str(i), rang=towncolors[t+1][i - 1],t=False,stations=[],town=towns[t]))
            t+=1
            
        # Adding StationWin screens
        t=0
        for k in (7,3,1,2,1,2):
            for i in range(1, k+1):
                line = open(os.path.join(script_dir, towns[t]+"\\line" + str(i) + ".txt"), "r", encoding='utf-8')
                lines = line.readlines()
                for j in range(1, len(lines) + 1):
                    screens.append(StationWin(name=str(i) + ',' + str(j)+towns[t], nam=i, adad=j, rang=towncolors[t+1][i - 1], esm=towns[t]+"\\line" + str(i) + "info.txt",town=towns[t]))
            t+=1
        # Adding other screens
        screens+=[WelcomeWindow(name="welcome"),Setting(name="setting")]
        for i in range(6):
            screens += [
                LinesPage(name=towns[i]+"line",town=towns[i]),
                Map(name=towns[i]+"map",town=towns[i]),
                APIMap(name=towns[i]+"apimap",town=towns[i]),
                Nav(name=towns[i]+"nav",town=towns[i]) 
            ]
        
        # Adding all screens to the ScreenManager
        for screen in screens:
            sm.add_widget(screen)
        
        sm.current = "welcome"
        return sm

        
        
if __name__=="__main__":
    MyApp().run()


