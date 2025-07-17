from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import os
#from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDTextButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import OneLineListItem,MDList,TwoLineListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
import sqlite3
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from random import choices
#Window.size = [360,600]

for i in range(1,8):
    Builder.load_file(f"Pages/Page{str(i)}.kv")

class Page1(MDScreen):
    pass
class Page2(MDScreen):
    pass
class Page3(MDScreen):
    pass
class Page4(MDScreen):
    pass
class Page5(MDScreen):
    pass
class Page6(MDScreen):
    pass
class Page7(MDScreen):
    pass



class PassSaver(MDApp):
    
    def build(self):
        self.cr = MDScreenManager()
        self.cr.add_widget(Page1())
        self.cr.add_widget(Page2())
        self.cr.add_widget(Page3())
        self.cr.add_widget(Page4())
        self.cr.add_widget(Page5())
        self.cr.add_widget(Page6())
        self.cr.add_widget(Page7())
        return self.cr
    
    def on_start(self):
        self.con = sqlite3.connect("base.db")
    
    def on_close(self):
        self.con.close()
    
    def Page7_(self,instance):
        self.Next(6)
        Pge = self.root.current_screen.ids.List_Page7
        Pge.clear_widgets()

        cur = self.con.cursor()
        result = cur.execute(f"select * from {self.TABLE}")
        self.dic = {}
        for elmt in result:
            self.dic[elmt[0]] = elmt[1:]
            one = TwoLineListItem(text = elmt[0],secondary_text = elmt[1],secondary_theme_text_color = "Custom",secondary_text_color = [1,0,0,1],on_release = self.Voire)
            Pge.add_widget(one)
    
    def Voire(self,instance):
        self.Next()
        self.root.current_screen.ids.Top_Page8.title = instance.text
        self.root.current_screen.ids.ident.text = self.dic[instance.text][0]
        self.root.current_screen.ids.pass_Page8.text = self.dic[instance.text][1]

    def Save(self,instance):
        Motif = self.root.current_screen.ids.Motif.text
        Ident = self.root.current_screen.ids.Ident.text
        Pass  = self.root.current_screen.ids.Pass.text
        cur = self.con.cursor()
        result = cur.execute(f"select * from {self.TABLE}")
        if "" in [Motif,Ident,Pass]:
            toast("Tout champs Obligatoire !")
        
        try: 
            self.add_in_table(Motif,Ident,Pass)
            self.Question_1 = self.show_question(Quest="Ajoute effectué\nAjouter encore ?",foncts=[self.Yes,self.No])
        except:
            toast("Quelque chose s'est mal passé")

    def Yes(self,instance):
        self.Question_1.dismiss()
    
    def No(self,instance):
        self.Question_1.dismiss()
        self.back(4)
        
    def add_in_table(self,Motif,Iden,Pass):
        cur = self.con.cursor()
        cur.execute(f"Insert into {self.TABLE} (Motif,Ident,Pass) values (?,?,?)",(Motif,Iden,Pass))
        self.con.commit()

    def Genere_code(self,instance):
        Char = "azertyuiopqsdfghjklmwxcvbn%123456789*0@"
        self.root.current_screen.ids.Genere.text = "".join(choices(Char,k=12))
    
    def Copy(self,instance):
        Clipboard.copy(self.root.current_screen.ids.Genere.text)
        self.root.current_screen.ids.Genere.icon_right = "check"
        Clock.schedule_once(lambda dt: self.do_it(),1)
    
    def Copy_8(self,instance):
        Clipboard.copy(self.root.current_screen.ids.pass_Page8.text)
        self.root.current_screen.ids.pass_Page8.icon_right = "check"
        Clock.schedule_once(lambda dt: self.do_it_8(),1)
    
    def Copy_8_1(self,instance):
        Clipboard.copy(self.root.current_screen.ids.ident.text)
        self.root.current_screen.ids.ident.icon_right = "check"
        Clock.schedule_once(lambda dt: self.do_it_8_1(),1)
    
    def do_it_8(self):
        self.root.current_screen.ids.pass_Page8.icon_right = "eye"
    
    def do_it_8_1(self):
        self.root.current_screen.ids.ident.icon_right = "eye"

    def do_it(self):
        self.root.current_screen.ids.Genere.icon_right = "eye"

    def Show_choice(self,title="Choix de l'option",List=["Generer",'Voire',"Ajouter"]):
        Item = []
        self.dic = []
        Lis = MDList()
        for elmt in List:
            One = OneLineListItem(text = elmt)
            chek = MDCheckbox(
                size_hint=(None, None),
                size=("48dp", "48dp"),
                pos_hint={'center_y': 0.5},
                active=False,  # État initial
                on_release = lambda x : self.Chois(x)
            )
            self.dic.append(chek)
            One.add_widget(chek)
            Lis.add_widget(One)
            Item.append(One)
        
        Cont = MDBoxLayout(orientation =  'vertical')
        Scol = ScrollView()
        Scol.add_widget(Lis)
        Cont.add_widget(Scol)
        But = MDFlatButton(
                    text = "[b]VALIDER[/b]",
                    on_release = self.Ok2
                )
        Cont.add_widget(But)
        self.Quest = Popup(
            title = title,
            content = Cont,
        )
        self.Quest.open()
    
    def Chois(self,instance):
        for elmt in self.dic:
            if elmt != instance:
                elmt.active = False
        instance.active = not instance.active
    
    def Ok2(self):
        self.Quest.dismiss()

    def Next(self,val = None):
        #Pge = self.root.current_screen.ids.cr.current
        Pge = self.cr.current
        self.cr.current = f"Page{str(int(Pge[-1])+1) if not val else val}"
    
    def Next_Button(self,instance,val = None):
        self.Next(val)

    def back(self,val = None):
        Pge = self.cr.current
        self.cr.current = f"Page{str(int(Pge[-1])-1) if not val else val}"
    
    def back_Button(self,instance,val = None):
        self.back(val)

    def return_liste_table(self):
        cur = self.con.cursor()
        listes = cur.execute("SELECT name FROM sqlite_master  WHERE type = 'table'")
        return [liste[0] for liste in listes]

    def existes(self,ident,passs):
        if f"{ident}_{passs}" in self.return_liste_table():
            return True
        return False
    
    def verifi_Pass(self,pass1,pass2):
        return pass1 == pass2 and len(pass1)>=8
    
    def Connecter(self,instance):
        ident = self.root.current_screen.ids.Ident2.text
        paas1 = self.root.current_screen.ids.Pass1.text
        paas2 = self.root.current_screen.ids.Pass2.text

        self.connection(ident,paas1,paas2)

    def connection(self,ident,pass1 ,pass2 = None):
        if ident and self.verifi_Pass(pass1,pass2):
            if self.existes(ident,pass1):
                toast("Echec de creation ...")
            else:
                try:
                    cur = self.con.cursor()
                    Name = f"{ident}_{pass1}"
                    cur.execute(f"CREATE Table {Name} (Motif TEXT , Ident TEXT,Pass TEXT)")
                    self.con.commit()
                    toast("Success")
                    self.back()
                except:
                    toast("Error")
        else:
            toast("Verification invalid !")
    
    def Go(self,instance):
        Ident ,passe = self.root.current_screen.ids.Ident.text,self.root.current_screen.ids.Pass.text
        if self.existes(Ident,passe):
            self.TABLE = f"{Ident}_{passe}"
            self.show_info(title = "Bienvenue",text = f"Bienvenue dans PassSaver M/Mme {Ident}",fonct = lambda:self.Next(3))#fonct=self.Show_choice)
        else:
            toast("Compte introuvable !")
    
    def show_question(self,Quest,foncts,Rep = ["Oui","Non"]):
        List_but = []
        for elmt,fonct in zip(Rep,foncts):
            But = MDFlatButton(
                text = f"[b]{elmt}[/b]",
                on_release = fonct
            )
            List_but.append(But)

        self.MD2 = MDDialog(
        title = "Question",
        text = Quest,
        buttons = List_but,)
        self.MD2.open()

        return self.MD2
    
    def show_info(self,title,text,rep="Ok",fonct = None):
        self.Md1 = MDDialog(
            title = title,
            text = text,
            buttons = [
                MDFlatButton(
                    text = f"[b]{rep}[/b]",
                    on_release = lambda x :self.Ok(x,fonct)
                )
            ]
        )
        
        self.Md1.open()
    
    def Ok(self,instance,fonct):
        self.Md1.dismiss()
        if fonct:
            fonct()

class Show(MDDialog):
    def __init__(self, title="", text="",buttons=None, **kwargs):
        super().__init__(**kwargs)   
        self.title = title
        self.text = text
        self.buttons = buttons or []

    def info(self, text):
        self.title = "Information"
        self.text = text
        self.buttons = [
            MDFlatButton(
                text="Ok",
                on_release=self.ok
            )
        ]
        self.open()
    
    def Question(self,Quest,foncts,Rep = ["Oui","Non"]):
        self.title = "Question"
        self.text = Quest
        List_but = []
        for elmt,fonct in zip(Rep,foncts):
            But = MDFlatButton(
                text = elmt,
                on_release = fonct
            )
            List_but.append(But)
        self.buttons = List_but

        self.open()

        return self
    
    def ok(self, *args):
        self.dismiss()

def toast(text):
    Show().info(text)

PassSaver().run()
