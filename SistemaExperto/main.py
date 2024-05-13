from ctypes import sizeof
from lib2to3.pgen2.token import LEFTSHIFT
from logging import RootLogger
from operator import length_hint
from select import select
from tkinter import *
from tkinter import filedialog as fd
import shutil
import copy
import os
import tkinter
from turtle import width  
from PIL import ImageTk,Image
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import threading
import os
import random
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Frame utilizado para mostrar los graficos
class graph_frame(Frame):
    def __init__(self):
        Frame.__init__(self,root)
       
    
    def add_graph(self,fig):
        self.mpl_canvas=FigureCanvasTkAgg(fig,self)
        
        self.mpl_canvas.get_tk_widget().pack(fill=BOTH,expand=True)
        self.mpl_canvas._tkcanvas.pack( fill=BOTH, expand=True)
    def remove_graph(self):
        self.mpl_canvas.get_tk_widget().pack_forget()
        self.mpl_canvas._tkcanvas.pack_forget()
        del self.mpl_canvas

class bird:
    def __init__(self)->None:
        self.name=""
        self.size=""
        self.description=""
        self.habitat=""
        self.comments=""
        self.other_names=""
        self.distribution=""
        self.jalisco_distribution=""
        self.image="sources/default.jpeg"

        #Caracteristics
        self.caracteristics={}

#******************************
class conejo:
    def __init__(self2)->None:
        self2.name=""
        self2.size=""
        self2.description=""
        self2.habitat=""
        self2.comments=""
        self2.other_names=""
        self2.distribution=""
        self2.jalisco_distribution=""
        self2.image="sources/default.jpeg"

        #Caracteristics
        self2.caracteristics={}
#******************************        

class visualizer:
    def __init__(self,menu,frame1,bird,rules,clasifier)->None:
        self.frame1=frame1
        self.clasifier=clasifier
        self.name=Label(self.frame1,text="AVE",background='#353437')
        self.name.configure(font=("Arial",50))
        
        openImage=Image.open(bird.image)
        img=openImage.resize((200,300))
        self.photo=ImageTk.PhotoImage(img)
        self.image=Label(self.frame1,image=self.photo)

        self.size=Label(self.frame1,text="AVE",background='#353437')
        self.size.configure(font=("Arial",40))
        self.description=Label(self.frame1,text="AVE",background='#353437')
        self.description.configure(font=("Arial",40))
        self.habitat=Label(self.frame1,text="AVE",background='#353437')
        self.habitat.configure(font=("Arial",40))
        self.comments=Label(self.frame1,text="AVE",background='#353437')
        self.comments.configure(font=("Arial",40))
        self.explanation=Label(self.frame1,text="AVE",background='#353437')
        self.explanation.configure(font=("Arial",40))
        self.menu_window=menu
        self.bird=bird
        self.rules=rules
        self.addButton=Button(self.frame1,text="Agregar Ave",command=self.add_bird,bg="#7a7b7c", fg="white")
        self.addButton.config(height=2,width=15)
        self.menuButton=Button(self.frame1,text="Menu Principal",command=self.main_window,bg="#7a7b7c", fg="white")
        self.menuButton.config(height=2,width=15)
        self.showBird()

#***********************************************

def __init__(self2,menu,frame1,conejo,rules,clasifier)->None:
        self2.frame1=frame1
        self2.clasifier=clasifier
        self2.name=Label(self2.frame1,text="onejo",background='#353437')
        self2.name.configure(font=("Arial",50))
        
        openImage=Image.open(conejo.image)
        img=openImage.resize((200,300))
        self2.photo=ImageTk.PhotoImage(img)
        self2.image=Label(self2.frame1,image=self2.photo)

        self2.size=Label(self2.frame1,text="Conejo",background='#353437')
        self2.size.configure(font=("Arial",40))
        self2.description=Label(self2.frame1,text="Conejo",background='#353437')
        self2.description.configure(font=("Arial",40))
        self2.habitat=Label(self2.frame1,text="Conejo",background='#353437')
        self2.habitat.configure(font=("Arial",40))
        self2.comments=Label(self2.frame1,text="Conejo",background='#353437')
        self2.comments.configure(font=("Arial",40))
        self2.explanation=Label(self2.frame1,text="Conejo",background='#353437')
        self2.explanation.configure(font=("Arial",40))
        self2.menu_window=menu
        self2.conejo=conejo
        self2.rules=rules
        self2.addButton=Button(self2.frame1,text="Agregar Conejo",command=self2.add_bird,bg="#7a7b7c", fg="white")
        self2.addButton.config(height=2,width=15)
        self2.menuButton=Button(self2.frame1,text="Menu Principal",command=self2.main_window,bg="#7a7b7c", fg="white")
        self2.menuButton.config(height=2,width=15)
        self2.showBird()

#***********************************************

def add_conejo(self2):
        self2.addfunction=addconejo(self2.menu_window,self2.frame1,self2.clasifier)
        self2.hide()
        self2.addfunction.show()

#***********************************************
def add_bird(self):
        self.addfunction=addBird(self.menu_window,self.frame1,self.clasifier)
        self.hide()
        self.addfunction.show()

def show(self):
        self.name.pack()
        self.image.pack()
        self.size.pack()
        self.description.pack()
        self.habitat.pack()
        self.comments.pack()
        self.explanation.pack()

        if(self.bird.name=="Desconocida"):
            self.addButton.pack(side=TOP)
        self.menuButton.pack(side=TOP)
#***********************************************
def show(self2):
        self2.name.pack()
        self2.image.pack()
        self2.size.pack()
        self2.description.pack()
        self2.habitat.pack()
        self2.comments.pack()
        self2.explanation.pack()

        if(self2.conejo.name=="Desconocida"):
            self2.addButton.pack(side=TOP)
        self2.menuButton.pack(side=TOP)
#***********************************************
    #Oculta la vista de la descripciÃ³n del ave
def hide(self):
        self.name.pack_forget()
        self.image.pack_forget()
        self.size.pack_forget()
        self.description.pack_forget()
        self.habitat.pack_forget()
        self.comments.pack_forget()
        self.explanation.pack_forget()
        if(self.bird.name=="Desconocida"):
            self.addButton.pack_forget()
        self.menuButton.pack_forget()

#************************************************
def hide(self2):
        self2.name.pack_forget()
        self2.image.pack_forget()
        self2.size.pack_forget()
        self2.description.pack_forget()
        self2.habitat.pack_forget()
        self2.comments.pack_forget()
        self2.explanation.pack_forget()
        if(self2.conejo.name=="Desconocida"):
            self2.addButton.pack_forget()
        self2.menuButton.pack_forget()
#************************************************



def showBird(self):
        self.name=Label(self.frame1,text=self.bird.name,background='#353437',fg="white")
        self.name.configure(font=("Arial",35))

        openImage=Image.open(self.bird.image)
        img=openImage.resize((200,200))
        self.photo=ImageTk.PhotoImage(img)       
        self.image=Label(self.frame1,image=self.photo)

        self.size=Label(self.frame1,text=self.bird.size,wraplength=1200,background='#353437',fg="white")
        self.size.configure(font=("Arial",14))
        self.description=Label(self.frame1,text=self.bird.description,wraplength=1200,background='#353437',fg="white")
        self.description.configure(font=("Arial",14))
        self.habitat=Label(self.frame1,text=self.bird.habitat,wraplength=1200,background='#353437',fg="white")
        self.habitat.configure(font=("Arial",14))
        self.comments=Label(self.frame1,text=self.bird.comments,wraplength=1200,background='#353437',fg="white")
        self.comments.configure(font=("Arial",14))
        exp="\n\n\nEl ave fue encontrada en base a las siguientes caracterÃ­sticas:\n"
        for key in self.rules.keys():
            exp+=key+":"+self.rules[key]+"\n"

        self.explanation=Label(self.frame1,text=exp,wraplength=1200,background='#353437',fg="white")
        self.explanation.configure(font=("Arial",14))

    #******************************
def showConejo(self2):
        self2.name=Label(self2.frame1,text=self2.conejo.name,background='#353437',fg="white")
        self2.name.configure(font=("Arial",35))

        openImage=Image.open(self2.bird.image)
        img=openImage.resize((200,200))
        self2.photo=ImageTk.PhotoImage(img)       
        self2.image=Label(self2.frame1,image=self2.photo)

        self2.size=Label(self2.frame1,text=self2.conejo.size,wraplength=1200,background='#353437',fg="white")
        self2.size.configure(font=("Arial",14))
        self2.description=Label(self2.frame1,text=self2.conejo.description,wraplength=1200,background='#353437',fg="white")
        self2.description.configure(font=("Arial",14))
        self2.habitat=Label(self2.frame1,text=self2.conejo.habitat,wraplength=1200,background='#353437',fg="white")
        self2.habitat.configure(font=("Arial",14))
        self2.comments=Label(self2.frame1,text=self2.conejo.comments,wraplength=1200,background='#353437',fg="white")
        self2.comments.configure(font=("Arial",14))
        exp="\n\n\nEl ave fue encontrada en base a las siguientes caracterÃ­sticas:\n"
        for key in self2.rules.keys():
            exp+=key+":"+self2.rules[key]+"\n"

        self2.explanation=Label(self2.frame1,text=exp,wraplength=1200,background='#353437',fg="white")
        self2.explanation.configure(font=("Arial",14))
    #******************************




    #Muestra la vista principal
def main_window(self):
        self.hide()
        self.menu_window.show()

def main_window(self2):
        self2.hide()
        self2.menu_window.show()    
    
def closing(self):
        del self

def closing(self2):
        del self2

class addBird:
    def __init__(self,menu,frame1,clasifier)->None:
        self.frame1=frame1
        self.main_menu=menu
        self.clasifier=clasifier
        self.load_caracteristics()
        # self.name=Label(self.frame1,text="AVE",background='#353437')
        # self.name.configure(font=("Arial",50))

        # openImage=Image.open(bird.image)
        # img=openImage.resize((200,300))
        # self.photo=ImageTk.PhotoImage(img)
        # self.image=Label(self.frame1,image=self.photo)
        self.labels = []
        self.entries = []

        for caracteristic in self.caracteristics:
            self.labels.append(Label(self.frame1,text=caracteristic.capitalize(),background='#353437',fg="white"))
            if(caracteristic=="descripcion" or caracteristic=="habitat" or caracteristic=="comentarios"):
                self.entries.append(Text(self.frame1, height=2, width=45))
            else:
                self.entries.append(Entry(self.frame1,width=60))

        
#*************************************************************************
class addConejo:
    def __init__(self2,menu,frame1,clasifier)->None:
        self2.frame1=frame1
        self2.main_menu=menu
        self2.clasifier=clasifier
        self2.load_caracteristics()
        # self.name=Label(self.frame1,text="AVE",background='#353437')
        # self.name.configure(font=("Arial",50))

        # openImage=Image.open(bird.image)
        # img=openImage.resize((200,300))
        # self.photo=ImageTk.PhotoImage(img)
        # self.image=Label(self.frame1,image=self.photo)
        self2.labels = []
        self2.entries = []

        for caracteristic in self2.caracteristics:
            self2.labels.append(Label(self2.frame1,text=caracteristic.capitalize(),background='#353437',fg="white"))
            if(caracteristic=="descripcion" or caracteristic=="habitat" or caracteristic=="comentarios"):
                self2.entries.append(Text(self2.frame1, height=2, width=45))
            else:
                self2.entries.append(Entry(self2.frame1,width=60))
#*************************************************************************



        # self.descrip°Õm¼8ˆ|#%%Þ kÍÂÔ‹R»È„J\äNW>BF‚y‚K&L­5€iŒ¡‘R„½8rR;©ãb[7‡Ùè—'ô\–ØwY6(Æ±ç0Ç	*->!d±D)*B«Ka˜ùÐE„Èñˆ
T_ ÑGŽo	3hý¼Ü/\D”Bì²@?ÄíF¤¿71xº»VÒgÙö¢Öm¾)í˜«¿Ó^IÂÒª5‘Gã–û¹—¹ý¢R±ÑGâ@{mIõz©óY¨¿±çemixa+ò`3mUdËiRUTØ¨ó¼òÆš¾YèŒ•–Ü´ “[îé›6½÷Tr&^ÁÖ1Eëû¹ñ¢è›Ê8é:ªWñ*ÂyÛ+#îZ¡JR™ÍM$Óà5³²³:ž)N×»¿PR"ký9ÙR¾Ö}°\{=guäŽÏ×ó¿ùüOSð	t-gµ¥>¥g;ÃÓ”ð~„ýxZìÚGÑ30ÛVŽd¯YnÖ_ñèát{Ý‡DP‹ç­ 4ßö+þ3zo…®(©¨ôAxVJötúu%Õx@ýŽq½Ç‘n_Œ/Hö{Îh>¨õY°«š1^ ñgbß«´}[ç½žë²KÃí™ê0nîþ¿‘M~ÙùVþ+Ù'£é8«ÜêÛãÓïOÓ½[×Ë.ú†JV=àö¦?›Â@y¥Ç\²•Ýo{ËgPÚð v¼×˜ÍÛ@Ät×Úä^ø©Âž<ÓsÖé@?õÊ¼{œÞ­†©2 PK     šXèœ~ÉL  SO  K  Report/StaticResources/RegisteredResources/team_spirit20861140841048598.png ¢ (                      „¹wXÓKð/œ„ „N½Cè¤( H½#UEé$8@Ñ€´ ‡^QiJï$h€ 
ŠtP8JW)
êýêïÞç¾ÿÜçÍ7»3Ÿ™E‚+“ bE™;€@Ð2ÇHPN­™•“	Ç3ˆžÊee¦ca?ÃÁÇ,ÀbC0òÀ¹øY ÌL F@Ú?Vf+?« ðð3~6A^~!VQÄ~AÎ3pnfV.>7#œ™‹_ˆC„NÏ)Â´`ÁÈÀuF€UPh`¾<|ì N!Nfn3Äâã’‘•áçædãCòðH x‘Ü¼RÜüR¼¼2ÜHu	¤‚ª´š”„œŠ”†¤´&RJQME[ßÁÍÛ? ( žšŸœ—ûoÒÂâ’'O7v<íëxÖþ´mÿèäÛßÀççÑ×ÓÝ_À÷÷áïß_ÿPN¾lîííí~úøßêFë}þnnñÍ›7”Ñ7]½½¤.2™Lìêìéê}ÚÞÔÒÒRQZøðáÃŒ$|I^fA~AZRZvvvJ\*Çb±W¯^µ···3»dggg`` *¥®,©ª©©©¦¦¦ªª*— œxŸIðTšO–Kœ“C„X2Àâaädæc€˜9™ ô 7Œ—ž"È*ÌËJÏÃef¡ç¤ã…ñnF^6!@JˆM„›…^TT|Îð0s3q2Ñ³‚ØØxYì‚¬ ØUÀ^œa§6”ë7”Ž™sö"ø±ûÇÁÆñøøûñññÁ·ƒ£ƒ£oß¾£ÃÃ¯@0€@8<~¾Ÿ¯_Ì/`ŒÀøúõèèèç÷ãï‡?Éƒ´A «2”ñ%'>þ­~Ë¦z÷Ž¦yû:çä¼§ßíxáLp¤b•Ïl`hÚÀ“þßÓªë7'>ÉÌñ!y°ãÝDŽÿÛÌ7ÊsÉRiö:ÔB¨²}|üQ<ÞQ	 ”`žHØ >b¼/éoCö€wGsá,Îa »(e+ò¹eÃÿOÓÇ°B-e&Å(ÝÖL:GI‰‚ìólÙâC2Jç(‹)…ˆ&’lI¯¹º;áÚôÉ“Ô(¢Ð?“‡]”)[|ò¿ç•IŒð ÄÿjIÏÆŽ¿–§>Ü~ei…b€Ò&’‰ùÀ9íÇÿ×ÒÿG£dÿ
kè£²Î¬1IV½ò/Ï`!1bÜZ"û,°&*È5~N›`P‡,‹Àœw’cÚ(+µsÜ£}ÿÿw’ÿW“•knäL£z7D¤Èbá°ò¿Ä»ó";0âM¿sãK\XÌÁXÃ`·.d¼Ñ+Ø¡¬G’F]èôsY¥
ƒ7fš:Ù970Ì:Ä¨Æ¸ ìN>"xv.…‰Ÿ 4DuÆ½Ä.ÖxëÉ 2Ó‡^)‹gMöË ŒëbtlYÜÿPã#´é©=¹s©÷¾Y£*n#à‚öì¬ãKpl¨ÙgzÆVÖêŸ-×KKMÉ}Âè‰ÂüC.*ÙiNì®éçÅr%¹­Ç’‚Uì$”zBˆ»a¹UÄ´a¤V§.ò B?s×¨¬ñ±SGÝ‰ó¡Âã^¼$ËîüùP`9Ê´å‚¹ÔñÛ
Ø§øXÇÏ±­°ÆŸœa;u]:/
”õÈ ŠVÇ¡Ùÿ@·-dü~öå‚ÊŸ9û%Ø<|Ä9S—ê®çîe=Ò4*Œà\»Ý¬?îxîcÐ‰Âpw0à:Oôƒo:Ñ&äî‚ú­<ºq/N,,/±çq‡mÔjµ©ÇâDq•ê.R_Ù‘ßn¿ƒÝiÃG(¸.øs{ñ š¶Ò…6”?‡NßÑ‰¶µ7•õÈÒ\I£[õe&R$ÇNÛ²Í7±•å<’2ú´3ªâRÚ@_5ß&°U\ºÈ!Yª`.Iþ/S‚nê×x'ö:¬(wÆæ'Eö™]éˆ+‰"åmM•G¤½¿¹²ìNîŽ¬ßv?7ú>16øª.}Äóƒ¾N|Ä¦Ëb	_Ø® v{ÛêÕ9Ô%˜%]ÞnƒÿÓ¦tküíˆà¿Ä¦úþ(vIH¡/ó Ž)ÿ‡-­â‹¹LÕnyHBçâþ§ËT¦ËˆoUˆlØ@Ë<:x5u¢%hÔºÎ¨·lÿCšQ¾Þð,$¬˜fÚ½gë¥N:e±ƒ¬Åm¸ªÔ5_nïÓð[Ê3]±A­
Ÿr—UûuÇï7­K‘ÖeÑ›´ÐôŸ‘ükyj!`JçB“ŽªM`áÀ¤ö"Õ-4Éò=Vmÿ&ðÎ-¶CÏ›¶²kÂr±yŒ:Ú*âÒNš¬•s)	ßdMaÚñäSDR—Üö½4û­ó›>Öbª‡RÿÒ2ÔÜOšÄõÓìI0(Ø
ÕØ¢§Î7qæÙbŽL8’õ…‹Î±¦Û=,D¯ø!ÆrÿYîl‹h&é5“ŽvªyÞÒOôÅ­°RÀ+Œqb&Qƒñ+A'âÃhr·82Ùsm«{R{ý~bpæ8à¨Ï[<É
Ûéê‘+À™T8…ø:X¸ H=@dºX
UrœáÎðÌ‚Ò¹»ó¡¬˜8
Ø¯­ íHßçÎ$nøàžöL¿ìB(ÿÿ°1Ùæhmn–©Q% …Ž/qTš»£‰&ÉÛYú	b9]˜`¾õ€;¤Ñ€5`Ô½í­.áÁ©CW[	äJpJ^[ô(]/^øu>›iEñw\é›½ðkaEÈ÷
¢†Ë/Yœ W»dw”Ù¸Xu\8œÍöž›É²ÛyLD“øæD,F«‰ÎèÆ!*9V©5‘Ìë€oLYrVOŒ{»âm¡(¾grzØÈ;Þ˜¼ÄËO~ö$LEªãX"jI{…êþ-ê}ÎÉù“
2ÚŽÜ ¥#êÊP\cÜôZ—Ì^AbÄæÛ…8þ£ÎCç»‹€›f@ÂÑš‡ÓlD}ð†KC'8h§nŠ‰<zM‡ :/$1GFß¨Žóý?£%±I—EÖ£ü(‰a´¹»þ[|Õ´%3ÖBwzÅ¹ß‚pýDw'õÛ:5#–I7’\mÏbÒ‰¾O…’CgKFÏ•@Š$þœš›ÓG|&á‚7&„£”Wá¥ïÊšæ”MžyÕ=8®Iú¦m†x(›S>™ü‰TÛ¡K}-ë±VKðAÀFBŠé´;£”ÑVän]¤Ýoë²TôâTäwG?¿˜ïF?¡K’XÂƒy;¬,àûx¤9éÌî(ô±«6ºzÉ9ßy©#Çµí‘q*ª¿…P’ÏN8VZÍ­9ä‹?lQÑ”y?=\ÎÛúH S»Pˆ"™Ð;<¼  B_ÿÞbŽ½ì23\þÊD°nµpAùSX)Ü<+wÒ¬¬ëí-,™„~’áõ
L”-Íº`þŸ´§×Ï7²Î„å“¬Õy¹òju‡Ì~Ë-6¾»Ýý¨#]c	÷šÑîó®à
@·$†÷ü—
”–w-|Ò·3õ¶¯xú9“”`$¤¹=ríò¼P[ÜpDà92Ê-ù:	»Qj}û¿Côà6©Ž¨pžšõ”0fZ}ÔR²}ïee`|½{OÖb6>âÎY]C3ÇEF³¦Àí4Q¼q;Ícùª®Ü,_ËpHÓ¬§fmFîÞýq¾ÝÄY­@Ëp\³Ó+‚Ïý§àá=­îxýOûEM]j´,ØÒÒh^Ý&ðº©¢«þraEb©9¹¯§¦åŸ|¥ë´Lû¹«½"oØ§Áëá’¯˜HG3
{}ueÂÝ]-ÒŸÚTW—[žÇÍ(}£yÖ¢‚(çLA£ŸÚ9ÀõvˆùüRUk<st+™M;ÍÜ…ÜWßÔqã£Ù™Ö0uåvÁ ª”ûYÁÒ}>âJ°d§çm©‘‘8*ì=n,¹Ý]Õî!‘„ìü¤œoç~)°€®*³tï©îG“ûîK·Èêb‚ÐåÌî=¾)‹©äRøn
Ú$sná2ƒrÀV!‘3þI8rZ|š¯?;­5“ÉÔó)u1™›‹³Dc‚ó„»ëºÞJlõf-&ãcE[Û4ë$\§´r"
–ò×ºÄiË¦yóç?
Mk¹uOb6±¥ØÐ
t_òÂ|À¹‹žmrpEì>êrVˆU–E÷fj$-¹|‘FÒSuÿcòèÞzÙ=ù¢þÜõ#ãå»7[}ÁGgØºÀÎœ×¸ËZcþãµ¥	ÑoŠº`&Ã„‘7#;µ8ö4ŸQÈ®ekVoüu?ÁœÎ[¾Y:oôù1Ì 9Íç«¯`89–’ÉÕ¸4½ª%FÓjE;Ö½”9LÍ HÃh2Úíáhü«-Eè{]Wõ”uP¶Ù÷eŸÿêŒ>:@ÚüG·Sˆ_lnWq¿¸-~îÊtÔûø”Úa¨”<œç]4O§®ß|67§;YóëyZmqÊƒ]D0/6Ýu‹W±Ë=ûsñôýÓ_ywœÏ¡TéÎ´ÛPt£~Í‡ôÉ3:¹¸†ßGw6ï<¤W‹ð‹wÑžC)"ˆïŠD°¼)<"í÷ÖÑoÑ“T ~ê’qéŠá¶[¼+p¡]\ÝîsáÇÆß¿î,ÈR#ÁÄsq×B&,ˆ8í—°Nª¥eg-üîi.e‹¶$£­Kç=ž<Ù¾Äÿà›–ùksÓÏ=]?yÂˆPê¡-/§ýºµæ™3ræ¥h&’5¡ ûäðtzAUó‚±ü1@ÑßFŸ!†ƒ‰â^~˜ìò‹A‚~)ÝxÂb›¼Áš•¬…3}å¸Gx|dÍd±`Ð°h'ë?”¾{fzjÅI>bpß,Î™TÄ¥‚À
Ú—®¼­fÍ_›Q¢i‰ó¬¿˜ûêhIrf&)ýÇQùáÔï®0¶ž+øÆ÷ÐÄ{gswa—íà™¢FÄ•ÈSŸ»Ü€º~‡ÝÍ‹™–>‹"ŸÕ5ŽÞÅ_	!¥z´ã=ú^Ü–ß,ìyêw¥XCá¸¶}E€zþO,^ŸÉ2+ÕÝ×ó’½‘•xx¢@siRk÷ââ¯×EÎÜ@“2¦9w²ðÝ·£ÿ‹±º#»ç|úfŽQIA’z|4óÃèZ¨üZÊ‚éÜš‹"mÙ (uÞr]d<‡‚Œ¿u-é{ ÿÞYË4Ë£!ês±Gî¸©CtÀ”!#^²­Ù0
¼žÿ‡À#šxaB?’SL	ŠVú²ª÷Ôõo¯Ÿuh·¯Ýý÷ÝCYª<½)ÆÃÇcW=ÖŒ³%L~Ê Q=6Ùœ¯…n2Îéð§qj³äè©‹A›“Ëôÿ~…cxàyL½‰ØÀÍR/¿P•”Ó…µù=È¼¥«+ïú³M ‡@ˆ.ñ¼©jiœ‰—pF­µêÏ§¦´\²<jÉÌæ>²TÅ§F×vò^œ§¹È·è¥ÆvãÂ#d|Ð×·±
ÜæøÄØÖë¾;	~þ•+.ò´®æ÷ëÊZœD01¬UnÌ+¯@Ë=)–sßL¡RÂ©é©EL·Ä©Éß"1˜›Â;RÈ}‹ø‰DìW¸
¼t’j9EšåPá>6„rîšÁ›ß¸”tóÊaëÇŠf½â(«f¥×}vY•@ôqp[D¨LÓfdiZ5¯^÷Íe^IôÈÁ/æKk…ó_D4ši¿A#"âØ¾S@ùÁ(øÜ/)Q‡ýþˆóÃ(Ÿst“ù3f^]¦–ýºn˜‹ý;¤c+évÆnraëgyÖý\Zà?9±
¼
_ÓIÓ0R¤îuž74iIŠózJ•§þCQ„¼ãÄxÿ§ªS?C©AÓ%ÝC${Ê*S`IjÈÖ¼G5IƒøDH;í²'¹Ñ¾¨Ôãr–G	ÞãÑÝî!a¬—y1¶ˆ2IýE*€U)X"Ð~ÊôœDåøP¤ˆÎî³Ba›plý$ï:Ü~eFŠ6ó¡¸ÄÒ$Ù£ï‘EÒ.Êf#Êƒ‰^×”¥b©uPª»F
ð#«ð¶ØÒ:Ë#ï‘òÂ38Pª¼Óúdû ¾Ù*Z-Þãîˆgv‚“hîc.zvùžå$çÑy•öUzR÷Ygo.%¢wMÙþÆ¢æå§ì&ŒÑ‡(£žõ&ÔsòÞ˜ç U>•\ÔöÂsA#‡P‘€B=žŽy.P‘ˆçÂ¿ÿ]•úf$ýYÒMÙÆ:ÚÝ9}0ØÊ«"qêÙæã§ÉaúáòûÁoô3o9š7sÄ'Ý/ø®t×ðÚû^ru*ëm 5ý|ò2˜Þ³B>"8{Mú{¯¹ºVÈ¦ÿå)±’Ë‰E5Râw}T”Sû°µŒ$„æúLÅ]“°øŠ?ChäúŒäêŒ8mòïúLe£YJÆoÝ¥jàOÏßc­N=õb[Ÿ©l4$KÕhÕcá2ÔhpQáåb’
ìÈ‹\]­N<¯˜‡…(Ë™ElFˆ¡âx±rŸ4"6Û/‘««T‰¦9(¯=â
½§aPDý?.åbUÄMöÉÕ•šDî¬‰MDå±<-—3"b3ÿ+_¹/ñÂž3Yêz(¦ñ¼g8…€·4ñÇtyþ€(sWwOËc?1“ŒÏ®»4K©Ð&9"€ú™–Ë‹|òºqž­¨oiŠYÂú»C”aÕÝ‘º«6Œ9ùxËþ·Ô‘í°ÇÈôÝÝ£aµÌ$èÔºKó ”2­pÖÝeoéIVjV'Þ¦WIÅ%‹øTK²R“‘žU&v ¤¦¢.¼‡;Ã¥î¹ Ávw£ÂPÌ¤$Íu-Ÿ,Kw²’¢6‘óœr ˜Øð‚ê÷”\á¥aäjEÏô½ÅLxQÞÃ)c$¡|L¬_û}½4Š"¥H+tš¯)¸8éUpñFW÷_öXWíÜ4z‚>.¶aS½ýß,Œ™D¯Ù¥ÿñ×›pÛ÷3=T­'ƒÕ
4žŽvëWGÃå¥?º7ã¾‹·[/¬MrcG	]ÂóMŸº•»"ç¹IÿÐSÃÙº8‡ž}¬››òõÛ­–R :Î¹áüîk:òÙg¶¤¾‚3Ex«ÐMW­[Þ·ÂÂcµu=Û µXî[ï¿&U+Ít÷Iþ%u7.ì¼ŒDû†~Nµt&+}P(½ÙlÙ£¢RÿÃèÝ/»ÙƒeÇ¹òžuŒ\A£Ë|¸Ñ•ôÇg’!j‘¥óÆá.Ö!—ÉJH¿.ßQÖ8_mÀ”0“ÐôÚOê¥/ï4\ÞŠ¢§fvÙ˜Œ*Eú¹rŸd
yX±š•š¿Nòq%+ÝÎ×¦NrGY‡ý×-ç×UL÷fî,ÓŒÕ_µÄƒW‚˜ºí´†Ï¤Ç];nÍÍŸ•P¶3–]dBIµ*[m½*·†‡ÍhJñ<RÀó¤T&wjnaKR»³Ä+_›Å~!ÁýY=®û—•Sq¿Ñr9|±_yDðÌüb®ûí—h&~eëø×yæö~õmYT„B2”¯¦Õ¤óÛ:½ké@Vªh×|åIOòr0KÔð@<ÿ •¤¯Œº4 ô°‹{Þ³ÉÜóp‹ÿ¿«ÌkEw­Å‡¥äÌ^7wL¿ôØùO]·H˜_Ö¥«%÷J…uÅpµ,ÀR^rÊÑ}:6^ O74Pè²ïáë¨£Ê	¼x90·Í<ÒïÅ¼i–iß.Ò½÷î¥†K{²ÒµP…·XÛ¢ù’^ß‡ÏÚ Bß%‰rÆž	¬»Ñp&ÌVqËŠŸ¿¦Y&|gÍÄª|	LÄÔÛ}£r1ë:ªY]qÿu~!ÿGÜØØ¯>;>.ÄW¡›_˜¦ÿ`¡þ—ÑÙh0Wp$“:-U"õá¥Œn©aº¥-Yéªÿ§`ÒîÕÇm™õO»ôg"ûF•ø‡0ÅzÞ“¤šWžÛø
óF–T×¯¶×ØÑ&¹°Ì-4©¼º9‘ž.îÏZPßH ÔSwK¯AîrXË?·œlél…¤{`¶(‰MRMç?š·œQé‡…]iàóðÓîmá6Z„TKkòkÓS÷IùdÙ-ãQÖ’êºã”PX-ŒTb¾Êké>ÄÑy_;:/0±ù¨•D§¬	Öf£=wp	ûLj^,o>¯kæxPw®½–Lä'³_ˆÜ÷î‚­iÙMk»Ð¡ÿqèÌÙ­D<{PV»cB‘’QÕÝ/§„vV+¤—}²8©—=Š\ÙªoØÈ|‘ëÖÔùØ—³¨_êø)¨ûCö<šaG^ÑÄlÜ$ÖefŽÀ¶*¹iÝ_rÀ^ñ‡Dá09&Ò¼[›ESPDOÓuüÂ¤c*p"‹b"u›X:ót?êªO«[{6’ñ!w¡Üa¥Ù#uwÖe–þ˜lZP3¸VKðœœÓ×2mH§pƒµ‰3ðHš:áÊ½±¦ >1žÂÂ²ôó±†œó<¨BI‚¶îâq/ÊSüWj¿ÄŽ¢œ®rûðÇœÆœËÜÓ)%—å)ù°çê°AAuÕzÛ€HA$‹˜‹Iˆ1ùuc²“Åi±[ÒHXÃÒìµ¯n¬Ó(Ç€’8 Ö=íÅÏ_=9]×Òôµo§þ“~ 1®þvOh{igD¢©‡»D¦gTÇðÔŸÔJ\s¦~k,'lškáæÏ^‹E1‡”šgIc»ï_ëèjƒNy^Ë’Å~ÍÆ™_]D:¼s¿ÙVÞ^×ñ'(åŠÐòæûË}‡0	r·´}eÐuüZü«¥Ýä£gkûÛ66m.”žDZâƒ¥Í8cÁýÀ˜Ë!@::ëé²xÙ-¥4#‹‘T2]X–Ì®[°_ÕT;:P˜m¦|~á2«rX»}ÁÁQÕ0Ô?Êêš¿å\˜½¿¤ðŸ{¸WÈù«UƒAÚn^]^¹-Ø€Ôm þ

‹s9W—Ç;ô”\ºòÕÃ/•tˆÕÖ‰,rè›„¿S3¼2Wò²ýÇ@ažð9"±´nò‚œ„ ×	ßPx"._ê(Ç_9±íô¢=³D©N/üóUâƒÙ©êŸÙ&Zf>w!¿êêjßŒÐ¨šç~Žóißš^P’zþOŠüÄy  ŽYXZ¼’m¼_cqß©­íB×©/qŠ¤ÉôÇ¼üB{¶¨š•°Öq%qî;ˆ¨AN¢)`×˜C®Æø³ëÞûf¾—ïy4ÜhO~=–;©jè³
‰*,Ë}ÏE‡) (ÌÍÈaÒ¤{jˆ
ú^Ý¹iÔüëÈE©XÓ6~#J×v|zÑÈùrÓíöM‹²ËÈe‰ƒ“¹÷åø}üì¿Zºn‡¥ÀÆ,t,Í_™7þ¡‡¿ÝwD»N“œ™H1…ÙÉ9îºíþ©ã3´Ç•^‘äFòëúÎDcÓºm«×bÝ&Cìo›‚ÂêØ¯AJÂÜ×§£jü²\*×S&›ùmH7 Ô^wËáœÖÃ¨škÙË3•+= Ãj@J’¶>í®®nª°m5ªZÝh6˜2Ó¶)öŒ‘Y˜‘öÖB÷ºÕu…pš‘Ÿk)’ã
àWE~³¿Ýæô[[i<D¦ÜcEšŸ_íK>•v%:Í.éËëÿÏÍ½6ß]ø(Ü£ . «B¡¨×juÔËïó×µ¼Új+TIôHÁ—æW^;pòOŒó7t •	°¤¼\Ò Ü~¤ëªqÙÑnÍEŽV#µÓb¼ƒ¿_Ï	-µûîs—2 lGRõÊKº-Ï×ØÖ%ÙM“VÍä¶¿qo6×}óé˜ÖCÚ4bhÆÜçð˜‰ížÌµûÂ(6½îA%lsZ2ß’¦Ž&Þðú•N]`aÌ¿(’«‚L)«%Bjm+ä'ÛÿŽ!¨HîbIB˜ÏµzâàŸ iè@ ôª:"2Ì=BDÓ¿SŒ¼,¥f¦äGe¶ú\žÕÍaDUÙ¬&“ýá;ÓA‚2¡[j§ÿˆ)]ºßHŸ7¯’H›BQ9Ž­HEõèŒ-rÊdMÔñjÀWÍm‘
Åÿ&
ÚünbÛFÏdÍÌ~öýûõ1äþ™ÆëÊpAd!V#8¤e‹l[mýïðTTÓ:§&¸kXÿœ8çZSÊ_,¹FcÆúÇ·qæ!CêT
ðT#«Ó×áei—/Å3ãÜzÿ/ÞÔ$É¤JA©Ôì­—W:­ÖÕú¼È•>èú‚5ÚºŸBøÁ”Vk2Ã<½û¦¥Gý¢©;
’¦µZ
¢šV`èÀM'ÚŒô^ÅÇ¢§~µ~AúEe`—:°þr£Må#W½äVÑè«W×!eû¹~lF&	ë•¯Aâ£Ì†jgjœ¿<©¼?Šsaò¸Ï<³tDùžt-Êwh5êg}ÞJÈ„};¡ºÔ|Œ¤¬§VÓc¸0„GlQŽ¯ºé¯ª=¯	xÌß»ÁI”Ž€T†c‚—ŒÇ#µï¥loyÝÈ<¡ÎTÞ0¢¬ÓßNëÃ~ØNnXƒ—º¼d‹Rö·XzÖÒ©Ó"lÏòèe°y¯;Mæ`àµä«™òÚAdf‘>'ðàµr»sÀ|†¬šAFçD¥žþ6'F9j)~Ô¢Ôit-\wVµ/êÊåm™¼ÙÅøŒW¸7È'<Ní`¢¢¦3‚þà£šV¥V[G”ÂÜ†? Ã,à³(éÕä8êÖœÊÅgI’)ˆ2áé^½šC};îÛkõÞ©»º!ÕÊÚ¾,­âÜš%¡öƒ|!y¥nYô¬¾Ôl´®ûöV9 ¦úYm¸¥Ë[M‚c.ÉNÈ¡4 w`¤ùíí6aW“R§	.]âÆôš%k·]©œ?·:š×7g3ÄAoíêF¸2a;^îÀºÀ#¡-sƒ€æL¥ s¸÷ü÷’µÚšàO¼5-º©®Ý~ðÔ&y1Ì"$é}iU9EÓ 3j{†9Qæóq¾ò¿þËŠ,™W97˜Ê	¤TÂ¼F™ÂŸÒÅ8$«vnè¥~.Il€¤²lå–{•Âm?m{¾ˆnm{Àg˜ÈrÆÈÉI¡ì{ÁrzqWÔªÁò@–IûîÀøv÷§ .y>+O»…n#ÝpÝ"T¾f]DaæÖË««ú²iß†ïÄîCâ'€)¢¢¤Ó©Só‰åïæÍ¼Ÿ\DfxeX¬‚÷ß‡Ú÷º,»ÎVj÷*/\°éCç£k„—l¤fäÇŒ^c€­%¿QN•¦D,LšÄtÞ~à&ðE²È¼Wa´/ Ö~>c£Iu\HÄ9ÍNùbÖœÆÊ)±úŽò›¢¥&9Â‘ë\ô´–ø‹ÍÅ›®sF7×ß¸&y)G‚­\€R!ê'uëM/¤)|­úNÕú|Dâ|_–š;P)ž”tsP’VÇå˜ì|F²LiN}'¡ñÉÂÒ8òF¥^.­Èn+öPÔ†^qbÉ^ü‡T¯<Å¤ÛüµÐ„—QÖ…æ½÷*p09ÓK4ýê¶ÓËÁò¥lÚßÐ^Zåß…",ÍÜ"­­Œà*ÒW¦T\lóÔ‚¿nr@ÈùœÑ…¸’yf§1Y—Âì{I&\>ëÞ2\­Øøt;7O¶^rôY?þØ6é]åk3<–kßÞÂ7Ä°ÊJof¡h›ÊÚnžü
­®Ty¢Þî*[â|å²¼;t˜Íª0=
i÷p™»›\¢Î:;ÔÕdQº3]˜ÊS”aPG)ÜÞj.¿&PjõZ?Îc—©Ôf|la,÷Íj.ç1VÆ½é¿dùž_M±¼ÞôÂä»¹1¹/"'áÇ†ðJ”“áªµÐvÑG­‚4µ…eXž X.@HÂnqÓ¯ž³¥ÆRzþÛÎziW`]}£cNäÐ×/«¾Ä£hþK’§ò™þ¯Åô*è³lƒUyÂ°‰šJNõ¶Ckm¾Þ“ÐÍºŽ”ú›êž¯Ã‘…s3¿Oleöï›Ñ³q°¸Í
ƒ1“U6BõÖVÝ]“R‹ŽO¯÷)„4äÎG–(¡‡™Í}@„jÙÛÁ÷~WÛˆš_¢ePÔ4ž„ªø!	‹ÈB‡EýAn­‚—_ŸÖ(G®·žŽñ¸¨êÇÇù¨9„üþw•!NŒ>þ"åJn±gÆ*Õ›œM2ñ‘kü™¯1°\3©^ð÷?¯éV–ÔÈŽj“
 ø>ýBÊãØz•=îªr.Ž[Ã‘N8|WÎ™©UŒ:´+ˆšÍDQ;Û“„cls­árŒ§<•—SI!Î˜‹BüâNAÞ´xdZY $™ò#äN “$ä„8û^Tµ¸Æ5¿¯^íUd"-N`÷ÁÏ:Ó8Mf†pÁÈ–]ÓÀ	z•w¬ÜyÙ|A¡£i!å¹œ‡d‰s>zjiHžÉ…èXS‚··¿¿v‡Õ¥Ô~ŸkéAÅyÅéÇFHÙ4Çxk{ÄuÙ´ê¹èßªããÒ“_Õû–²Íüf*¢Br‘·óŠï“¬ÕÂåUe†d½Q}|&Š5-ìúkgµr
gk·’Ó¾o‡ØëOpÊå ÃäU%åWCîN~…j„©^›PâÙ±&¢‰0.Ó8™£¦¬ª@˜…×¿-v{u¹Àúúót”ÑŒZÏHaþWÖHëUOš32	ßP2Ù˜ßk7¶•,¡N\æ™ÞGÀ´ïéðâ¸dŽS±Ûë€k‰µžjŸ¨X‡$KC@ÖÛØ^ÏJ‚»Úm4 Àºr­À¢§úF­x“%?ËÞÞœOèxf¥¦ƒ
Q–3jÄ…B§5ŽË¢&j	æN×_Ð©—­!ÃÌ|‰ˆœ’ƒ®*Å/òpB.®œ’øçÏ5ËœÛØRãñ5Ñ!´Z»‡¼·Í-ûùÜ eŽ‰w“HÂc”•l‹\®Ž”ZÒ¯ý¢ªg†ý­Ùù³Y“Ä;¿þ]íº»4¥Ú>^˜o2nŒ"Z!¥²6(ªô¯\ã{€JönëÕ—•«w¬‡„“–¦ÔÚ'ÿ¡å#¤¨ƒ”€?Ûõ‰É=¶L=;ä}ÚADMé™ï?¿ó«€TÙYÚV#ŒFÛ5­’Ášú¸­†ÁSø$ìÓN'ç‘"Ü']¼)„¾%'ã¦tý¼Q4Šï˜f¯ˆ‚ËqÔÊ‡ÀYdžÙe”9 ®Q1aÎy¾9µÂ!(©PC83—+tÜ\QÞ” MuÒÔ"¦ Êru¦ÐÜE‘Õ%ÓVDzg¥ÐKpË<’DvÙœÙ~
ö±Ÿ£Žª\˜Ÿ?QÓ“ãèÐ‹§Äý³\éËR;s…y•C¹²_z9·Â8H¾t Ó5½di»ž=o«és[úÊƒ¼:„*K·ç0/‚~{/aé!¡ÙgP¼•YØ¼@½=ZâÞñÝ7òƒ/%âš‹SÚçƒ¥ö‰e+è?”-¬bG>îŠéžÄŒž¿ ¼Ó«®é–º¹˜y›¥ùÈý óJX§A—ÄÜÒìñ—ofj%¥mjô(m+¹šŒ_õÉ~±îlâRK«6÷á $ÉY˜ˆyxå-BÕ½w¢o_¤œoçb5Bùà—×:z/#²rHÆ½>×Z³N9ÌÓ±FB!LJÍ®óÂnÃ)ÒíôŽ£èš*2û„tdLëY“}#1¹V8š)Ö[e=Êlfr=
5J9Ô*jrË%™‡äË©rÁ´HgkÜÙ‘ßjË%£¥}‘¾«ü>Ò|ÎÇG¬Ò#WjÞ-"ÎûÙ-º×p£E¸ƒ%“¹î¤ò¦«¥½‚ŽSd¤¥’ÆyÄ:u˜‡²=j1+°jh9çÔ`½5D‡
Fj4Ô¾¸ÿfrÊ´þÆÿðIa ³ÖÝ{ße-ôlûpø
œš=ê£â%Òãíˆ~DÀ¶=ý»ºí?Äó¸Í<.õrÊœÙh—QoÁŒ4ö*C¬Ó`•{l·~DÚûgK¼!Gì½“å®ªY#"ùµãÞèá@œkG„À¯™wlf¿*Ò*Ühýð:Okƒ¦ÕˆwCê˜¥Úõ4KH½XX|°Qä‡†E¬÷Þ1‘<¹ØFÅ6©} ¤š¯’¢òC9M—’ÜqØ«¨ž5#2¥Z=éýùelšµ]>ž$÷BöBÅCn;†U#pK-æ†auß$ÛÑÍd4û²û'Ýgð„²¡sƒ{¬ºuxÊêIïˆä(G¨ñO¢wr_¼ÅÅ°ŒK2õÄx°bØ“í0[Qýþ‚÷_ñÕŸìÆîg“Ùú+ø,«ª‰Îz¨ÔkL±æCFúÎ¾ñÌhñB$aªebÏ"Ýz³@_)}¬Raû’0Q6-Ò½àýxÃ+5’)$y†ksvñ«À:p|Zr=¾5ò	oûÊ/'óUI´(­jìó½”úaà~xØ‘À¶Då%ëgÉ»‡òn‹p¢9R¢Å×Š:­š3‹Gqø(«µ?Žìuw]pÇ|Zf¼«×Ñ(ªDN*YÆç:Å.×'cUwH6¬„Ïzµ (Ö}(x¨O¿~ýŒšgpóä\ÃØ‰<7’“!ûÌ1ãT|I(ÙÔožºqØ¡¨þïŒw•Ï	¥émykrˆ%ÔÊ}¦»ˆ:}ÄŽlì|ìÜkã±€8´ªìäœ×Cé™Ù÷ºd´îJºB]dLÕÎ¡<‘Dj}ÔaG9/¡ÀºÊÞØg:>Iý‹,ôÉˆûFf†is¢<ß-¾“÷^Ëžwb’æÜÖà©‘õ¶nH@*3ßª™c.’óBÛnÆÄwµÀ¦­¼%ÛT	E\*’&5ßx[Ä‰òêŒôúaCÚ«ÝR§úX‚ðŽ\šý-	oñ½&200]b2ŒØ’p13dA.Vñ1CŸÁï0F"ë:ü·K¦ÔˆŸ„Kð}Æ7|)ŠQÕ¡_äVsÉšpäþ8BjrÊÿ°
Œg®/%'€2î2@†æòíxÆÄÿÁ}‹/Èæ³¤ú|u¢®Ä¢aÛäPoÂ{…|Ï\ÌOüvNåjkz¯ÁU¹´Èì
\6…©à°ªÁ_ÀÚ¯òcÏâÅ8a#‚‚El|¡fNñ•è¾,¡âšúþ[<ûÌ‚lÊ]¤Ë¢¿³Õ#%t~oCiáîaÔ•þw€@jP¸JþÊ%Éc“(*1‘cH`ú°¡ðñÐÈ™Ñ‘Ÿþ=}»Š-w^ø¾œdžSÁ‡Ä&!oçP`¥2­Iúµ4·H¿»ùÎK‡eò!øB™i­>á+riÝriÑR„KWÆýt1rerj¾] Hm®­õYúEšZ"16èwõß-ìÇ”WBîñIc-nIg›˜+šÁ?e›[¡mG$²6-{äT6kÖ
Œ¶þˆè~)@®K‡ýK¡PÚ:ÈcŠ-\FxN¹êãóƒ¥`áEŸèr[¨X 	öÈ+¥‚å+>*¨Y¿æGYÙzJª©µÊÆÑ8ãƒ‘û,„W„9¦°ã cåS_‹¥ÛÓG>¿1MþŒNÕû’Dá»oÝì+„j¸w¹b™5×3ëÍ/Ž¯à("|8{X•kÖQ}_.*rQcr<ùÉ±¡¢Ô{Tö>6guµ¹/Ûê¬;™óöÇÈ³—Ñ­kâ¬áø»­3s(›©Ñ’g˜oÉ˜æRÚqÙH-ùõÃ²²ÖÏc·GGžÆ˜ÝÐ·•Ýv3qÛùÌîìVXRâ[e$2ìMü!›Ìt+›"\…‘p^”OýùX‡×:º'¨¢/ß	VÑ`±±N]ºJ}Ûùö.dK zV‰¡>OÈì>B(¤- ¦fá“ë0,é6žp
¼1±&kì-|.fÃH¸M¥¯å-"ÌÚeäôC<$o¿ö¬
µ«˜,w4æ™šS5™™ð}—¼fÍOÅxjŽ¯ÜðNó!‘»ÌWÙãIÆqHÓVµö-7ÌÝúì£!euƒ¬Ï¶KJøÄ[”r­<+dåÒ¬?o¡”˜Ï/¨Ò³+ vºmúO$	¢Ü@”3©©çç"¾¼L°ô›¨dÓºüëøþvúÀOq¸X˜	5f{*¶.s!µÖYÓLfL§©÷„ß&MiâUVƒ»B•*ò6ÇÂ4Á¾JŠç°L’Y]Ü°v)‰µ-*n+â‹£é†Ià‘/Þ2”#ŸåQxW9}ôâ®2©åÞ»ÐþøFÎÇ-;‘˜±å3/3©Ù‘†¤+”høj=™È°ji(óUfB‰¬…•¸ém.BÀö9]žŽöx&‘wóq=¿Ÿëë¼B{¢[”FìYîl~1ÒI+/’âÇ˜ýu8ÏHœÍß»ºËÁ¢É)½ÊÜ¹¿s5L1F˜c~˜Gªg¸= „§ë·¼ÖÆ? +ì·_x­¢òx
­¿8‘õ#5åA×¥ÁW$ø	SGO~€ôæß¢OIr]ë¾ðÊh?Üûs—÷öÇ÷?Z†}Îz’_™‹Í1“j¿Ô€vöV÷êô¦eb2xóRž6jŸÏ2è¿À0.ëôºëHèAŸƒ2Itý9+j8ç/—|˜ÿJWä½Ù%’wú„—±%/žñ†—›}äLLŽßÆSrVlh$Æåb½)™ïŸºßb?Õb6Õ÷Üw„ãi}df	Oh|Lß¢ÝBßËBöÐ¸óÄöËzw<iÏ…xÈ×3jÔ7ÑŽ~‹½…Î|¨ól$øÒ$ ÷ø6`hªÑ@åÞ»ˆ¥…‹‡{¡}Ãíhp9ë®cfó1L¶7P•‡§·OþþÜyáUåŸEuú÷(`~ãX”Aàád&?Î Á2ìJ`xƒýç,rŽM‹#Eõä`S©¯ýßûÈ	ï±‰§}w¶wÜ,ÆA¯ÒÁ…D½ë[t½eL{B¢¬CQ&XF¹ö%@ pp=ïW'âQÿóÏÂ"ë]ÆðÓÒø¸lÚíã5DÊØ•@üƒ£ZÊE24GV.ŽFáñÑô[`]	 WÎ¶—¼âÛd»Ï¡ò±z‡6Ýä½©¤ÒeL>1L¸Ï¹—ìÄ
å[îÞøÈÚwÙdóÞþÜº¼—¥ôvoÅ€ÓÜ{2ò\·+²é¨wS.4’·9ê›Kslê6È¦‰CÄ1Æ’¬:é-þ˜ðyþ—ïÔÓª´‡€ÊH’¯Ë‡2²Fûô¿ÂÄ4Øîo%}0[ª_ê®¿SÎ×áZU+Ð¦¦£àÄ­†ÒyÕ›uc:KßR™H¢¼zc¾W<ÒƒÇ¡÷à ¿€zÞ/Ñ_‚dBˆ2½¼8¥?ˆ<Î+Õ™u çÝ—=ü4ÏU7¦î9b—žÖb;£G/âÊÊ{»_Î» Xf¨·iÌ`’t‡;7»X{Á©†XUÚ\ÝØÞ!B«jÜøePYëÜYŸVöþÌ>ÄC~uolU©–ñ{˜ë°G·“¨óý›çÚ5Œ
-ðWmOLWºèÁdšÖ	b¯X©¡‘Åp–ò¶	¼Sù5n1˜i&4Í›M¶{' =”ÈgÌ/Âvß´eó2"!‡vÞk’JW»ÅˆÒ¤€ˆ¸îGÓxP\
ÀÝ¿=#ƒ+[d(ðŽþÆ·xò£‡óÝW%[ÓÞ`oq™ûšA¯Ò½_©¦éÂ±tMa$Öæ©à¸„”nÞýöÿ†©3#F^³¿ ;ø"ƒ=Õ=L¶NöHÙ‹Q™¦)vÌi»Š?£NÄ5.‹|þ%²îM‰Xz;XÚØ7é¥—™,R¨0OÀ„Ì?^ÀÚ\,Í5IÇ³÷~?9‰-Ž…Å4ôÜìì=ÈSzƒ¥£”	9v³“`œÍŒraàêû'ø;ÍzÀ:àëì‘®*]š¿÷GyÈ™{·ÄpìX«‚±&#
'8ÊhkÕ~ôÛ'pÕg©Ó:Ý6X«ä^H Ž!@§|äÐ@ˆKªiàCnÂ2ô
«À¼ûïlŽ‹l°1´H’#úO@É:§˜Ù™&²‹X«¤"/î»? =.ÚsŠ>ÜûŒmÑØë/çgv”+§ÏÄçãiÞÐN0îÎ„·ÈæNùšÝÞ.ÎV,ß²½cƒ¸‚Dü†~î±ìµ‘#cêNb!_ì¢t¢98zõÈ'É	•µ[[CÂ èýŠýï^Õ½\²’Jäß”¯¥§–ô{ÏCŸŽ‚÷—Á™Õm\z`®ÇX@ë$’•BÙ#C³"&v]—†#ô„iº	¼‰ÑXgÃA{§(ÈaÊ]I‡Å`pül¥ÞLŸþé—SïÍ"é2ƒ¶ø#˜
']ÂÚ“-HÂ,tÛ¶ø<òŽJùûˆ¥áA[[(n—ÌÜ¯D“•×ÇY“+÷áiºN½ÏE>/ÿ"øy}qÒc]ÖO(Š÷ÀêÀn×mAzÕió×ò,iº½Òkw¶ÃvæõgûôN¿AñÑ*ýÁ)Kö~Çµm\	³‰4NE²5ÉK l|}´³¹R´Q8üôÁpw_­n—ë¸úp×hHà=|ïZ¥7Ý×‡òAìÍVóþWÂ€ñ«òB‚"	8>ÖèþÛ î²&Ò» è)ñ1Îï¬l‘*ý°«Gã¡ÂÞ¯¨ÑlæØçÈ\Ù¸0’Ï¯ËGk¯5F¯/Í¦÷lÜûéEèçX»\bX[.1y_Ôã÷¾èâPÌŠ¼r±Oòaª+«¢®"bÏ¢;åilÓºÜ¢ß£›Ä2Pÿ½z§Uýúøióp÷F°˜Ç83ƒ¡ú„ØKL"Fƒ<ïÁ;MO¶˜÷„ËK
hðl8ÕûÑGÃz‹~~æ­„º¾Þi/v¾Ã‹UÙbzÏÀqê2/èÍfgÁÁkÁH’™¼¶ØSòïl>Ù(wÙ/OË³„¤˜Úé<íçY½éÄ`ÏŒªV´È÷½é{%þØÃÛûËåè¯{ï^ÅÐæíZÒGlÙØ{|.µª`éw@Ç³ß¿Û}»¼Å[¡7í¥ÇÍéUÝbé½ ;<“Ú¨6¨d‹ÉËAâ:>z±ônÐvB6Ô62øâ²doäý€Â>ÇâX”cq:§.ÄÌÜ…ƒx5=À÷CŠþzŒÙX™~G+`òV#gÊVC5¡ìµB‚‡ôý}­Ü{\p«J¯ ×Veß3÷Ôvi`ÐRÛ[fO„¡ë‘€Ý†èVÐÄ6î.eÃ]ñõØ‹žô$Q¹gÿðòÑ×½Ïü}3fúÃÏ9ËY¥ØØ–ª(Fuˆ^Op“V˜„ÜãØÓ!2à„ú“fE#/Ö?¸È~pibè9¢Å1\ä&CþêÇ™k–×')€ž‹³º¾µœwtX(–xZ˜ÜñÎÙÒ°¢_z3±ú½ˆß.v:OÇ˜wó….$TµŠîqÝ¶$ÐÈÑ4irP¨0-ÿÀûÎÔÏSÁ	©¬»Êþ.ÔÎ+Ö*Ü"“ ›c—0[1Ã‚bÁTñvìÚtIÀæüÍ¸ºØ˜ãOóz³º§¸ïÈ	äâYÍC„²öÜ2ã)×@;†X.ƒ¨'—6œ¼è¸4š¥=ñ±sùÛñç÷Ì!xQ`ÊY´ß´h`×ÅpêSc	=oìÂèI×ú#/AC™p~¡‘*¶¡å¯NÍú>ýœŸÄ #‰–3aAÐç4¬¼¸<íá×ß§ý^ærŒMdÍã$81ž	'äsØ£Ž<gµm.7+ÿl{Ñ;-ïþË	•: ‹=. Lã†š›4À}V1tè¾Ø%Ï¤z²
”xN-ì¢@9s?3.®áäxÿsLï”¥m³Í¡aM‚QYìÐ„ã¢˜ùsÓË^Ü±Uo$õ=#¦_Ç§Ã§‡‡öFÝHyš"Ú¼/\<)Ýyt a­ ÜùSc²£s“˜<ádBbjÕ÷¤Ó›“Cñwîö^ W/ECöâ#h÷Ì!ÃÓ“[-¬@@ä9³±FÜµk½(Ð‚!ûãW”Š/þÍ½ì¤Øœ@v®ºBÿ|4xÍ‰eÎáº £š°Fg{¸ùýÑÎN7®”ü
2'rã×áá¯»†À®×ñõ§“=L±·h·õg—ôŸ½xÅ:8£úqûà¢ÊïÝ;·µ*¨²olôÃ:½¿‹F/ú‹«Xûï“÷w€EîôJ\‡±Ézs&hÓ§ä]™¸ø¹éöiFÞ‰ÙHóƒß?ßÿ>ùQ³–OIRëÇ`µÏží•È?v-ý}«®çÇFPna8¿ý±û¼ùùÝÙªp;¼‚ØçÎ%àÎssbsÜý±¹W&Ø#µý~»—	^– «øì½Wçt{ jêïÏ6è§ÁóâY)·ö–Ç®<¸3u_ï—¢¼ëš0Ë®{~õÐŸ§W½`p §¾',«‘H“Ç:áä÷”?Î>·äÍú=®ÏØëšJ»IÌ¿ª’*YÛ{,vI ÒÙbÎx%ªòûôÉâÉþ®Êoš—ø†(Ð†œBåìÃoCžÇ_Õ¥}€†6«Ø²GZ²O4ï‡ƒ~c®Þ!‰2àXíbÉ*Ùð,ÈEpÂ6~¼ÜØûóôèS+æãƒCÌàPNhŽÄÖ¢$Ä †!;Ï15Õöò3>“LUŠ‡öj!—{zûúzõô§‡{ÏÍ§Sí¸¶ÀžFðÞ³X®9~Ú½ÁQÜ†´ ÆÚƒêo¿“E$g‹ŠŠW§Ü\ÊêÎû	gOAOÈš½:TÈ7 ²ƒ{šI’`[M½Ü)qø¼ç8F)YÜ,y4ë´uH•÷+á÷ŠóI™	³²Ó×{b¿Cõt]IÃWýSƒåCÁùn`Þl7˜›Tû*?>d#«[ó/h¬wwdmï#É à		bÑ¹ Ž¡ÝGa¹¡`îhr}‘Û_ÞÊ‹¥_åw¥<øù—ì"KO\ÿœ62îLÁFÒã©SÄDr>Má¸jÉôÐ²÷ÆUÐÏÒ¤á½†ù46[+H›&CM¬He~‚_•Å
¢öTBnh)¸æ@eƒâ+qXØ¾à1ýª.V°?]xKxÑÎcU8N*/I‘Xõ’ivâ•çk˜'ÈþWU¼[€ó$€¬$‡sÞ’Ÿ`ó¤#±Q™9¶ÎÀ©à##ú­$šƒ_{B‚îCE’oàã¤ä`kªéžŠSLcÙ8öEÌF1•+—€ÛÝ€Þ‰¼DŽÖ)ùÇˆüÓ@‹e)ØHÙ´{îsÑÄI (ñ-Vˆ”LÃŒ™l¤—ðÃxmFmPyÃ—ó ®ä+ v1´	ìDþ
ÒKóÓ)±Z^9il’Ïé1ÑõßwHØHd¨þÃ¢²íeŒ4P4¯º˜á%/íséœIÐµOpMÌ§}³1.›‚OÈVãë[4±µ_@Ïí±8ïWª+ƒÌQ¦›ž†§.\·ÿâ™RV.§²Þ*J¨L8†M0e¸`l°=UO	S‘Kr¬¬!Ä…ÄqžMÈ#¬>”Åq o÷iÉ»òGdzò¥™–ø]=NpÕY¬ØY«þ¨=úÕÇ#Kd{ZÜ VŸ*«sŽqÏò£`®(~øÚÝd¥x:¬NÉEwRnòÑÑª+ B÷äl«ZES¦éžâi7Ú˜.ŠëH“¿è¥Œ´W\µÅ›qz’»¡5¤*büNÿäÉo¤ÿÄáæîUºV½Ì«Úxý-jR²åq& îFÛ&yšù3íxï–ü°ýò*Èàd.ñ¦/L^\ñÏÌ6šh‚I¯t$¬Š¦…c=S7p*Öj¡§¼ºÑŒprháBdA(÷É9WEçŒ>úâ¯W¬È›s0ÜƒÃº’ó^ñxæñ‹¤< õ_—%1Ð4Á‚s¨j$æ9Á«~­šŒQtMtÈ0A±¨”í7€gà4{¼(h_6a0L6“e´ÕôE•ì:(~ƒ¶(P	‹€^ÝP}’jFñš Þ²
qjŒ½u•wÎëã¥³BBLs<©wAD!xW"‰‹v#œ‘6ÇýL²šÆà°ú‰ìˆ—©×cÙû²ÇÅÆFMD_½2:"¿ú@·ª…uBö³WQòÀå ½®ì®ø5:Þ=U*kU?— ¥’FokâCwÖsû†Sƒr?§ñC=ö@Ôxufˆ9M§DÈDÄûû=_«%sáqu#•XÁr3?û0ƒÿUqÙ5q§q|7»›W7	á%Ç{€DBTðMz`I0òZy+H=c« Âr%–6Ý,A+E@9Ç7°8¥giõeCây2´ÚÎÜT~¤åœN9Œ:Åt@¹uÿžÝçyöû<ßy•à2oÛÁºi"ý@‚ë ­ÎøÈò],§¦b_+àö‚fô²R‡J‰p°ši!cOÊ<”ü€ëº‚,PºBòìñUÙïôë5;“žÆ‚»Ìiõu5ß¦pU¢-lHß8Ì¹ Yäé²‰zCŒþU§êSWO‚Ìh4Ü_áËaÌa¶¨mµXgç$¶R"³Ð±Áxµ'äŽhfÔ±Ùs	,ˆ5H|\¯Pù(µ!á:¥ÈÕfŽc'w.¢Îêj‹”£¹îdëlˆÍKÎ}"
ä†8à8ŽŽ=Ûž/VI÷ÇÑoÿ0:¨é=:8—h$ebé3==°Ý*2Õ™ª2|’¼Þ#YØáö'š;njg~×nÆºþâ€©^O`Ôà×Š…A#öé ’mwÇùïIž›P^Nà4 ÉCé»ùâ¶~*¨"—‚‚õ°@ó‘ÌÜÚïEt¿7µ€b¥kºC=>Ê¦o7£®¡žà‰~SQF¯Â…EøÈñLóúÊ…ÞHWëÛo¬&xÕ°˜÷a'g/Õ»T¨VêDÕæ¦ È+-’-Ÿÿó[˜Q¨uhVæmLhÆ/`ÎzR+¸‡,S3Ò¥Bf¼h.*Ÿ@3–ÉÿõÈZ÷2®1‡•³§’¢Œ¼„”SuÔ˜¼ÑCeJK
¢ÓyóÛÀ“òÝ×ÇÂô´€¨åöLÈ•+´\šåI[ù~ÛºÙuwa2™9ïŠåƒøƒ! ^¶¬10µ‚š{Øü	´N…ÐTën¦D=Ú¾4HxXñB˜©ˆŽŽãÒ%Ô@.u°Ì@³sâ7|1×NeøàlPC#tW-æ³ÕÚeò<øÙ*uéžBhtë%êf¥Ýý#ô ¨f3£‘¥ÀðlLQ©ñ³ÅdÙ÷þ¥Ù‰ºì¨¼UûŠhn@RJ`hó®B=ì¡Y­'×a5É¼¯ŽOù‹É«]§ðâö‡¡’ô¸Ó „Baãf*IüÜ[ÿ™(~ö9êªï7*.„ƒSž.£‚OsÆfs
SÌRü	Y©qÕëÝõ›¥>Ü¹É‹{wÎí°¶Â‡3º¨w«NûŽ—Í| >à8¹Îh|i¢à°œQ1vÍ5ž7$ÎààyT²BiKšÜ×Í¼â°Úkó„÷x+çÌL1ÓMÄ6BóÈLH/¨YûúÈ9´L‚Ô™ÐEÆ+Ê\bÍ>síXS½ÅÝÄ¶¯¯ 9,àg¦s¢AtúJŒÄ\cŠ&ó /‚*ê§…r&ŽýÝå³ÀœjC e
'p³~ÎøÓI3êçˆ
ª'4|À©;ãDbøb¨“[@`ÝmÀrJNÊ± @Âž•¹*ih“#ú\µükpöv¿¬ºi›šy$´Ü]%'LJ5Þ2â„Þx;{]ýbæƒðÜè>ÏF­âQU¡!@S(°sb"¦½z>>^LyîUèÖöòQ6ÚàJcbTF~ª^ß¬õlô’ä1ay!Hc âŽö]`ZÛU:åÏ÷~_ùmæÚÓPS`òK‰É°Ç¼g«®pX½¤	a;HÃýJÀS
Ž]!ÉuÀ »‘c«#†dÙf=…ÔÍï¬_ù-{å·å
ÝzÙ2­™)H™i=•©ïŠ‡n7IÈhNJ»Íe½%Î4™džPYÏ~
1VÃïÏ/®9râ³6O	Y¯©ž\%™p}O˜ÉoîbþdöåaŸ&5óX‘ŒZÍ÷¯sòˆNœÈ^õ/þú2ÅÌ‹'Ÿìnz?&${6†§î‹¸÷É0€r¦E´Ž¤å\Á…/§cÉcøƒ›10¡³Ø}"têyûôœÃàn&ó,CCï¶uÄ;³*9ªÔÝˆ{¼%T¼´ÄèÆÉ÷ÜŸé·	 wöU	¡Û‚²ÄU÷¥|#Ú¬U%Gû2Û6‡Ä¬B«yhš¸tÃXKþ7Ž8%hà˜cìô$IÃã³?p?Ðý=¡@‰Püš±©Tã™ˆ¶ò/"¬4,L’ó46(.‹’Ø`î¤úB_‡-d¶Ùª¨t‘³×e'ŠævAÍðÀ~µ™ÏzYªâÏ¯ÂÑŠK~r¿îÌ9ÞìZäøÇáUŠµU'ÏrÕ(!“
%hä·“~ù‡;Ø±(¼¼o;Õ7Ý1Fy*ÉÍÒÞõ™f|Ú¿¬wŸ<›k8ó-Çbøçª©·ÚöþrjŽÃ,ùn=²´ùxßtç˜Í$9sû$çú2˜ðÜ»un[’º€‘Œô(Î|[Èà¶Ä´‚âcaX<w—S3ìÆ ‹µ}BåQï¹T¾ãF†ëJÕ”t<¶f’B—D¡L¹¬$¯ì§Ûýœ.}íÖÓË…s'ê»k 7ëKÃ´U…¤ÔæŠ…v¯ìúÝè§ÛÔJå¾MgO¡3eB‹ÓÍ€šy¬ÈX5Ñ,$yvíW/ Ý':®²sÍ›+6í\þýDçžSºÖižCêþìñï­L!¶r¡iêAÇf¹hIÑå¿Òx£T4vJõº“ëþ
”úÆÄÄY_Zë		[eÏ”eåƒ—»
)a*9IÍä¿.ÜN_±º\ó)æßÐôîdCD×u’¼S¹@í•$ˆŠK_zY_#+­¦îç#ãR¹Äâp+'{–w®ÉŠì†J&¨á©Ú†š.}ŠX&Š	m€žÜ	Ù9Ud‘ÒÞ†Êß)wµ£åµÏA2ÿ–[²vD ™óÇ=wÌñq/à âMCóúŽ4‹@æë1ð ¸ª‡‘æhù„*
Z1—ÊhhÐ×ªzÊ©ÝP¸'Äõ¨*`‘BN|}´ÃÜ·ŸÆÇ†¨FjÀÂó¶°<¿Ë&Û	]5GKÀÖ“ÁhdÑêœ4´oÓ-(]îÙhÏ_š¢in5¬{èéÕvuì„ZIS^H¥ÛÍ0˜òç375/ô><¯†8…ánêYÛo£Å2ß?zqzAÄ<¿$Ì©íéå<Ròydþ“Žh–Õ~aF®¬:Q×‹¾ø¢Â;khá ±]Ï<~ÏŽ2Ÿ¾Ðó6Ñ`—ºp‹gzØ]˜.ŽÑû¹>œè¢’’nßÔ4‰6qhn6_Nõ‚(ýŽI§¢‘„,8Ü…I1OSïý€SöDœ"0W1q“FÖûûý’µlñpu¨ç#æu:û3IÊà0ˆ2ê—!¡}hÈ«72MüEðhùïß™)|g’™³\&xó	\µ€èøúù¡g·Ö;¬Á£èrûESyõíÃ
¥eKˆa+Ã=6Ã×°çI”Øu…¨ /áä¥!}ë[ˆ0Zàp	GønZ¸ù¶ÚüÇ"Œ{L…¥!ìäíˆ!¡,>æK—Ûšh{%óÚytµ™ošÝD˜hžÐÆ±'z¹·ã<·úoüškÏ¾1Ç˜äŠÄÄÂÚÛÿØ%21~¯á6—²­ÑØ’°W{ºaÝøcÒÈ&çé‰"ê#ë®AÛˆmÍäÚQ=!˜ïåXÍ…qØÜÁZ‘úÚ„ÈJ­&ã$ÎP¡Ë'ætu‘E`7SBÞæî›^Œ=N¥ð8H²¦VŽO»[òÝMÒ,q ÖT—ÒüË
’¹ãÁ†7œg!ö)ØZl´ç˜¨ÿPK     šXèœ~ÉL  SO  K  Report/StaticResources/RegisteredResources/team_spirit21080007706708703.png ¢ (                      „¹wXÓKð/œ„ „N½Cè¤( H½#UEé$8@Ñ€´ ‡^QiJï$h€ 
ŠtP8JW)
êýêïÞç¾ÿÜçÍ7»3Ÿ™E‚+“ bE™;€@Ð2ÇHPN­™•“	Ç3ˆžÊee¦ca?ÃÁÇ,ÀbC0òÀ¹øY ÌL F@Ú?Vf+?« ðð3~6A^~!VQÄ~AÎ3pnfV.>7#œ™‹_ˆC„NÏ)Â´`ÁÈÀuF€UPh`¾<|ì N!Nfn3Äâã’‘•áçædãCòðH x‘Ü¼RÜüR¼¼2ÜHu	¤‚ª´š”„œŠ”†¤´&RJQME[ßÁÍÛ? ( žšŸœ—ûoÒÂâ’'O7v<íëxÖþ´mÿèäÛßÀççÑ×ÓÝ_À÷÷áïß_ÿPN¾lîííí~úøßêFë}þnnñÍ›7”Ñ7]½½¤.2™Lìêìéê}ÚÞÔÒÒRQZøðáÃŒ$|I^fA~AZRZvvvJ\*Çb±W¯^µ···3»dggg`` *¥®,©ª©©©¦¦¦ªª*— œxŸIðTšO–Kœ“C„X2Àâaädæc€˜9™ ô 7Œ—ž"È*ÌËJÏÃef¡ç¤ã…ñnF^6!@JˆM„›…^TT|Îð0s3q2Ñ³‚ØØxYì‚¬ ØUÀ^œa§6”ë7”Ž™sö"ø±ûÇÁÆñøøûñññÁ·ƒ£ƒ£oß¾£ÃÃ¯@0€@8<~¾Ÿ¯_Ì/`ŒÀøúõèèèç÷ãï‡?Éƒ´A «2”ñ%'>þ­~Ë¦z÷Ž¦yû:çä¼§ßíxáLp¤b•Ïl`hÚÀ“þßÓªë7'>ÉÌñ!y°ãÝDŽÿÛÌ7ÊsÉRiö:ÔB¨²}|üQ<ÞQ	 ”`žHØ >b¼/éoCö€wGsá,Îa »(e+ò¹eÃÿOÓÇ°B-e&Å(ÝÖL:GI‰‚ìólÙâC2Jç(‹)…ˆ&’lI¯¹º;áÚôÉ“Ô(¢Ð?“‡]”)[|ò¿ç•IŒð ÄÿjIÏÆŽ¿–§>Ü~ei…b€Ò&’‰ùÀ9íÇÿ×ÒÿG£dÿ
kè£²Î¬1IV½ò/Ï`!1bÜZ"û,°&*È5~N›`P‡,‹Àœw’cÚ(+µsÜ£}ÿÿw’ÿW“•knäL£z7D¤Èbá°ò¿Ä»ó";0âM¿sãK\XÌÁXÃ`·.d¼Ñ+Ø¡¬G’F]èôsY¥
ƒ7fš:Ù970Ì:Ä¨Æ¸ ìN>"xv.…‰Ÿ 4DuÆ½Ä.ÖxëÉ 2Ó‡^)‹gMöË ŒëbtlYÜÿPã#´é©=¹s©÷¾Y£*n#à‚öì¬ãKpl¨ÙgzÆVÖêŸ-×KKMÉ}Âè‰ÂüC.*ÙiNì®éçÅr%¹­Ç’‚Uì$”zBˆ»a¹UÄ´a¤V§.ò B?s×¨¬ñ±SGÝ‰ó¡Âã^¼$ËîüùP`9Ê´å‚¹ÔñÛ
Ø§øXÇÏ±­°ÆŸœa;u]:/
”õÈ ŠVÇ¡Ùÿ@·-dü~öå‚ÊŸ9û%Ø<|Ä9S—ê®çîe=Ò4*Œà\»Ý¬?îxîcÐ‰Âpw0à:Oôƒo:Ñ&äî‚ú­<ºq/N,,/±çq‡mÔjµ©ÇâDq•ê.R_Ù‘ßn¿ƒÝiÃG(¸.øs{ñ š¶Ò…6”?‡NßÑ‰¶µ7•õÈÒ\I£[õe&R$ÇNÛ²Í7±•å<’2ú´3ªâRÚ@_5ß&°U\ºÈ!Yª`.Iþ/S‚nê×x'ö:¬(wÆæ'Eö™]éˆ+‰"åmM•G¤½¿¹²ìNîŽ¬ßv?7ú>16øª.}Äóƒ¾N|Ä¦Ëb	_Ø® v{ÛêÕ9Ô%˜%]ÞnƒÿÓ¦tküíˆà¿Ä¦úþ(vIH¡/ó Ž)ÿ‡-­â‹¹LÕnyHBçâþ§ËT¦ËˆoUˆlØ@Ë<:x5u¢%hÔºÎ¨·lÿCšQ¾Þð,$¬˜fÚ½gë¥N:e±ƒ¬Åm¸ªÔ5_nïÓð[Ê3]±A­
Ÿr—UûuÇï7­K‘ÖeÑ›´ÐôŸ‘ükyj!`JçB“ŽªM`áÀ¤ö"Õ-4Éò=Vmÿ&ðÎ-¶CÏ›¶²kÂr±yŒ:Ú*âÒNš¬•s)	ßdMaÚñäSDR—Üö½4û­ó›>Öbª‡RÿÒ2ÔÜOšÄõÓìI0(Ø
ÕØ¢§Î7qæÙbŽL8’õ…‹Î±¦Û=,D¯ø!ÆrÿYîl‹h&é5“ŽvªyÞÒOôÅ­°RÀ+Œqb&Qƒñ+A'âÃhr·82Ùsm«{R{ý~bpæ8à¨Ï[<É
Ûéê‘+À™T8…ø:X¸ H=@dºX
UrœáÎðÌ‚Ò¹»ó¡¬˜8
Ø¯­ íHßçÎ$nøàžöL¿ìB(ÿÿ°1Ùæhmn–©Q% …Ž/qTš»£‰&ÉÛYú	b9]˜`¾õ€;¤Ñ€5`Ô½í­.áÁ©CW[	äJpJ^[ô(]/^øu>›iEñw\é›½ðkaEÈ÷
¢†Ë/Yœ W»dw”Ù¸Xu\8œÍöž›É²ÛyLD“øæD,F«‰ÎèÆ!*9V©5‘Ìë€oLYrVOŒ{»âm¡(¾grzØÈ;Þ˜¼ÄËO~ö$LEªãX"jI{…êþ-ê}ÎÉù“
2ÚŽÜ ¥#êÊP\cÜôZ—Ì^AbÄæÛ…8þ£ÎCç»‹€›f@ÂÑš‡ÓlD}ð†KC'8h§nŠ‰<zM‡ :/$1GFß¨Žóý?£%±I—EÖ£ü(‰a´¹»þ[|Õ´%3ÖBwzÅ¹ß‚pýDw'õÛ:5#–I7’\mÏbÒ‰¾O…’CgKFÏ•@Š$þœš›ÓG|&á‚7&„£”Wá¥ïÊšæ”MžyÕ=8®Iú¦m†x(›S>™ü‰TÛ¡K}-ë±VKðAÀFBŠé´;£”ÑVän]¤Ýoë²TôâTäwG?¿˜ïF?¡K’XÂƒy;¬,àûx¤9éÌî(ô±«6ºzÉ9ßy©#Çµí‘q*ª¿…P’ÏN8VZÍ­9ä‹?lQÑ”y?=\ÎÛúH S»Pˆ"™Ð;<¼  B_ÿÞbŽ½ì23\þÊD°nµpAùSX)Ü<+wÒ¬¬ëí-,™„~’áõ
L”-Íº`þŸ´§×Ï7²Î„å“¬Õy¹òju‡Ì~Ë-6¾»Ýý¨#]c	÷šÑîó®à
@·$†÷ü—
”–w-|Ò·3õ¶¯xú9“”`$¤¹=ríò¼P[ÜpDà92Ê-ù:	»Qj}û¿Côà6©Ž¨pžšõ”0fZ}ÔR²}ïee`|½{OÖb6>âÎY]C3ÇEF³¦Àí4Q¼q;Ícùª®Ü,_ËpHÓ¬§fmFîÞýq¾ÝÄY­@Ëp\³Ó+‚Ïý§àá=­îxýOûEM]j´,ØÒÒh^Ý&ðº©¢«þraEb©9¹¯§¦åŸ|¥ë´Lû¹«½"oØ§Áëá’¯˜HG3
{}ueÂÝ]-ÒŸÚTW—[žÇÍ(}£yÖ¢‚(çLA£ŸÚ9ÀõvˆùüRUk<st+™M;ÍÜ…ÜWßÔqã£Ù™Ö0uåvÁ ª”ûYÁÒ}>âJ°d§çm©‘‘8*ì=n,¹Ý]Õî!‘„ìü¤œoç~)°€®*³tï©îG“ûîK·Èêb‚ÐåÌî=¾)‹©äRøn
Ú$sná2ƒrÀV!‘3þI8rZ|š¯?;­5“ÉÔó)u1™›‹³Dc‚ó„»ëºÞJlõf-&ãcE[Û4ë$\§´r"
–ò×ºÄiË¦yóç?
Mk¹uOb6±¥ØÐ
t_òÂ|À¹‹žmrpEì>êrVˆU–E÷fj$-¹|‘FÒSuÿcòèÞzÙ=ù¢þÜõ#ãå»7[}ÁGgØºÀÎœ×¸ËZcþãµ¥	ÑoŠº`&Ã„‘7#;µ8ö4ŸQÈ®ekVoüu?ÁœÎ[¾Y:oôù1Ì 9Íç«¯`89–’ÉÕ¸4½ª%FÓjE;Ö½”9LÍ HÃh2Úíáhü«-Eè{]Wõ”uP¶Ù÷eŸÿêŒ>:@ÚüG·Sˆ_lnWq¿¸-~îÊtÔûø”Úa¨”<œç]4O§®ß|67§;YóëyZmqÊƒ]D0/6Ýu‹W±Ë=ûsñôýÓ_ywœÏ¡TéÎ´ÛPt£~Í‡ôÉ3:¹¸†ßGw6ï<¤W‹ð‹wÑžC)"ˆïŠD°¼)<"í÷ÖÑoÑ“T ~ê’qéŠá¶[¼+p¡]\ÝîsáÇÆß¿î,ÈR#ÁÄsq×B&,ˆ8í—°Nª¥eg-üîi.e‹¶$£­Kç=ž<Ù¾Äÿà›–ùksÓÏ=]?yÂˆPê¡-/§ýºµæ™3ræ¥h&’5¡ ûäðtzAUó‚±ü1@ÑßFŸ!†ƒ‰â^~˜ìò‹A‚~)ÝxÂb›¼Áš•¬…3}å¸Gx|dÍd±`Ð°h'ë?”¾{fzjÅI>bpß,Î™TÄ¥‚À
Ú—®¼­fÍ_›Q¢i‰ó¬¿˜ûêhIrf&)ýÇQùáÔï®0¶ž+øÆ÷ÐÄ{gswa—íà™¢FÄ•ÈSŸ»Ü€º~‡ÝÍ‹™–>‹"ŸÕ5ŽÞÅ_	!¥z´ã=ú^Ü–ß,ìyêw¥XCá¸¶}E€zþO,^ŸÉ2+ÕÝ×ó’½‘•xx¢@siRk÷ââ¯×EÎÜ@“2¦9w²ðÝ·£ÿ‹±º#»ç|úfŽQIA’z|4óÃèZ¨üZÊ‚éÜš‹"mÙ (uÞr]d<‡‚Œ¿u-é{ ÿÞYË4Ë£!ês±Gî¸©CtÀ”!#^²­Ù0
¼žÿ‡À#šxaB?’SL	ŠVú²ª÷Ôõo¯Ÿuh·¯Ýý÷ÝCYª<½)ÆÃÇcW=ÖŒ³%L~Ê Q=6Ùœ¯…n2Îéð§qj³äè©‹A›“Ëôÿ~…cxàyL½‰ØÀÍR/¿P•”Ó…µù=È¼¥«+ïú³M ‡@ˆ.ñ¼©jiœ‰—pF­µêÏ§¦´\²<jÉÌæ>²TÅ§F×vò^œ§¹È·è¥ÆvãÂ#d|Ð×·±
ÜæøÄØÖë¾;	~þ•+.ò´®æ÷ëÊZœD01¬UnÌ+¯@Ë=)–sßL¡RÂ©é©EL·Ä©Éß"1˜›Â;RÈ}‹ø‰DìW¸
¼t’j9EšåPá>6„rîšÁ›ß¸”tóÊaëÇŠf½â(«f¥×}vY•@ôqp[D¨LÓfdiZ5¯^÷Íe^IôÈÁ/æKk…ó_D4ši¿A#"âØ¾S@ùÁ(øÜ/)Q‡ýþˆóÃ(Ÿst“ù3f^]¦–ýºn˜‹ý;¤c+évÆnraëgyÖý\Zà?9±
¼
_ÓIÓ0R¤îuž74iIŠózJ•§þCQ„¼ãÄxÿ§ªS?C©AÓ%ÝC${Ê*S`IjÈÖ¼G5IƒøDH;í²'¹Ñ¾¨Ôãr–G	ÞãÑÝî!a¬—y1¶ˆ2IýE*€U)X"Ð~ÊôœDåøP¤ˆÎî³Ba›plý$ï:Ü~eFŠ6ó¡¸ÄÒ$Ù£ï‘EÒ.Êf#Êƒ‰^×”¥b©uPª»F
ð#«ð¶ØÒ:Ë#ï‘òÂ38Pª¼Óúdû ¾Ù*Z-Þãîˆgv‚“hîc.zvùžå$çÑy•öUzR÷Ygo.%¢wMÙþÆ¢æå§ì&ŒÑ‡(£žõ&ÔsòÞ˜ç U>•\ÔöÂsA#‡P‘€B=žŽy.P‘ˆçÂ¿ÿ]•úf$ýYÒMÙÆ:ÚÝ9}0ØÊ«"qêÙæã§ÉaúáòûÁoô3o9š7sÄ'Ý/ø®t×ðÚû^ru*ëm 5ý|ò2˜Þ³B>"8{Mú{¯¹ºVÈ¦ÿå)±’Ë‰E5Râw}T”Sû°µŒ$„æúLÅ]“°øŠ?ChäúŒäêŒ8mòïúLe£YJÆoÝ¥jàOÏßc­N=õb[Ÿ©l4$KÕhÕcá2ÔhpQáåb’
ìÈ‹\]­N<¯˜‡…(Ë™ElFˆ¡âx±rŸ4"6Û/‘««T‰¦9(¯=â
½§aPDý?.åbUÄMöÉÕ•šDî¬‰MDå±<-—3"b3ÿ+_¹/ñÂž3Yêz(¦ñ¼g8…€·4ñÇtyþ€(sWwOËc?1“ŒÏ®»4K©Ð&9"€ú™–Ë‹|òºqž­¨oiŠYÂú»C”aÕÝ‘º«6Œ9ùxËþ·Ô‘í°ÇÈôÝÝ£aµÌ$èÔºKó ”2­pÖÝeoéIVjV'Þ¦WIÅ%‹øTK²R“‘žU&v ¤¦¢.¼‡;Ã¥î¹ Ávw£ÂPÌ¤$Íu-Ÿ,Kw²’¢6‘óœr ˜Øð‚ê÷”\á¥aäjEÏô½ÅLxQÞÃ)c$¡|L¬_û}½4Š"¥H+tš¯)¸8éUpñFW÷_öXWíÜ4z‚>.¶aS½ýß,Œ™D¯Ù¥ÿñ×›pÛ÷3=T­'ƒÕ
4žŽvëWGÃå¥?º7ã¾‹·[/¬MrcG	]ÂóMŸº•»"ç¹IÿÐSÃÙº8‡ž}¬››òõÛ­–R :Î¹áüîk:òÙg¶¤¾‚3Ex«ÐMW­[Þ·ÂÂcµu=Û µXî[ï¿&U+Ít÷Iþ%u7.ì¼ŒDû†~Nµt&+}P(½ÙlÙ£¢RÿÃèÝ/»ÙƒeÇ¹òžuŒ\A£Ë|¸Ñ•ôÇg’!j‘¥óÆá.Ö!—ÉJH¿.ßQÖ8_mÀ”0“ÐôÚOê¥/ï4\ÞŠ¢§fvÙ˜Œ*Eú¹rŸd
yX±š•š¿Nòq%+ÝÎ×¦NrGY‡ý×-ç×UL÷fî,ÓŒÕ_µÄƒW‚˜ºí´†Ï¤Ç];nÍÍŸ•P¶3–]dBIµ*[m½*·†‡ÍhJñ<RÀó¤T&wjnaKR»³Ä+_›Å~!ÁýY=®û—•Sq¿Ñr9|±_yDðÌüb®ûí—h&~eëø×yæö~õmYT„B2”¯¦Õ¤óÛ:½ké@Vªh×|åIOòr0KÔð@<ÿ •¤¯Œº4 ô°‹{Þ³ÉÜóp‹ÿ¿«ÌkEw­Å‡¥äÌ^7wL¿ôØùO]·H˜_Ö¥«%÷J…uÅpµ,ÀR^rÊÑ}:6^ O74Pè²ïáë¨£Ê	¼x90·Í<ÒïÅ¼i–iß.Ò½÷î¥†K{²ÒµP…·XÛ¢ù’^ß‡ÏÚ Bß%‰rÆž	¬»Ñp&ÌVqËŠŸ¿¦Y&|gÍÄª|	LÄÔÛ}£r1ë:ªY]qÿu~!ÿGÜØØ¯>;>.ÄW¡›_˜¦ÿ`¡þ—ÑÙh0Wp$“:-U"õá¥Œn©aº¥-Yéªÿ§`ÒîÕÇm™õO»ôg"ûF•ø‡0ÅzÞ“¤šWžÛø
óF–T×¯¶×ØÑ&¹°Ì-4©¼º9‘ž.îÏZPßH ÔSwK¯AîrXË?·œlél…¤{`¶(‰MRMç?š·œQé‡…]iàóðÓîmá6Z„TKkòkÓS÷IùdÙ-ãQÖ’êºã”PX-ŒTb¾Êké>ÄÑy_;:/0±ù¨•D§¬	Öf£=wp	ûLj^,o>¯kæxPw®½–Lä'³_ˆÜ÷î‚­iÙMk»Ð¡ÿqèÌÙ­D<{PV»cB‘’QÕÝ/§„vV+¤—}²8©—=Š\ÙªoØÈ|‘ëÖÔùØ—³¨_êø)¨ûCö<šaG^ÑÄlÜ$ÖefŽÀ¶*¹iÝ_rÀ^ñ‡Dá09&Ò¼[›ESPDOÓuüÂ¤c*p"‹b"u›X:ót?êªO«[{6’ñ!w¡Üa¥Ù#uwÖe–þ˜lZP3¸VKðœœÓ×2mH§pƒµ‰3ðHš:áÊ½±¦ >1žÂÂ²ôó±†œó<¨BI‚¶îâq/ÊSüWj¿ÄŽ¢œ®rûðÇœÆœËÜÓ)%—å)ù°çê°AAuÕzÛ€HA$‹˜‹Iˆ1ùuc²“Åi±[ÒHXÃÒìµ¯n¬Ó(Ç€’8 Ö=íÅÏ_=9]×Òôµo§þ“~ 1®þvOh{igD¢©‡»D¦gTÇðÔŸÔJ\s¦~k,'lškáæÏ^‹E1‡”šgIc»ï_ëèjƒNy^Ë’Å~ÍÆ™_]D:¼s¿ÙVÞ^×ñ'(åŠÐòæûË}‡0	r·´}eÐuüZü«¥Ýä£gkûÛ66m.”žDZâƒ¥Í8cÁýÀ˜Ë!@::ëé²xÙ-¥4#‹‘T2]X–Ì®[°_ÕT;:P˜m¦|~á2«rX»}ÁÁQÕ0Ô?Êêš¿å\˜½¿¤ðŸ{¸WÈù«UƒAÚn^]^¹-Ø€Ôm þ

‹s9W—Ç;ô”\ºòÕÃ/•tˆÕÖ‰,rè›„¿S3¼2Wò²ýÇ@ažð9"±´nò‚œ„ ×	ßPx"._ê(Ç_9±íô¢=³D©N/üóUâƒÙ©êŸÙ&Zf>w!¿êêjßŒÐ¨šç~Žóißš^P’zþOŠüÄy  ŽYXZ¼’m¼_cqß©­íB×©/qŠ¤ÉôÇ¼üB{¶¨š•°Öq%qî;ˆ¨AN¢)`×˜C®Æø³ëÞûf¾—ïy4ÜhO~=–;©jè³
‰*,Ë}ÏE‡) (ÌÍÈaÒ¤{jˆ
ú^Ý¹iÔüëÈE©XÓ6~#J×v|zÑÈùrÓíöM‹²ËÈe‰ƒ“¹÷åø}üì¿Zºn‡¥ÀÆ,t,Í_™7þ¡‡¿ÝwD»N“œ™H1…ÙÉ9îºíþ©ã3´Ç•^‘äFòëúÎDcÓºm«×bÝ&Cìo›‚ÂêØ¯AJÂÜ×§£jü²\*×S&›ùmH7 Ô^wËáœÖÃ¨škÙË3•+= Ãj@J’¶>í®®nª°m5ªZÝh6˜2Ó¶)öŒ‘Y˜‘öÖB÷ºÕu…pš‘Ÿk)’ã
àWE~³¿Ýæô[[i<D¦ÜcEšŸ_íK>•v%:Í.éËëÿÏÍ½6ß]ø(Ü£ . «B¡¨×juÔËïó×µ¼Új+TIôHÁ—æW^;pòOŒó7t •	°¤¼\Ò Ü~¤ëªqÙÑnÍEŽV#µÓb¼ƒ¿_Ï	-µûîs—2 lGRõÊKº-Ï×ØÖ%ÙM“VÍä¶¿qo6×}óé˜ÖCÚ4bhÆÜçð˜‰ížÌµûÂ(6½îA%lsZ2ß’¦Ž&Þðú•N]`aÌ¿(’«‚L)«%Bjm+ä'ÛÿŽ!¨HîbIB˜ÏµzâàŸ iè@ ôª:"2Ì=BDÓ¿SŒ¼,¥f¦äGe¶ú\žÕÍaDUÙ¬&“ýá;ÓA‚2¡[j§ÿˆ)]ºßHŸ7¯’H›BQ9Ž­HEõèŒ-rÊdMÔñjÀWÍm‘
Åÿ&
ÚünbÛFÏdÍÌ~öýûõ1äþ™ÆëÊpAd!V#8¤e‹l[mýïðTTÓ:§&¸kXÿœ8çZSÊ_,¹FcÆúÇ·qæ!CêT
ðT#«Ó×áei—/Å3ãÜzÿ/ÞÔ$É¤JA©Ôì­—W:­ÖÕú¼È•>èú‚5ÚºŸBøÁ”Vk2Ã<½û¦¥Gý¢©;
’¦µZ
¢šV`èÀM'ÚŒô^ÅÇ¢§~µ~AúEe`—:°þr£Må#W½äVÑè«W×!eû¹~lF&	ë•¯Aâ£Ì†jgjœ¿<©¼?Šsaò¸Ï<³tDùžt-Êwh5êg}ÞJÈ„};¡ºÔ|Œ¤¬§VÓc¸0„GlQŽ¯ºé¯ª=¯	xÌß»ÁI”Ž€T†c‚—ŒÇ#µï¥loyÝÈ<¡ÎTÞ0¢¬ÓßNëÃ~ØNnXƒ—º¼d‹Rö·XzÖÒ©Ó"lÏòèe°y¯;Mæ`àµä«™òÚAdf‘>'ðàµr»sÀ|†¬šAFçD¥žþ6'F9j)~Ô¢Ôit-\wVµ/êÊåm™¼ÙÅøŒW¸7È'<Ní`¢¢¦3‚þà£šV¥V[G”ÂÜ†? Ã,à³(éÕä8êÖœÊÅgI’)ˆ2áé^½šC};îÛkõÞ©»º!ÕÊÚ¾,­âÜš%¡öƒ|!y¥nYô¬¾Ôl´®ûöV9 ¦úYm¸¥Ë[M‚c.ÉNÈ¡4 w`¤ùíí6aW“R§	.]âÆôš%k·]©œ?·:š×7g3ÄAoíêF¸2a;^îÀºÀ#¡-sƒ€æL¥ s¸÷ü÷’µÚšàO¼5-º©®Ý~ðÔ&y1Ì"$é}iU9EÓ 3j{†9Qæóq¾ò¿þËŠ,™W97˜Ê	¤TÂ¼F™ÂŸÒÅ8$«vnè¥~.Il€¤²lå–{•Âm?m{¾ˆnm{Àg˜ÈrÆÈÉI¡ì{ÁrzqWÔªÁò@–IûîÀøv÷§ .y>+O»…n#ÝpÝ"T¾f]DaæÖË««ú²iß†ïÄîCâ'€)¢¢¤Ó©Só‰åïæÍ¼Ÿ\DfxeX¬‚÷ß‡Ú÷º,»ÎVj÷*/\°éCç£k„—l¤fäÇŒ^c€­%¿QN•¦D,LšÄtÞ~à&ðE²È¼Wa´/ Ö~>c£Iu\HÄ9ÍNùbÖœÆÊ)±úŽò›¢¥&9Â‘ë\ô´–ø‹ÍÅ›®sF7×ß¸&y)G‚­\€R!ê'uëM/¤)|­úNÕú|Dâ|_–š;P)ž”tsP’VÇå˜ì|F²LiN}'¡ñÉÂÒ8òF¥^.­Èn+öPÔ†^qbÉ^ü‡T¯<Å¤ÛüµÐ„—QÖ…æ½÷*p09ÓK4ýê¶ÓËÁò¥lÚßÐ^Zåß…",ÍÜ"­­Œà*ÒW¦T\lóÔ‚¿nr@ÈùœÑ…¸’yf§1Y—Âì{I&\>ëÞ2\­Øøt;7O¶^rôY?þØ6é]åk3<–kßÞÂ7Ä°ÊJof¡h›ÊÚnžü
­®Ty¢Þî*[â|å²¼;t˜Íª0=
i÷p™»›\¢Î:;ÔÕdQº3]˜ÊS”aPG)ÜÞj.¿&PjõZ?Îc—©Ôf|la,÷Íj.ç1VÆ½é¿dùž_M±¼ÞôÂä»¹1¹/"'áÇ†ðJ”“áªµÐvÑG­‚4µ…eXž X.@HÂnqÓ¯ž³¥ÆRzþÛÎziW`]}£cNäÐ×/«¾Ä£hþK’§ò™þ¯Åô*è³lƒUyÂ°‰šJNõ¶Ckm¾Þ“ÐÍºŽ”ú›êž¯Ã‘…s3¿Oleöï›Ñ³q°¸Í
ƒ1“U6BõÖVÝ]“R‹ŽO¯÷)„4äÎG–(¡‡™Í}@„jÙÛÁ÷~WÛˆš_¢ePÔ4ž„ªø!	‹ÈB‡EýAn­‚—_ŸÖ(G®·žŽñ¸¨êÇÇù¨9„üþw•!NŒ>þ"åJn±gÆ*Õ›œM2ñ‘kü™¯1°\3©^ð÷?¯éV–ÔÈŽj“
 ø>ýBÊãØz•=îªr.Ž[Ã‘N8|WÎ™©UŒ:´+ˆšÍDQ;Û“„cls­árŒ§<•—SI!Î˜‹BüâNAÞ´xdZY $™ò#äN “$ä„8û^Tµ¸Æ5¿¯^íUd"-N`÷ÁÏ:Ó8Mf†pÁÈ–]ÓÀ	z•w¬ÜyÙ|A¡£i!å¹œ‡d‰s>zjiHžÉ…èXS‚··¿¿v‡Õ¥Ô~ŸkéAÅyÅéÇFHÙ4Çxk{ÄuÙ´ê¹èßªããÒ“_Õû–²Íüf*¢Br‘·óŠï“¬ÕÂåUe†d½Q}|&Š5-ìúkgµr
gk·’Ó¾o‡ØëOpÊå ÃäU%åWCîN~…j„©^›PâÙ±&¢‰0.Ó8™£¦¬ª@˜…×¿-v{u¹Àúúót”ÑŒZÏHaþWÖHëUOš32	ßP2Ù˜ßk7¶•,¡N\æ™ÞGÀ´ïéðâ¸dŽS±Ûë€k‰µžjŸ¨X‡$KC@ÖÛØ^ÏJ‚»Úm4 Àºr­À¢§úF­x“%?ËÞÞœOèxf¥¦ƒ
Q–3jÄ…B§5ŽË¢&j	æN×_Ð©—­!ÃÌ|‰ˆœ’ƒ®*Å/òpB.®œ’øçÏ5ËœÛØRãñ5Ñ!´Z»‡¼·Í-ûùÜ eŽ‰w“HÂc”•l‹\®Ž”ZÒ¯ý¢ªg†ý­Ùù³Y“Ä;¿þ]íº»4¥Ú>^˜o2nŒ"Z!¥²6(ªô¯\ã{€JönëÕ—•«w¬‡„“–¦ÔÚ'ÿ¡å#¤¨ƒ”€?Ûõ‰É=¶L=;ä}ÚADMé™ï?¿ó«€TÙYÚV#ŒFÛ5­’Ášú¸­†ÁSø$ìÓN'ç‘"Ü']¼)„¾%'ã¦tý¼Q4Šï˜f¯ˆ‚ËqÔÊ‡ÀYdžÙe”9 ®Q1aÎy¾9µÂ!(©PC83—+tÜ\QÞ” MuÒÔ"¦ Êru¦ÐÜE‘Õ%ÓVDzg¥ÐKpË<’DvÙœÙ~
ö±Ÿ£Žª\˜Ÿ?QÓ“ãèÐ‹§Äý³\éËR;s…y•C¹²_z9·Â8H¾t Ó5½di»ž=o«és[úÊƒ¼:„*K·ç0/‚~{/aé!¡ÙgP¼•YØ¼@½=ZâÞñÝ7òƒ/%âš‹SÚçƒ¥ö‰e+è?”-¬bG>îŠéžÄŒž¿ ¼Ó«®é–º¹˜y›¥ùÈý óJX§A—ÄÜÒìñ—ofj%¥mjô(m+¹šŒ_õÉ~±îlâRK«6÷á $ÉY˜ˆyxå-BÕ½w¢o_¤œoçb5Bùà—×:z/#²rHÆ½>×Z³N9ÌÓ±FB!LJÍ®óÂnÃ)ÒíôŽ£èš*2û„tdLëY“}#1¹V8š)Ö[e=Êlfr=
5J9Ô*jrË%™‡äË©rÁ´HgkÜÙ‘ßjË%£¥}‘¾«ü>Ò|ÎÇG¬Ò#WjÞ-"ÎûÙ-º×p£E¸ƒ%“¹î¤ò¦«¥½‚ŽSd¤¥’ÆyÄ:u˜‡²=j1+°jh9çÔ`½5D‡
Fj4Ô¾¸ÿfrÊ´þÆÿðIa ³ÖÝ{ße-ôlûpø
œš=ê£â%Òãíˆ~DÀ¶=ý»ºí?Äó¸Í<.õrÊœÙh—QoÁŒ4ö*C¬Ó`•{l·~DÚûgK¼!Gì½“å®ªY#"ùµãÞèá@œkG„À¯™wlf¿*Ò*Ühýð:Okƒ¦ÕˆwCê˜¥Úõ4KH½XX|°Qä‡†E¬÷Þ1‘<¹ØFÅ6©} ¤š¯’¢òC9M—’ÜqØ«¨ž5#2¥Z=éýùelšµ]>ž$÷BöBÅCn;†U#pK-æ†auß$ÛÑÍd4û²û'Ýgð„²¡sƒ{¬ºuxÊêIïˆä(G¨ñO¢wr_¼ÅÅ°ŒK2õÄx°bØ“í0[Qýþ‚÷_ñÕŸìÆîg“Ùú+ø,«ª‰Îz¨ÔkL±æCFúÎ¾ñÌhñB$aªebÏ"Ýz³@_)}¬Raû’0Q6-Ò½àýxÃ+5’)$y†ksvñ«À:p|Zr=¾5ò	oûÊ/'óUI´(­jìó½”úaà~xØ‘À¶Då%ëgÉ»‡òn‹p¢9R¢Å×Š:­š3‹Gqø(«µ?Žìuw]pÇ|Zf¼«×Ñ(ªDN*YÆç:Å.×'cUwH6¬„Ïzµ (Ö}(x¨O¿~ýŒšgpóä\ÃØ‰<7’“!ûÌ1ãT|I(ÙÔožºqØ¡¨þïŒw•Ï	¥émykrˆ%ÔÊ}¦»ˆ:}ÄŽlì|ìÜkã±€8´ªìäœ×Cé™Ù÷ºd´îJºB]dLÕÎ¡<‘Dj}ÔaG9/¡ÀºÊÞØg:>Iý‹,ôÉˆûFf†is¢<ß-¾“÷^Ëžwb’æÜÖà©‘õ¶nH@*3ßª™c.’óBÛnÆÄwµÀ¦­¼%ÛT	E\*’&5ßx[Ä‰òêŒôúaCÚ«ÝR§úX‚ðŽ\šý-	oñ½&200]b2ŒØ’p13dA.Vñ1CŸÁï0F"ë:ü·K¦ÔˆŸ„Kð}Æ7|)ŠQÕ¡_äVsÉšpäþ8BjrÊÿ°
Œg®/%'€2î2@†æòíxÆÄÿÁ}‹/Èæ³¤ú|u¢®Ä¢aÛäPoÂ{…|Ï\ÌOüvNåjkz¯ÁU¹´Èì
\6…©à°ªÁ_ÀÚ¯òcÏâÅ8a#‚‚El|¡fNñ•è¾,¡âšúþ[<ûÌ‚lÊ]¤Ë¢¿³Õ#%t~oCiáîaÔ•þw€@jP¸JþÊ%Éc“(*1‘cH`ú°¡ðñÐÈ™Ñ‘Ÿþ=}»Š-w^ø¾œdžSÁ‡Ä&!oçP`¥2­Iúµ4·H¿»ùÎK‡eò!øB™i­>á+riÝriÑR„KWÆýt1rerj¾] Hm®­õYúEšZ"16èwõß-ìÇ”WBîñIc-nIg›˜+šÁ?e›[¡mG$²6-{äT6kÖ
Œ¶þˆè~)@®K‡ýK¡PÚ:ÈcŠ-\FxN¹êãóƒ¥`áEŸèr[¨X 	öÈ+¥‚å+>*¨Y¿æGYÙzJª©µÊÆÑ8ãƒ‘û,„W„9¦°ã cåS_‹¥ÛÓG>¿1MþŒNÕû’Dá»oÝì+„j¸w¹b™5×3ëÍ/Ž¯à("|8{X•kÖQ}_.*rQcr<ùÉ±¡¢Ô{Tö>6guµ¹/Ûê¬;™óöÇÈ³—Ñ­kâ¬áø»­3s(›©Ñ’g˜oÉ˜æRÚqÙH-ùõÃ²²ÖÏc·GGžÆ˜ÝÐ·•Ýv3qÛùÌîìVXRâ[e$2ìMü!›Ìt+›"\…‘p^”OýùX‡×:º'¨¢/ß	VÑ`±±N]ºJ}Ûùö.dK zV‰¡>OÈì>B(¤- ¦fá“ë0,é6žp
¼1±&kì-|.fÃH¸M¥¯å-"ÌÚeäôC<$o¿ö¬
µ«˜,w4æ™šS5™™ð}—¼fÍOÅxjŽ¯ÜðNó!‘»ÌWÙãIÆqHÓVµö-7ÌÝúì£!euƒ¬Ï¶KJøÄ[”r­<+dåÒ¬?o¡”˜Ï/¨Ò³+ vºmúO$	¢Ü@”3©©çç"¾¼L°ô›¨dÓºüëøþvúÀOq¸X˜	5f{*¶.s!µÖYÓLfL§©÷„ß&MiâUVƒ»B•*ò6ÇÂ4Á¾JŠç°L’Y]Ü°v)‰µ-*n+â‹£é†Ià‘/Þ2”#ŸåQxW9}ôâ®2©åÞ»ÐþøFÎÇ-;‘˜±å3/3©Ù‘†¤+”høj=™È°ji(]="verde"
        self.aux.caracteristics["alas"]="negras"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/colibri_pico_ancho.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Zafiro oreja blanca"
        self.aux.description="Adulto: Macho: Ojos negros, pico rojo con la punta negra. LÃ­nea ocular blanca (muy conspicua), resto de la cabeza y gorja morado iridiscentes (aparentemente negras). Lados y flancos verdes; vientre y cobertoras inferiores de la cola blanquecinas. Espalda y cobertoras alares verdes. Cola redondeada oscura. Hembra: Parecida al macho adulto pero con frente grisÃ¡cea, zona malar blanca, nuca verde, vientre grisÃ¡ceo, punta de rectrices exteriores blancas y garganta, pecho, flancos y lados blanquecinos con filas de motas verdes. Juvenil: Parecido a la hembra adulta pero con tonos mÃ¡s opacos y deslavados."
        self.aux.habitat="claros y bordes de bosques montaÃ±osos (e.g., pino, pino-encino, encino) cercanos a arroyos. Sitios de posible observaciÃ³n en el bosque: claros en Ã¡reas de pino y eucalipto, vegetaciÃ³n secundaria nativa y vegetaciÃ³n circundante a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de nÃ©ctar floral y en ocasiones consume insectos pequeÃ±os y araÃ±as. Dado que el zafiro oreja blanca no es muy afÃ­n a los ecosistemas urbanos, cuando entra a ellos prefiere Ã¡reas con niveles bajos de perturbaciÃ³n, por lo que no se observa fuera de suburbios, parques y relictos de vegetaciÃ³n nativa."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="rojo"
        self.aux.caracteristics["pecho"]="verde"
        self.aux.caracteristics["vientre"]="verde"
        self.aux.caracteristics["espalda"]="morada"
        self.aux.caracteristics["alas"]="negras"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/zafiro_oreja_blanca.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="ColibrÃ­ berilo"
        self.aux.description="Adulto: Macho: Ojos negros, pico rojo con la punta negra. LÃ­nea ocular blanca (generalmente inconspicua), resto de la cabeza verde oscuro iridiscente. Flancos, lados y vientre grisÃ¡ceos. Espalda verde; rabadilla y cobertoras superiores de la cola cafÃ©-canela. Alas cafÃ© rojizo. Cola cuadrada (levemente emarginada) rojiza. Hembra: Parecida al macho adulto pero con coloraciÃ³n general verde opaca (no iridiscente). Juvenil: Parecido a la hembra adulta pero con vientre blanquecino y coloraciÃ³n general mÃ¡s clara."
        self.aux.habitat="Ecotonos y claros de bosques montaÃ±osos (principalmente encino) y sembradÃ­os tropicales. Sitios de posible observaciÃ³n en el bosque: Ã¡reas arboladas con sotobosque en floraciÃ³n y vegetaciÃ³n circundante a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de nÃ©ctar floral, en ocasiones consume insectos y rara vez pequeÃ±as araÃ±as. El colibrÃ­ berilo es uno de los colibrÃ­es endÃ©micos de MÃ©xico y Centro AmÃ©rica. Sin embargo, existen registros ocasionales en el Sur de Arizona y Suroeste de Texas (EUA)."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="rojo"
        self.aux.caracteristics["pecho"]="verde"
        self.aux.caracteristics["vientre"]="gris"
        self.aux.caracteristics["espalda"]="morada"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/colibri_berilo.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="ColibrÃ­ corona violeta"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico rojo con la punta negra. Corona violeta. Garganta, pecho y vientre blancos, lados y flancos verde claro. Nuca, espalda y cobertoras del ala verde olivo. Alas oscuras. Cola emarginada verde olivo. Juvenil: Parecido al adulto pero con corona verde (en ocasiones con violeta claro en la frente)."
        self.aux.habitat="Matorrales, bosques, vegetaciÃ³n riparia y Ã¡reas semiabiertas. Sitios de posible observaciÃ³n en el bosque: prÃ¡cticamente en cualquier sitio del bosque con plantas en floraciÃ³n y sitios cercanos a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de nÃ©ctar floral, en ocasiones consume insectos y rara vez pequeÃ±as araÃ±as. Dadas las preferencias de hÃ¡bitat del colibrÃ­ corona violeta, es comÃºn observarlo cercano a cuerpos de agua."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="rojo"
        self.aux.caracteristics["corona"]="violeta"
        self.aux.caracteristics["pecho"]="blanco"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="verde"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="verde"
        self.aux.image="sources/colibri_corona_violeta.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Momoto corona cafÃ©"
        self.aux.description="Adulto: (sexos similares) Ojos cafÃ©s, pico largo y punteado negro. Corona rojiza, mÃ¡scara negra rodeada por plumas azules y/o moradas. Pecho verde con mota central negra, vientre verde amarillento. Alas azul-verde. Cola verde (en ocasiones con tonalidades azules) con dos raquetas terminales (base azul-verde y punta negra). Juvenil: Parecido al adulto pero con coloraciÃ³n general menos intensa."
        self.aux.habitat="Bosques y matorrales. Sitios de posible observaciÃ³n en el bosque: Ã¡reas boscosas (e.g., pino, eucalipto, casuarina), caÃ±adas con vegetaciÃ³n secundaria nativa y vegetaciÃ³n aledaÃ±a a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de frutos e insectos. El momoto corona cafÃ© es una de las aves mÃ¡s coloridas y vistosas del Bosque Los Colomos. Debido al movimiento pendular de su cola larga, tambiÃ©n recibe el nombre de pÃ¡jaro reloj, o simplemente pÃ©ndulo."
        self.aux.caracteristics["ojos"]="cafe"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["corona"]="cafe"
        self.aux.caracteristics["pecho"]="verde"
        self.aux.caracteristics["vientre"]="verde"
        self.aux.caracteristics["alas"]="Azul-verde"
        self.aux.caracteristics["cola"]="verde"
        self.aux.image="sources/momoto_corona_cafe.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="MartÃ­n pescador norteÃ±o"
        self.aux.description="Adulto: Macho: Ojos negros, pico negro con base gris. Marca loral blanca, resto de la cabeza azul con copete prominente. Collar blanco, franja pectoral azul con motas rojizas (inconspicuas generalmente), pecho y vientre blancos, flancos azules. Espalda, rabadilla y cobertoras superiores de la cola azules. Alas azules con motas blancas. Cola azul con rectrices exteriores barradas de blanco y negro. Hembra: Parecida al macho adulto pero con franja pectoral azul (con parches rojizos), una franja pectoral inferior rojiza, y lados y flancos rojizos. Juvenil: Parecido a la hembra adulta pero sin franja pectoral inferior."
        self.aux.habitat="PrÃ¡cticamente en cualquier cuerpo de agua (e.g., rÃ­os, lagos, pantanos, estuarios, bahÃ­as). Sitios de posible observaciÃ³n en el bosque: Ãºnicamente registrado en el Estanque de los patos."
        self.aux.comments="Se alimenta bÃ¡sicamente de peces y ocasionalmente consume cangrejos, ranas, mamÃ­feros pequeÃ±os, aves pequeÃ±as, lagartijas y frutos. DespuÃ©s del martÃ­n-pescador de collar (Megaceryle torquata), el martÃ­n pescador norteÃ±o es el martÃ­n pescador mÃ¡s grande del paÃ­s."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["pecho"]="blanco"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="azul"
        self.aux.caracteristics["alas"]="azul"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/martin_pescador.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Carpintero del desierto"
        self.aux.description="Adulto: Macho: Ojos negros, pico gris oscuro (aparentemente negro). Corona roja, resto de la cabeza cafÃ©-gris claro. Pecho cafÃ©-gris claro, vientre amarillento, cobertoras inferiores de la cola barradas de blanco y negro. Espalda, rabadilla y alas barradas de blanco y negro. Cola negra con rectrices centrales y exteriores barradas de negro y blanco. Al vuelo exhibe parche blanquecino en la base de primarias. Hembra: Parecida al macho adulto pero sin corona roja. Juvenil: Parecido a la hembra adulta pero con el pico mÃ¡s corto"
        self.aux.habitat="Zonas Ã¡ridas a semihÃºmedas (e.g., matorrales xerÃ³fitos, plantaciones). Sitios de posible observaciÃ³n en el bosque: principalmente eucaliptales, no obstante se puede observar en cualquier arbolado del bosque."
        self.aux.comments="Se alimenta de insectos, frutos, semillas y nÃ©ctar floral. Durante la Ã©poca reproductiva emite vocalizaciones fuertes y el cinceleo contra los Ã¡rboles es mucho mÃ¡s frecuente. Al igual que la mayorÃ­a de los pÃ¡jaros carpinteros, el carpintero del desierto anida en cavidades"
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["corona"]="rojo"
        self.aux.caracteristics["pecho"]="cafe"
        self.aux.caracteristics["vientre"]="amarillo"
        self.aux.caracteristics["espalda"]="blanco negro"
        self.aux.caracteristics["alas"]="blanco negro"
        self.aux.caracteristics["cola"]="blanco negro"
        self.aux.image="sources/carpintero_del_desierto.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Chupasavia maculado"
        self.aux.description="Adulto: Macho: Ojos negros, pico gris oscuro. Corona roja con borde negro, lÃ­nea superciliar blanca, lÃ­nea ocular negra, franja blanca de la frente a la nuca (unida a franja pectoral levemente amarillenta). Garganta roja con borde negro, vientre y cobertoras inferiores de la cola blancas jaspeadas de negro. Espalda barrada de blanco y negro. Alas negras con banda vertical blanca, plumas primarias barradas levemente de negro y blanco. Cola negra con rectrices centrales blancas barradas con negro. Hembra: Parecida al macho adulto pero con garganta blanca y con coloraciÃ³n amarillenta en pecho, cuello, nuca y espalda. Juvenil: Con mismos caracteres que los adultos pero con coloraciÃ³n general cafÃ© amarillento claro."
        self.aux.habitat="Bosques de encino-pino, bordes de arbolados y huertos. Sitios de posible observaciÃ³n en el bosque: solamente registrado en Ã¡reas de casuarina y pino ubicadas al Norte del Estanque de los patos."
        self.aux.comments="Se alimenta de savia, insectos y frutos. Por su hÃ¡bito alimenticio, el chupasavia maculado deja anillos de perforaciones en los Ã¡rboles, elemento con el cual se puede inferir su presencia (en algunos casos). Este chupasavia es silencioso en comparaciÃ³n con los demÃ¡s pÃ¡jaros carpinteros, por lo que en ocasiones puede pasar desapercibido."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="blanco negro"
        self.aux.caracteristics["alas"]="blanco negro"
        self.aux.caracteristics["cola"]="negro"
        self.aux.image="sources/chupasavia_maculado.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Mosquero copetÃ³n"
        self.aux.description="Adulto: (sexos similares) Ojos negros, maxila negra, mandÃ­bula rosÃ¡cea. Anillo ocular blanco proyectado hacia el dorso, cabeza cafÃ© rojiza con copete prominente. Cara, garganta y pecho cafÃ©-canela, vientre amarillo-canela. Nuca y espalda cafÃ©-olivo. Alas cafÃ© oscuro con dos barras alares blanquecinas y borde de secundarias y terciarias amarillo-canela. Cola cafÃ©. Juvenil: Parecido al adulto pero con coloraciÃ³n general mÃ¡s pÃ¡lida y con barras alares mÃ¡s anchas"
        self.aux.habitat="Bosques de niebla, de pino, pino-encino, encino y Ã¡reas semiÃ¡ridas abiertas. Sitios de posible observaciÃ³n en el bosque: Ã¡reas con arbolados densos (e.g., zonas de eucalipto, pino y/o casuarina)."
        self.aux.comments="Se alimenta principalmente de insectos. ComÃºnmente se posa en perchas visibles. En caso de estar alarmado, su comportamiento se torna inquieto, mueve incesantemente la cola y eleva aÃºn mÃ¡s su copete."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="cafe"
        self.aux.caracteristics["pecho"]="cafe-canela"
        self.aux.caracteristics["vientre"]="amarillo-canela"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="cafe"
        self.aux.image="sources/mosquero_copeton.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="PibÃ­ TengofrÃ­o"
        self.aux.description="Adulto: (Sexos similares) Ojos negros, maxila negra, mandÃ­bula rosÃ¡cea. Anillo ocular blanquecino, loras gris claro, resto de la cabeza gris oscuro con copete prominente. Garganta y pecho gris claro, vientre amarillo deslavado. Alas oscuras con dos barras alares grises. Escapulares gris claro. Cola gris. Juvenil: Parecido al adulto pero con cobertoras inferiores de la cola y vientre amarillo claros; barras alares cafÃ© claro."
        self.aux.habitat="Bosques de pino, pino-encino y encino. Sitios de posible observaciÃ³n en el bosque: PrÃ¡cticamente en cualquier Ã¡rea del bosque."
        self.aux.comments="Se alimenta principalmente de insectos. Al igual que la mayorÃ­a de los tirÃ¡nidos, este pibÃ­ se posa en perchas visibles y las utiliza como sitio base para acechar a los insectos que caza al vuelo."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="cafe"
        self.aux.caracteristics["pecho"]="gris"
        self.aux.caracteristics["vientre"]="amarillo"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="cafe"
        self.aux.image="sources/pibi_tengofrio.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Mosquero mÃ­nimo"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico negro con la base de la mandÃ­bula amarillo-anaranjada. Anillo ocular y loras blancas, resto de la cabeza gris-cafÃ©. Garganta y vientre blancos, pecho gris-cafÃ© claro. Espalda y rabadilla grises. Alas negras con dos barras alares blancas; secundarias y terciarias con borde blanquecino. Cola emarginada gris. Juvenil: Parecido al adulto pero con toda la mandÃ­bula inferior amarillo-anaranjada, dos barras alares cafÃ© claro y vientre amarillo deslavado."
        self.aux.habitat="Bosques, pastizales y borde de caminos rurales. Sitios de posible observaciÃ³n en el bosque: prÃ¡cticamente en cualquier Ã¡rea del bosque con excepciÃ³n de Ã¡reas altamente frecuentadas por los usuarios del bosque y/o no arboladas."
        self.aux.comments="Se alimenta principalmente de insectos y araÃ±as, ocasionalmente consume frutos. Debido a que algunas especies del gÃ©nero Empidonax son prÃ¡cticamente indistinguibles entre sÃ­, se recomienda identificarlos hasta nivel de gÃ©nero. No obstante, el canto es una de sus marcas de campo mÃ¡s confiables. El canto del mosquero mÃ­nimo es un psÃ­ metÃ¡lico constante en grupos de 4 a 9 emisiones por vocalizaciÃ³n (nÃºmero de repeticiones variable)."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["pecho"]="gris cafe"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="gris"
        self.aux.caracteristics["alas"]="negro"
        self.aux.caracteristics["cola"]="gris"
        self.aux.image="sources/mosquetero_minimo.jpg"
        self.aves.append(self.aux)

        #self.aves.append(self.aux)

    #*************************************************************
    def load_conejos(self2):
        self2.default_conejo.name="Desconocida"
        self2.default_conejo.image="sources/default.jpeg"
        
        self2.aux=conejo()
        self2.aux.name="Garceta pie dorado"
        self2.aux.description="Adulto: (sexos similares) Ojos amarillos, pico negro. Loras amarillas (en ocasiones anaranjadas). Cuerpo blanco. Tarsos negros, patas amarillas. Juvenil: Parecido al adulto pero con pico negro (o amarillo con la punta negra), patas y tarsos amarillos (en ocasiones verde amarillento)."
        self2.aux.habitat="PrÃ¡cticamente cualquier hÃ¡bitat acuÃ¡tico (e.g., lagos, pantanos, charcas, playas y manglares). Sitios de posible observaciÃ³n en el bosque: comÃºnmente sobrevuela el bosque al amanecer en direcciÃ³n Suroeste-Noreste."
        self2.aux.comments="Se alimenta principalmente de peces, insectos y crustÃ¡ceos. Ocasionalmente consume caracoles, ranas, lagartijas y pequeÃ±os roedores. Anteriormente, en los 1800s, sus plumas eran utilizadas para decorar sombreros, razÃ³n por la cual sus poblaciones decayeron. Afortunadamente, en la actualidad ya no es utilizada con ese fin y sus poblaciones han vuelto a la normalidad."
        self2.aux.caracteristics["ojos"]="amarillo"
        self2.aux.caracteristics["pico"]="negro"
        self2.aux.caracteristics["loras"]="amarillo"
        self2.aux.caracteristics["cuerpo"]="blanco"
        self2.aux.caracteristics["tarsos"]="negro"
        self2.aux.image="sources/garceta_pie_dorado.jpg"
        self2.conejos.append(self2.aux)
    #*************************************************************

    def question(self,q,opt):
        options=[]
        options.append("Otro")
        for key in opt.keys():
            options.append(key)
        self.selection=StringVar()
        self.chooses=StringVar()
        self.chooses.set("Otro")
        self.instructions=Label(self.frame1,text="Seleccione el color de las siguientes partes del ave:\n\n",background='#353437',fg="white")
        self.instructions.configure(font=("Arial",25))
        self.instructions.pack()
        # self.image=ImageTk.PhotoImage(Image.open("bird_main_menu.png"))
        # self.panel=Label(self.frame1,image=self.image)
        # self.panel.pack(side="bottom",fill="both",expand="yes")
        self.caracteristica=Label(self.frame1,text=q,background='#353437',fg="white")
        self.caracteristica.configure(font=("Arial",25))
        self.caracteristica.pack()
        self.drop=OptionMenu(self.frame1,self.chooses,*options)
        self.drop.config(height=1,width=20)
        self.drop.pack()
        self.button=Button(self.frame1,text="Siguiente",command=self.clicked,bg="#7a7b7c",fg="white")
        self.button.config(height=2,width=10)
        self.button.pack()
        self.button.wait_variable(self.selection)
        self.cont = 0
        self.listo = False
        # self.panel.pack_forget()
        self.instructions.pack_forget()
        self.drop.pack_forget()
       # self.panel.pack_forget()
        self.button.pack_forget()
        self.caracteristica.pack_forget()
        return self.selection
        
    def clicked(self):
        print(self.chooses.get())
        self.selection.set(self.chooses.get())

    #****************************************************************
    def question(self2,q,opt):
        options=[]
        options.append("Otro")
        for key in opt.keys():
            options.append(key)
        self2.selection=StringVar()
        self2.chooses=StringVar()
        self2.chooses.set("Otro")
        self2.instructions=Label(self2.frame1,text="Seleccione el color de las siguientes partes del ave:\n\n",background='#353437',fg="white")
        self2.instructions.configure(font=("Arial",25))
        self2.instructions.pack()
        # self.image=ImageTk.PhotoImage(Image.open("bird_main_menu.png"))
        # self.panel=Label(self.frame1,image=self.image)
        # self.panel.pack(side="bottom",fill="both",expand="yes")
        self2.caracteristica=Label(self2.frame1,text=q,background='#353437',fg="white")
        self2.caracteristica.configure(font=("Arial",25))
        self2.caracteristica.pack()
        self2.drop=OptionMenu(self2.frame1,self2.chooses,*options)
        self2.drop.config(height=1,width=20)
        self2.drop.pack()
        self2.button=Button(self2.frame1,text="Siguiente",command=self2.clicked,bg="#7a7b7c",fg="white")
        self2.button.config(height=2,width=10)
        self2.button.pack()
        self2.button.wait_variable(self2.selection)
        self2.cont = 0
        self2.listo = False
        # self.panel.pack_forget()
        self2.instructions.pack_forget()
        self2.drop.pack_forget()
       # self.panel.pack_forget()
        self2.button.pack_forget()
        self2.caracteristica.pack_forget()
        return self2.selection
        
    def clicked(self2):
        print(self2.chooses.get())
        self2.selection.set(self2.chooses.get())

    #***************************************************************************


    def clasify(self):
        #self.load_birds()
        self.loadall()
        self.possible_aves=copy.copy(self.aves)
        self.possible_rules={}
        self.rules={}
        other=True
        while(other):
            self.possible_rules={}
            for ave in self.possible_aves:
                for key in ave.caracteristics.keys():
                    if(key not in self.rules):
                        if(key not in self.possible_rules):
                            self.possible_rules[key]={}
                        if(ave.caracteristics[key] not in self.possible_rules[key]):
                            self.possible_rules[key][ave.caracteristics[key]]=1
                        else:
                            self.possible_rules[key][ave.caracteristics[key]]+=1
                        
            color=StringVar()
            caracteristic=""
            for key in self.possible_rules.keys():
                color.set(self.question(key,self.possible_rules[key]).get())
                caracteristic=key
                self.rules[key]=color.get()
                print(color.get())
                break
            index=0
            elements=len(self.possible_aves)
            while index < elements:
                print(self.possible_aves[index].name)
                if(caracteristic not in self.possible_aves[index].caracteristics):
                    self.possible_aves[index].caracteristics[caracteristic]="otro"
                if(self.possible_aves[index].caracteristics[caracteristic]!=color.get()):
                    del self.possible_aves[index]
                    elements-=1
                else:
                    index+=1
            
            
            if(len(self.possible_aves)<2):
                other=False
            
        
        if(len(self.possible_aves)==1):
            avetoshow=self.possible_aves[0]

            self.visual=visualizer(self.menu_window,self.frame1,avetoshow,self.rules,self)
        else:
            self.visual=visualizer(self.menu_window,self.frame1,self.default_ave,self.rules,self)
        
        self.visual.show()
    

    def show(self):
        self.title.pack()
        self.clasify()
        
    #*******************************************************
    def clasify(self2):
        #self.load_birds()
        self2.loadall()
        self2.possible_conejos=copy.copy(self2.aves)
        self2.possible_rules={}
        self2.rules={}
        other=True
        while(other):
            self2.possible_rules={}
            for ave in self2.possible_conejos:
                for key in conejo.caracteristics.keys():
                    if(key not in self2.rules):
                        if(key not in self2.possible_rules):
                            self2.possible_rules[key]={}
                        if(ave.caracteristics[key] not in self2.possible_rules[key]):
                            self2.possible_rules[key][conejo.caracteristics[key]]=1
                        else:
                            self2.possible_rules[key][conejo.caracteristics[key]]+=1
                        
            color=StringVar()
            caracteristic=""
            for key in self2.possible_rules.keys():
                color.set(self2.question(key,self2.possible_rules[key]).get())
                caracteristic=key
                self2.rules[key]=color.get()
                print(color.get())
                break
            index=0
            elements=len(self2.possible_conejos)
            while index < elements:
                print(self2.possible_conejos[index].name)
                if(caracteristic not in self2.possible_conejos[index].caracteristics):
                    self2.possible_conejos[index].caracteristics[caracteristic]="otro"
                if(self2.possible_conejos[index].caracteristics[caracteristic]!=color.get()):
                    del self2.possible_conejos[index]
                    elements-=1
                else:
                    index+=1
            
            
            if(len(self2.possible_conejos)<2):
                other=False
            
        
        if(len(self2.possible_conejos)==1):
            conejotoshow=self2.possible_conejos[0]

            self2.visual=visualizer(self2.menu_window,self2.frame1,conejotoshow,self2.rules,self2)
        else:
            self2.visual=visualizer(self2.menu_window,self2.frame1,self2.default_conejo,self2.rules,self2)
        
        self2.visual.show()
    

    def show(self2):
        self2.title.pack()
        self2.clasify()
        
    #*******************************************************
    #Oculta la vista del apartado de clasificaciÃ³n
    def hide(self):
        self.title.pack_forget()
        self.menuButton.pack_forget()
        
  
    #Muestra la vista principal
    def main_window(self):
        self.hide()
        
        self.menu_window.show()

    def closing(self):
        self.visual.closing()
        del self

#**********************************************************
def hide(self2):
        self2.title.pack_forget()
        self2.menuButton.pack_forget()
        
  
    #Muestra la vista principal
def main_window(self2):
        self2.hide()
        
        self2.menu_window.show()

def closing(self2):
        self2.visual.closing()
        del self2   
#**********************************************************
class main_menu:
    def __init__(self) -> None:
        
        
        openImage=Image.open("sources/bird.jpg")
        img=openImage.resize((1550,800))
        # self.image=ImageTk.PhotoImage(img)
                
        # self.panel=Label(root,image=self.image)
        self.frame1 = Frame(root,background='#353437')
        self.title=Label(self.frame1, text="Clasificador de aves\n\n\n",font=("Arial",25),background='#353437',fg="white")
        self.clasifier_button=Button(self.frame1,text="Encontrar ave",command=self.show_clasifier_window,bg="#7a7b7c",fg="white")
        self.clasifier_button.config(height=5,width=30)
        self.clasifier_window = clasifier(self,self.frame1)

    #Muestra la vista principal
    def show(self):
        
        # self.panel.place(x=0,y=0)
        self.frame1.pack(pady = 20 )
        self.title.pack()
        self.clasifier_button.pack()
    
    #Oculta la vista principal
    def hide(self):
        self.title.pack_forget()
        self.clasifier_button.pack_forget()

    #Muestra la vista del clasificador
    def show_clasifier_window(self):
        self.hide()
        
        #self.clasifier_window.load_birds()
        self.clasifier_window.clasify()

    #Funcion para terminar los procesos 
    def closing(self):
        self.clasifier_window.closing()
        del self
#**************************************************************

def __init__(self2) -> None:
        
        
        openImage=Image.open("sources/bird.jpg")
        img=openImage.resize((1550,800))
        # self.image=ImageTk.PhotoImage(img)
                
        # self.panel=Label(root,image=self.image)
        self2.frame1 = Frame(root,background='#353437')
        self2.title=Label(self2.frame1, text="Clasificador de aves\n\n\n",font=("Arial",25),background='#353437',fg="white")
        self2.clasifier_button=Button(self2.frame1,text="Encontrar ave",command=self2.show_clasifier_window,bg="#7a7b7c",fg="white")
        self2.clasifier_button.config(height=5,width=30)
        self2.clasifier_window = clasifier(self2,self2.frame1)

    #Muestra la vista principal
def show(self2):
        
        # self.panel.place(x=0,y=0)
        self2.frame1.pack(pady = 20 )
        self2.title.pack()
        self2.clasifier_button.pack()
    
    #Oculta la vista principal
def hide(self2):
        self2.title.pack_forget()
        self2.clasifier_button.pack_forget()

    #Muestra la vista del clasificador
def show_clasifier_window(self2):
        self2.hide()
        
        #self.clasifier_window.load_birds()
        self2.clasifier_window.clasify()

    #Funcion para terminar los procesos 
def closing(self2):
        self2.clasifier_window.closing()
        del self2

#**************************************************************

if __name__ == "__main__":
    try:
        root = Tk()
        def on_closing():
            program.closing()
            root.destroy()
            
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.title("Sistema experto")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d" % (w, h))
        root.configure(bg='#353437')
        program=main_menu()
        program.show()
        root.mainloop()
    except:
        quit()