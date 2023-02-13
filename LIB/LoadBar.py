##///
##||| LOADBAR.PY TITANIUM
##||| Change list:
##||| * The code for it was already there, but for unknown reasons instead of using "Vertical Stretch", scaled down centered was used.
##|||    This makes loading screens be as full screen as possible if "_hi" versions of loading screens exist.
##||| 
##||| 
##\\\ 

import BBLib
import Raster
import Bladex
import os
import string


##BAR_X=63.0
##BAR_Y=399.0

BAR_X=64.0
BAR_Y=425.0
BAR2_Y=356.0
ScaledCenteredScale = 0.62

class BaseProgressBar:
  "Clase base de las barras de progreso de carga"

  def __init__(self,total_increments):
    self.total_increments=total_increments
    self.RectSize=(512.0,16.0)
    self.SolidBar=0
    self.hBmpBar=None
    self.PrefixText="Loading "
    self.Mode = "ScaledCentered"

    if not self.SolidBar:
      Bladex.ReadBitMap("../../Data/Gray_progress_bar.bmp","LoadBarBmp")
      self.hBmpBar=Raster.BmpHandle("LoadBarBmp")

  def __del__(self):
    self.Clear()

  def Clear(self):
    pass


  def BarIncrement(self,n_file,text):

    if Raster.ClassIdName()=="B_Direct3DRasterDevice":
      if n_file%10:
        return

    str="%s%s."%(self.PrefixText,text)
    percentage=float(n_file)/float(self.total_increments)
    if percentage>1.0:
      percentage=1.0

    w,h=Raster.GetSize()

    if self.Mode == "VerticalStretch":
      AdjustedRectWidth=self.RectSize[0]*h/480.0
      AdjustedRectHeight=self.RectSize[1]*h/480.0
    elif self.Mode == "ScaledCentered":
      AdjustedRectWidth=self.RectSize[0]*ScaledCenteredScale*h/480.0
      AdjustedRectHeight=self.RectSize[1]*ScaledCenteredScale*h/480.0
    else:
      AdjustedRectWidth=self.RectSize[0]
      AdjustedRectHeight=self.RectSize[1]

    Raster.ResetScale();
    Raster.Cls(0,0,0)
    Raster.SetAlpha(0.8)

    percentage_width=percentage*self.RectSize[0]

    if self.Mode == "VerticalStretch":
      AdjustedRectX=w/2 - (320 - BAR_X)*(h/480.0)
      AdjustedRectY=BAR_Y*h/480.0
    elif self.Mode == "ScaledCentered":
      AdjustedRectX=w/2 - (320 - BAR_X)*ScaledCenteredScale*(h/480.0)
      AdjustedRectY=BAR2_Y * (h/480.0)
    else:
      AdjustedRectX=BAR_X + (w-640.0) * 0.5
      AdjustedRectY=BAR_Y + (h-480.0) * 0.5

    x1=AdjustedRectX
    x2=x1+AdjustedRectWidth
    y1=AdjustedRectY
    y2=AdjustedRectY+AdjustedRectHeight

    # 3D Drawing Begins
    Raster.SetRasterParameter("startscene","")

    Raster.SetPenColor(0,0,0);
    Raster.Rectangle(x1,y1,x2,y2)

    if self.SolidBar==1:
      x2=x1+percentage*AdjustedRectWidth
      Raster.SetFillColor(140,220,10);
      Raster.SolidRectangle(x1,y1,x2,y2)
    else:
      Raster.SetPosition(x1,y1)
      Raster.SetPenColor(180,23,44)
      Raster.DrawBitmap(self.hBmpBar,percentage*AdjustedRectWidth,AdjustedRectHeight)
      Raster.SetPosition(0,0)

    Raster.SetRasterParameter("endscene","")
    # 3D Drawing Ends

    Raster.SysWrite(10,h-25,str,240,240,20)
    Raster.SwapBuffers()



class BackImageBar:
  def __init__(self,background_image=None):
    self.imagehook=0
    if background_image:
      back_image=BBLib.B_BitMap24()
      background_hi_image=""
      if background_image[-8:] <> "_hi.jpg":
        background_hi_image = background_image[0:len(background_image) - 4] + "_hi.jpg"

      if not os.path.exists(background_image) and not os.path.exists(background_hi_image):
        print "Missing BackImage :"
        print background_image
        background_hi_image = "../../Data/Menu/Save/EnglishUS/Cargando_hi.jpg"

      if back_image.ReadFromFile(background_hi_image) or back_image.ReadFromFile(background_image):
        w,h=back_image.GetDimension()
        if w == 640:
          self.Mode = "ScaledCentered"
        elif string.find(background_hi_image, "Cargando") <> -1 or string.find(background_hi_image, "Guardando") <> -1:
          self.Mode = "VerticalStretch" #Changed -LeadHead
        else:
          self.Mode = "VerticalStretch" #Changed -LeadHead

        Raster.SetBackgroundImage(w,h,"RGB","Normal",self.Mode,back_image.GetData())
        back_image.Clear()

        Raster.ResetScale();
        Raster.Cls(0,0,0)
        Raster.SwapBuffers()
        self.imagehook=1




  def Clear(self):
    if self.imagehook:
      Raster.RemoveBackgroundImage()
      self.imagehook=0



class ProgressBar(BaseProgressBar,BackImageBar):
  "Clase auxiliar para poner una barra de progreso durante la carga de un nivel"

  def __init__(self,total_increments,background_image=None,auto_remove=1):
    BaseProgressBar.__init__(self,total_increments)
    BackImageBar.__init__(self,background_image)

    BBLib.ResetnOpenedInputFiles()
    BBLib.SetOnOpenInputFileFunc(self.BarIncrement)
    self.filehook=1
    self.cleared=0

    if auto_remove:
      Bladex.AddScheduledFunc(0,self.Clear,())


  def Clear(self):
    if self.cleared == 0:
      self.cleared = 1
      BaseProgressBar.Clear(self)
      BackImageBar.Clear(self)
      if self.filehook:
        BBLib.RemoveOnOpenInputFileFunc()
        self.filehook=0




class AutoProgressBar(BaseProgressBar,BackImageBar):

  def __init__(self,total_increments,prefix_text="Loading",background_image=None):

    BaseProgressBar.__init__(self,total_increments)
    BackImageBar.__init__(self,background_image)
    self.CurrentPoint=0
    self.PrefixText=prefix_text

  def Increment(self,text=""):
    self.CurrentPoint=self.CurrentPoint+1
    self.BarIncrement(self.CurrentPoint,text)

  def Clear(self):
    BaseProgressBar.Clear(self)
    BackImageBar.Clear(self)    

class ECTSProgressBar(ProgressBar):
  def __init__(self,total_increments,background_image=None,auto_remove=1):
    ProgressBar.__init__(self,total_increments,background_image)
    self.updated=0

  def BarIncrement(self,n_file,text):

    if n_file>self.total_increments/2 and not self.updated:
      BBLib.RemoveOnOpenInputFileFunc()
      back_image=BBLib.B_BitMap24()
      if back_image.ReadFromFile("Blade_progress2_hi.jpg") or back_image.ReadFromFile("Blade_progress2.jpg"):
        Raster.RemoveBackgroundImage()
        w,h=back_image.GetDimension()
        if w == 640:
          self.Mode = "ScaledCentered"
        else:
          self.Mode = "VerticalStretch" #Changed -LeadHead

        Raster.ResetScale();
        Raster.SetBackgroundImage(w,h,"RGB","Normal",self.Mode,back_image.GetData())
        Raster.Cls(0,0,0)
        Raster.SwapBuffers()

      self.updated=1
      BBLib.SetOnOpenInputFileFunc(self.BarIncrement)

    self.BarIncrement2(n_file,text)


  def BarIncrement2(self,n_file,text):
    if Raster.ClassIdName()=="B_Direct3DRasterDevice":
      if n_file%10:
        return

    str="%s%s."%(self.PrefixText,text)
    percentage=float(n_file)/float(self.total_increments)
    if percentage>1.0:
      percentage=1.0

    w,h=Raster.GetSize()


    if self.Mode == "VerticalStretch":
      AdjustedRectWidth=self.RectSize[0]*h/480.0
      AdjustedRectHeight=self.RectSize[1]*h/480.0
    elif self.Mode == "ScaledCentered":
      AdjustedRectWidth=self.RectSize[0]*ScaledCenteredScale*h/480.0
      AdjustedRectHeight=self.RectSize[1]*ScaledCenteredScale*h/480.0
    else:
      AdjustedRectWidth=self.RectSize[0]
      AdjustedRectHeight=self.RectSize[1]


    Raster.ResetScale();
    Raster.Cls(0,0,0)
    Raster.SetAlpha(0.8)

    percentage_width=percentage*self.RectSize[0]

    if self.Mode == "VerticalStretch":
      AdjustedRectX=w/2 - (320 - BAR_X)*(h/480.0)
      AdjustedRectY=BAR_Y*h/480.0
    elif self.Mode == "ScaledCentered":
      AdjustedRectX=w/2 - (320 - BAR_X)*ScaledCenteredScale*(h/480.0)
      AdjustedRectY=BAR2_Y * (h/480.0)
    else:
      AdjustedRectX=BAR_X + (w-640.0) * 0.5
      AdjustedRectY=BAR_Y + (h-480.0) * 0.5

    x1=AdjustedRectX
    x2=x1+AdjustedRectWidth
    y1=AdjustedRectY
    y2=AdjustedRectY+AdjustedRectHeight

    # 3D Drawing Begins
    Raster.SetRasterParameter("startscene","")

    Raster.SetPenColor(0,0,0);
    Raster.Rectangle(x1,y1,x2,y2)

    if self.SolidBar==1:
      x2=x1+percentage*AdjustedRectWidth
      Raster.SetFillColor(140,220,10);
      Raster.SolidRectangle(x1,y1,x2,y2)
    else:
      Raster.SetPosition(x1,y1)
      Raster.SetPenColor(180,23,44)
      Raster.DrawBitmap(self.hBmpBar,percentage*AdjustedRectWidth,AdjustedRectHeight)
      Raster.SetPosition(0,0)

    Raster.SetRasterParameter("endscene","")
    # 3D Drawing Ends

    Raster.SysWrite(10,h-25,str,240,240,20)
    Raster.SwapBuffers()

    if percentage == 1.0:
      self.Clear()


class LanguageProgressBar(ECTSProgressBar):
  def __init__(self,total_increments,background_image=None,auto_remove=1):
    import Language
    self.path = Language.Current + '/'

    if not os.path.exists(self.path):
        self.path = 'EnglishUS/'

    ProgressBar.__init__(self,total_increments,self.path + background_image)
    self.updated=0

  def BarIncrement(self,n_file,text):

    if n_file>self.total_increments/2 and not self.updated:
      BBLib.RemoveOnOpenInputFileFunc()
      back_image=BBLib.B_BitMap24()

      if back_image.ReadFromFile(self.path + "Blade_progress2_hi.jpg") or back_image.ReadFromFile(self.path + "Blade_progress2.jpg"):
        Raster.RemoveBackgroundImage()
        w,h=back_image.GetDimension()
        if w == 640:
          self.Mode = "ScaledCentered"
        else:
          self.Mode = "VerticalStretch" #Changed -LeadHead

        Raster.ResetScale();
        Raster.SetBackgroundImage(w,h,"RGB","Normal",self.Mode,back_image.GetData())
        Raster.Cls(0,0,0)
        Raster.SwapBuffers()

      self.updated=1
      BBLib.SetOnOpenInputFileFunc(self.BarIncrement)
      
    ECTSProgressBar.BarIncrement2(self,n_file,text)


class DemoProgressBar(ECTSProgressBar):
  def __init__(self,total_increments,background_image=None):
    import Language
    self.path = Language.Current + '/'

    if not os.path.exists(self.path):
        self.path = 'EnglishUS/'

    self.updated=1
    self.segment_size=total_increments/4

    self.segment1 = (self.segment_size) - self.segment_size * 0.05
    self.segment2 = (self.segment_size * 2) - self.segment_size * 0.1
    self.segment3 = (self.segment_size * 3) + self.segment_size * 0.3

    ProgressBar.__init__(self,total_increments,self.path + background_image)

  def BarIncrement(self,n_file,text):

    if Raster.ClassIdName()=="B_Direct3DRasterDevice":
      if n_file%10:
        return

    if (n_file>self.segment3 and self.updated==3) or (n_file>self.segment2 and self.updated==2) or (n_file>self.segment1 and self.updated==1):
      BBLib.RemoveOnOpenInputFileFunc()
      back_image=BBLib.B_BitMap24()
      if back_image.ReadFromFile(self.path + "Blade_progress"+`self.updated+1`+".jpg"):
        Raster.RemoveBackgroundImage()
        w,h=back_image.GetDimension()
        if w == 640:
          self.Mode = "ScaledCentered"
        else:
          self.Mode = "VerticalStretch" #Changed -LeadHead

        Raster.ResetScale();
        Raster.SetBackgroundImage(w,h,"RGB","Normal",self.Mode,back_image.GetData())
        Raster.Cls(0,0,0)
        Raster.SwapBuffers()

      self.updated=self.updated+1
      BBLib.SetOnOpenInputFileFunc(self.BarIncrement)
    
    ECTSProgressBar.BarIncrement2(self,n_file,text)
