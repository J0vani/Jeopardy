import wx
import wx.lib.buttons

##utilizar foor loop
app = wx.App(False)

# https://www.python-course.eu/python3_functions.php
# https://www.quora.com/How-do-I-call-a-variable-from-another-function-in-Python
# https://stackoverflow.com/questions/48653549/creating-a-button-with-a-bitmap-image-wxpython

class Windows(wx.Frame):
    def __init__(self, parent, title):
        super(Windows, self).__init__(parent, title=title, size=(1000, 600))
        #self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("PFONDO.jpg", wx.BITMAP_TYPE_ANY))
        self.num = 0
        self.InitUI()
        self.Center()
        self.Show()
        sumapuntos = 0

        font1 = wx.Font(16, wx.ROMAN, wx.ITALIC, wx.NORMAL)

        #colorFrame = wx.Colour(40, 143, 245)
        #self.SetBackgroundColour(colorFrame)
        #self.SetBackgroundStyle("PFONDO.jpg")


        q = wx.Panel(self, size=(1000, 50))

        t1 = wx.StaticText(q, label="Teoría Básica", pos=(80, 0))
        t1.SetFont(font1)
        t2 =wx.StaticText(q, label="Identif ED's", pos=(330, 0))
        t2.SetFont(font1)
        t3 = wx.StaticText(q, label="Teoría ", pos=(555, 0))
        t3.SetFont(font1)
        t33 = wx.StaticText(q, label="Preelim. ", pos=(600, 0))
        t33.SetFont(font1)
        t4 = wx.StaticText(q, label='Libre ', pos=(850, 0))
        t4.SetFont(font1)

        r = wx.Panel(self, size=(1000, 20), pos=(0, 500))

        self.Boton1 = wx.Button(r, label="EQUIPO 1", pos=(200, 0))
        self.Boton2 = wx.Button(r, label="EQUIPO 2", pos=(700, 0))

        '''def puntaje(puntos,sumapuntos):

            if (puntos != 0):
                sumapuntos = sumapuntos + puntos
                return sumapuntos'''
        self.Puntaje1 = wx.StaticText(r, -1, "0", (150, 0))
        self.Puntaje2 = wx.StaticText(r, -1, "0", (600, 0))


        self.Boton1.Bind(wx.EVT_BUTTON, lambda a: (self.Boton1.SetLabel("LISTO"), self.Boton2.SetLabel("EQUIPO 2"),self.change()))
        self.Boton1.Bind(wx.EVT_BUTTON,
                         lambda a: (self.Boton1.SetLabel(int(Pun))))
        '''puntos = self.count
        v = puntaje(puntos, sumapuntos)
        sumapuntos = v
        cant = (str(sumapuntos))
        wx.StaticText(r, -1 ,cant,(200,50))'''

        self.Boton2.Bind(wx.EVT_BUTTON, lambda a: (self.Boton2.SetLabel("LISTO"), self.Boton1.SetLabel("EQUIPO 1"), self.change()))
        '''puntos = self.count
        v = puntaje(puntos, sumapuntos)
        sumapuntos = v
        cant = (str(sumapuntos))
        wx.StaticText(r, -1, cant,(700, 50))'''
    def change(self):
        if self.Boton2.GetLabel() == "LISTO":
            self.Puntaje1.SetLabel("SI")
        if self.Boton1.GetLabel() == "LISTO":
            self.Puntaje2.SetLabel("NO")

        # self.frame_number += 1
    def InitUI(self):

        p = wx.Panel(self, pos=(100, 200))

        gs = wx.GridSizer(6, 4, 0, 0)

        for i in range(1, 21):
            btn = "100"
            if i >= 5:
                btn = "200"
            if i >= 9:
                btn = "300"
            if i >= 13:
                btn = "400"
            if i >= 17:
                btn = "500"
            btns = wx.Button(p, label=btn, size=(250, 150))  # 0, wx.EXPAND
            btns.Bind(wx.EVT_BUTTON, self.nuevo_frame, btns)
            # print(self.num)
            # print(btns.myname)
            self.num += 1
            btns.myname = self.num
            # btns.myname = ["Dfault", self.num]
            # print(btns.myname)

            gs.Add(btns)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        p.SetSizer(gs)

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("PFONDO.jpg")
        dc.DrawBitmap(bmp, 0, 0)

    def nuevo_frame(self, event):
        bnt = event.GetEventObject().myname
        c = Question()
        c.numbers_to_question(bnt)
        self.des = c.correct
        self.count = c.value
        if c.a.find('.png') != -1:
            ra = wx.Bitmap(c.a, wx.BITMAP_TYPE_ANY)
            rb = wx.Bitmap(c.b, wx.BITMAP_TYPE_ANY)
            rc = wx.Bitmap(c.c, wx.BITMAP_TYPE_ANY)
            rd = wx.Bitmap(c.d, wx.BITMAP_TYPE_ANY)


        wx.Frame.__init__(self, parent=None, title="ventana", size=(1000, 715))
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("P/"+c.image, wx.BITMAP_TYPE_ANY))
        self.Show()
        self.Center()
        q = wx.Panel(self, size=(770, 370), pos=(206, 208))

        if c.a.find('.png') != -1:
            btn_a = wx.BitmapButton(q, 1,ra, pos=(0, 0),size=(715,70))
            btn_a.SetBackgroundColour("#F7F7F7")
            btn_a.Bind(wx.EVT_BUTTON, self.cosas)
            print(btn_a.GetId())
        else:
            btn_a = wx.lib.buttons.GenButton(q, label=c.a, pos=(0, 0), size=(715, 70), name="c.a", id=1)
            btn_a.Bind(wx.EVT_BUTTON, self.cosas)
            btn_a.SetBackgroundColour("#F7F7F7")

        if c.b.find('.png') != -1:
            btn_b = wx.BitmapButton(q, 2, rb, pos=(15, 100), size=(715, 70))
            btn_b.SetBackgroundColour("#F7F7F7")
            btn_b.Bind(wx.EVT_BUTTON, self.cosas)
            print(btn_b.GetId())
        else:
            btn_b = wx.lib.buttons.GenButton(q, label=c.b, pos=(15, 100), size=(715, 70), name="c.b", id=2)
            btn_b.Bind(wx.EVT_BUTTON, self.cosas)
            btn_b.SetBackgroundColour("#F7F7F7")

        if c.c.find('.png') != -1:
            btn_c = wx.BitmapButton(q, 3, rc, pos=(35, 200), size=(715, 70))
            btn_c.SetBackgroundColour("#F7F7F7")
            btn_c.Bind(wx.EVT_BUTTON, self.cosas)
            print(btn_c.GetId())
        else:
            btn_c = wx.lib.buttons.GenButton(q, label=c.c, pos=(35, 200), size=(715, 70), name="c.c", id = 3)
            btn_c.Bind(wx.EVT_BUTTON, self.cosas)
            btn_c.SetBackgroundColour("#F7F7F7")

        if c.d.find('.png') != -1:
            btn_d = wx.BitmapButton(q, 4, rd, pos=(55, 300), size=(715, 70))
            btn_d.SetBackgroundColour("#F7F7F7")
            btn_d.Bind(wx.EVT_BUTTON, self.cosas)
            print(btn_d.GetId())
        else:
            btn_d = wx.lib.buttons.GenButton(q, label=c.d, pos=(55, 300), size=(715, 70), name="c.d" , id = 4)
            btn_d.Bind(wx.EVT_BUTTON,self.cosas)
            btn_d.SetBackgroundColour("#F7F7F7")

    def cosas(self,event):
        v = event.GetId()
        print(v)
        #print(self.des)
        #print(v)
        sumapuntos = 0

        if self.des == v:
            if self.des == 1:
                wx.StaticBitmap(self, -1, wx.Bitmap("R/good.png", wx.BITMAP_TYPE_ANY), pos=(850, 208))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(865, 308))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(885, 408))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(905, 508))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/GoodAnswer.png", wx.BITMAP_TYPE_ANY), pos=(130, 120))
                x = self.count
                return x

            if self.des == 2:
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(850, 208))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/good.png", wx.BITMAP_TYPE_ANY), pos=(865, 308))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(885, 408))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(905, 508))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/GoodAnswer.png", wx.BITMAP_TYPE_ANY), pos=(130, 120))
                x = self.count

            if self.des == 3:
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(850, 208))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(865, 308))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/good.png", wx.BITMAP_TYPE_ANY), pos=(885, 408))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(905, 508))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/GoodAnswer.png", wx.BITMAP_TYPE_ANY), pos=(130, 120))
                x = self.count

            if self.des == 4:
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(850, 208))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(865, 308))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/bad.png", wx.BITMAP_TYPE_ANY), pos=(885, 408))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/good.png", wx.BITMAP_TYPE_ANY), pos=(905, 508))
                wx.StaticBitmap(self, -1, wx.Bitmap("R/GoodAnswer.png", wx.BITMAP_TYPE_ANY), pos=(130, 120))
                x = self.count

        else :wx.StaticBitmap(self, -1,wx.Bitmap("R/BadAnswer.png", wx.BITMAP_TYPE_ANY),pos=(130, 120))
        x = -self.count

        '''if (x != 0):
            sumapuntos = sumapuntos + puntaje1
            return sumapuntos'''

class Question(object):  # wx.Frame

    # def __init__(self, title, parent=None):
    # w = Windows.InitUI(None)
    def numbers_to_question(self, argument):
        """Dispatch method"""
        method_name = 'quest_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid quest")
        # Call the method as we return it
        return method()

    def quest_1(self):
        self.a = "A) Es una ecuación que se puede derivar con respecto a una o más variables independientes"
        self.b = "B) Es una ecuación que se puede derivar con respecto a una o más variables dependientes"
        self.c = "C) Es una ecuación que contiene derivadas de una o más funciones con \n respecto a una o más variables independientes"
        self.d = "D) Es una ecuación que contiene derivadas con respecto a una o más variables dependientes"
        self.image = "TB100.png"
        self.correct = 3
        self.value = 100
        return self.a, self.b, self.c, self.d, self.image, self.correct,self.value

    def quest_2(self):
        self.a = "A) Primer orden, parcial"
        self.b = "B) Segundo orden, ordinaria"
        self.c = "C) Segundo orden, parcial"
        self.d = "D) Primer orden, ordinaria"
        self.image = "ID100.png"
        self.correct = 4
        self.value = 100
        return self.a, self.b, self.c, self.d, self.image

    def quest_3(self):
        self.a = "A) Es una función que al sustituirse en la ecuación diferencial la reduce a una identidad"
        self.b = "B) Es una función que al integrarse genera una identidad equivalente a la ecuación original"
        self.c = "C) Es una función que se puede derivar y factorizar para ser sustituible"
        self.d = "D) Es una ecuación que puede derivarse y sustituirse en un diferencial"
        self.image = "TP100.png"
        self.correct = 1
        self.value = 100
        return self.a, self.b, self.c, self.d, self.image

    def quest_4(self):
        self.a = "QUESTIONS/QL100/a.png"
        self.b = "QUESTIONS/QL100/b.png"
        self.c = "QUESTIONS/QL100/c.png"
        self.d = "QUESTIONS/QL100/d.png"
        self.correct = 3
        self.value = 100
        self.image = "L100.png"
        return self.a, self.b, self.c, self.d, self.image

    def quest_5(self):
        self.a = "A) Es aquella ecuación diferencial que puede ser expresada en función de una variable independiente exclusivamente."
        self.b = "B) Es aquella ecuación diferencial que contiene derivadas con respecto a solo una variable independiente"
        self.c = "C) Es aquella ecuación diferencial que contiene derivadas con respecto a solo una variable dependiente"
        self.d = "D) Es aquella ecuación diferencial que contiene derivadas con respecto a dos o mas variables independientes."
        self.image = "TB200.png"
        self.correct = 2
        self.value = 200
        return self.a, self.b, self.c, self.d, self.image

    def quest_6(self):
        self.a = "A) Tercer orden, ordinaria."
        self.b = "B) Segundo orden, ordinaria."
        self.c = "C) Tercer orden, parcial."
        self.d = "D) Segundo orden, parcial."
        self.image = "ID200.png"
        self.correct = 2
        self.value = 200
        return self.a, self.b, self.c, self.d, self.image

    def quest_7(self):
        self.a = "A) Soluciones generales y particulares."
        self.b = "B) Soluciones globales y particulares."
        self.c = "C) Soluciones explícitas e implícitas. "
        self.d = "D) Soluciones explícitas e iniciales."
        self.image = "TP200.png"
        self.correct = 3
        self.value = 200
        return self.a, self.b, self.c, self.d, self.image

    def quest_8(self):
        self.a = "A) Smith, Azimov, Einstein."
        self.b = "B) Copérnico, Diderot, Chambers."
        self.c = "C) Leibniz, Bernoulli, Euler."
        self.d = "D) Deming, Watson, Volta"
        self.image = "L200.png"
        self.correct = 3
        self.value = 200
        return self.a, self.b, self.c, self.d, self.image

    def quest_9(self):
        self.a = "A) El exponente más alto en la ecuación diferencial."
        self.b = "B) La maxima cantidad de derivadas presentes en la ecuación diferencial."
        self.c = "C) El posicionamiento de las derivadas en la ecuación diferencial."
        self.d = "D) La máxima derivada presente en dicha ecuación diferencial."
        self.image = "TB300.png"
        self.correct = 4
        self.value = 300
        return self.a, self.b, self.c, self.d, self.image

    def quest_10(self):
        self.a = "A) Sexto orden, ordinaria, variable dependiente t. "
        self.b = "B) Quinto orden, parcial, variable dependiente t. "
        self.c = "C) Sexto orden, ordinaria, variable dependiente w. "
        self.d = "D) Quinto orden, ordinaria, variable dependiente w."
        self.image = "ID300.png"
        self.correct = 4
        self.value = 300
        return self.a, self.b, self.c, self.d, self.image

    def quest_11(self):
        self.a = "A) Soluciones globales y particulares"
        self.b = "B) Soluciones generales y particulares."
        self.c = "C) Soluciones explícitas e implícitas."
        self.d = "D) Soluciones explícitas e iniciales."
        self.image = "TP300.png"
        self.correct = 2
        self.value = 300
        return self.a, self.b, self.c, self.d, self.image

    def quest_12(self):
        self.a = "QUESTIONS/QL300/a.png"
        self.b = "QUESTIONS/QL300/b.png"
        self.c = "QUESTIONS/QL300/c.png"
        self.d = "QUESTIONS/QL300/d.png"
        self.image = "L300.png"
        self.correct = 2
        self.value = 300
        return self.a, self.b, self.c, self.d, self.image

    def quest_13(self):
        self.a = "A) Parciales y No parciales."
        self.b = "B) Ordinarias y Lineales."
        self.c = "C) Parciales y ordinarias."
        self.d = "D) Explicitas e implícitas."
        self.image = "TB400.png"
        self.correct = 3
        self.value = 400
        return self.a, self.b, self.c, self.d, self.image

    def quest_14(self):
        self.a = "A) Sexto orden, ordinaria, variable independiente t."
        self.b = "B) Quinto orden, ordinaria, variable dependiente w."
        self.c = "C) Sexto orden, ordinaria, variable dependiente t."
        self.d = "D) Quinto orden, ordinaria, variable independiente w."
        self.image = "ID400.png"
        self.correct = 1
        self.value = 400
        return self.a, self.b, self.c, self.d, self.image

    def quest_15(self):
        self.a = "A) Para conocer su solucion general."
        self.b = "B) Para conocer su solución explícita."
        self.c = "C) Para conocer su solución implícita. "
        self.d = "D) Para conocer su solución particular."
        self.image = "TP400.png"
        self.correct = 4
        self.value = 400
        return self.a, self.b, self.c, self.d, self.image

    def quest_16(self):
        self.a = "QUESTIONS/QL400/a.png"
        self.b = "QUESTIONS/QL400/b.png"
        self.c = "QUESTIONS/QL400/c.png"
        self.d = "QUESTIONS/QL400/d.png"
        self.image = "L400.png"
        self.correct = 1
        self.value = 400
        return self.a, self.b, self.c, self.d, self.image

    def quest_17(self):
        self.a = "QUESTIONS/QTB500/a.png"
        self.b = "QUESTIONS/QTB500/b.png"
        self.c = "QUESTIONS/QTB500/c.png"
        self.d = "QUESTIONS/QTB500/d.png"
        self.image = "TB500.png"
        self.correct = 1
        self.value = 500
        return self.a, self.b, self.c, self.d, self.image

    def quest_18(self):
        self.a = "A) Octavo orden, ordinaria, variable independiente t, lineal."
        self.b = "B) Quinto orden, ordinaria, variable dependiente w, no lineal."
        self.c = "C) Quinto orden, ordinaria, variable dependiente t, lineal."
        self.d = "D) Octavo orden, ordinaria, variable independiente t, no lineal."
        self.image = "ID500.png"
        self.correct = 4
        self.value = 500
        return self.a, self.b, self.c, self.d, self.image

    def quest_19(self):
        self.a = "A) Para determinar si una ecuación diferencial existe."
        self.b = "B) Para determinar si existe una única ecuación diferencial en el fenómeno analizado."
        self.c = "C) Para determinar si existe una solución de una ecuación diferencial y saber si es única."
        self.d = "D) Para determinar si la solución de una ecuación diferencial es explícita o implícita."
        self.image = "TP500.png"
        self.correct = 3
        self.value = 500
        return self.a, self.b, self.c, self.d, self.image

    def quest_20(self):
        self.a = "QUESTIONS/QL500/a.png"
        self.b = "QUESTIONS/QL500/b.png"
        self.c = "QUESTIONS/QL500/c.png"
        self.d = "QUESTIONS/QL500/d.png"
        self.image = "L500.png"
        self.correct = 4
        self.value = 500
        return self.a, self.b, self.c, self.d, self.image


Windows(None, title="Jeopardy")
app.MainLoop()