import Bladex
import Scorer
import Raster
import BBLib
import BUIx
import Sounds
import Language

from os import listdir, path

StayImage = 8
FadeImage = 3.0
StateImage = 0

musiccredits             = None

class B_CreditsImageWidget(BUIx.B_RectWidget):
    def __init__(self,Parent,MenuDescr,StackMenu = 0):
        import Menu

        self.ResX = Raster.GetSize()[0]
        self.ResY = Raster.GetSize()[1]
        self.BitmapsHandler = []
        self.path = "../../Data/Credits/"+Language.Current
        self.OldSndNewMenuVol = Menu.SndNewMenu.Volume
        self.OldSndCorreGemaVol= Menu.SndCorreGema.Volume
        Menu.SndNewMenu.Volume = 0
        Menu.SndCorreGema.Volume = 0

        currentmap = Bladex.GetCurrentMap()
        
        Credits = []
        if(not path.isdir(self.path)):
            self.path = "../../Data/Credits/English"
        for f in listdir(self.path):
            Credits.append("/" + f)
        Credits.sort()
        self.BitmapsNames = Credits

        type = 0
        
        self.StateImage = 0
        self.FadeImage = 3
        self.image1 = 0
        self.image2 = 1
        self.Pages = 0
        self.Cache = 0
        self.Fade = 0
        self.StackMenu = StackMenu

        for i in self.BitmapsNames:
            self.Pages = self.Pages + 1
    
        BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],4256,2394)

        if type:
            self.SetDrawFunc(self.DrawFadeImage)
            Bladex.ReadBitMap(self.BitmapsNames[0],self.BitmapsNames[0])
            self.BitmapsHandler.append(Raster.BmpHandle(self.BitmapsNames[0]))
        else:
            self.SetDrawFunc(self.DrawSlice)

        char = Bladex.GetEntity("Player1")
        
        global musiccredits

        if not musiccredits:
                musiccredits             = Bladex.CreateSound('../../Sounds/tema.mp3', 'MusicCreditos')
                musiccredits.Volume      = 1.0
                musiccredits.MinDistance = 100000
                musiccredits.MaxDistance = 200000
        musiccredits.PlayStereo(1)
        self.MusicVolume = Bladex.GetMusicVolume()
        Bladex.SetMusicVolume(0)
        self.StayImage = (((60.0 * 4) + 37.0) / self.Pages)
        self.StateImage = 1
        self.StartImageTime = 0
     
        self.Selected=0
        self.Solid=0
        self.Border=0

        self.bitmap = BBLib.B_BitMap24()
        self.bitmap.ReadFromFile(self.path+self.BitmapsNames[self.image1])
        Raster.SetBackgroundImage(4256,2394,"RGB","Normal","Cover",self.bitmap.GetData())

    def ActivateItem(self,act):
        if act==0:
            w=self.StackMenu.Top()
            try:
                w.FinalRelease()
            except:
                pass
            self.StackMenu.Pop()
            musiccredits.Stop()
            Bladex.SetMusicVolume(self.MusicVolume)

    def __del__(self):
        Bladex.TriggerEventInner()
        import Menu
        Raster.RemoveBackgroundImage()
        Menu.SndNewMenu.Volume = self.OldSndNewMenuVol
        Menu.SndCorreGema.Volume = self.OldSndCorreGemaVol

    def DrawSlice(self,x,y,time):
        Raster.Cls(0,0,0)

        if self.StartImageTime == 0:
            self.StartImageTime = time

        stime = time - self.StartImageTime

        if stime >= self.StayImage:
            self.StartImageTime = time
            self.image1 = self.image1 + 1

            if self.image1 >= self.Pages:
                global musiccredits
                if not musiccredits:
                        musiccredits             = Bladex.CreateSound('../../Sounds/tema.mp3', 'MusicCreditos')
                        musiccredits.Volume      = 1.0
                        musiccredits.MinDistance = 100000
                        musiccredits.MaxDistance = 200000
                musiccredits.PlayStereo(1)
                self.image1 = 0
                Bladex.TriggerEvent(22)

            Raster.RemoveBackgroundImage()
            self.bitmap.ReadFromFile(self.path+self.BitmapsNames[self.image1])

            Raster.SetBackgroundImage(4256,2394,"RGB","Normal","Cover",self.bitmap.GetData())


    def DrawFadeImage(self,x,y,time):    
        if self.StartImageTime == 0:
            self.StartImageTime = time

        x = y = 0

        stime = time - self.StartImageTime

        if self.StateImage >= 1:
            if self.StateImage == 1:
                self.StateImage = 2
            elif self.StateImage == 2: #and self.Cache <> 1:
                Bladex.ReadBitMap(self.BitmapsNames[self.image2],self.BitmapsNames[self.image2])
                self.BitmapsHandler.append(Raster.BmpHandle(self.BitmapsNames[self.image2]))
                self.StateImage = 3

            Raster.SetPenColor(255,255,255)    
            Raster.SetPosition(x,y)
            Raster.SetAlpha(1.0)
            Raster.DrawBitmap(self.BitmapsHandler[self.image1],self.ResX,self.ResY)

            if stime >= self.StayImage:
                self.StartImageTime = time
                self.StateImage = 0
            
                self.alpha = 0
        else:
            #self.alpha = stime / self.FadeImage	    

            #if self.alpha >= 1.0:
            #    self.alpha = 1.0
            #    self.StateImage = 1
            #    self.StartImageTime = time
            self.StateImage = 1

            Raster.SetPenColor(255,255,255)    
            Raster.SetPosition(x,y)
            #Raster.SetAlpha(1.0 - self.alpha)
            Raster.SetAlpha(1.0)
            Raster.DrawBitmap(self.BitmapsHandler[self.image1],self.ResX,self.ResY)

            #Raster.SetPenColor(255,255,255)    
            #Raster.SetPosition(x,y)
            #Raster.SetAlpha(self.alpha)
            #Raster.DrawBitmap(self.BitmapsHandler[self.image2],self.ResX,self.ResY)
        
            if self.StateImage:
                self.image1 = self.image2  

                self.image2 = self.image1 + 1

                if self.image2 >= self.Pages:
                #if self.image2 >= 2:
                    self.image2 = 0
                    self.Cache = 1


def NoExitMenu(val):
    return 1

def Show(type = 0,r = 255,g = 255,b = 255):
    import Menu
    Menu.ActivateMenu("credits")
    Menu._MainMenu.MenuPrevItem()
    Menu._MainMenu.MenuPrevItem()
    Menu._MainMenu.ActivateMenuItem()

    Menu.EscapeFunction = NoExitMenu

