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
    #Oculta la vista de la descripción del ave
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
        exp="\n\n\nEl ave fue encontrada en base a las siguientes características:\n"
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
        exp="\n\n\nEl ave fue encontrada en base a las siguientes características:\n"
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



        # self.descrip��m�8�|#%%� k��ԋR��ȏ��J\�NW>BF�y�K&L�5�i���R��8rR;��b[7���'�\��wY6(Ʊ�0�	*->!d�D)*B�Ka���E���
T_��G�o	3h���/\D�B�@?ā�F��71x��V�g����m�)�����^I�Ҫ5�G�������R��G�@{mI�z��Y����emi�xa+�`3mUd�iRUTب��ƚ�Y���ܴ �[���6��Tr&^��1E�������8�:�W�*�y�+#�Z�JR��M$��5���:�)N׻�PR"k�9�R��}�\{=gu������OS�	t-g��>�g;�Ӕ�~��xZ��G�30�V�d�Yn�_���t{݇DP�����4��+�3zo��(���AxVJ�t�u%�x@��q���n_�/H�{�h>��Y���1^��gb߫�}[罞�K���0n�����M~��V�+�'��8�������Oӽ[��.��JV=���?��@y��\���o{�gP�� v�����@āt���^��<�s��@?�ʼ{�ޭ��2 PK    ��X�~�L  SO  K  Report/StaticResources/RegisteredResources/team_spirit20861140841048598.png � (�                     ��wX�K�/�� �N�C��(�H�#UE�$8@р� �^QiJ�$h� 
�tP8JW)
����������7�3�������E���+� bE�;�@�2�HPN��������	�3���ee�ca?���,�bC0����Y �L F@�?Vf+?� ���3~6A^~!VQ�~A�3pnfV.>7#����_�C�N�)��`���uF�UPh`�<|� N!Nfn3��㒑����d�C��H x�ܼR��R��2�Hu	�������������&RJQME[����? ( �������oҝ��'O7v<��x���m���ۏ��������_������_�PN�l����~�����F�}�nn�͛7��7]����.2�L�����}�����RQZ���Ì$|I^fA~AZRZvvvJ\*��b�W�^����3�dggg``�*��,����������*� �x��I�T�O�K��C�X2��a�d�c���9��� 7���"�*��J��ef����nF^6!@J�M���^TT|��0s3q2ѳ���xY사 �U�^�a�6��7����s�"�������������������o߾��ï@0�@8<~���_�/`�������������?���A �2��%'>��~˦z���y�:�伧��x�Lp�b��l`h�����Ӫ�7'>���!y���D��ې�7�s�Ri�:�B��}|�Q<�Q	 �`�H� >b�/�oC���wGs�,�a �(��e+�e��O�ǰB-e&�(��L:GI����l��C2J�(�)��&�lI���;���ɓ�(��?��]�)[|��I�� ��jI�Ǝ���>�~ei�b��&����9������G�d�
k裲��1IV��/�`!1b�Z"�,�&*�5~N�`P�,����w�c�(+�sܣ}��w��W��kn�L�z�7D��bᰝ�Ļ�";0�M�s�K\X��X�`�.d��+؏��G�F]��sY�
�7f�:�970�:ĨƸ �N>"xv.��� 4Duƽ�.�x�� 2Ӈ^)�gM�� ��btlY���P�#��=�s���Y�*��n#�����Kpl��gz�V��-�KKM�}����C.�*�iN����r%��ǒ�U�$�zB��a�UĴ�a�V�.�B?sר��SG݉���^�$ˁ���P`9ʴ傹���
؝��X�ϱ��Ɵ�a;u]�:/
��� �Vǡِ�@�-d�~��ʟ9�%؝<|�9S����e=�4*��\�ݬ?�x�cЉ�pw0�:O�o:�&����<�q/N,,/��q�m�j����Dq��.R_ّ�n���i�G(�.�s�{� ��҅6�?�N�щ��7����\I�[��e&R$�N۲�7���<�2���3��R�@_5ߐ&�U��\��!Y�`.I�/S�n��x'�:�(w��'E��]�+�"�mM�G������N�v?7�>16���.}�󃁾N|Ħ�b	�_خ�v{���9�%�%]�n��Ӎ�tk��������(vIH�/� �)��-�⋹L�nyHB�����T���oU�l�@�<:x5u�%hԺΨ�l�C�Q���,$��fڽg�N:e����m���5_n���[�3]�A�
��r�U�u��7�K��eћ������kyj!`J�B���M`����"�-4��=Vm��&��-�C����k�r�y�:�*��N���s)	�dMa���SDR����4���>�b��R��2��O�����I0(��
�آ��7q��b�L8����α��=,D��!ƍr�Y�l�h&�5��v�y��O�ŭ�R�+�qb&Q��+A'��hr�82�sm�{R{�~bp�8��[<�
ۏ��+��T8��:X��H=@d��X
Ur����̂ҹ�󡬘8
د� �H���$n����L��B(���1��hmn��Q% ��/qT����&Ɂ�Y�	b9]�`���;�р5`Խ�.���CW[	�JpJ^[�(]/^�u>�iE�w\雽�kaE��
���/Y� W�d�w�ٸXu\8�����ɲ�yLD���D,F�����!*9V�5���oLYrVO�{��m�(�grz��;ޘ���O~�$LE���X"jI{���-�}����
2ڎ� �#��P\c��Z��^Ab��ۅ8���C绋��f@�њ��lD}��KC'8h�n��<zM��:/$1GFߨ���?�%�I�E֣�(�a����[|մ%3�Bwz��߂�p�Dw'��:5#�I7�\m�b҉�O��CgKFϕ@�$�����G|&��7&���W���ʚ�M�y�=8�I��m�x(�S>���T��K}-�VK�A�FB��;���V�n]��o�T��T�wG?���F?�K�X���y;�,��x�9���(���6�z�9�y�#ǵ�q*���P��N8VZͭ9�?lQ��y?=\���H S��P�"��;<�  B_��b���23\��D�n�pA�SX)�<+wҬ���-,��~���
L�-ͺ`������7�΄哬��y��ju��~�-6�����#]c	�������
@�$����
��w�-|ҷ3���x�9��`$��=r��P[�pD��92�-�:	�Qj}��C��6���p����0fZ}�R�}�ee�`|�{�O�b6>��Y]C3�EF����4Q�q;�c����,_�pHӬ�fmF���q���Y�@�p\��+������=��x�O�EM]j�,���h^�&�����raEb�9�����|���L����"oا��ᒯ�HG3
{}ue��]�-ҟ�TW�[���(}�y֢�(�LA���9��v���RUk<st+�M;�܅�W��q�ٙ�0u�v� ���Y��}>�J�d��m����8*�=n,��]��!�������o�~)���*�t��G���K���b�����=�)���R�n�
�$sn�2�r�V!�3�I8rZ|��?;�5����)u1����Dc����Jl�f-&�cE[�4�$\��r"
��׺�i˦y��?
Mk�uOb6����
t_���|����mrpE�>�rV�U�E�fj$-�|�F�Su�c���z�=�����#��7[}�Ggغ���׸�Zc�㵥	�o��`&Ä�7#;�8�4�QȮekVo�u?���[�Y:o��1� 9�竏�`8�9���ո4��%F�jE;ֽ�9L� H��h2���h��-E�{]W��uP�����e���>:@��G�S�_l�nWq��-~��t�����a��<��]4O���|67�;Y��yZmqʃ]D0/6�u��W��=�s����_�yw�ϡT����Pt�~͇��3:����Gw6�<�W���wўC)"��D��)<"����oѓT�~�q��[�+p�]\��s��Ɲ���,�R#��sq�B&,�8헰N��eg-��i.e��$��K�=�<پ������ks��=]?yP��-/�����3r�h&�5�����tzAU����1@��F�!����^~���A�~)�x��b�������3}�Gx�|d�d�`аh'�?��{fzj�I>bp�,�ΙTĥ��
ڗ���f�_�Q�i�󬿘��hIrf&)��Q����0��+�����{gswa�����Fĕ�S�����~��͋��>�"��5���_	!�z��=�^ܖ�,�y�w�XCḶ}E�z��O,^��2+���󒽑�x�x�@siRk����E��@�2�9w��ݷ�����#��|�f�QIA�z|4���Z��Zʂ�ܚ�"m� (u�r]d<����u-�{���Y�4ˣ!�s�GC��t��!#^���0
�����#�xaB?�SL	�V�������o��uh������CY�<�)���cW=֌�%L~� Q=6ٜ��n2���qj��詋A�����~�cx�yL�����R/�P��Ӆ��=����+���M �@�.�ji���pF���ϧ��\�<j���>�TŧF�v�^���ȷ���v��#d|�׷�
�������;	~��+.�����Z�D01�Un�+�@�=)�s�L�R©�EL�ĩ��"1���;R�}���D�W�
�t�j9E��P�>6��r���߸�t��a���f��(�f��}vY�@�qp[D�L�fdiZ5�^��e^I���/�Kk��_D4�i�A#"���S@��(��/)Q������(�st��3f^]����n���;�c+�v�nra�gy��\Z�?9�
�
_�I�0R��u�74iI��z�J����CQ����x���S?C�A�%�C${�*S`Ij���G5I��DH;�'�Ѿ���r�G	�����!a��y1��2I�E*�U)X�"�~���D��P����Ba�pl�$�:�~eF�6���$٣�E�.�f#ʃ�^ה�b�uP���F
�#����:�#���38P����d����*�Z-���gv��h�c.zv���$��y��UzR�Ygo.%�wM�������&�ч(����&�s�ޘ� U>�\���sA#��P��B=��y.P���¿�]��f$�Y�M��:��9}0�ʫ"q����ɏa�����o�3o9�7s�'�/��t����^ru�*�m 5�|�2�޳B>"8{M�{���V�Ȧ��)��ˉE�5R�w}T�S����$���L�]����?Ch�����8m���Le�YJ�oݥj�O��c�N=�b[��l4$K�h�c�2�hpQ��b��
�ȋ\]�N<����(˙ElF���x�r�4"6�/���T��9(�=�
��aPD�?.�bU�M���Օ�D��MD�<-�3"b3�+_�/�3Y�z(��g8���4��ty��(sWwO�c?1��Ϯ�4K��&9"����ˋ|�q���oi�Y���C�a�ݑ��6�9�x���ԑ�������a��$�ԺK�2�p��eo�IVjV'ަWI�%��TK�R���U&v ���.��;å� �vw��P̤$�u-�,Kw���6��r ��������\��a�jE����LxQ��)c$�|L�_�}�4�"�H+t��)�8�Up�FW�_�XW��4z�>.�aS���,��D�٥��כp��3=T�'��
4��v�WG��?�7㾋�[/�MrcG	]��M����"���I��S�ٺ8��}�����ۭ�R�:Ν����k:��g����3Ex��MW�[޷��c�u=� �X��[�&U+�t�I�%u7.켌D��~N�t&+}P(��l٣�R����/�كeǹ�u�\A��|�ѕ��g��!j�����.�!��JH�.�Q�8_m��0����O�/�4\����fv٘�*E��r�d
yX�����N�q%+��צNrGY���-��UL�f�,ӌ�_�ăW����Ϥ�];n�͟�P�3�]dBI�*[m�*����hJ�<R���T&wjnaKR���+_��~!��Y=����Sq��r9|�_yD���b���h&~e���y��~�mYT�B2���դ�ہ:�k�@V�h�|�IO�r0K��@<�������4����{�����p�����kEw�Ň���^7wL����O]�H�_֥�%�J�u�p�,�R^r��}:6^�O74P���먣�	�x90��<����i�i�.ҽ�K{�ҵP��Xۢ��^߇�ڠB�%�rƞ	���p&�Vqˊ���Y&|g�Ī|	L���}�r1�:�Y]q�u~!�G��د>;>.�W��_���`�����h0Wp$�:-U"�᥌n�a��-Y���`����m��O��g"�F���0�z����W����
�F�Tׯ�����&���-4���9��.��ZP�H��SwK�A��rX�?��l�l��{`�(�MRM�?���Q釅]i�����m�6Z�TKk�k�S�I�d�-�Q֒���PX-�Tb��k�>��y_;:/0����D��	�f��=wp	�Lj^,o>�k�x�Pw���L�'�_���i�Mk�С�q��٭D<{PV�cB��Q��/��vV+��}�8��=�\٪o��|�����ؗ��_��)��C�<�aG^��l�$�ef����*�i�_r�^񇍐�D�09&Ҽ[�ESPDO�u�¤c*p"�b"u�X:�t?�O�[{6��!w��a��#uw�e���lZP3�VK�Ӑ�2mH�p���3�H�:�ʽ�� >1��²�󱆜�<�BI����q/�S�Wj��Ď���r��ǜƜ���)%��)����AAu�zۀHA$���I�1�uc���i�[�HX��쵯n��(ǀ�8��=���_=9]����o���~ 1��vOh{igD����D�gT��ԟ�J\s�~k,'l��k���^�E1���gIc��_��j�Ny^˒�~�ƙ_]D:�s��V�^��'(������}�0	r��}�e�u�Z�����gk��66m.��DZ����8c�����!@::��x�-�4�#��T2]X���[�_�T;:P�m�|~�2�rX�}��Q�0�?�ꚿ�\�����{��W���U�A�n^]^�-؀�m �

�s9W��;��\����/�t��։,r蛄�S3�2W���@a��9"��n򂜄 �	�Px"._�(�_9����=�D�N/��U��٩��&Zf>w!���jߌШ��~��iߚ^P�z�O���y���YXZ��m�_cqߍ���Bש/q����Ǽ�B{������q%q�;��AN�)`טC�������f���y4�hO~=�;�j菳
�*,�}�E�) (���a��{j�
�^ݹi����E�X�6~#J�v|z���r���M��ˏ�e�������}��Z�n����,t,�_�7�����wD�N���H1���9�����3�Ǖ^��F����DcӺm��bݍ&C�o����دAJ��ק�j��\*�S&��mH7��^w���è�k��3�+= �j@J��>�n��m5�Z�h6�2��)���Y����B����u�p���k)��
�WE~��ݍ��[[i<D��cE��_�K>�v%:�.�����ͽ6�]�(ܣ .��B���ju����׵��j+TI�H���W�^;p�O��7t �	���\� �~��q��n�E�V#��b���_Ϗ	-���s�2 lGR��K�-����%�M�V�䶿qo6�}����C�4bh�����̵��(6��A%lsZ2ߒ��&����N]`a̿�(���L)�%Bjm+�'���!�H�bIB�ϵz��� i�@ ��:"2�=BDӿS��,�f��Ge��\���aDU٬&���;�A�2�[j���)]��H��7��H�BQ9��HE��-r�dM��j�W�m�
��&
��nb�F�d��~����1������pAd!V#8�e�l[m���TT�:�&�kX��8�ZS�_,�Fc��Ƿq�!C�T
�T#����ei�/�3��z�/��$ɤJA�Ԑ쭗W:�����ȕ>���5ں�B���Vk2�<����G����;
���Z
��V`��M'ڌ�^�Ǣ�~�~A�Ee`�:��r�M�#W��V��W�!e��~lF&�	��A��̆jgj��<��?�sa��<�tD��t-ʏwh5�g}�JȄ};���|����V�c�0�GlQ���鯪=�	x�߻�I���T�c����#��loy��<��T�0����N��~�NnX����d�R��Xz�ҩ�"l���e�y�;M�`�����ځAdf�>'��r�s�|���AF�D���6'F9j)~Ԣ�it-\wV�/���m������W��7�'<N�`���3�����V�V[G��܆? �,�(���8�֜��gI�)�2��^��C};��k�ީ��!��ھ,���ܚ%���|!y�nY����l����V9 ��Ym���[M�c.�Nȡ4 w`����6aW�R�	.]���%k�]��?�:��7g3�Ao��F�2a;^����#�-s���L� s������ښ�O��5-����~���&y�1�"$�}iU9E� 3j{�9Q��q���ˊ,�W97��	�T¼F���8$�vn�~.Il����l�{��m?m{��nm{�g���r���I��{�rzqWԪ��@�I����v�� .y>+O��n#��p�"�T�f]Da��˫���i߆���C�'�)���өS����ͼ�\Dfxe�X���߇�����,��Vj�*/\��C��k��l�f�ǌ^c��%�QN��D,L��t�~�&�E�ȼWa�/ �~>c�Iu\H�9�N�b֜��)������&9��\������ś�sF7�߸&y)G���\�R!�'u�M/�)|��N���|D�|_��;P)��tsP�V���|F�LiN}'�����8�F�^.��n+�PԆ^qb�^��T�<Ť���Ё��Q����*p09�K4�������l���^Z��߅",��"����*�W�T�\l�Ԃ�nr@���х��yf�1Y���{I&�\>��2\���t;7O�^r�Y?��6�]�k3<�k���7���Jof�h���n��
��Ty���*[�|岼;�t�ͪ0=
i�p���\��:;��dQ��3]��S�aPG)��j.�&Pj�Z?�c���f|la,��j.�1Vƽ��d��_M��������1�/"'�ǆ�J��᪵�v��G��4��e�X� X.@H�nqӯ�����Rz���ziW`]}�cN���/��ģh�K�������*�l�Uy°��JN��Ckm�ޓ�ͺ�������Ñ�s3�Ole����q���
�1�U6B��V�]�R��O��)�4��G�(����}@�j����~Wۈ�_�eP�4����!	��B�E�An���_��(G�����������9���w�!N�>�"�Jn�g�*՛�M2�k���1�\3�^��?���V��Ȏj�
 �>�Bʁ��z�=�r.�[ÑN8|WΙ�U��:�+���DQ;ۓ�cls���r��<��SI!Θ�B��NA��xdZY $���#�N �$��8�^T���5��^�Ud"-N`���:�8�M�f�p�Ȗ]��	z�w��y�|A��i!����d�s>zjiH�Ʌ�XS�����v�ե�~�k�A�y���FH�4�xk{�uٴ��ߪ��ғ_������f*�Br������Ue�d�Q}|&�5-��kg�r
gk��Ӿo���Op��� ��U%�WC�N~�j��^�P�ٱ&��0.�8�����@��׿-v{u�����t�ьZ�Ha�W�H�UO�32	�P2����k7��,�N\��G������d�S���k����j��X�$KC@���^�J���m4���r�����F��x�%�?��ޜO�xf���
�Q�3jąB�5�ˢ&j	�N�_Щ��!��|������*�/�pB.������5����R��5�!�Z�����-��� e��w�H�c��l�\���Zү���g������Y��;��]�4��>^�o2n�"Z!��6(���\�{�J�n�՗��w��������'���#�����?����=�L=;�}�ADM��?��T�Y�V#�F��5���������S�$��N'�"�']��)��%'�t��Q4��f����q�ʇ�Yd��e�9 �Q1a�y�9��!(�PC83�+t�\Qޔ Mu��"���ru���E��%�V�Dzg��Kp�<�Dvٜ�~
�������\��?Qӓ��Ћ����\��R;s�y�C��_z9��8H�t �5�di��=o��s[�ʃ��:�*K��0/�~{/a�!��g�P��Yؼ@�=Z����7�/%�⚋S�烥��e+�?�-�bG>���Č�� �ӫ�閺��y����� �JX�A��������ofj%�mj�(m+���_��~��l�RK�6�� $�Y��yx�-Bսw�o_��o�b5B���ם:z/#�rHƽ>�Z�N9�ӱFB!LJͮ��n�)�����*2��td�L�Y�}#1�V8�)�[e=�lfr=
5J9�*j�r�%���˩r���Hgkܝّ�j�%��}����>�|��G��#Wj�-"���-��p�E��%���򦫥���Sd�����yā:u����=j1+�jh9��`�5D�
Fj4Ծ��frʴ����Ia����{�e-�l�p�
��=���%����~D��=����?���<.�rʜ�h�Qo��4�*C��`�{l�~D��gK��!�G��宪Y#"������@�kG����wl�f�*�*�h��:Ok��ՈwC꘥��4KH�XX|�Q����E���ޏ1�<��F�6�}� ������C9M���qث��5#2�Z=���e�l��]>�$�B�B�Cn;�U#pK-�au�$���d�4���'�g����s�{��ux��I��(G��O�wr_��Ű�K2��x�bؓ�0[Q����_������g����+�,����z��kL��CF�ξ��h�B$a�eb�"�z�@_)}�Ra��0Q6-�ҽ��x�+5�)$y�ksv��:p|Zr=�5�	o��/'�UI�(�j�����a�~xؑ��D�%�gɻ���n�p�9R����:��3�Gq�(��?��uw]p�|Zf����(�DN*Y��:�.�'cUwH6���z� (�}(x�O�~���gp��\�ؐ�<7��!��1�T|I(��o��qء���w��	��mykr��%��}���:}Ďl�|��k㱀8������C����d��J�B]dL�Ρ<�Dj}�aG9/������g:>I��,�Ɉ��Ff�is�<�-���^˞wb����ੑ��nH@*3ߪ�c.��B�n��w�����%�T	E\*�&5�x[ĉ����aCګ�R��X���\��-	o�&20�0]b2�ؒp13dA.V�1C���0F"�:��K�Ԉ��K�}�7|)�Qա_�Vsɚp��8Bjr���
�g�/%'�2�2@����x����}�/�泤�|u��Ģa��Po�{�|�\�O�vN�jkz��U����
\6��ప�_�گ�cϏ��8a#��El|�fN��,����[<��̂l�]������#%t~oCi��aԕ�w�@jP�J��%�c�(*1�cH`������șё���=}��-w^���d�S���&!o�P`�2�I��4�H����K�e�!�B�i�>�+ri�ri�R�KW��t1rerj�]�Hm���Y�E�Z"16�w��-�ǔW��B��Ic-nIg��+��?e�[�mG$�6-{�T6k�
�����~)@�K��K�Pڐ:�c�-\FxN�����`�E��r[�X 	��+���+>*�Y��GY�zJ������8パ�,�W�9���c�S_����G>�1M��N���D�o��+�j�w��b�5�3��/���("|8{X�k�Q}_.*rQcr<�ɱ���{T�>6gu��/��;����ȳ���k⍬����3s(��ђg�oɘ�R�q�H-��ò���c�GG�Ƙ�з��v3q�����VXR�[e$�2�M�!��t+�"\��p^�O��X��:�'���/�	V�`��N]�J�}���.dK�zV��>O��>B(�- �f��0,�6��p
�1�&k�-|.f�H�M���-"��e��C<$o����
����,w4晚S5���}��f�O�xj����N�!���W��I�qH�V���-7����!eu��϶KJ��[�r��<+d�Ҭ?o����/�ҳ+�v�m�O$	��@�3�������"��L����dӺ����v��Oq�X�	5f{*�.s!��Y�LfL�����&Mi�UV��B�*�6��4��J��L�Y]ܰv)��-�*n+⋣�I��/�2�#��QxW9}��2��޻���F��-;����3/3��ّ��+�h�j=�Ȱji(�UfB������m.B��9]���x&�w�q=����B{�[�F�Y�l~1ҁI+/��ǘ�u8�H���������)��ܹ�s5L1F�c~�G�g�=���뷼��? +�_x���x
��8��#5�Aץ�W$�	SG�O~���ߢOIr]���h?��s�����?Z�}�z�_���1�j�Ԁv�V����eb2x�R�6j��2��0.�����H�A��2It�9+j8�/�|��JW��%�w�����%/�񆗛}�LL���SrVlh$��b�)��b?�b6���w���i}df	O�h|Lߢ�B��B�и����zw<iυx��3j�7ю~�����|��l$��$ ��6`h��@�޻�����{�}��hp9�cf�1�L�7P����O����y�U�Eu��(`~�X�A��d&?� �2�J`x���,r�M�#E��`S������	ﱉ�}w�w�,�A����D��[t�eL{B��CQ&XF��%@ pp=�W'�Q�����"�]������lڐ��5D�ؕ@���Z�E24GV.�F����[`]	 Wζ����d�ϡ�z�6�佩��eL>1L�Ϲ���
�[������w�d���ܺ����voŀ��{2�\�+��wS.4��9�Ksl�6Ȧ�C�1ƒ�:�-����y����Ӫ����H��ˇ2�F�����4��o%}0[�_Ꝯ��S���ZU+Ц����ď���y՛uc:K�R�H��zc�W<҃ǡ�࠿�z�/�_�dB�2��8�?�<�+��u �ݗ=�4�U7��9b���b;�G/���{�_�λ Xf��i�`�t�;7�X{���XU�\���!B�j��e�PY��Y�V���>�C~uolU���{��G��������5�
-�WmOLW���d��	b�X����p��	�S�5n1��i&4͛M�{' =��g�/�vߴe�2"�!�v�k�JW�ňҤ����G�x�P\
�ݿ=#�+[d(���Ʒx�����W%[��`oq���A�ҽ_���±tMa$��ค�n�������3#F^�� ;�"�=�=L�N�HًQ��)v�i��?�N�5.�|�%��M�Xz;X��7饗�,R��0O���?^��\,�5Iǳ�~?9�-���4����=�Sz����	9v��`�͌ra���'�;�z�:��쑮*]���Gyș{��p�X���&#
'8�h�k�~��'p�g��:�6X��^H �!@�|��@�K�i�Cn�2�
�����l��l�1�H�#�O@�:��ٙ&��X��"/�?�=.�s�>���m���/�gv�+�����i��N0�΄����N����.ΏV,���c���D��~�쵑#c�Nb!_좏t�98z��'�	��[[C� �����^ս\��J�ߔ�����{�C��������m\z`��X@�$���B�#C�"&v]��#�i�	���Xg�A{�(�a�]I��`p�l��L���S��"�2���#�
�']�ړ-H�,t�۶�<�J�����A[[(n��ܯD����Y�+��i�N��E>/�"�y}q�c]�O(�����n�mAz�i���,i���kw��v��g��N�A��*��)K�~ǵm\	��4NE�5�K�l|}���R�Q8���pw_��n���p�hH�=|�Z�7�ׇ�A��V��W��B�"	8>���� ��&һ��)�1���l�*����G��ޯ��l����\ٸ0�ϯ�Gk�5F�/ͦ��l���E��X�\bX[.1y_������P̊�r�O�a�+���"bϢ;�il��ܢߣ��2P��z��U���i�p�F���83�����KL"F�<��;MO�����K
h�l8���G�z�~~�����i/v�ËU�bz��q�2/��fg��k�H�����S��l>�(w�/O˳�����<��Y���`ό�V�����{%��������{�^����Z�Gl��{|.��`�w@ǳ߿�}���[�7����U�b� ;<�ڨ6��d���A�:>z��n�vB6�62��do����>Ǎ�X�cq:�.�����x5=��C��z��X�~G+`�V#g�VC5��B����}��{\p�J���Ve�3��vi`�R��[fO��둀݆�V��6�.e�]��؋��$Q�g����׽��}3f���9�Y�����(Fu�^Op�V������!2����fE#/�?��~pib�9��1\�&C��Ǚk��')��������w�tX(�xZ���΁����_z3�����.v�:Oǘw�.$T���qݶ$���4i�rP�0-������S�	�����.��+�*�"���c�0[1��b�T�v��tI���͸�ؘ�O�z������	��Y�C���ܝ2�)�@;�X.��'�6���4��=�s������!xQ`�Y�ߴh`��p�Sc	=o���I��#/AC�p~��*���N��>���� #��3aA��4���<���ߧ�^�r�Md��$81�	'�sأ�<g��m.7+�l{�;-���	�: �=.�L㆚�4�}V1t��%Ϥz�
�x�N�-�@9s?3.���x�sLm�͡aM�QY�Є㢘��s��^�ܱUo$�=#�_ǧç���F�Hy�"ڼ/\<)�yt�a� ��Sc��s��<�dBbj���Ӂ��C�w��^ W/EC��#h��!�ӓ[-�@@�9��Fܵk�(��!��W��/�ͽ�؜@v��B�|4x͉�e������Fg{�����N7���
2'r���Ꮿ���������=L��h��g����x�:8��q�����;��*��ol��:����F/���X���w�E��J\���zs&hӧ�]������iFމ�H��?��>�Q���OIR��`�Ϟ��?v-�}����FPna8��������٪p;�����%��ssbs����W&�#���~��	^�� ���W�t{ j���6����Y)���Ǯ<�3u_��0ˮ{~�П�W�`p ��',��H��:����?�>�����=����J�I̿��*Y�{,vI ��b�x%����������o����(І�B���oC��_ե}��6�زGZ�O4~c��!�2�X�b�*��,�Ep�6~�������S+��C��PNh���֢$� �!;�15���3>�LU���j!�{z��z����{�ͧS���F�޳X�9~ڽ�Q܆� �ڃ�o���E$g���W��\����	gOAOȚ�:T�7 ��{�I�`[M��)q���8F)Y�,y4�uH��+����I�	�����{b�C�t]I�W�S��C��n`�l7��T�*?>d#�[�/h�wwdm�#� �		bѹ ���Ga��`�hr}��_�ʋ�_�w�<����"KO\��62�L�F���S�Dr>M��j��в��U��Ҥ὆�46[�+H�&CM�He~�_��
��TBnh)���@e��+q�Xؾ�1��.V�?]xKx��cU8N*/I�X��i�v��k�'��WU�[��$��$�s���`�#�Q�9�����##��$��_{B��CE��o���`k�鞊SL�c�8�E�F1�+���݀މ�D��)�ǈ��@�e)�Hٴ{�s��I (�-V��LÐ��l����xmFmPy×��+ v1�	�D�
�K��)�Z^9il���1���wH�Hd��â��e�4P4����%/�s�IеOpM̧}�1.��O�V��[4��_@��8�W�+��Q�����.\���RV.���*J�L8�M0�e�`l�=UO	S�K�r��!ą�q�M�#�>��q o��iɻ�Gdz����]�=Np�Y��Y���=���#Kd{ZܠV��*�s�q��`��(~���d�x:��N�EwRn�эѪ+ B��l�ZES���i7ژ.��H��襌�W\�śqz���5�*b�N���o������U�V�̫�x�-jR��q&��F�&y��3�x�����*��d.�/�L^\���6�h�I�t$����c=S7p*�j����ьprh�BdA(��9WE�>��W�țs0ܝ�ú��^�x��< �_�%1�4��s��j$�9��~���QtMt�0A����7�g�4{�(h_6a0L6�e���E��:�(~���(P	��^�P}�jF� ޲
qj��u�w��㥳BBLs<�wAD!xW"��v#��6��L������숗��c������FMD_�2:"��@���uB��WQ��堽���5:�=U*k�U?� ��Fok�Cw�s��S�r?��C=�@�xuf�9M�D�D���=_�%s�qu#�X�r3?�0��Uq�5q�q|7��W7	�%�{�DBT�Mz`I0�Zy+H=c���r%�6�,A+E@9�7�8�g�i���eC�y2�����T~��N9�:�t@�u����y��<ߏy��2o���i"�@�렭����],��b_+���f��R�J�p��i!cO�<���뺂,P�B���U����5;��Ƃ��i�u5ߦpU�-lH�8̹ Y���zC��U��SWO��h4�_���a��a��m�Xg�$�R"�б�x�'�hfԱ�s	,�5H|\�P�(�!�:���f�c�'w�.���j�����d�l���K�}"
�8�8���=۞/VI���o�0:���=:8�h$e�b�3==��*2ՙ�2|���#Y���'�;njg~�nƺ� ^O`��׊�A#�頒mw���I��P^N�4��C����~*�"�����@������Et�7��b�k�C=>ʦo7������~SQF�E���L��ʅ�HW��o�&xհ��a'g�/ջT�V�D�����+-�-���[�Q�uhV�mLh�/`�zR+��,S3ҥBf�h.*�@3�����Z�2�1����������SuԘ��CeJK
��y���������������Lȕ+�\��I[�~ۺ�uwa2�9������! ^��10���{��	�N��T�n�D=ھ4HxX�B�������%�@.u��@�s�7|1�Ne��lPC#tW-����e�<��*u鞏Bht�%�f���#� �f3������lLQ����d����ٍ��쨼U��hn@RJ`h�B=�Y�'�a5����O����]������������ �Ba�f*I��[��(~�9��7*.��S�.��Os�fs
S�R��	Y�q�������>ܹɋ{w��3��w�N����| >�8��h|i�జQ1v�5�7$���yT�BiK���ͼ��k��x+��L1�M�6B��LH/�Y���9�L�ԙ�E�+�\b͝>s�XS���Ķ�� 9,�g�s�At�J��\c�&� /�*꧅r&��ݐ����jC�e
'p�~���I3��
�'�4|��;�Db�b��[@`�m�rJNʱ�@����*ih�#�\��kp�v���i��y$��]%'LJ5�2��x;{]�b惍���>�F��QU�!@S(�sb"��z>>^Ly�U����Q6��JcbTF~�^߬�l���1ay!�Hc���]`Z�U:���~_�m���PS`�K����Ǽg��pX��	a;H��J�S
�]!�u����c�#�d�f=����_�-{���
�z�2��)H�i=��n7I�hNJ��e�%�4�d��PY�~
1V���/�9r�6O	Y���\%�p}O��o�b�d��a�&5�X��Z���s��N��^�/��2���'��nz?&${6����0�r�E����\��/�c�c���10���}"t�y�����n&�,CC�u�;�*9��݈{�%T�������ܟ�	 w�U	�����U��|#ڬU%G�2�6�ĬB�yh��t�XK�7�8%h��c��$I��?p?��=�@�P�����T㙈��/"�4,L��46(.���`��B_�-d�٪�t����e'��vA���~���zY��ϯ�ъK~r���9��Z����U��U'�r�(!��
%h䷓~��;ر(��o;�7�1Fy*������f|�ڝ��w�<�k8�-�b�窩����rj���,�n=���x�t��$9s�$��2��ܻun[������(�|[������ca�X<w�S3�Ơ��}B�Q�T��F��JՔt<�f�B�D�L��$�����.}���ː�s'��k 7�KôU���抅v���ݝ���J�MgO�3eB��̀�y��X5�,$yv�W/ �':��s͛+6�\��D瞏S��i�C�����L!�r��i�A�f�hI����x�T4vJ�����
������Y_Z�		[eϔe僗�
)a*9I��.�N�_��\�)�����dCD�u��S�@��$��K_zY_#+����#�R���p+'{�w�Ɋ�J&������.}�X&�	m���	�9Ud��ކ��)w����A2��[�vD����=w��q/� �MC���4�@��1𠸪���h��*
Z1��hh�תzʩ�P�'����*`�BN|}��ܷ��ǆ�Fj���<��&�	]5GK�֓�hd���4�o�-(]��h�_��in5�{���vu�ZIS^H���0���375/�><��8���n�Y�o��2�?z�qzA�<�$̩���<R�yd���h��~aF��:Q׋����;kh� ��]�<~ώ2����6�`��p�gz�]�.����>�袒�n��4�6qhn6_N��(��I����,8܅I1OS���S�D�"0W1q�F������l�pu��#�u:�3I��0�2��!�}hȫ72M�E�h��ߙ)|g����\&x�	\�������g��;����r�ESy���
�eK�a+�=6�װ�I��u�� /��!�}�[�0Z�p	G�nZ������"�{L��!�����!�,>�K���h{%��yt��o��D�h��Ʊ'z���<��o��kϾ1ǘ��������%21~��6��������W{�a��c���&���"�#�Aۈm���Q=!���X��q���Z���ڄ�J�&�$�P��'��tu�E`7SB���^�=N��8H���V�O�[��M�,q �T����
�����7�g!�)�Zl�瘨�PK    ��X�~�L  SO  K  Report/StaticResources/RegisteredResources/team_spirit21080007706708703.png � (�                     ��wX�K�/�� �N�C��(�H�#UE�$8@р� �^QiJ�$h� 
�tP8JW)
����������7�3�������E���+� bE�;�@�2�HPN��������	�3���ee�ca?���,�bC0����Y �L F@�?Vf+?� ���3~6A^~!VQ�~A�3pnfV.>7#����_�C�N�)��`���uF�UPh`�<|� N!Nfn3��㒑����d�C��H x�ܼR��R��2�Hu	�������������&RJQME[����? ( �������oҝ��'O7v<��x���m���ۏ��������_������_�PN�l����~�����F�}�nn�͛7��7]����.2�L�����}�����RQZ���Ì$|I^fA~AZRZvvvJ\*��b�W�^����3�dggg``�*��,����������*� �x��I�T�O�K��C�X2��a�d�c���9��� 7���"�*��J��ef����nF^6!@J�M���^TT|��0s3q2ѳ���xY사 �U�^�a�6��7����s�"�������������������o߾��ï@0�@8<~���_�/`�������������?���A �2��%'>��~˦z���y�:�伧��x�Lp�b��l`h�����Ӫ�7'>���!y���D��ې�7�s�Ri�:�B��}|�Q<�Q	 �`�H� >b�/�oC���wGs�,�a �(��e+�e��O�ǰB-e&�(��L:GI����l��C2J�(�)��&�lI���;���ɓ�(��?��]�)[|��I�� ��jI�Ǝ���>�~ei�b��&����9������G�d�
k裲��1IV��/�`!1b�Z"�,�&*�5~N�`P�,����w�c�(+�sܣ}��w��W��kn�L�z�7D��bᰝ�Ļ�";0�M�s�K\X��X�`�.d��+؏��G�F]��sY�
�7f�:�970�:ĨƸ �N>"xv.��� 4Duƽ�.�x�� 2Ӈ^)�gM�� ��btlY���P�#��=�s���Y�*��n#�����Kpl��gz�V��-�KKM�}����C.�*�iN����r%��ǒ�U�$�zB��a�UĴ�a�V�.�B?sר��SG݉���^�$ˁ���P`9ʴ傹���
؝��X�ϱ��Ɵ�a;u]�:/
��� �Vǡِ�@�-d�~��ʟ9�%؝<|�9S����e=�4*��\�ݬ?�x�cЉ�pw0�:O�o:�&����<�q/N,,/��q�m�j����Dq��.R_ّ�n���i�G(�.�s�{� ��҅6�?�N�щ��7����\I�[��e&R$�N۲�7���<�2���3��R�@_5ߐ&�U��\��!Y�`.I�/S�n��x'�:�(w��'E��]�+�"�mM�G������N�v?7�>16���.}�󃁾N|Ħ�b	�_خ�v{���9�%�%]�n��Ӎ�tk��������(vIH�/� �)��-�⋹L�nyHB�����T���oU�l�@�<:x5u�%hԺΨ�l�C�Q���,$��fڽg�N:e����m���5_n���[�3]�A�
��r�U�u��7�K��eћ������kyj!`J�B���M`����"�-4��=Vm��&��-�C����k�r�y�:�*��N���s)	�dMa���SDR����4���>�b��R��2��O�����I0(��
�آ��7q��b�L8����α��=,D��!ƍr�Y�l�h&�5��v�y��O�ŭ�R�+�qb&Q��+A'��hr�82�sm�{R{�~bp�8��[<�
ۏ��+��T8��:X��H=@d��X
Ur����̂ҹ�󡬘8
د� �H���$n����L��B(���1��hmn��Q% ��/qT����&Ɂ�Y�	b9]�`���;�р5`Խ�.���CW[	�JpJ^[�(]/^�u>�iE�w\雽�kaE��
���/Y� W�d�w�ٸXu\8�����ɲ�yLD���D,F�����!*9V�5���oLYrVO�{��m�(�grz��;ޘ���O~�$LE���X"jI{���-�}����
2ڎ� �#��P\c��Z��^Ab��ۅ8���C绋��f@�њ��lD}��KC'8h�n��<zM��:/$1GFߨ���?�%�I�E֣�(�a����[|մ%3�Bwz��߂�p�Dw'��:5#�I7�\m�b҉�O��CgKFϕ@�$�����G|&��7&���W���ʚ�M�y�=8�I��m�x(�S>���T��K}-�VK�A�FB��;���V�n]��o�T��T�wG?���F?�K�X���y;�,��x�9���(���6�z�9�y�#ǵ�q*���P��N8VZͭ9�?lQ��y?=\���H S��P�"��;<�  B_��b���23\��D�n�pA�SX)�<+wҬ���-,��~���
L�-ͺ`������7�΄哬��y��ju��~�-6�����#]c	�������
@�$����
��w�-|ҷ3���x�9��`$��=r��P[�pD��92�-�:	�Qj}��C��6���p����0fZ}�R�}�ee�`|�{�O�b6>��Y]C3�EF����4Q�q;�c����,_�pHӬ�fmF���q���Y�@�p\��+������=��x�O�EM]j�,���h^�&�����raEb�9�����|���L����"oا��ᒯ�HG3
{}ue��]�-ҟ�TW�[���(}�y֢�(�LA���9��v���RUk<st+�M;�܅�W��q�ٙ�0u�v� ���Y��}>�J�d��m����8*�=n,��]��!�������o�~)���*�t��G���K���b�����=�)���R�n�
�$sn�2�r�V!�3�I8rZ|��?;�5����)u1����Dc����Jl�f-&�cE[�4�$\��r"
��׺�i˦y��?
Mk�uOb6����
t_���|����mrpE�>�rV�U�E�fj$-�|�F�Su�c���z�=�����#��7[}�Ggغ���׸�Zc�㵥	�o��`&Ä�7#;�8�4�QȮekVo�u?���[�Y:o��1� 9�竏�`8�9���ո4��%F�jE;ֽ�9L� H��h2���h��-E�{]W��uP�����e���>:@��G�S�_l�nWq��-~��t�����a��<��]4O���|67�;Y��yZmqʃ]D0/6�u��W��=�s����_�yw�ϡT����Pt�~͇��3:����Gw6�<�W���wўC)"��D��)<"����oѓT�~�q��[�+p�]\��s��Ɲ���,�R#��sq�B&,�8헰N��eg-��i.e��$��K�=�<پ������ks��=]?yP��-/�����3r�h&�5�����tzAU����1@��F�!����^~���A�~)�x��b�������3}�Gx�|d�d�`аh'�?��{fzj�I>bp�,�ΙTĥ��
ڗ���f�_�Q�i�󬿘��hIrf&)��Q����0��+�����{gswa�����Fĕ�S�����~��͋��>�"��5���_	!�z��=�^ܖ�,�y�w�XCḶ}E�z��O,^��2+���󒽑�x�x�@siRk����E��@�2�9w��ݷ�����#��|�f�QIA�z|4���Z��Zʂ�ܚ�"m� (u�r]d<����u-�{���Y�4ˣ!�s�GC��t��!#^���0
�����#�xaB?�SL	�V�������o��uh������CY�<�)���cW=֌�%L~� Q=6ٜ��n2���qj��詋A�����~�cx�yL�����R/�P��Ӆ��=����+���M �@�.�ji���pF���ϧ��\�<j���>�TŧF�v�^���ȷ���v��#d|�׷�
�������;	~��+.�����Z�D01�Un�+�@�=)�s�L�R©�EL�ĩ��"1���;R�}���D�W�
�t�j9E��P�>6��r���߸�t��a���f��(�f��}vY�@�qp[D�L�fdiZ5�^��e^I���/�Kk��_D4�i�A#"���S@��(��/)Q������(�st��3f^]����n���;�c+�v�nra�gy��\Z�?9�
�
_�I�0R��u�74iI��z�J����CQ����x���S?C�A�%�C${�*S`Ij���G5I��DH;�'�Ѿ���r�G	�����!a��y1��2I�E*�U)X�"�~���D��P����Ba�pl�$�:�~eF�6���$٣�E�.�f#ʃ�^ה�b�uP���F
�#����:�#���38P����d����*�Z-���gv��h�c.zv���$��y��UzR�Ygo.%�wM�������&�ч(����&�s�ޘ� U>�\���sA#��P��B=��y.P���¿�]��f$�Y�M��:��9}0�ʫ"q����ɏa�����o�3o9�7s�'�/��t����^ru�*�m 5�|�2�޳B>"8{M�{���V�Ȧ��)��ˉE�5R�w}T�S����$���L�]����?Ch�����8m���Le�YJ�oݥj�O��c�N=�b[��l4$K�h�c�2�hpQ��b��
�ȋ\]�N<����(˙ElF���x�r�4"6�/���T��9(�=�
��aPD�?.�bU�M���Օ�D��MD�<-�3"b3�+_�/�3Y�z(��g8���4��ty��(sWwO�c?1��Ϯ�4K��&9"����ˋ|�q���oi�Y���C�a�ݑ��6�9�x���ԑ�������a��$�ԺK�2�p��eo�IVjV'ަWI�%��TK�R���U&v ���.��;å� �vw��P̤$�u-�,Kw���6��r ��������\��a�jE����LxQ��)c$�|L�_�}�4�"�H+t��)�8�Up�FW�_�XW��4z�>.�aS���,��D�٥��כp��3=T�'��
4��v�WG��?�7㾋�[/�MrcG	]��M����"���I��S�ٺ8��}�����ۭ�R�:Ν����k:��g����3Ex��MW�[޷��c�u=� �X��[�&U+�t�I�%u7.켌D��~N�t&+}P(��l٣�R����/�كeǹ�u�\A��|�ѕ��g��!j�����.�!��JH�.�Q�8_m��0����O�/�4\����fv٘�*E��r�d
yX�����N�q%+��צNrGY���-��UL�f�,ӌ�_�ăW����Ϥ�];n�͟�P�3�]dBI�*[m�*����hJ�<R���T&wjnaKR���+_��~!��Y=����Sq��r9|�_yD���b���h&~e���y��~�mYT�B2���դ�ہ:�k�@V�h�|�IO�r0K��@<�������4����{�����p�����kEw�Ň���^7wL����O]�H�_֥�%�J�u�p�,�R^r��}:6^�O74P���먣�	�x90��<����i�i�.ҽ�K{�ҵP��Xۢ��^߇�ڠB�%�rƞ	���p&�Vqˊ���Y&|g�Ī|	L���}�r1�:�Y]q�u~!�G��د>;>.�W��_���`�����h0Wp$�:-U"�᥌n�a��-Y���`����m��O��g"�F���0�z����W����
�F�Tׯ�����&���-4���9��.��ZP�H��SwK�A��rX�?��l�l��{`�(�MRM�?���Q釅]i�����m�6Z�TKk�k�S�I�d�-�Q֒���PX-�Tb��k�>��y_;:/0����D��	�f��=wp	�Lj^,o>�k�x�Pw���L�'�_���i�Mk�С�q��٭D<{PV�cB��Q��/��vV+��}�8��=�\٪o��|�����ؗ��_��)��C�<�aG^��l�$�ef����*�i�_r�^񇍐�D�09&Ҽ[�ESPDO�u�¤c*p"�b"u�X:�t?�O�[{6��!w��a��#uw�e���lZP3�VK�Ӑ�2mH�p���3�H�:�ʽ�� >1��²�󱆜�<�BI����q/�S�Wj��Ď���r��ǜƜ���)%��)����AAu�zۀHA$���I�1�uc���i�[�HX��쵯n��(ǀ�8��=���_=9]����o���~ 1��vOh{igD����D�gT��ԟ�J\s�~k,'l��k���^�E1���gIc��_��j�Ny^˒�~�ƙ_]D:�s��V�^��'(������}�0	r��}�e�u�Z�����gk��66m.��DZ����8c�����!@::��x�-�4�#��T2]X���[�_�T;:P�m�|~�2�rX�}��Q�0�?�ꚿ�\�����{��W���U�A�n^]^�-؀�m �

�s9W��;��\����/�t��։,r蛄�S3�2W���@a��9"��n򂜄 �	�Px"._�(�_9����=�D�N/��U��٩��&Zf>w!���jߌШ��~��iߚ^P�z�O���y���YXZ��m�_cqߍ���Bש/q����Ǽ�B{������q%q�;��AN�)`טC�������f���y4�hO~=�;�j菳
�*,�}�E�) (���a��{j�
�^ݹi����E�X�6~#J�v|z���r���M��ˏ�e�������}��Z�n����,t,�_�7�����wD�N���H1���9�����3�Ǖ^��F����DcӺm��bݍ&C�o����دAJ��ק�j��\*�S&��mH7��^w���è�k��3�+= �j@J��>�n��m5�Z�h6�2��)���Y����B����u�p���k)��
�WE~��ݍ��[[i<D��cE��_�K>�v%:�.�����ͽ6�]�(ܣ .��B���ju����׵��j+TI�H���W�^;p�O��7t �	���\� �~��q��n�E�V#��b���_Ϗ	-���s�2 lGR��K�-����%�M�V�䶿qo6�}����C�4bh�����̵��(6��A%lsZ2ߒ��&����N]`a̿�(���L)�%Bjm+�'���!�H�bIB�ϵz��� i�@ ��:"2�=BDӿS��,�f��Ge��\���aDU٬&���;�A�2�[j���)]��H��7��H�BQ9��HE��-r�dM��j�W�m�
��&
��nb�F�d��~����1������pAd!V#8�e�l[m���TT�:�&�kX��8�ZS�_,�Fc��Ƿq�!C�T
�T#����ei�/�3��z�/��$ɤJA�Ԑ쭗W:�����ȕ>���5ں�B���Vk2�<����G����;
���Z
��V`��M'ڌ�^�Ǣ�~�~A�Ee`�:��r�M�#W��V��W�!e��~lF&�	��A��̆jgj��<��?�sa��<�tD��t-ʏwh5�g}�JȄ};���|����V�c�0�GlQ���鯪=�	x�߻�I���T�c����#��loy��<��T�0����N��~�NnX����d�R��Xz�ҩ�"l���e�y�;M�`�����ځAdf�>'��r�s�|���AF�D���6'F9j)~Ԣ�it-\wV�/���m������W��7�'<N�`���3�����V�V[G��܆? �,�(���8�֜��gI�)�2��^��C};��k�ީ��!��ھ,���ܚ%���|!y�nY����l����V9 ��Ym���[M�c.�Nȡ4 w`����6aW�R�	.]���%k�]��?�:��7g3�Ao��F�2a;^����#�-s���L� s������ښ�O��5-����~���&y�1�"$�}iU9E� 3j{�9Q��q���ˊ,�W97��	�T¼F���8$�vn�~.Il����l�{��m?m{��nm{�g���r���I��{�rzqWԪ��@�I����v�� .y>+O��n#��p�"�T�f]Da��˫���i߆���C�'�)���өS����ͼ�\Dfxe�X���߇�����,��Vj�*/\��C��k��l�f�ǌ^c��%�QN��D,L��t�~�&�E�ȼWa�/ �~>c�Iu\H�9�N�b֜��)������&9��\������ś�sF7�߸&y)G���\�R!�'u�M/�)|��N���|D�|_��;P)��tsP�V���|F�LiN}'�����8�F�^.��n+�PԆ^qb�^��T�<Ť���Ё��Q����*p09�K4�������l���^Z��߅",��"����*�W�T�\l�Ԃ�nr@���х��yf�1Y���{I&�\>��2\���t;7O�^r�Y?��6�]�k3<�k���7���Jof�h���n��
��Ty���*[�|岼;�t�ͪ0=
i�p���\��:;��dQ��3]��S�aPG)��j.�&Pj�Z?�c���f|la,��j.�1Vƽ��d��_M��������1�/"'�ǆ�J��᪵�v��G��4��e�X� X.@H�nqӯ�����Rz���ziW`]}�cN���/��ģh�K�������*�l�Uy°��JN��Ckm�ޓ�ͺ�������Ñ�s3�Ole����q���
�1�U6B��V�]�R��O��)�4��G�(����}@�j����~Wۈ�_�eP�4����!	��B�E�An���_��(G�����������9���w�!N�>�"�Jn�g�*՛�M2�k���1�\3�^��?���V��Ȏj�
 �>�Bʁ��z�=�r.�[ÑN8|WΙ�U��:�+���DQ;ۓ�cls���r��<��SI!Θ�B��NA��xdZY $���#�N �$��8�^T���5��^�Ud"-N`���:�8�M�f�p�Ȗ]��	z�w��y�|A��i!����d�s>zjiH�Ʌ�XS�����v�ե�~�k�A�y���FH�4�xk{�uٴ��ߪ��ғ_������f*�Br������Ue�d�Q}|&�5-��kg�r
gk��Ӿo���Op��� ��U%�WC�N~�j��^�P�ٱ&��0.�8�����@��׿-v{u�����t�ьZ�Ha�W�H�UO�32	�P2����k7��,�N\��G������d�S���k����j��X�$KC@���^�J���m4���r�����F��x�%�?��ޜO�xf���
�Q�3jąB�5�ˢ&j	�N�_Щ��!��|������*�/�pB.������5����R��5�!�Z�����-��� e��w�H�c��l�\���Zү���g������Y��;��]�4��>^�o2n�"Z!��6(���\�{�J�n�՗��w��������'���#�����?����=�L=;�}�ADM��?��T�Y�V#�F��5���������S�$��N'�"�']��)��%'�t��Q4��f����q�ʇ�Yd��e�9 �Q1a�y�9��!(�PC83�+t�\Qޔ Mu��"���ru���E��%�V�Dzg��Kp�<�Dvٜ�~
�������\��?Qӓ��Ћ����\��R;s�y�C��_z9��8H�t �5�di��=o��s[�ʃ��:�*K��0/�~{/a�!��g�P��Yؼ@�=Z����7�/%�⚋S�烥��e+�?�-�bG>���Č�� �ӫ�閺��y����� �JX�A��������ofj%�mj�(m+���_��~��l�RK�6�� $�Y��yx�-Bսw�o_��o�b5B���ם:z/#�rHƽ>�Z�N9�ӱFB!LJͮ��n�)�����*2��td�L�Y�}#1�V8�)�[e=�lfr=
5J9�*j�r�%���˩r���Hgkܝّ�j�%��}����>�|��G��#Wj�-"���-��p�E��%���򦫥���Sd�����yā:u����=j1+�jh9��`�5D�
Fj4Ծ��frʴ����Ia����{�e-�l�p�
��=���%����~D��=����?���<.�rʜ�h�Qo��4�*C��`�{l�~D��gK��!�G��宪Y#"������@�kG����wl�f�*�*�h��:Ok��ՈwC꘥��4KH�XX|�Q����E���ޏ1�<��F�6�}� ������C9M���qث��5#2�Z=���e�l��]>�$�B�B�Cn;�U#pK-�au�$���d�4���'�g����s�{��ux��I��(G��O�wr_��Ű�K2��x�bؓ�0[Q����_������g����+�,����z��kL��CF�ξ��h�B$a�eb�"�z�@_)}�Ra��0Q6-�ҽ��x�+5�)$y�ksv��:p|Zr=�5�	o��/'�UI�(�j�����a�~xؑ��D�%�gɻ���n�p�9R����:��3�Gq�(��?��uw]p�|Zf����(�DN*Y��:�.�'cUwH6���z� (�}(x�O�~���gp��\�ؐ�<7��!��1�T|I(��o��qء���w��	��mykr��%��}���:}Ďl�|��k㱀8������C����d��J�B]dL�Ρ<�Dj}�aG9/������g:>I��,�Ɉ��Ff�is�<�-���^˞wb����ੑ��nH@*3ߪ�c.��B�n��w�����%�T	E\*�&5�x[ĉ����aCګ�R��X���\��-	o�&20�0]b2�ؒp13dA.V�1C���0F"�:��K�Ԉ��K�}�7|)�Qա_�Vsɚp��8Bjr���
�g�/%'�2�2@����x����}�/�泤�|u��Ģa��Po�{�|�\�O�vN�jkz��U����
\6��ప�_�گ�cϏ��8a#��El|�fN��,����[<��̂l�]������#%t~oCi��aԕ�w�@jP�J��%�c�(*1�cH`������șё���=}��-w^���d�S���&!o�P`�2�I��4�H����K�e�!�B�i�>�+ri�ri�R�KW��t1rerj�]�Hm���Y�E�Z"16�w��-�ǔW��B��Ic-nIg��+��?e�[�mG$�6-{�T6k�
�����~)@�K��K�Pڐ:�c�-\FxN�����`�E��r[�X 	��+���+>*�Y��GY�zJ������8パ�,�W�9���c�S_����G>�1M��N���D�o��+�j�w��b�5�3��/���("|8{X�k�Q}_.*rQcr<�ɱ���{T�>6gu��/��;����ȳ���k⍬����3s(��ђg�oɘ�R�q�H-��ò���c�GG�Ƙ�з��v3q�����VXR�[e$�2�M�!��t+�"\��p^�O��X��:�'���/�	V�`��N]�J�}���.dK�zV��>O��>B(�- �f��0,�6��p
�1�&k�-|.f�H�M���-"��e��C<$o����
����,w4晚S5���}��f�O�xj����N�!���W��I�qH�V���-7����!eu��϶KJ��[�r��<+d�Ҭ?o����/�ҳ+�v�m�O$	��@�3�������"��L����dӺ����v��Oq�X�	5f{*�.s!��Y�LfL�����&Mi�UV��B�*�6��4��J��L�Y]ܰv)��-�*n+⋣�I��/�2�#��QxW9}��2��޻���F��-;����3/3��ّ��+�h�j=�Ȱji(]="verde"
        self.aux.caracteristics["alas"]="negras"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/colibri_pico_ancho.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Zafiro oreja blanca"
        self.aux.description="Adulto: Macho: Ojos negros, pico rojo con la punta negra. Línea ocular blanca (muy conspicua), resto de la cabeza y gorja morado iridiscentes (aparentemente negras). Lados y flancos verdes; vientre y cobertoras inferiores de la cola blanquecinas. Espalda y cobertoras alares verdes. Cola redondeada oscura. Hembra: Parecida al macho adulto pero con frente grisácea, zona malar blanca, nuca verde, vientre grisáceo, punta de rectrices exteriores blancas y garganta, pecho, flancos y lados blanquecinos con filas de motas verdes. Juvenil: Parecido a la hembra adulta pero con tonos más opacos y deslavados."
        self.aux.habitat="claros y bordes de bosques montañosos (e.g., pino, pino-encino, encino) cercanos a arroyos. Sitios de posible observación en el bosque: claros en áreas de pino y eucalipto, vegetación secundaria nativa y vegetación circundante a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de néctar floral y en ocasiones consume insectos pequeños y arañas. Dado que el zafiro oreja blanca no es muy afín a los ecosistemas urbanos, cuando entra a ellos prefiere áreas con niveles bajos de perturbación, por lo que no se observa fuera de suburbios, parques y relictos de vegetación nativa."
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
        self.aux.name="Colibrí berilo"
        self.aux.description="Adulto: Macho: Ojos negros, pico rojo con la punta negra. Línea ocular blanca (generalmente inconspicua), resto de la cabeza verde oscuro iridiscente. Flancos, lados y vientre grisáceos. Espalda verde; rabadilla y cobertoras superiores de la cola café-canela. Alas café rojizo. Cola cuadrada (levemente emarginada) rojiza. Hembra: Parecida al macho adulto pero con coloración general verde opaca (no iridiscente). Juvenil: Parecido a la hembra adulta pero con vientre blanquecino y coloración general más clara."
        self.aux.habitat="Ecotonos y claros de bosques montañosos (principalmente encino) y sembradíos tropicales. Sitios de posible observación en el bosque: áreas arboladas con sotobosque en floración y vegetación circundante a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de néctar floral, en ocasiones consume insectos y rara vez pequeñas arañas. El colibrí berilo es uno de los colibríes endémicos de México y Centro América. Sin embargo, existen registros ocasionales en el Sur de Arizona y Suroeste de Texas (EUA)."
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
        self.aux.name="Colibrí corona violeta"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico rojo con la punta negra. Corona violeta. Garganta, pecho y vientre blancos, lados y flancos verde claro. Nuca, espalda y cobertoras del ala verde olivo. Alas oscuras. Cola emarginada verde olivo. Juvenil: Parecido al adulto pero con corona verde (en ocasiones con violeta claro en la frente)."
        self.aux.habitat="Matorrales, bosques, vegetación riparia y áreas semiabiertas. Sitios de posible observación en el bosque: prácticamente en cualquier sitio del bosque con plantas en floración y sitios cercanos a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de néctar floral, en ocasiones consume insectos y rara vez pequeñas arañas. Dadas las preferencias de hábitat del colibrí corona violeta, es común observarlo cercano a cuerpos de agua."
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
        self.aux.name="Momoto corona café"
        self.aux.description="Adulto: (sexos similares) Ojos cafés, pico largo y punteado negro. Corona rojiza, máscara negra rodeada por plumas azules y/o moradas. Pecho verde con mota central negra, vientre verde amarillento. Alas azul-verde. Cola verde (en ocasiones con tonalidades azules) con dos raquetas terminales (base azul-verde y punta negra). Juvenil: Parecido al adulto pero con coloración general menos intensa."
        self.aux.habitat="Bosques y matorrales. Sitios de posible observación en el bosque: áreas boscosas (e.g., pino, eucalipto, casuarina), cañadas con vegetación secundaria nativa y vegetación aledaña a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de frutos e insectos. El momoto corona café es una de las aves más coloridas y vistosas del Bosque Los Colomos. Debido al movimiento pendular de su cola larga, también recibe el nombre de pájaro reloj, o simplemente péndulo."
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
        self.aux.name="Martín pescador norteño"
        self.aux.description="Adulto: Macho: Ojos negros, pico negro con base gris. Marca loral blanca, resto de la cabeza azul con copete prominente. Collar blanco, franja pectoral azul con motas rojizas (inconspicuas generalmente), pecho y vientre blancos, flancos azules. Espalda, rabadilla y cobertoras superiores de la cola azules. Alas azules con motas blancas. Cola azul con rectrices exteriores barradas de blanco y negro. Hembra: Parecida al macho adulto pero con franja pectoral azul (con parches rojizos), una franja pectoral inferior rojiza, y lados y flancos rojizos. Juvenil: Parecido a la hembra adulta pero sin franja pectoral inferior."
        self.aux.habitat="Prácticamente en cualquier cuerpo de agua (e.g., ríos, lagos, pantanos, estuarios, bahías). Sitios de posible observación en el bosque: únicamente registrado en el Estanque de los patos."
        self.aux.comments="Se alimenta básicamente de peces y ocasionalmente consume cangrejos, ranas, mamíferos pequeños, aves pequeñas, lagartijas y frutos. Después del martín-pescador de collar (Megaceryle torquata), el martín pescador norteño es el martín pescador más grande del país."
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
        self.aux.description="Adulto: Macho: Ojos negros, pico gris oscuro (aparentemente negro). Corona roja, resto de la cabeza café-gris claro. Pecho café-gris claro, vientre amarillento, cobertoras inferiores de la cola barradas de blanco y negro. Espalda, rabadilla y alas barradas de blanco y negro. Cola negra con rectrices centrales y exteriores barradas de negro y blanco. Al vuelo exhibe parche blanquecino en la base de primarias. Hembra: Parecida al macho adulto pero sin corona roja. Juvenil: Parecido a la hembra adulta pero con el pico más corto"
        self.aux.habitat="Zonas áridas a semihúmedas (e.g., matorrales xerófitos, plantaciones). Sitios de posible observación en el bosque: principalmente eucaliptales, no obstante se puede observar en cualquier arbolado del bosque."
        self.aux.comments="Se alimenta de insectos, frutos, semillas y néctar floral. Durante la época reproductiva emite vocalizaciones fuertes y el cinceleo contra los árboles es mucho más frecuente. Al igual que la mayoría de los pájaros carpinteros, el carpintero del desierto anida en cavidades"
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
        self.aux.description="Adulto: Macho: Ojos negros, pico gris oscuro. Corona roja con borde negro, línea superciliar blanca, línea ocular negra, franja blanca de la frente a la nuca (unida a franja pectoral levemente amarillenta). Garganta roja con borde negro, vientre y cobertoras inferiores de la cola blancas jaspeadas de negro. Espalda barrada de blanco y negro. Alas negras con banda vertical blanca, plumas primarias barradas levemente de negro y blanco. Cola negra con rectrices centrales blancas barradas con negro. Hembra: Parecida al macho adulto pero con garganta blanca y con coloración amarillenta en pecho, cuello, nuca y espalda. Juvenil: Con mismos caracteres que los adultos pero con coloración general café amarillento claro."
        self.aux.habitat="Bosques de encino-pino, bordes de arbolados y huertos. Sitios de posible observación en el bosque: solamente registrado en áreas de casuarina y pino ubicadas al Norte del Estanque de los patos."
        self.aux.comments="Se alimenta de savia, insectos y frutos. Por su hábito alimenticio, el chupasavia maculado deja anillos de perforaciones en los árboles, elemento con el cual se puede inferir su presencia (en algunos casos). Este chupasavia es silencioso en comparación con los demás pájaros carpinteros, por lo que en ocasiones puede pasar desapercibido."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="blanco negro"
        self.aux.caracteristics["alas"]="blanco negro"
        self.aux.caracteristics["cola"]="negro"
        self.aux.image="sources/chupasavia_maculado.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Mosquero copetón"
        self.aux.description="Adulto: (sexos similares) Ojos negros, maxila negra, mandíbula rosácea. Anillo ocular blanco proyectado hacia el dorso, cabeza café rojiza con copete prominente. Cara, garganta y pecho café-canela, vientre amarillo-canela. Nuca y espalda café-olivo. Alas café oscuro con dos barras alares blanquecinas y borde de secundarias y terciarias amarillo-canela. Cola café. Juvenil: Parecido al adulto pero con coloración general más pálida y con barras alares más anchas"
        self.aux.habitat="Bosques de niebla, de pino, pino-encino, encino y áreas semiáridas abiertas. Sitios de posible observación en el bosque: áreas con arbolados densos (e.g., zonas de eucalipto, pino y/o casuarina)."
        self.aux.comments="Se alimenta principalmente de insectos. Comúnmente se posa en perchas visibles. En caso de estar alarmado, su comportamiento se torna inquieto, mueve incesantemente la cola y eleva aún más su copete."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="cafe"
        self.aux.caracteristics["pecho"]="cafe-canela"
        self.aux.caracteristics["vientre"]="amarillo-canela"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="cafe"
        self.aux.image="sources/mosquero_copeton.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Pibí Tengofrío"
        self.aux.description="Adulto: (Sexos similares) Ojos negros, maxila negra, mandíbula rosácea. Anillo ocular blanquecino, loras gris claro, resto de la cabeza gris oscuro con copete prominente. Garganta y pecho gris claro, vientre amarillo deslavado. Alas oscuras con dos barras alares grises. Escapulares gris claro. Cola gris. Juvenil: Parecido al adulto pero con cobertoras inferiores de la cola y vientre amarillo claros; barras alares café claro."
        self.aux.habitat="Bosques de pino, pino-encino y encino. Sitios de posible observación en el bosque: Prácticamente en cualquier área del bosque."
        self.aux.comments="Se alimenta principalmente de insectos. Al igual que la mayoría de los tiránidos, este pibí se posa en perchas visibles y las utiliza como sitio base para acechar a los insectos que caza al vuelo."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="cafe"
        self.aux.caracteristics["pecho"]="gris"
        self.aux.caracteristics["vientre"]="amarillo"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="cafe"
        self.aux.image="sources/pibi_tengofrio.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Mosquero mínimo"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico negro con la base de la mandíbula amarillo-anaranjada. Anillo ocular y loras blancas, resto de la cabeza gris-café. Garganta y vientre blancos, pecho gris-café claro. Espalda y rabadilla grises. Alas negras con dos barras alares blancas; secundarias y terciarias con borde blanquecino. Cola emarginada gris. Juvenil: Parecido al adulto pero con toda la mandíbula inferior amarillo-anaranjada, dos barras alares café claro y vientre amarillo deslavado."
        self.aux.habitat="Bosques, pastizales y borde de caminos rurales. Sitios de posible observación en el bosque: prácticamente en cualquier área del bosque con excepción de áreas altamente frecuentadas por los usuarios del bosque y/o no arboladas."
        self.aux.comments="Se alimenta principalmente de insectos y arañas, ocasionalmente consume frutos. Debido a que algunas especies del género Empidonax son prácticamente indistinguibles entre sí, se recomienda identificarlos hasta nivel de género. No obstante, el canto es una de sus marcas de campo más confiables. El canto del mosquero mínimo es un psí metálico constante en grupos de 4 a 9 emisiones por vocalización (número de repeticiones variable)."
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
        self2.aux.habitat="Prácticamente cualquier hábitat acuático (e.g., lagos, pantanos, charcas, playas y manglares). Sitios de posible observación en el bosque: comúnmente sobrevuela el bosque al amanecer en dirección Suroeste-Noreste."
        self2.aux.comments="Se alimenta principalmente de peces, insectos y crustáceos. Ocasionalmente consume caracoles, ranas, lagartijas y pequeños roedores. Anteriormente, en los 1800s, sus plumas eran utilizadas para decorar sombreros, razón por la cual sus poblaciones decayeron. Afortunadamente, en la actualidad ya no es utilizada con ese fin y sus poblaciones han vuelto a la normalidad."
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
    #Oculta la vista del apartado de clasificación
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