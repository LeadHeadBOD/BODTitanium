##///
##||| SCORERWIDGETS.PY TITANIUM
##||| Change list:
##||| * Small key icons next to key names should now properly scale.
##||| * 
##||| * 
##||| * 
##||| * 
##||| * 
##\\\ 





import BUIx
import Bladex
import Raster
import Interpolator
#import Enm_Def
import Reference
import math
import pdb
import netgame
import WidgetsExtra
import types
import Language
import MenuText

font_server=BUIx.B_FontServer()

class B_GameTextWidget(BUIx.B_TextWidget):
  def __init__(self,parent,name):
    BUIx.B_TextWidget.__init__(self,parent,name,"\n\n\n\n\n",font_server,Language.MapaDeLetrasHi)
    self.Background=BUIx.B_RectWidget(self,name+"Background",0,0)
    self.Background.SetSolid(1)
    self.SetDrawFunc(self.Draw)
    self.SetScale(0.25)

  def SetAlpha(self,al):
    BUIx.B_TextWidget.SetAlpha(self,al)
    #self.Background.SetAlpha(al*0.5)

  def Draw(self,x,y,time):
    self.Background.DefDraw(x,y,time)
    self.DefDraw(x,y,time)    # Posibles etiquetas.

  def SetText(self,txt):
    BUIx.B_TextWidget.SetText(self,txt)
    w,h=self.GetSize()
    self.Background.SetSize(w,h)





class BarIncClass(Interpolator.LinearInt):
  def __init__(self,init_value,end_value,widget):
    Interpolator.LinearInt.__init__(self,init_value,end_value)
    self.widget=widget

  def Execute(self,value):
    ret=Interpolator.LinearInt.Execute(self,value)
    self.widget.SetPosition(ret,0)

  def EndExecute(self):
    self.widget.FinalUpdate()









class B_SmoothBarWidget(BUIx.B_BarWidget):
  def __init__(self,parent,name,width,height):
    BUIx.B_BarWidget.__init__(self,parent,name,width,height)
    self.interpolator=Interpolator.Interp("interp"+name,0)
    self.Updating=0
    self.CurrentTarget=self.GetPosition()


  def SetPosition(self,pos,smooth=1):
    currpos=self.GetPosition()
    if currpos==pos:
      return

    if smooth:
      if self.Updating==1:
        if self.CurrentTarget!=pos:
          #Si ya est� actualizando y recibe una nueva petici�n para otra posici�n
          # Trata de atenderla m�s tarde
          Bladex.AddScheduledFunc(Bladex.GetTime()+1.5,self.SetPosition,(pos,1))
          print "Posponed SetPosition",pos,smooth
          return
      else:
        self.Updating=1
        self.CurrentTarget=pos
        now=Bladex.GetTime()
        #print "Updating level bar: now:",now,"pos:",pos,"currpos:",currpos
        m_interp=BarIncClass(currpos,pos,self)
        self.interpolator.AddAction(now,now+1.5,m_interp)
    else:
      BUIx.B_BarWidget.SetPosition(self,pos)


  def FinalUpdate(self):
    self.Updating=0
    BUIx.B_BarWidget.SetPosition(self,self.CurrentTarget)







class B_Obj3DWidget(BUIx.B_RectWidget):
  def __init__(self,Parent,Name,width,Height,BODName,ObjectName=""):
    BUIx.B_RectWidget.__init__(self,Parent,Name,width,Height)
    self.SetData(self)
    self.BODName=BODName
    self.ObjectName=ObjectName
    self.SetDrawFunc(self.Draw)
    self.Selected=0
    self.Solid=0
    self.Border=0
    self.Scale=0.1


  def Draw(self,x,y,time):
    if self.BODName==None:
      return

    if self.GetVisible()==0:
      return

#    if self.Selected:
#      Raster.SetAlpha(1.0)
#    else:
#      Raster.SetAlpha(0.40)

    self.DefDraw(x,y,time)    # Posibles etiquetas.
    w,h=self.GetSize()
    Raster.SetAlpha(self.GetAlpha())
    if self.GetAutoScale():
      rw,rh=Raster.GetSize()
      self.Scale=0.1*rw/640.0

    rw, rh = Raster.GetSize()
    rwu, rhw = Raster.GetUnscaledSize()
    scale = rwu*1.0/rw
    Bladex.DrawBOD(self.BODName,x * scale,y * scale,w * scale,h * scale,self.Scale,1)

  def SetBOD(self,BODName):
    self.BODName=BODName

  def GetBOD(self):
    return self.BODName

  def SetObjectName(self,ObjectName):
    self.ObjectName=ObjectName

  def GetObjectName(self):
    return self.ObjectName


def GetUnusedKeys(inv):
      import darfuncs

      i = 0
      for j in range(inv.nKeys):
        key = Bladex.GetEntity(inv.GetKey(j))

        if type(key.Data) is types.IntType:
          auxval = key.Data
          key.Data = darfuncs.EmptyClass()
          key.Data.Used = auxval

        if key.Data==None:
          key.Data = darfuncs.EmptyClass()
          key.Data.Used = 1
        if key.Data.Used>0:
          i=i+1
      return i





if netgame.GetNetState() == 0:
  import Select

  ObjSlTimer = -500



  class B_InvKeyRing3DWidget(BUIx.B_TextWidget):
    def __init__(self,Parent,Name,width,Height,BODName,char):


      BUIx.B_TextWidget.__init__(self,Parent,Name,"",font_server,Language.MapaDeLetrasHi)
      self.SetChar(char)
      self.SetAlpha(1.0)
      self.Scale = 0.075
      self.SetScale(0.25)
      self.SetDrawFunc(self.Draw)
      self.SetVisible(1)
      self.SetColor(128,128,128)




    def SetChar(self,char):
      self.char=char
      self.inv=char.GetInventory()


    def Draw(self,x,y,time):
      global ObjSlTimer
      import darfuncs

      if self.inv.nKeys==0:
        return

      if self.GetVisible()==0:
        return

      Raster.SetAlpha(self.GetAlpha())

      i = 0
      for j in range(self.inv.nKeys):
        key = Bladex.GetEntity(self.inv.GetKey(j))

        if type(key.Data) is types.IntType:
          auxval = key.Data
          key.Data = darfuncs.EmptyClass()
          key.Data.Used = auxval


        if key.Data==None:
          key.Data = darfuncs.EmptyClass()
          key.Data.Used = 1
        if key.Data.Used>0:
          i=i+1

      Bladex.DrawBOD("Llavero",x+24,y+24,0,0,self.Scale,1)
      self.SetText(`i`)
      self.DefDraw(x+10,y+50,time)


  class B_InvKey3DWidget(BUIx.B_TextWidget):
    def __init__(self,Parent,Name,width,Height,BODName,char):


      BUIx.B_TextWidget.__init__(self,Parent,Name,"",font_server,Language.MapaDeLetrasHi)
      self.SetChar(char)
      self.SetAlpha(1.0)
      self.Scale = 0.075
      self.SetScale(0.25)
      self.SetDrawFunc(self.Draw)
      self.SetVisible(1)
      self.SetColor(128,128,128)




    def SetChar(self,char):
      self.char=char
      self.inv=char.GetInventory()


    def Draw(self,x,y,time):
      global ObjSlTimer
      import darfuncs

      if self.inv.nKeys==0:
        return

      if self.GetVisible()==0:
        return

      if self.inv.GetSelectedObject() != "KeyRing":
        return

      if ObjSlTimer < 0:
        return

      if ObjSlTimer + 5 < Bladex.GetTime():
        ObjSlTimer = -1
        return


      Raster.SetAlpha(self.GetAlpha())

      i = 0
      for j in range(self.inv.nKeys):
        key = Bladex.GetEntity(self.inv.GetKey(j))

        if type(key.Data) is types.IntType:
          auxval = key.Data
          key.Data = darfuncs.EmptyClass()
          key.Data.Used = auxval

        if key.Data==None:
          key.Data = darfuncs.EmptyClass()
          key.Data.Used = 1
        if key.Data.Used>0:
          rw, rh = Raster.GetSize()                                                                # 
          rwu, rhw = Raster.GetUnscaledSize()                                                      # 
          rscale = rwu*1.0/rw                                                                      # We need scaling for proper widescreen support
          xoffset = 16                                                                             # To anyone at FireFalcom/General Arcade/Sneg - yes, line 306 WAS used  
          yoffset = 8                                                                              # 
          Bladex.DrawBOD(key.Kind,(x+xoffset)*rscale,(y+yoffset)*rscale+i*32,0,0,self.Scale,1)     #  -LeadHead
          self.SetText(Select.GetSelectionData(key.Name)[2])
          self.DefDraw(x+24,y+i*16,time)
          i=i+1






  class B_InvTabletWidget(BUIx.B_TextWidget):
    def __init__(self,Parent,Name,Text,char,tbidx):
      #pdb.set_trace
      BUIx.B_TextWidget.__init__(self,Parent,Name,Text,font_server,"../../Data/Icons/Iconosrunas_hi.bmp");
      self.SetScale(0.25)
      self.SetChar(char)
      self.SetAlpha(1.0)
      self.SetColor(123,98,42)
      #self.Scale=0.0
      self.Name=Name
      self.tbidx = tbidx
      self.SetDrawFunc(self.Draw)

    def SetChar(self,char):
      self.char=char
      self.inv=char.GetInventory()


    def Draw(self,x,y,time):
      import GotoMapVars
      pt = GotoMapVars.PlacedTablets[self.tbidx]
      if (pt==0) and (self.inv.GetTablet(self.Name)==None):
        return

      if self.GetVisible()==0:
        return

      if pt:
        self.SetAlpha(0.25)
      else:
        self.SetAlpha(1.0)

      self.DefDraw(x,y,time)


  class B_InvSpecialKeyWidget(BUIx.B_BitmapWidget):
    def __init__(self,Parent,Name,width,Height,char):
      BUIx.B_BitmapWidget.__init__(self,Parent,Name,width,Height,Name,"../../Data/Icons/Iconosllaves.mmp");
      self.SetChar(char)
      self.SetAlpha(1.0)
      self.SetColor(255,255,255)
      self.Scale=0.0
      self.Name=Name
      self.SetDrawFunc(self.Draw)

    def SetChar(self,char):
      self.char=char
      self.inv=char.GetInventory()


    def Draw(self,x,y,time):

      #pdb.set_trace()
      if self.inv.GetSpecialKey(0)==None:
        return

      if self.inv.GetSpecialKey(self.Name)==None:
        self.SetAlpha(0.2)
      else:
        self.SetAlpha(1.0)


      #pdb.set_trace()
      if self.GetVisible()==0:
        return

      w,h=self.GetSize()
      self.DefDraw(x,y,time)










  def CreateEnemyWidget(RootName,Frame,set_autoscale=0,SizeXY=28):

    wEnemy=BUIx.B_BitmapWidget(Frame,RootName,SizeXY,SizeXY,"Demon","../../Data/Icons/Demon.bmp");
    wEnemy.SetColor(255,255,255)

    wVenomEnemy=WidgetsExtra.B_FlashBitmapWidget(Frame,RootName,SizeXY,SizeXY,"Enemy Poisoned","../../Data/Icons/Icono Veneno.bmp");
    wVenomEnemy.SetColor(255,255,255)
    wVenomEnemy.MaxAlpha=0.5
    wVenomEnemy.SetFlash(5)
    wVenomEnemy.SetVisible(0)
    wEnemy.AddLabel(wVenomEnemy,0.5,0.5,
                    BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                    BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
                    BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                    )

    wEnemyLifeLabel=BUIx.B_TextWidget(wEnemy,RootName+"LifeLabel","250",font_server,Language.MapaDeLetrasHi)
    wEnemyLifeLabel.SetScale(0.25)
    wEnemyLifeLabel.SetColor(255,0,0)
    wEnemyLifeLabel.SetAlpha(0.5)
    wEnemy.AddLabel(wEnemyLifeLabel,2,0,
                    BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom,
                    BUIx.B_Widget.B_FR_Right,BUIx.B_Widget.B_FR_Right,
                    BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                    )


    wEnemyLevelLabel=BUIx.B_TextWidget(wEnemy,RootName+"LevelLabel","8",font_server,Language.MapaDeLetrasHi)
    wEnemyLevelLabel.SetScale(0.25)
    wEnemyLevelLabel.SetColor(0,159,220)
    wEnemyLevelLabel.SetAlpha(0.5)
    wEnemy.AddLabel(wEnemyLevelLabel,1,0,
                    BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                    BUIx.B_Widget.B_FR_Right,BUIx.B_Widget.B_FR_Right,
                    BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                    )

    wEnemyLifeBar=WidgetsExtra.B_FlashBarWidget(wEnemy,RootName+"LifeBar",32,5)
    wEnemyLifeBar.SetFlashColor(53, 141, 36)
    wEnemyLifeBar.SetColor(255,0,0)
    wEnemyLifeBar.SetBackgroundColor(0,0,0)
    wEnemyLifeBar.SetFlash(0)
    wEnemyLifeBar.Continuous= 0
    wEnemyLifeBar.SetBackgroundAlpha(1.0)
    wEnemyLifeBar.SetAlpha(1.0)
    wEnemyLifeBar.SetBitmap("BitmapBarraEnemigo")
    wEnemy.AddLabel(wEnemyLifeBar,0.5,12,
                    BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom,
                    BUIx.B_Widget.B_FR_HCenter,BUIx.B_Widget.B_FR_HCenter,
                    BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                    )

    wEnemyKeyLabel=B_Obj3DWidget (wEnemy,RootName+"Key",32,32,"Llave")
    wEnemyKeyLabel.Scale=0
    wEnemyKeyLabel.SetAlpha(1.0)
    wEnemy.AddLabel(wEnemyKeyLabel,0.5,15+5,
                    BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom,
                    BUIx.B_Widget.B_FR_HCenter,BUIx.B_Widget.B_FR_HCenter,
                    BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                    )

    wEnemyObjLabel=B_Obj3DWidget(wEnemy,RootName+"Obj",32,32,"Pocima")
    wEnemyObjLabel.Scale=0
    wEnemyObjLabel.SetAlpha(1.0)
    wEnemy.AddLabel(wEnemyObjLabel,0.5,52+7,
                    BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom,
                    BUIx.B_Widget.B_FR_HCenter,BUIx.B_Widget.B_FR_HCenter,
                    BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                    )
    if set_autoscale:
      wEnemy.SetAutoScale(1)
      wVenomEnemy.SetAutoScale(1)
      wEnemyLifeLabel.SetAutoScale(1)
      wEnemyLevelLabel.SetAutoScale(1)
      wEnemyKeyLabel.SetAutoScale(1)
      wEnemyObjLabel.SetAutoScale(1)

    return wEnemy,wVenomEnemy,wEnemyLifeLabel,wEnemyLevelLabel,wEnemyKeyLabel,wEnemyObjLabel,wEnemyLifeBar









  # def CreateObjectWidget(RootName,BODName,Frame):
  #   wObject=B_Obj3DWidget(Frame,RootName,24,32,BODName)
  #   wObject.SetSolid(0)
  #   wObject.SetBorder(0)
  #   wObjectLabel=BUIx.B_TextWidget(wObject,RootName+"Label","",font_server,"../../Data/Mapa de letras.bmp")
  #   wObjectLabel.SetColor(170,170,170)
  #   wObjectLabel.SetAlpha(1.0)
  #   wObject.AddLabel(wObjectLabel,0.5,4,
  #                   BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom,
  #                   BUIx.B_Widget.B_FR_HRelative,BUIx.B_Widget.B_FR_HCenter,
  #                   BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
  #                   )
  #   return wObject,wObjectLabel







  CYCLE_SPEED = 0.25

  class B_ObjectsFrame(BUIx.B_FrameWidget):
    def __init__(self,Parent,Name,width,Height,char,InitObjPositions=[(0, 6),   (25, 6),   (50, 6),   (75, 6),   (100, 6),
                                                                      (0,40),   (25,40),   (50,40),   (75,40),   (100,40),
                                                                      (0,64),   (25,64),   (50,64),   (75,64),   (100,64),
                                                                      (0,98),   (25,98),   (50,98),   (75,98),   (100,98)]):
      BUIx.B_FrameWidget.__init__(self,Parent,Name,width,Height)
      self.wObjects=[]
      self.nObjects=len(InitObjPositions)
      self.SetChar(char)
      self.LastTime      = 0.0
      self.LastSelection = 0


      self.NameText=BUIx.B_TextWidget(self,"ObjName","",font_server,Language.MapaDeLetrasHi)
      self.NameText.SetScale(0.25)
      self.NameText.SetColor(255,255,255)
      self.NameText.SetAlpha(1.0)
      self.AddWidget(self.NameText,0.5,56,
                       BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                       BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
      # self.NameText.SetAutoScale(1)

      self.BarraBonita = BUIx.B_BitmapWidget(self,"ObjNameBg",125,20,"MARCOINVENTARIO","../../Data/marcoinventario.mmp");
      self.BarraBonita.SetColor(255,255,255)
      self.BarraBonita.SetAlpha(0.75)
      self.AddWidget(self.BarraBonita,0.5,52,
                       BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                       BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
      # self.BarraBonita.SetAutoScale(1)
      self.BarraBonita.SetVisible(0)


      for i in range(self.nObjects):
        self.AddNewObject("ObjectElement_"+str(i), InitObjPositions[i])
      self.AddWidgets()

      self.SetDrawFunc(self.Draw)



    def AddNewObject(self, object_name, InitObjPosition):
        wObj=B_Obj3DWidget(self,object_name,24,32,"Pocima")
        wObj.SetAlpha(1.0)
        wObj.InitAlpha=1.0
        wObj.Position=InitObjPosition
        wObj.Scale=0
        # wObj.SetAutoScale(1)
        self.wObjects.append(wObj)

    def Draw(self,x,y,time):
      self.DefDraw(x,y,time)    # Posibles etiquetas.

      nb=len(self.BODList)
      if nb>self.nObjects:
        print "Error in objects frame, trying to display more objects than "+`self.nObjects`
        return


      text = ""
      iCentral = 0
      for i in range(nb):
      	if self.inv.IsObjectSelected(i):
      	  iCentral = i

      if self.LastSelection != iCentral:
        self.LastTime      = time+CYCLE_SPEED
        self.LastSelection = iCentral

      if self.LastTime > time:
         DeltaVariation = (self.LastTime-time)/CYCLE_SPEED
      else:
         DeltaVariation = 0

      if nb>0:
        Advance = (3.1415*2)/nb
        for i in range(nb):
          wObjCurr=self.wObjects[i]

          Angle = Advance*(i-iCentral+DeltaVariation)
          SelFactor = (math.cos(Angle)+1.0)/2.0
          wx,wy = self.GetSize()
          rw,rh=Raster.GetSize()
          wx =wx*640/rw
          wy =wy*480/rh
          self.MoveWidgetTo(wObjCurr.Name(),(math.sin(Angle)+1.0)*(wx-25.0)/2.0,SelFactor*20.0)

          wObjCurr.SetBOD(self.BODList[i])
          wObjCurr.SetVisible(1)
          wObjCurr.SetAlpha((SelFactor**2)*0.9+0.1)

          nMaxItems=self.inv.GetMaxNumberObjectsAt(i)
          if self.inv.IsObjectSelected(i):
            if self.BODList[i] == "Llavero":
            	text = "("+`GetUnusedKeys(self.inv)`+") "
            elif nMaxItems>1:
                    nItems=self.inv.GetNumberObjectsAt(i)
                    text="("+str(nItems)+"/"+str(nMaxItems)+") "
            else:
                    text = ""

      if self.inv.GetSelectedObject():
        self.NameText.SetText(text+Select.GetSelectionData(self.inv.GetSelectedObject())[2])
        self.BarraBonita.SetVisible(1)
      else:
        self.NameText.SetText("")
        self.BarraBonita.SetVisible(0)

      for i in range(nb,self.nObjects):
        self.wObjects[i].SetVisible(0)

      self.RecalcLayout()


    def SetBODs(self,BODList):
      self.BODList = BODList


    def SetObjectNames(self,ObjectNameList):
      nb=len(ObjectNameList)
      if nb>self.nObjects:
        print "Error in objects frame, trying to display more objects than "+`self.nObjects`
        return

      for i in range(nb):
        wObjCurr=self.wObjects[i]
        wObjCurr.SetObjectName(ObjectNameList[i])


    def SetChar(self,char):
      self.char=char
      self.inv=char.GetInventory()



    def AddWidgets(self):
      for i in self.wObjects:
        self.AddWidget(i,i.Position[0],i.Position[1],
                       BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                       BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)





  class B_HandWidget(BUIx.B_FrameWidget):
    def __init__(self,Parent,Name,width,Height,Side,
                 InitObjAlpha=[1.0,0.3,0.2,0.1,0.05],
                 InitObjPositions=[(5,10),(35,20),(75,30),(110,40),(140,50)],
                 Wants_auto_scale=0):
      BUIx.B_FrameWidget.__init__(self,Parent,Name,width,Height)
      self.SetAutoScale(Wants_auto_scale)

      if(len(InitObjAlpha)!=len(InitObjPositions)):
        raise InitError, "Init size mismatch"

      self.nObjects=len(InitObjAlpha)
      self.Side=Side

      self.wObjects=[]
      for i in range(self.nObjects):
        wObj=B_Obj3DWidget(self,"HandElement_"+str(i),140,140,"Unset")
        wObj.SetAlpha(InitObjAlpha[i])
        wObj.InitAlpha=InitObjAlpha[i]
        wObj.Position=InitObjPositions[i]
        wObj.Scale=0.1
        wObj.SetAutoScale(Wants_auto_scale)
        self.wObjects.append(wObj)

      # Textos del objeto seleccionado
      self.wNameText=BUIx.B_TextWidget(self,"NameText","",font_server,Language.MapaDeLetrasHi)
      self.wNameText.SetScale(0.25)
      self.wNameText.SetColor(170,170,170)
      self.wNameText.SetAlpha(1.0)
      self.wNameText.SetAutoScale(Wants_auto_scale)
      self.wDefText=BUIx.B_TextWidget(self,"DefText","+0 DEF ",font_server,Language.MapaDeLetrasHi)
      self.wDefText.SetScale(0.25)
      self.wDefText.SetAlpha(1.0)
      self.wDefText.SetColor(255,0,0)
      self.wDefText.SetAutoScale(Wants_auto_scale)
      self.wPowText=BUIx.B_TextWidget(self,"PowText","+0 POW",font_server,Language.MapaDeLetrasHi)
      self.wPowText.SetScale(0.25)
      self.wPowText.SetAlpha(1.0)
      self.wPowText.SetColor(0,160,221)
      self.wPowText.SetAutoScale(Wants_auto_scale)
      self.wAltPowText=BUIx.B_TextWidget(self,"AltPowText","+0 POW",font_server,Language.MapaDeLetrasHi)
      self.wAltPowText.SetScale(0.25)
      self.wAltPowText.SetAlpha(1.0)
      self.wAltPowText.SetColor(0,160,221)
      self.wAltPowText.SetAutoScale(Wants_auto_scale)
      self.wResText=BUIx.B_TextWidget(self,"ResText","RESISTANCE: 0/0",font_server,Language.MapaDeLetrasHi)
      self.wResText.SetScale(0.25)
      self.wResText.SetAlpha(1.0)
      self.wResText.SetColor(119,241,252)
      self.wResText.SetAutoScale(Wants_auto_scale)

      self.AddWidget(self.wNameText,0.5,0,
                     BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                     BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

      self.AddWidget(self.wDefText,0.5,12,
                     BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_Right,
                     BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

      self.AddWidget(self.wPowText,0.5,12,
                     BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_Left,
                     BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

      self.AddWidget(self.wAltPowText,0.5,12,
                     BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                     BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

      self.AddWidget(self.wResText,0.5,24,
                     BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                     BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

      self.AddWidgets()

    def AddWidgets(self):
      wid_pos=BUIx.B_FrameWidget.B_FR_AbsoluteLeft
      wid_anc=BUIx.B_FrameWidget.B_FR_Left
      if self.Side!="Left":
        wid_pos=BUIx.B_FrameWidget.B_FR_AbsoluteRight
        wid_anc=BUIx.B_FrameWidget.B_FR_Right

      for i in self.wObjects:
        self.AddWidget(i,i.Position[0],i.Position[1],
                       wid_pos,wid_anc,
                       BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)



    def ResetPositions(self):
      for i in self.wObjects:
        self.RemoveWidget(i.Name(),0)
      self.AddWidgets()
      index=0
      for i in self.wObjects:
        i.SetAlpha(i.InitAlpha)
        index=index+1



    def SetBODs(self,BODList):
      nb=len(BODList)
      if nb>self.nObjects:
        print "Error in hand widgets, trying to display more objects than "+`self.nObjects`
        return

      for i in range(nb):
        self.wObjects[i].SetBOD(BODList[i])
        self.wObjects[i].SetVisible(1)

      for i in range(nb,self.nObjects):
        self.wObjects[i].SetVisible(0)

    def SetObjectNames(self,ObjectNameList):
      nb=len(ObjectNameList)
      if nb>self.nObjects:
        print "Error in hand widgets, trying to display more objects than "+`self.nObjects`
        return
      for i in range(nb):
        wObjCurr=self.wObjects[i]
        wObjCurr.SetObjectName(ObjectNameList[i])

    def SetText(self,name,power,defence,res,res_max):
      #print name,power,defence,res,res_max
      if power==None or name==None:
        self.SwitchOffText()
      if defence!=None and res!=None and res_max != None:
        self.SetNamePowDefResText(name,power,defence,res,res_max)
      elif res!=None and res_max != None:
        self.SetNamePowResText(name,power,res,res_max)
      elif defence!=None:
        self.SetNamePowDefText(name,power,defence)


    def SwitchOffText(self):
      self.wNameText.SetText("")
      self.wDefText.SetVisible(0)
      self.wPowText.SetVisible(0)
      self.wAltPowText.SetVisible(0)
      self.wResText.SetVisible(0)

    def SetNamePowDefText(self,name,power,defence):
      self.wNameText.SetText(name)

      self.wDefText.SetVisible(1)
      self.wPowText.SetVisible(1)
      self.wAltPowText.SetVisible(0)
      self.wResText.SetVisible(0)

      def_text= `defence`+' DEF '
      if defence>=0:
        def_text= '+'+def_text
        self.wDefText.SetColor(0,160,221)
      else:
        self.wDefText.SetColor(255,0,0)
      self.wDefText.SetText(def_text)

      power_text= `power`+' POW'
      if power>=0:
        power_text= '+'+power_text
        self.wPowText.SetColor(0,160,221)
      else:
        self.wPowText.SetColor(255,0,0)
      power_text= ' '+power_text
      self.wPowText.SetText(power_text)

      self.RecalcLayout()

    def SetNamePowResText(self,name,power,resistance,max_resistance):
      self.wNameText.SetText(name)

      self.wDefText.SetVisible(0)
      self.wPowText.SetVisible(0)
      self.wAltPowText.SetVisible(1)
      self.wResText.SetVisible(1)

      power_text= `power`+ ' ' + MenuText.GetMenuText("POW")
      if power>=0:
        power_text= '+'+power_text
        self.wAltPowText.SetColor(0,160,221)
      else:
        self.wAltPowText.SetColor(255,0,0)
      power_text= ' '+power_text
      self.wAltPowText.SetText(power_text)

      resistance_text= MenuText.GetMenuText("RESISTANCE") + ': '+`resistance`+' / '+`max_resistance`
      self.wResText.SetText(resistance_text)
      self.RecalcLayout()

    def SetNamePowDefResText(self,name,power,defence,resistance,max_resistance):
      self.wNameText.SetText(name)

      self.wDefText.SetVisible(1)
      self.wPowText.SetVisible(1)
      self.wAltPowText.SetVisible(0)
      self.wResText.SetVisible(1)

      def_text= `defence`+ ' ' + MenuText.GetMenuText("DEF")
      if defence>=0:
        def_text= '+'+def_text
        self.wDefText.SetColor(0,160,221)
      else:
        self.wDefText.SetColor(255,0,0)
      self.wDefText.SetText(def_text)

      power_text= `power`+ ' ' + MenuText.GetMenuText("POW")
      if power>=0:
        power_text= '+'+power_text
        self.wPowText.SetColor(0,160,221)
      else:
        self.wPowText.SetColor(255,0,0)
      power_text= ' '+power_text
      self.wPowText.SetText(power_text)

      resistance_text= MenuText.GetMenuText("RESISTANCE") + ': '+`resistance`+' / '+`max_resistance`
      self.wResText.SetText(resistance_text)
      self.RecalcLayout()


  class FadeInClass(Interpolator.LinearInt):
    def __init__(self,init_value,end_value,parent,widget):
      Interpolator.LinearInt.__init__(self,init_value,end_value)
      self.parent=parent
      self.widget=widget

    def Execute(self,value):
      ret=Interpolator.LinearInt.Execute(self,value)
      self.widget.MultiplyAlpha(ret)
      self.parent.view_status=1


    def EndExecute(self):
      self.parent.view_status=2






  class FadeOutClass(Interpolator.LinearInt):
    def __init__(self,init_value,end_value,parent,widget):
      Interpolator.LinearInt.__init__(self,init_value,end_value)
      self.parent=parent
      self.widget=widget

    def Execute(self,value):
      ret=Interpolator.LinearInt.Execute(self,value)
      self.widget.MultiplyAlpha(ret)
      self.parent.view_status=3

    def EndExecute(self):
      self.widget.SetVisible(0)
      self.parent.view_status=0







  class CycleClass:
    def __init__(self,init_value,end_value,parent,parentwidget,objwidget):
      self.init_value=init_value
      self.end_value=end_value
      self.periodX=end_value[0]-init_value[0]
      self.periodY=end_value[1]-init_value[1]
      self.periodAlpha=end_value[2]-init_value[2]
      self.periodWidth=end_value[0]-init_value[0]
      self.periodHeight=end_value[1]-init_value[1]
      self.parent=parent
      self.parentwidget=parentwidget
      self.objwidget=objwidget
      self.parent.view_status=2

    def Execute(self,value):
      ret=(self.init_value[0]+self.periodX*value,
           self.init_value[1]+self.periodY*value,
           self.init_value[2]+self.periodAlpha*value,
          )
      self.parentwidget.MoveWidgetTo(self.objwidget.Name(),ret[0],ret[1])
      self.objwidget.SetAlpha(ret[2])


    def EndExecute(self):
      self.parent.EndCycle()







  import pdb
  class InvControl:
    def __init__(self,name,widget,char,view_period=2.0,cycle_period=0.3,fadein_period=0.3,fadeout_period=0.3,
                 end_cycle_callback=None,Wants_auto_scale=0):
      self.view_time=-2.0       # Auxiliar
      self.cycle_time=-2.0      # Auxiliar
      self.cycle_count=0        # Auxiliar
      print "invcontrol",name

      self.view_period=view_period       # Tiempo que permanece visible
      self.cycle_period=cycle_period     # Tiempo que tarda en ciclar
      self.fadein_period=fadein_period   # Tiempo que tarda en aparecer
      self.fadeout_period=fadeout_period  # Tiempo que tarda en desaparecer
      self.view_status=0  #0:no visible, 1:Apareciendo, 2: Visible, 3: Desapareciendo
      self.widget=widget
      self.SetChar(char)
      self.interpolator=Interpolator.Interp(name,0)


      self.name=name
      self.m_FadeIn=FadeInClass(0.0,1.0,self,self.widget)
      self.m_FadeOut=FadeOutClass(1.0,0.0,self,self.widget)
      self.SetBODs()
      self.end_cycle_callback=end_cycle_callback


    def SetChar(self,char):
      self.char=char
      self.inv=char.GetInventory()

    def CycleFunc(self):
      #print "InvControl:CycleFunc"
      time=Bladex.GetTime()
      self.view_time=time
      Bladex.AddScheduledFunc(time+self.view_period,self.FadeOut,())


    def EndCycle(self):
      #print "InvControl:EndCycle"
      self.cycle_count=self.cycle_count+1
      if self.cycle_count==self.widget.nObjects:
        self.cycle_count=0
        self.CycleFunc()
        #pdb.set_trace()
        if self.widget.wObjects[0].GetVisible():
          name=Reference.GetObjectFriendlyName(self.widget.wObjects[0].GetBOD())
          power, defence, res, res_max= Reference.GiveObjectPowDefResResMaxData(self.widget.wObjects[0].GetObjectName())
          self.widget.SetText(name, power, defence, res, res_max)
        else:
          self.widget.SetText(None, None, None, None, None)




    def SetBODs(self):
      pass


    def FadeOut(self):
      time=Bladex.GetTime()
      if time-self.view_time>self.view_period:
        self.view_status=3
        if self.end_cycle_callback:
          #print "InvControl:FadeOut() entering end_cycle_callback: "+`self.end_cycle_callback`
          self.end_cycle_callback()
        self.interpolator.AddAction(time,time+self.fadeout_period,self.m_FadeOut)



    def CycleElements(self):
      #print "InvControl:CycleElements()"
      self.SetBODs()
      if self.widget.wObjects[0].GetVisible():
        name=Reference.GetObjectFriendlyName(self.widget.wObjects[0].GetBOD())
        power, defence, res, res_max= Reference.GiveObjectPowDefResResMaxData(self.widget.wObjects[0].GetObjectName())
        self.widget.SetText(name, power, defence, res, res_max)
      else:
        self.widget.SetText(None, None, None, None, None)

      #if self.char.Wuea==Enm_Def.WUEA_WAIT:
    #  return
      time=Bladex.GetTime()
      if self.view_status==2:  #Si es visible puedo ciclar
        if time-self.cycle_time>self.cycle_period:
          self.cycle_time=time
          self.view_time=time
          end_cycle_time=time+self.cycle_period

          if len(self.widget.wObjects)>1:
            init_list=[]
            for i in self.widget.wObjects:
              init_list.append(i.Position[0],i.Position[1],i.InitAlpha)

            len_init_list=len(init_list)
            m_Cycle=CycleClass(init_list[0],
                               init_list[self.widget.nObjects-1],
                               self,
                               self.widget,
                               self.widget.wObjects[0]
                              )
            self.interpolator.AddAction(time,end_cycle_time,m_Cycle)

            for i in range(1,len_init_list):
              m_Cycle=CycleClass(init_list[i],
                                 init_list[i-1],
                                 self,
                                 self.widget,
                                 self.widget.wObjects[i]
                                )
              self.interpolator.AddAction(time,end_cycle_time,m_Cycle)


      if time-self.view_time>self.view_period:
        if self.view_status==0:
          #pdb.set_trace()
          self.Alpha=0.0
          self.widget.MultiplyAlpha(self.Alpha)
          self.widget.SetVisible(1)
          self.view_status=1
          self.interpolator.AddAction(time,time+self.fadein_period,self.m_FadeIn)
          Bladex.AddScheduledFunc(Bladex.GetTime()+self.view_period,self.FadeOut,())
        elif self.view_status==1:
          pass
        elif self.view_status==2:
          pass
        #elif self.view_status==3:
          #self.view_status=1
          #Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,self.FadeIn,())
          #print "Not implemented"
        self.view_time=time



    def HideElements(self):
      if self.view_status==1:
        time=Bladex.GetTime()
        if time-self.view_time>1.0:
          self.view_status=0
          self.widget.SetVisible(0)
        else:
          Bladex.AddScheduledFunc(time+2.0,self.HideElements,())


  class InvArrowsControl(BUIx.B_FrameWidget):
    def __init__(self,Parent,Name,width,Height,char,wants_auto_scale=0):
      wants_auto_scale = 0
      #pdb.set_trace
      BUIx.B_FrameWidget.__init__(self,Parent,Name,width,Height)

      self.wNameText=BUIx.B_TextWidget(self,"NameText","UNSPECIFIED ARROWS",font_server,Language.MapaDeLetrasHi)
      self.wNameText.SetScale(0.25)
      self.wNameText.SetAlpha(1.0)
      self.wNameText.SetColor(170,170,170)
      self.AddWidget(self.wNameText,0.5,0,
                     BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                     BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

      self.wNumText=BUIx.B_TextWidget(self,"NumText","0/0",font_server,Language.MapaDeLetrasHi)
      self.wNumText.SetScale(0.25)
      self.wNumText.SetAlpha(1.0)
      self.wNumText.SetColor(0,159,220)
      # self.wNumText.SetAutoScale(1)
      self.AddWidget(self.wNumText,0.5,12,
                     BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                     BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

      self.SetChar(char)
      self.Name=Name
      self.SetDrawFunc(self.Draw)

      self.SetAutoScale(wants_auto_scale)
      self.wNumText.SetAutoScale(wants_auto_scale)
      self.wNameText.SetAutoScale(wants_auto_scale)

    def SetChar(self,char):
      self.char=char
      self.inv=char.GetInventory()


    def Draw(self,x,y,time):
      #pdb.set_trace()
      quiver= self.inv.GetSelectedQuiver()
      if not quiver:
        return

      #if quiver!=self.inv.GetLeftBack() and quiver!=self.inv.GetRightBack():
      if not self.inv.HoldingBow and not self.inv.HasBowOnBack:
        return

      object=Bladex.GetEntity(quiver)
      if Language.Current != "Chinese" and Language.Current != "Russian":
        self.wNameText.SetText(Reference.GetObjectFriendlyName(object.Data.ArrowType)+"s")
      else:
        self.wNameText.SetText(Reference.GetObjectFriendlyName(object.Data.ArrowType))
      self.wNumText.SetText(`object.Data.NumberOfArrows()`+"/"+`object.Data.MaxArrows`)
      self.RecalcLayout()
      w,h=self.GetSize()
      self.DefDraw(x,y,time)

  class InvShieldControl(InvControl):
    InvMode=0  # 0: Shields, 1:Quivers

    def CycleElements(self):
      #print "InvShieldControl:CycleElements()"
      if self.inv.HoldingShield or self.inv.HasShieldOnBack:
        self.SetInvMode(0)
      else:
        sel_weapon=self.inv.GetSelectedWeapon()
        if sel_weapon:
          sel_entity=Bladex.GetEntity(sel_weapon)
          if Reference.GiveObjectFlag(sel_weapon)==Reference.OBJ_BOW:
            self.SetInvMode(1)
          else:
            self.SetInvMode(0)
      InvControl.CycleElements(self)

    def CycleFunc(self):
      #pdb.set_trace()
      InvControl.CycleFunc(self)
      if self.InvMode==0:  #Shields
        self.inv.CycleShields()
      else:
        self.inv.CycleQuivers()
      self.SetBODs()
      self.widget.ResetPositions()


    def SetBODs(self):
      GetObjFunc=None

      nItems=0
      if self.InvMode==0:
        GetObjFunc=self.inv.GetShield
        nItems=self.inv.nShields
      else:
        GetObjFunc=self.inv.GetQuiver
        nItems=self.inv.nQuivers


      BODList=[]
      ObjectNameList=[]
      for i in range(nItems):
        Obj=GetObjFunc(i)
        ent=Bladex.GetEntity(Obj)
        BOD=ent.Kind
        BODList.append(BOD)
        Name=ent.Name
        ObjectNameList.append(Name)

      self.widget.SetBODs(BODList)
      self.widget.SetObjectNames(ObjectNameList)



    def SetInvMode(self,new_mode):
      if self.InvMode==new_mode:
        return

      self.InvMode=new_mode
      self.SetBODs()






  class InvWeaponsControl(InvControl):
    def __init__(self,name,widget,char,ShieldsControl,view_period=2.0,cycle_period=0.3,fadein_period=0.3,
                 fadeout_period=0.3,end_cycle_callback=None,Wants_auto_scale=0):
      InvControl.__init__(self,name,widget,char,view_period,cycle_period,fadein_period,fadeout_period,
                          end_cycle_callback,Wants_auto_scale)
      self.ShieldsControl=ShieldsControl



    def CycleFunc(self):
      #print "InvWeaponsControl:CycleFunc()"
      #pdb.set_trace()
      InvControl.CycleFunc(self)
      self.inv.CycleWeapons()
      self.SetBODs()
      self.widget.ResetPositions()

      if self.inv.HoldingShield or self.inv.HasShieldOnBack:
        self.ShieldsControl.SetInvMode(0)
      else:
        sel_weapon=self.inv.GetSelectedWeapon()
        if sel_weapon:
          sel_entity=Bladex.GetEntity(sel_weapon)
          if Reference.GiveObjectFlag(sel_weapon)==Reference.OBJ_BOW:
            self.ShieldsControl.SetInvMode(1)
          else:
            self.ShieldsControl.SetInvMode(0)


    def SetBODs(self):
      GetObjFunc=self.inv.GetWeapon
      BODList=[]
      ObjectNameList=[]
      for i in range(self.inv.nWeapons):
        Obj=GetObjFunc(i)
        ent=Bladex.GetEntity(Obj)
        BOD=ent.Kind
        BODList.append(BOD)
        Name=ent.Name
        ObjectNameList.append(Name)

      self.widget.SetBODs(BODList)
      self.widget.SetObjectNames(ObjectNameList)



  def AddKeyRingToInventory():
    import Actions
    import darfuncs
    if not Bladex.GetEntity("KeyRing"):
      KeyRing =Bladex.CreateEntity("KeyRing","Llavero",0,0,0)
      KeyRing.Static = 0
      darfuncs.SetHint(KeyRing,"Keys")
      Actions.TakeObject("Player1","KeyRing")


  class InvObjectsControl(InvControl):
    def __init__(self,name,widget,char,view_period=2.0,cycle_period=0.3,fadein_period=0.3,
                 fadeout_period=0.3,end_cycle_callback=None,Wants_auto_scale=0):
      InvControl.__init__(self,name,widget,char,
                          view_period,cycle_period,fadein_period,fadeout_period,
                          end_cycle_callback,
                          Wants_auto_scale)
      self.cycle_period=0.0     # Tiempo que tarda en ciclar
      self.end_cycle_callback = self.DeactivateUseFunc

    def DeactivateUseFunc(self):
      self.char.Data.InventoryActive = 0


    def CycleFunc(self):
      InvControl.CycleFunc(self)
      self.inv.CycleObjects()
      self.SetBODs()


    def SetBODs(self):
      BODList=[]
      ObjectNameList=[]
      for i in range(self.inv.nKindObjects):
        Obj0=self.inv.GetObject(i)
        ent=Bladex.GetEntity(Obj0)
        BOD=ent.Kind
        BODList.append(BOD)
        Name=ent.Name
        ObjectNameList.append(Name)

      self.widget.SetBODs(BODList)
      self.widget.SetObjectNames(ObjectNameList)




    def CycleElements(self):
      global ObjSlTimer
      if self.inv.nKeys:
       AddKeyRingToInventory()

      time=Bladex.GetTime()
      ObjSlTimer = time
      self.char.Data.InventoryActive = 1
      if self.view_status==2:  #Si es visible puedo ciclar
        if time-self.cycle_time>self.cycle_period:
          self.cycle_time=time
          self.view_time=time
          end_cycle_time=time+self.cycle_period
          self.CycleFunc()

      if time-self.view_time>self.view_period:
        if self.view_status==0:
          self.Alpha=0.0
          self.widget.MultiplyAlpha(self.Alpha)
          self.widget.SetVisible(1)
          self.view_status=1
          self.SetBODs()
          self.interpolator.AddAction(time,time+self.fadein_period,self.m_FadeIn)
          Bladex.AddScheduledFunc(Bladex.GetTime()+self.view_period,self.FadeOut,())
        elif self.view_status==1:
          pass
        elif self.view_status==2:
          pass
        elif self.view_status==3:
          #self.view_status=1
          #Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,self.FadeIn,())
          print "Not implemented"
        self.view_time=time
