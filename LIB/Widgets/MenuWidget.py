##///
##||| Widgets/MenuWidget.PY TITANIUM
##||| Change list:
##||| * v109 code merged with HD update code
##||| * Inaccessible Travelbook tabs now have grey text
##\\\ 

import BUIx
import Bladex
import Raster
import ScorerWidgets
import WidgetsExtra
import SpinWidget
import TextFXWidget
import pdb
#import Bldb
import BInput
#import IDebug
import BBLib
import MenuText
import sys
import string
import Language
import os
import Menu
import GameText
import netgame
import PanelFillerCommon
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition

#if netgame.GetNetState()==0:
#  import Scorer
global isQuitting
isQuitting = 0

BackButtonY = 100
BackGamepadButtonY = 70
AcceptBackY = 40
ColorWhite = [255, 255, 255]
ColorGrey = [123, 123, 123]

# global GamepadDisconnectMessageToDisplay
# GamepadDisconnectMessageToDisplay = 0

DefaultFont = Language.LetrasMenu

# if Bladex.IsRunningOnSteamDeck():
    # DefaultFont = Language.LetrasMenuBig

class Stack:
  def __init__(self):
    #print "Stack.__init__()"
    self.Items=[]

  def __del__(self):
    #print "Stack.__del__()"
    pass

  def nItems(self):
    return len(self.Items)

  def Push(self,item):
    self.Items.append(item)

  def Pop(self):
    self.Items=self.Items[:-1]

  def Top(self):
    try:
      return self.Items[-1]
    except:
      return None

  def Reset(self):
    self.Items=[]




class MenuStack(Stack):
  def __init__(self,final_callback):
    Stack.__init__(self)
    self.FinalCallBack=final_callback

  def Push(self,menu_item):
    #print "MenuStack Pushing",menu_item,"with refcount",sys.getrefcount(menu_item)
    s=self.Top()
    if not s:
      Bladex.SetAppMode("Menu")
    Bladex.SetRootWidget(menu_item.GetPointer())
    Stack.Push(self,menu_item)
    #print "RefCount (pushed)",sys.getrefcount(menu_item)

  def Pop(self):
    if isQuitting:
      Bladex.Quit()
    #print "MenuStack.Popping",self.Top(),"with refcount",sys.getrefcount(self.Top())
    Stack.Pop(self)
    s=self.Top()
    if s:
      Bladex.SetRootWidget(s.GetPointer())
    else:
      #print "Final CallBack"
      self.FinalCallBack()



class B_MenuFocusManager:
  def __init__(self):
    #print "B_MenuFocusManager.__init__()"
    self.MenuItems=[]
    self.Focus=None # Voy a llevar el foco aqu� en vez de dejarselo al C.

  def __del__(self):
    #print "B_MenuFocusManager.__del__()"
    self.Focus=None
    self.MenuItems=[]

  def AddMenuElement(self,menu_element):
    #print "B_MenuFocusManager.AddMenuElement()  (init)->",menu_element, sys.getrefcount(self)
    self.MenuItems.append(menu_element)
    self.Focus=menu_element
    #print "B_MenuFocusManager.AddMenuElement()  (end)->", sys.getrefcount(self)


  def GetFocus(self):
    return self.Focus


  def SetFocus(self,menu_element):
    accepts_focus=0
    try:
      accepts_focus=menu_element.AcceptsFocus()
    except:
      pass

    if accepts_focus==1:
      old_foc=self.GetFocus()
      if menu_element==old_foc:
        return 1
      if old_foc:
      	old_foc.SetHasFocus(0)
      menu_element.SetHasFocus(1)
      self.Focus=menu_element
      return 1

    return 0



  def SetFocus_Idx(self,menu_element_idx):
    try:
      menu_element=self.MenuItems[menu_element_idx]
      self.SetFocus(menu_element)
    except:
      print "Error setting focus to index",menu_element_idx



  def NextFocus(self):
    try:
      old_focus=self.GetFocus()
      index=self.MenuItems.index(old_focus)
      list=self.MenuItems[index+1:]+self.MenuItems[:index]
      for i in list:
        if self.SetFocus(i):
          try:
                i.FocusCallBack(i)
          except AttributeError:
                pass
          return
    except:
      print "B_MenuFocusManager::NextFocus() -> Exception ocurred."
      pass



  def PrevFocus(self):
    try:
      old_focus=self.GetFocus()
      index=self.MenuItems.index(old_focus)

      l1=self.MenuItems[:index]
      l2=self.MenuItems[index+1:]
      l1.reverse()
      l2.reverse()
      list=l1+l2

      for i in list:
        if self.SetFocus(i):
          try:
          	i.FocusCallBack(i)
          except AttributeError:
          	pass
          return

    except:
      print "B_MenuFocusManager::PrevFocus() -> Exception ocurred."
      pass

  def FinalRelease(self):
##    print "B_MenuFocusManager.FinalRelease()"
    for i in self.MenuItems:
      try:
        i.FinalRelease()
      except:
        pass




class B_MenuFrameWidget(B_MenuFocusManager,BUIx.B_FrameWidget):
  def __init__(self,Parent,Name,Width,Height,VertPos=0):
    #pdb.set_trace()
    #print "B_MenuFrameWidget.__init__()"
    BUIx.B_FrameWidget.__init__(self,Parent,Name,Width,Height)
    B_MenuFocusManager.__init__(self)
    self.VertPos=VertPos
    self.thisown=1
    self.SetAutoScale(1)
    #print "B_MenuFrameWidget.__init__() End",Name,Width,Height

  def __del__(self):
    #print "B_MenuFrameWidget.__del__()",self.Name()
    for i in self.MenuItems:
      #print "Deletting SetDrawFunc() of",i
      i.SetDrawFunc(None)

    B_MenuFocusManager.__del__(self)
    BUIx.B_FrameWidget.__del__(self)


#  def __str__(self):
#    print "class B_MenuFrameWidget ",self.Name()


  def AddMenuElement(self,menu_element,sep=0,
                     HPos=0.5,HIndicator=BUIx.B_FrameWidget.B_FR_HRelative,HAnchor=BUIx.B_FrameWidget.B_FR_HCenter):
    B_MenuFocusManager.AddMenuElement(self,menu_element)


    if sep == Menu.BackOptionVSep or sep == Menu.BackGamepadOptionVSep or sep == Menu.GamepadButtonVSep:
        YPos = BackButtonY
        if sep == Menu.BackGamepadOptionVSep:
            YPos = BackGamepadButtonY
        elif sep == Menu.GamepadButtonVSep:
            YPos = AcceptBackY
            menu_element.SetScale(0.7)
        self.AddWidget(menu_element,HPos,YPos,
                       HIndicator,HAnchor,
                       BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Top)
    else:
        self.AddWidget(menu_element,HPos,self.VertPos+sep,
                       HIndicator,HAnchor,
                       BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

    self.VertPos=self.VertPos+menu_element.GetSize()[1]+sep
    #print self.VertPos
    self.SetFocus(menu_element.Name())
    #print "B_MenuFrameWidget.AddMenuElement()  (end)->", sys.getrefcount(self)


  def AddMenuElementEx(self,menu_element,VPos=0,HPos=0.5,
                       HIndicator=BUIx.B_FrameWidget.B_FR_HRelative,HAnchor=BUIx.B_FrameWidget.B_FR_HCenter):
    B_MenuFocusManager.AddMenuElement(self,menu_element)

    self.AddWidget(menu_element,HPos,self.VertPos+sep,
                   HIndicator,HAnchor,
                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

    self.VertPos=self.VertPos+menu_element.GetSize()[1]+sep
    #print self.VertPos
    self.SetFocus(menu_element.Name())
    #print "B_MenuFrameWidget.AddMenuElement()  (end)->", sys.getrefcount(self)



# MenuDescr es un diccionario con los siguientes campos para describir el men�:
# "Name",            Nombre del men�.
# "Kind",            Clase de elemento, es una clase. Si no existe se usa B_MenuItemText.
# "FrameKind",       Clase del marco del elemento, es una clase. Si no existe se usa B_MenuTree.
# "ListDescr",       Lista de MenuDesc, puede no existir.
# "Command",         Si ListDscr est� vac�a o no existe, trata de ejecutar este.
# "VSep",            Separaci�n con el elemento anterior, si es el primero es el margen vertical.
# "Font",            Fuente para el elemento.
# "Options",         Lista de opciones para un elemento de tipo B_MenuItemOption.
# "SelOptionFunc",   Llama a esta funci�n para saber la opci�n seleccionada para un elemento
#                    de tipo B_MenuItemOption. Tiene que devolver una de las opciones de Options.
#                    Si no existe esta funci�n, toma la primera.
# "Actions",         Lista para las acciones que se pueden definir en la p�gina de teclado.
# "Position",        Lista que indica c�mo colocar los men�s.
# "PositionEx",      Lista que indica c�mo colocar los men�s, ampliaci�n.
# "Size",            Lista con el ancho y el alto.
# "BackGround",      Imagen de fondo.
# "PageDscrs",       Lista de Descripci�n de p�ginas.
# "PageDscr",        Descripci�n de p�ginas, es una diccionario con los siguientes campos:
#                    "PrevLabel",   Etiqueta a la p�gina anterior.
#                    "NextLabel",   Etiqueta a la p�gina siguiente.
#                    "Title",       T�tulo de la p�gina. (Obligatorio).
# "SpinValues",      Tupla con tres valores para configurar un SpinWidget: inferior, superior, pasos.
# "SpinGetValue"     Funci�n que le dice al SpinWidget c�mo obtener su valor inicial.
# "SpinSetValueEnd"  Funci�n que llama un SpinWidget al salir de contexto.
# "SpinOnChange"     Funci�n que llama un SpinWidget al cambiarse el valor

class B_MenuTreeItem:
  def __init__(self,MenuDescr,StackMenu):
    #print "MenuTreeItem.__init__()"
    self.SetAlpha(0.5)
    self.StackMenu=StackMenu
    self.MenuDescr=MenuDescr
    try:
    	self.FocusCallBack = MenuDescr["FocusCallBack"]
    except:
    	pass

  def __del__(self):
    #print "MenuTreeItem.__del__()"
    pass

  def __str__(self):
    print "B_MenuTreeItem widget with descriptor",self.MenuDescr

  def IncMenuItem(self):
      try:
        command=self.MenuDescr["LeftCommand"]
        command(self)
      except KeyError:
        pass


  def DecMenuItem(self):
      try:
        command=self.MenuDescr["RightCommand"]
        command(self)
      except KeyError:
        pass

  def ActivateItem(self,activate):
    if activate==1:
      NewFrame=self.CreateFrame()
      if NewFrame:
        self.StackMenu.Push(NewFrame)
        return 1
      else:
        try:
          command=self.MenuDescr["Command"]
          command(self)
          return 1
        except:
          return 0
    elif activate==0:
      w=self.StackMenu.Top()
      try:
        w.FinalRelease()
      except:
        pass
      self.StackMenu.Pop()
      #del(w)


  def CreateFrame(self):
    #print "CreateFrame()"
    frame_class=None

    try:
      frame_class=self.MenuDescr["FrameKind"]
    except KeyError:
      # B_MenuTree Necesita MenuDescr["ListDescr"], con esto me aseguro que lo tenga y si no, no pasa nada
      frame_class=B_MenuTree
      l_dscr=[]
      try:
        l_dscr=self.MenuDescr["ListDescr"]
      except KeyError:
        pass
      if l_dscr==[]:
        print "l_dscr==[]"
        return None
    try:
      NewFrame=frame_class(self,self.MenuDescr,self.StackMenu)
      return NewFrame
    except Exception, e:
      print "Error Creating frame of class",frame_class
      print "Exception:"
      print str(e)





class B_MenuTree(B_MenuFrameWidget):
  def __init__(self,Parent,Menudesc,StackMenu,VertPos=0):
    #print "MenuTree.__init__()"
    #print "MenuTree initial refcount",sys.getrefcount(self)

    Width,Height=Raster.GetSize()
    try:
      Width,Height=Menudesc["Size"]
    except KeyError:
      pass

    B_MenuFrameWidget.__init__(self,Parent,"MenuTree"+Menudesc["Name"],Width,Height,VertPos)

    self.Menudesc=Menudesc

    ValidIndex   = 0
    isValidIndex = 0

    for i in Menudesc["ListDescr"]:
      # print str(i)
      m_class=B_MenuItemTextNoFX
      try:
        m_class=i["Kind"]
      except KeyError:
        pass

      vsep=0
      try:
        vsep=i["VSep"]
      except KeyError:
        pass

      wSubMenu=m_class(self,i,StackMenu)
      if not isValidIndex:
        if wSubMenu.AcceptsFocus():
          isValidIndex = 1
        else:
          ValidIndex = ValidIndex+1

      HPos=0.5
      HIndicator=BUIx.B_FrameWidget.B_FR_HRelative
      HAnchor=BUIx.B_FrameWidget.B_FR_HCenter
      try:
        PosDscr=i["Position"]
        HPos=PosDscr[0]
        HIndicator=PosDscr[1]
        HAnchor=PosDscr[2]
      except KeyError:
        pass

      try:
        PosDscr=i["PositionEx"]
        HPos=PosDscr[0]
        HIndicator=PosDscr[1]
        HAnchor=PosDscr[2]
      except KeyError:
        B_MenuFrameWidget.AddMenuElement(self,wSubMenu,vsep,HPos,HIndicator,HAnchor)

    if Menudesc.has_key("iFocus"):
    	self.SetFocus_Idx(Menudesc["iFocus"])
    else:
    	self.SetFocus_Idx(ValidIndex)
    #print "MenuTree refcount (widgets added)",sys.getrefcount(self)


  def __del__(self):
    #print "B_MenuTree.__del__()"
    B_MenuFrameWidget.__del__(self)

  def __str__(self):
    print "B_MenuTree widget with Frame",self.Name()



class B_MenuSpin(SpinWidget.B_SpinWidget,B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu,font_server=ScorerWidgets.font_server):
    w=300
    h=19
    try:
      w,h=MenuDescr["Size"]
    except KeyError:
      pass

    font=DefaultFont
    try:
      font=MenuDescr["Font"]
    except KeyError:
      pass

    try:
      defaultValue=MenuDescr["DefaultValue"]
    except KeyError:
      defaultValue=-1

    SpinWidget.B_SpinWidget.__init__(self,Parent,MenuDescr["Name"],w,h,font_server,font,defaultValue)
    B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)

    try:
      l,u,s=MenuDescr["SpinValues"]
      SpinWidget.B_SpinWidget.SetLimits(self,l,u)
      SpinWidget.B_SpinWidget.SetSteps(self,s)
    except KeyError:
      pass

    try:
      self.SetValueEnd=MenuDescr["SpinSetValueEnd"]
    except KeyError:
      self.SetValueEnd=None

    if MenuDescr.has_key("SpinOnChange"):
        self.SpinOnChange = MenuDescr["SpinOnChange"]
    else:
        self.SpinOnChange = None

    try:
      val_func=MenuDescr["SpinGetValue"]
      val=val_func()
      SpinWidget.B_SpinWidget.SetValue(self,val)
    except KeyError:
      pass


  def IncMenuItem(self):
    self.IncrementValue()
    value = self.GetValue()
    if self.SpinOnChange:
       self.SpinOnChange(value)


  def DecMenuItem(self):
    self.DecrementValue()
    value = self.GetValue()
    if self.SpinOnChange:
       self.SpinOnChange(value)


  def FinalRelease(self):
    if self.SetValueEnd is not None:
      self.SetValueEnd(self.GetValue())



class B_MenuItemTextNoFX(BUIx.B_TextWidget,B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu,
               font_server=ScorerWidgets.font_server):

    #print "B_MenuItemText.__init__()",MenuDescr["Name"]
    font=DefaultFont

    try:
      font=MenuDescr["Font"]
    except KeyError:
      pass

    self.focusable = 1

    BUIx.B_TextWidget.__init__(self,Parent,"SubMenu"+MenuDescr["Name"],MenuDescr["Name"],font_server,font)
    B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)
    self.SetDrawFunc(self.Draw)
    self.SetAlpha(1.0)
    self.thisown=1



  def __del__(self):
    #print "B_MenuItemText.__del__()",self.Name()
    pass

  def __str__(self):
    print "B_MenuItemTextNoFX widget with text",self.GetTextData()


  def Draw(self,x,y,time):
    if self.GetVisible()==0:
      return

    # print "MenuItemText",self.Name()
    foc=self.GetHasFocus()
    if foc:
      self.SetColor(252,247,167)
    elif not self.focusable:
      self.SetColor(128, 128, 128)
    else:
      self.SetColor(207,144,49)

    self.DefDraw(x,y,time)



class B_MenuItemTextNoFXNoFocus(BUIx.B_TextWidget,B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu,
               font_server=ScorerWidgets.font_server):
    #print "B_MenuItemText.__init__()",MenuDescr["Name"]
    font=DefaultFont
    try:
      font=MenuDescr["Font"]
    except KeyError:
      pass

    BUIx.B_TextWidget.__init__(self,Parent,"SubMenu"+MenuDescr["Name"],MenuDescr["Name"],font_server,font)
    B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)
    self.SetDrawFunc(self.Draw)
    self.SetAlpha(1.0)
    self.thisown=1

  def __del__(self):
    #print "B_MenuItemText.__del__()",self.Name()
    pass

  def __str__(self):
    print "B_MenuItemTextNoFX widget with text",self.GetTextData()


  def Draw(self,x,y,time):
    if self.GetVisible()==0:
      return

    #print "MenuItemText",self.Name()
    foc=self.GetHasFocus()
    if foc:
      self.SetColor(252,247,167)
    else:
      self.SetColor(207,144,49)
    self.SetAlpha(0.4)
    self.DefDraw(x,y,time)
    self.SetAlpha(1.0)
  def AcceptsFocus(self):
    return 0








class B_MenuItemText(TextFXWidget.B_TextFXWidget,B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu,font_server=ScorerWidgets.font_server):
    #print "B_MenuItemText.__init__()",MenuDescr["Name"]
    font=DefaultFont
    try:
      font=MenuDescr["Font"]
    except KeyError:
      pass

    TextFXWidget.B_TextFXWidget.__init__(self,Parent,"SubMenu"+MenuDescr["Name"],MenuDescr["Name"],font_server,font)
    B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)


  def __del__(self):
##    print "B_MenuItemText.__del__()",self.Name()
    TextFXWidget.B_TextFXWidget.__del__(self)
    B_MenuTreeItem.__del__(self)

  def __str__(self):
    print "B_MenuItemText widget with text",self.GetTextData()


#if Bladex.GetMapType() > 0:
#  class B_VariableFocusTextMenuItem(B_MenuItemText):
#    def AcceptsFocus(self):
#      return 0
#else:
#  class B_VariableFocusTextMenuItem(B_MenuItemText):
#    def __str__(self):
#      print "B_MenuItemText widget with text",self.GetTextData()



class B_MenuItemTextNoFocus(B_MenuItemText):
  def AcceptsFocus(self):
    return 0




class B_MenuItemOption(B_MenuItemTextNoFX):
  def __init__(self,Parent,MenuDescr,StackMenu,
               font_server=ScorerWidgets.font_server):

    # print "Menu Option start"

    self.Options=["No option defined.",]
    self.SelOption=0
    self.OptionText=MenuDescr["Name"]

    try:
      self.Options=MenuDescr["Options"]
    except KeyError:
      pass

    try:
      GetSelFunc=MenuDescr["SelOptionFunc"]
      OptionSel=GetSelFunc()
      #print "DM OptionSel",self.OptionText,OptionSel,self.Options
      self.SelOption=OptionSel
      # print self.SelOption
    except KeyError:
      pass

    B_MenuItemTextNoFX.__init__(self,Parent,MenuDescr,StackMenu)
    #self.SetDrawFunc(self.Draw)
    self.Parent=Parent

    OptionText=self.OptionText+" < "+str(self.Options[self.SelOption])+" >"
    self.SetText(OptionText)

    try:
      GetPostInitCmd=MenuDescr["PostInitCommand"]
      GetPostInitCmd(self)
    except KeyError:
      pass

    # print "Menu Option end"


  def __del__(self):
    pass
    #print "B_MenuItemOption.__del__()",self.Name()

##  def Draw(self,x,y,time):
##    if self.GetVisible()==0:
##      return
##    foc=self.GetHasFocus()
##    if foc:
##      self.SetColor(240,240,240)
##    else:
##      self.SetColor(240,10,10)
##
##    self.DefDraw(x,y,time)

  def ActivateItem(self,activate):
    check_pass = None
    val = 1
    if self.MenuDescr.has_key("CheckPass"):
      check_pass=self.MenuDescr["CheckPass"]
      val = check_pass()

    if ((activate==1) and (val==1)):
      self.SelOption=self.SelOption+1
      self.SelOption=self.SelOption% len(self.Options)
      OptionText=self.OptionText+" < "+self.Options[self.SelOption]+" >"
      self.SetText(OptionText)

      try: # Puede que Parent no herede de Frame
        self.Parent.RecalcLayout()
      except:
        pass

      try:
        command=self.MenuDescr["Command"]
        command(MenuText.GetInverseMenuText(self.Options[self.SelOption]))
      except KeyError:
        pass
      try:
        command=self.MenuDescr["Command2"]
        command(MenuText.GetInverseMenuText(self.Options[self.SelOption]), self)
      except KeyError:
        pass
    elif activate==0:
      self.StackMenu.Pop()

  def FinalRelease(self):
    print "B_MenuItemOption.FinalRelease()"
    self.Parent=None
    #self.SetDrawFunc(None)

  def IncMenuItem(self):
    self.ActivateItem(1)


  def DecMenuItem(self):
    check_pass = None
    val = 1
    if self.MenuDescr.has_key("CheckPass"):
      check_pass=self.MenuDescr["CheckPass"]
      val = check_pass()

    if (val==1):
      self.SelOption=self.SelOption+len(self.Options)-1
      self.SelOption=self.SelOption% len(self.Options)
      OptionText=self.OptionText+" < "+self.Options[self.SelOption]+" >"
      self.SetText(OptionText)

      try: # Puede que Parent no herede de Frame
        self.Parent.RecalcLayout()
      except:
        pass

      try:
        command=self.MenuDescr["Command"]
        command(MenuText.GetInverseMenuText(self.Options[self.SelOption]))
      except KeyError:
        pass
      try:
        command=self.MenuDescr["Command2"]
        command(MenuText.GetInverseMenuText(self.Options[self.SelOption]), self)
      except KeyError:
        pass

  def SetSelOption(self, option):

    self.SelOption=option
    OptionText=self.OptionText+" < "+self.Options[self.SelOption]+" >"
    self.SetText(OptionText)

    try: # Puede que Parent no herede de Frame
      self.Parent.RecalcLayout()
    except:
      pass

  def AcceptsFocus(self):
    return self.focusable

class B_MenuItemPage(B_MenuFrameWidget):
  def __init__(self,Parent,PageDscr,MenuDescr,StackMenu):
    #print "Creating B_MenuItemPage()"
    #IDebug.set_trace()
    #Bldb.set_trace()
    #pdb.set_trace()
    self.TitleText=PageDscr["Title"]  #Tienen que tener t�tulo
    B_MenuFrameWidget.__init__(self,Parent,"MenuItemPage "+self.TitleText)
    #B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)
    font=Language.LetrasMenuSmall # Provisional
    font_server=ScorerWidgets.font_server    # Provisional

    self.BackgroundImage=None
    try:
      self.BackgroundImage=PageDscr["Background"]
    except KeyError:
      pass

    self.PrevLabel="Prev"
    try:
      self.PrevLabel=PageDscr["PrevLabel"]
    except KeyError:
      pass

    self.Title=BUIx.B_TextWidget(self,"Title MenuItemPage "+self.TitleText,self.TitleText,font_server,Language.LetrasMenuBig)
    self.Title.SetAlpha(0.8)
    self.Title.SetColor(252,247,167)
    self.AddWidget(self.Title,10,10,
                   BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)


    # Truco, cada PageDscr puede tener un font, pero los B_MenuItemText lo leen de MenuDescr
    try:
      font=PageDscr["Font"]
      MenuDescr["Font"]=font
    except KeyError:
      pass

    self.PrevItem=B_MenuItemText(self,self.TitleText+self.PrevLabel,self.PrevLabel,None,StackMenu)
    self.PrevItem.SetAlpha(1.0)
    self.PrevItem.SetColor(252,247,167)
    B_MenuFocusManager.AddMenuElement(self,self.PrevItem)
    self.AddWidget(self.PrevItem,10,10,
                   BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


    self.NextLabel="Next"
    try:
      self.NextLabel=PageDscr["NextLabel"]
    except KeyError:
      pass

    self.NextItem=B_MenuItemText(self,self.TitleText+self.NextLabel,self.NextLabel,None,StackMenu)
    self.NextItem.SetAlpha(1.0)
    self.NextItem.SetColor(252,247,167)
    B_MenuFocusManager.AddMenuElement(self,self.NextItem)
    self.AddWidget(self.NextItem,10,10,
                   BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


    self.ContinueItem=B_MenuItemText(self,self.TitleText+" Continue","Continue",None,StackMenu)
    self.ContinueItem.SetAlpha(1.0)
    self.ContinueItem.SetColor(252,247,167)
    B_MenuFocusManager.AddMenuElement(self,self.ContinueItem)
    self.AddWidget(self.ContinueItem,0.4,10,
                   BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_Left,
                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

    self.BackItem=B_MenuItemText(self,self.TitleText+" Back","Back",None,StackMenu)
    self.BackItem.SetAlpha(0.5)
    self.BackItem.SetColor(252,247,167)
    B_MenuFocusManager.AddMenuElement(self,self.BackItem)
    self.AddWidget(self.BackItem,0.4,10,
                   BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_Right,
                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

    #self.SetDrawFunc(self.Draw)
    self.Description="No Description"
    try:
      self.Description=PageDscr["Description"]
    except KeyError:
      pass

    self.DescriptionItem=B_MenuItemTextNoFocus(self,self.TitleText+" Description",self.Description,None,StackMenu)
    B_MenuFocusManager.AddMenuElement(self,self.DescriptionItem)
    self.DescriptionItem.SetAlpha(1.0)
    self.DescriptionItem.SetColor(252,247,167)
    self.AddWidget(self.DescriptionItem,25,0.7,
                   BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                   BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)


    try:
      BackgroundImage=PageDscr["BackGround"]
      self.BackgroundItem=WidgetsExtra.B_ImageWidget(self,self.TitleText+" Background",BackgroundImage)
      self.AddWidget(self.BackgroundItem,0.5,0.5,
                   BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                   BUIx.B_FrameWidget.B_FR_VRelative,BUIx.B_FrameWidget.B_FR_VCenter)
    except KeyError:
      pass

    B_MenuFocusManager.SetFocus(self,self.ContinueItem)


  def __del__(self):
    #print "Destroying ",self
    pass

  def __str__(self):
    print "B_MenuItemPage",self.TitleText


  def SetVisible(self,v):
    B_MenuFrameWidget.SetVisible(self,v)


#  def Draw(self,x,y,time):
#    if self.GetVisible()==0:
#      return
#    foc=self.GetHasFocus()
#    if foc:
#      self.SetColor(240,240,240)
#    else:
#      self.SetColor(240,10,10)
#
#    self.DefDraw(x,y,time)




class B_MenuItemPages(BUIx.B_TextWidget,B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu):
    font=DefaultFont
    font_server=ScorerWidgets.font_server    # Provisional
    BUIx.B_TextWidget.__init__(self,Parent,"B_MenuItemPages","B_MenuItemPages Text",font_server,font)
    B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)
    self.Pages=[]
    self.ActivePage=None
    self.SetDrawFunc(self.Draw)
    self.SetSizeChangedFunc(self.SizeChanged)
    PageDscrs=MenuDescr["PageDscrs"]
    for i in PageDscrs:
      self.AddPage(Parent,i,MenuDescr,StackMenu)
    self.SetActivePage(self.Pages[0])
    self.thisown=1

  def __del__(self):
    print "Deleting",self
    #del(self.Pages)


  def AddPage(self,Parent,pagedscr,MenuDescr,StackMenu):
    page=B_MenuItemPage(Parent,640,480,pagedscr,MenuDescr,StackMenu)
    self.Pages.append(page)


  def SetActivePage(self,page):
    if self.ActivePage:
      self.ActivePage.SetVisible(0)
    self.ActivePage=page
    if self.ActivePage:
      self.ActivePage.SetVisible(1)
      Bladex.SetRootWidget(self.ActivePage.GetPointer())

  def NextPageAux(self,desp):
    old_page=self.ActivePage
    index=self.Pages.index(old_page)
    index=index+desp
    index=index%len(self.Pages)
    self.SetActivePage(self.Pages[index])

  def NextPage(self):
    self.NextPageAux(1)

  def PrevPage(self):
    self.NextPageAux(-1)


  def GetPointer(self):
    if self.ActivePage:
      return self.ActivePage.GetPointer()
    else:
      return self.GetPointer()


  def AcceptsFocus(self):
    return 0

  def GetFocus(self):
    return self

  def NextFocus(self):
    if self.ActivePage:
      self.ActivePage.NextFocus()
    else:
      pass

  def PrevFocus(self):
    if self.ActivePage:
      self.ActivePage.PrevFocus()
    else:
      pass


  def ActivateItem(self,act):
    #print "B_MenuItemPages.ActivateItem()"
    if act and self.ActivePage:
      wTemp=self.ActivePage.GetFocus()
      #pdb.set_trace()
      if not wTemp.ActivateItem(1):
        if self.ActivePage.GetFocus()==self.ActivePage.PrevItem:
          self.PrevPage()
        elif self.ActivePage.GetFocus()==self.ActivePage.NextItem:
          self.NextPage()
    else:
      self.SetActivePage(None)
      B_MenuTreeItem.ActivateItem(self,act)


  def __str__(self):
    print "class B_MenuItemPages with",len(self.Pages),"pages"


  def Draw(self,x,y,time):
    if self.ActivePage:
      self.ActivePage.Draw(x,y,time)
    else:
      self.SetColor(100,100,240)
      self.SetAlpha(0.5)
      BUIx.B_TextWidget.DefDraw(self,100,100,time)


  def SizeChanged(self,reshz,resvt):
    for i in self.Pages:
      i.SizeChanged(reshz,resvt)

  def CreateFrame(self):
    return None



BackImageBitmap = None

class B_BackImageWidget(BUIx.B_RectWidget):

	def __init__(self,Parent,MenuDescr,StackMenu):
		global BackImageBitmap
		if not BackImageBitmap:
			BackImageBitmap  = BBLib.B_BitMap24()
			BackImageBitmap.ReadFromFile("../../Data/menu_wide.png")
		self.vidw = 1
		self.vidh = 1
		BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],self.vidw,self.vidh)
		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)

	def Draw(self,x,y,time):
		Raster.SetPosition(0,0)
		Raster.DrawImage(1920, 1080, "RGB", "Cover", BackImageBitmap.GetData())
		self.DefDraw(x,y,time)

	def FinalRelease(self):
		BUIx.B_RectWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 0

class B_BackBlank(BUIx.B_RectWidget):

	def __init__(self,Parent,MenuDescr,StackMenu):
		self.Bitmap  = BBLib.B_BitMap24()
		self.Bitmap.ReadFromFile("../../Data/Black.jpg")
		self.vidw = 1
		self.vidh = 1
		BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],self.vidw,self.vidh)
		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)

	def Draw(self,x,y,time):
		Raster.SetPosition(0,0)
		Raster.DrawImage(640,480,"BGR","Stretch",self.Bitmap.GetData())
		self.DefDraw(x,y,time)

	def FinalRelease(self):
		BUIx.B_RectWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 0


def SetCombosText(arg):
  import PanelFillerCombos
  return PanelFillerCombos.FillCombosText(arg)

def SetAbilitiesText(arg):
  import PanelFillerAbilities
  return PanelFillerAbilities.FillAbilitiesText(arg)

def SetItemsText(arg):      # Stolen from HD update -LeadHead
  import PanelFillerItems
  return PanelFillerItems.fillItemsText(arg)

def SetSpecialsText(arg):
  import PanelFillerSpecials
  return PanelFillerSpecials.FillSpecialsText(arg)

def SetMapText(arg):      # Stolen from HD update -LeadHead
  import PanelFillerMapText
  return PanelFillerMapText.FillMapText(arg)

def SetSecretsText(arg):      # Stolen from HD update -LeadHead
  import PanelFillerSecrets
  return PanelFillerSecrets.FillSecrets(arg)

def SetGamepadDisconnectFunc(isDisconnect):
    import Scorer
    global wDisconnectGamepadBox

    if isDisconnect == 1:
        wDisconnectGamepadBox=BUIx.B_TextWidget(Scorer.wMessageFrame,"MessageWidget","\n\n\n\n\n",ScorerWidgets.font_server,Language.LetrasMenuBig)
        wDisconnectGamepadBox.SetColor(255,255,255)
        wDisconnectGamepadBox.SetSolid(1)
        wDisconnectGamepadBox.SetText("\n "+MenuText.GetMenuText("Gamepad disconnected")+" \n")
        wDisconnectGamepadBox.SetJustification(BUIx.B_TextWidget.B_TEXT_HCenter)
        wDisconnectGamepadBox.SetBackgroundAlpha(0.95)
        wDisconnectGamepadBox.SetBackgroundColor(0,0,0)
        wDisconnectGamepadBox.SetAlpha(1)
        if not GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
            scale = 0.8
        else:
            scale = 2
        wDisconnectGamepadBox.SetScale(1)

        Scorer.wMessageFrame.AddWidget(wDisconnectGamepadBox,0.5,50,
              BUIx.B_FrameWidget.B_FR_HRelative,
              BUIx.B_FrameWidget.B_FR_HCenter,
              BUIx.B_FrameWidget.B_FR_AbsoluteBottom,
              BUIx.B_FrameWidget.B_FR_Bottom)

    elif isDisconnect == 0:
        Scorer.wMessageFrame.SetAlpha(0)
        Scorer.wMessageFrame.RemoveWidget("MessageWidget",0)


    Scorer.wMessageFrame.RecalcLayout()


### Pre-load Travelbook backgrounds to prevent stutter when pressing F1.
# Code stolen from HD update
def InitializeImages():
    import Language
    import GotoMapVars
    Raster.SetAlpha(0)
    language = PanelFillerCommon.GetLanguageFallback()    
    char = Bladex.GetEntity("Player1")
    if char.Kind=="Spidersmall":
      return
    Inventory = Bladex.GetEntity("Player1").GetInventory()


    localSpecials.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillaspecials_hi_empty.jpg")
    w, h = localSpecials.GetDimension()
    Raster.DrawResizeImage(w,h,"RGB","ScaledCentered2",localSpecials, 0, 0)

    localItems.ReadFromFile("../../Data/TB/EmptyPanels/plantillaGitems_hi_empty.jpg")
    w, h = localItems.GetDimension()
    Raster.DrawResizeImage(w,h,"RGB","ScaledCentered2",localItems, 0, 0)

    localWeapons.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillaweapons_hi_empty.jpg")
    w, h = localWeapons.GetDimension()
    Raster.DrawResizeImage(w,h,"RGB","ScaledCentered2",localWeapons, 0, 0)

    localHabilities.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillahabilities_hi_empty.jpg")
    w, h = localHabilities.GetDimension()
    Raster.DrawResizeImage(w,h,"RGB","ScaledCentered2",localHabilities, 0, 0)

    localMapText.ReadFromFile("../../Data/TB/EmptyPanels/texts_hi_empty.jpg")
    w, h = localMapText.GetDimension()
    Raster.DrawResizeImage(w, h,"RGB","ScaledCentered2",localMapText, 0, 0)

    localSecrets.ReadFromFile("../../Data/TB/EmptyPanels/secrets_hi_empty.jpg")
    w, h = localSecrets.GetDimension()
    Raster.DrawResizeImage(w,h,"RGB","ScaledCentered2",localSecrets, 0, 0)


# localSpecials  = BBLib.B_BitMap24()
# localItems  = BBLib.B_BitMap24()
# localWeapons  = BBLib.B_BitMap24()
# localHabilities  = BBLib.B_BitMap24()
# localMapText  = BBLib.B_BitMap24()
# localSecrets  = BBLib.B_BitMap24()

class B_BackWeapon(BUIx.B_FrameWidget):

	#def __init__(self,Parent,MenuDescr,StackMenu):
	def __init__(self,Parent,Menudesc,StackMenu,VertPos=0):
		import Language
		import GotoMapVars
		self.image = 1
		self.NumImages = 6
		self.PanelWidgets = []
		self.PanelWidgetsName = []

		self.Text = 0
		self.NumTexts = 4

		self.TextsAvail = [0, 0, 0, 0]

		self.vidw = 1
		self.vidh = 1

		self.addone = 0

		char = Bladex.GetEntity("Player1")
		print char.Kind

		Raster.UnifyRenderBuffers()

		if "ORCMURAL"    in GotoMapVars.BaList:
			self.TextsAvail[1] = 1
		if "ISLANDMURAL" in GotoMapVars.BaList:
			self.TextsAvail[2] = 1
		if  "NEJEVMURAL" in GotoMapVars.BaList:
			self.TextsAvail[3] = 1

		# Range Vars
		Inventory = Bladex.GetEntity("Player1").GetInventory()

		if (not Inventory.nTablets > 0) and not (1 in GotoMapVars.PlacedTablets) and not (self.TextsAvail[1] or self.TextsAvail[2] or self.TextsAvail[3]):
			self.addone = 1
		if  "SALATABLILLAS" in GotoMapVars.BaList or (1 in GotoMapVars.PlacedTablets) or (Inventory.nTablets > 0):
			self.addone = 0
			self.TextsAvail[0] = 1

		language = PanelFillerCommon.GetLanguageFallback()
		print language

		self.Specials = BBLib.B_BitMap24()
		self.Specials.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillaspecials_hi_empty.jpg")

		self.Items = BBLib.B_BitMap24()
		self.Items.ReadFromFile("../../Data/TB/" + language +"/Items/plantillaGitems_hi.jpg")

		self.Weapons = BBLib.B_BitMap24()
		self.Weapons.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillaweapons_hi_empty.jpg")


		self.Habilities = BBLib.B_BitMap24()
		self.Habilities.ReadFromFile("../../Data/TB/EmptyPanels/" + char.Kind + "/plantillahabilities_hi_empty.jpg")

		self.MapText  = BBLib.B_BitMap24()

		if not self.MapText.ReadFromFile("../../Data/TB/" + language + "/" + char.Kind + "/" + Bladex.GetCurrentMap() + "_hi.jpg"):
			if not self.MapText.ReadFromFile("../../Data/TB/" + language + "/"  + Bladex.GetCurrentMap() + "_hi.jpg"):
				if not self.MapText.ReadFromFile("../../Data/TB/" + language + "/" + char.Kind + "/" + Bladex.GetCurrentMap() + ".jpg"):
					self.MapText.ReadFromFile("../../Data/TB/" + language + "/"  + Bladex.GetCurrentMap() + ".jpg")

		if string.lower(Bladex.GetCurrentMap()) == "tower_m16":
			inv = Bladex.GetEntity("Player1").GetInventory()
			for i in range(inv.nWeapons):
				if (Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2") or (Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2Barbarian"):
					self.MapText.ReadFromFile("../../Data/TB/" + language + "/"  + "conTower_m16_hi.jpg")
				else:
					self.MapText.ReadFromFile("../../Data/TB/" + language + "/"  + "sinTower_m16_hi.jpg")


		self.Tablets  = BBLib.B_BitMap24()
		if (Inventory.nTablets > 0) or (1 in GotoMapVars.PlacedTablets):
			self.Tablets.ReadFromFile("../../Data/TB/"+ language  + "/tablillas_hi.jpg")

		self.Text1 = BBLib.B_BitMap24()
		if self.TextsAvail[1]:
			self.Text1.ReadFromFile("../../Data/TB/" + language  + "/muralorc_hi.jpg")
		self.Text2 = BBLib.B_BitMap24()
		if self.TextsAvail[2]:
			self.Text2.ReadFromFile("../../Data/TB/" + language  + "/muralisla1_hi.jpg")
		self.Text3 = BBLib.B_BitMap24()
		if self.TextsAvail[3]:
			self.Text3.ReadFromFile("../../Data/TB/" + language  + "/muralnejev_hi.jpg")


		BUIx.B_FrameWidget.__init__(self,Parent,Menudesc["Name"],self.vidw,self.vidh)

		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)

		self.SndCorreGema=Bladex.CreateSound("../../Sounds/golpe-2.wav","Chanje")
		self.SndCorreGema.Volume=0.5
		self.SndCorreGema.MinDistance=1000000.0
		self.SndCorreGema.MaxDistance=2000000

		if self.addone == 0:
			while not self.TextsAvail[self.Text]:
				self.Text = self.Text + 1
				if self.Text > self.NumTexts - 1:
					self.Text = 0

		self.SetupPanelWidgets()

	def AddButtonTexts(self, language):
		sys.path.append('../../SCRIPTS/Combos/' + language)
		import PanelButtonsLoca
		index = 0
		elem = "Button"
		for text in PanelButtonsLoca.buttons:
			textColor = ColorWhite
			name = language + elem + text
			font = PanelFillerCommon.CheckFontChineseFallback(elem)
			scale = 1
			if self.addone and index == 5:
				textColor = ColorGrey
			if self.SpecialsTab and index == 0:
				textColor = ColorGrey
			buttonWidget=PanelFillerCommon.InitWidget(self, name, text, font, elem, BUIx.B_TextWidget.B_TEXT_Left, textColor, scale)
			posX = PanelFillerCommon.CheckButtonOffset(index, buttonTextPosition[0] + (buttonOffset[0] * index))
			posY = buttonTextPosition[1]
			posX = PanelFillerCommon.CorrectPosX(posX)
			posY = PanelFillerCommon.CorrectPosY(posY)
			self.AddWidget(buttonWidget,posX,posY,relative,center,relativev,left)
			index = index + 1

	def RemovePanelWidgets(self):
		for elem in self.PanelWidgetsName:
			self.RemoveWidget(elem, 0)
		self.PanelWidgets = []
		self.PanelWidgetsName = []

	def SetupPanelWidgets(self):
		currImage = self.GetCurrentImage()
		self.RemovePanelWidgets()
		if currImage == 0:
			SetSpecialsText(self)
		elif currImage == 1:
			SetCombosText(self)
		elif currImage == 2:
			SetAbilitiesText(self)
		self.AddButtonTexts(PanelFillerCommon.GetLanguageFallback())

	def GetCurrentImage(self):
		import GotoMapVars
		currImage = self.image
		char = Bladex.GetEntity("Player1")
		Map = string.lower(Bladex.GetCurrentMap())
		self.SpecialsTab = 1

		Inventory = char.GetInventory()

		HaveCrush = 0

		for i in range(Inventory.nWeapons):
			Weapon = Inventory.GetWeapon(i)
			RootWeapon = Bladex.GetEntity(Weapon)
			if RootWeapon.Kind == "CrushHammer":
				HaveCrush = 1

		if Map in GotoMapVars.BackLevelNames:
			self.SpecialsTab = 0
		else:
			if (Map in GotoMapVars.LevelNames and GotoMapVars.LevelNames.index(Map) > 6) or ((char.Kind == "Dwarf_N") and HaveCrush):
				self.SpecialsTab = 0
		if self.image < self.SpecialsTab:
			currImage = (self.NumImages - (1 + self.addone))

		if self.image > (self.NumImages - (1 + self.addone)):
			currImage = self.SpecialsTab
		return currImage

	def Draw(self,x,y,time):

		Raster.SetTextShadow(4, 4)
		import string
		import Menu

		# x,y = Raster.GetSize()
		# Raster.SetPosition((x - 640)/2, (y - 480)/2)


		# Horizontal buttons range checking
		self.image = self.GetCurrentImage()

		# Vertical -Text- options range checking
		if self.Text < 0:
			self.Text = self.NumTexts - 1

		if self.Text > self.NumTexts - 1:
			self.Text = 0

		# Set logic conditions
		if self.image == 0:
			w, h = self.Specials.GetDimension()
			Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Specials.GetData())
		if self.image == 1:
			w, h = self.Habilities.GetDimension()
			Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Weapons.GetData())
		if self.image == 2:
			w, h = self.Weapons.GetDimension()
			Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Habilities.GetData())
		if self.image == 3:
			w, h = self.Items.GetDimension()
			Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Items.GetData())
		if self.image == 4:
			w, h = self.MapText.GetDimension()
			Raster.DrawImage(w, h,"RGB","ScaledCentered2",self.MapText.GetData())
		if self.image == 5:
			if self.Text == 0:
				w, h = self.Tablets.GetDimension()
				Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Tablets.GetData())
			if self.Text == 1:
				w, h = self.Text1.GetDimension()
				Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Text1.GetData())
			if self.Text == 2:
				w, h = self.Text2.GetDimension()
				Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Text2.GetData())
			if self.Text == 3:
				w, h = self.Text3.GetDimension()
				Raster.DrawImage(w,h,"RGB","ScaledCentered2",self.Text3.GetData())

		if  ((self.image == 5)):
		# and
		#	(
		#		(self.TextsAvail[1]) or
		#		(self.TextsAvail[2]) or
		#		(self.TextsAvail[3])
		#	)):
			Menu.TBUDSoundAble = 1
		else:
			Menu.TBUDSoundAble = 0

		Raster.SetPosition(0,0)
		self.DefDraw(0,0,time)

	def FinalRelease(self):
		BUIx.B_FrameWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 1

	def IncMenuItem(self):
		self.SndCorreGema.PlayStereo()
		self.image = self.image + 1
		self.SetupPanelWidgets()

	def DecMenuItem(self):
		self.SndCorreGema.PlayStereo()
		self.image = self.image - 1
		self.SetupPanelWidgets()

	def GetFocus(self):
	    return self

	def ActivateItem(self,activate):
		import Menu
		Menu.ActivateMenu()
		return

	def NextFocus(self):
		if self.image == 5:
			self.Text = self.Text + 1
			count = 0
			while not self.TextsAvail[self.Text]:
				if count == len(self.TextsAvail):
					break
				self.Text = self.Text + 1
				if self.Text > self.NumTexts - 1:
					self.Text = 0
				count = count + 1

	def PrevFocus(self):
		if self.image == 5:
			self.Text = self.Text - 1
			count = 0
			while not self.TextsAvail[self.Text]:
				if count == len(self.TextsAvail):
					break
				self.Text = self.Text - 1
				if self.Text < 0:
					self.Text = self.NumTexts - 1
				count = count + 1

	def __del__(self):
		import Menu
		Menu.TBUDSoundAble = 1

class B_BackFeatures(BUIx.B_RectWidget):

	def __init__(self,Parent,MenuDescr,StackMenu):
		path = "../../Data/Demo/"+ Language.Current + "/"
		if not os.path.exists(path + "DEMO-SCREEN.jpg"):
			path = "../../Data/Demo/EnglishUS/"
		self.Bitmap  = BBLib.B_BitMap24()
		self.Bitmap.ReadFromFile(path + "DEMO-SCREEN.jpg")
		self.CurrentBitmap = BBLib.B_BitMap24()
		self.CurrentBitmap = self.Bitmap
		self.vidw = 1
		self.vidh = 1
		BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],self.vidw,self.vidh)
		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)
		self.Time2Exit=None
		global isQuitting
		isQuitting = 0

	def Draw(self,x,y,time):
		global isQuitting
		isQuitting = 1
		if self.Time2Exit==None:
			self.Time2Exit=time
		if time-self.Time2Exit>10.0:
			Bladex.Quit()
		Raster.SetPosition(0,0)
		Raster.DrawImage(4256,2394,"RGB","Stretch",self.CurrentBitmap.GetData())
		self.DefDraw(x,y,time)

	def FinalRelease(self):
		BUIx.B_RectWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 0
