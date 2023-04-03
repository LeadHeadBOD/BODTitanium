##///
##||| FINAL.PY TITANIUM
##||| Change list:
##||| * Restored the missing "The end" camera and game text.
##||| * Doors actually close now and don't leave a huge gap in the middle. (Refer to puertas.py)
##||| * Added fancy light effect?
##\\\ 


import Bladex
import Scorer
import Reference
import AuxFuncs
import Credits
import darfuncs
import Language
import MemPersistence
import GotoMapVars

#execfile("final.py")

SceneOpenDoorsStartTime = 0

finaldoor1 = Bladex.GetEntity("PuertaFin0")
finaldoor2 = Bladex.GetEntity("PuertaFin1")

SceneOpenDoorsTime = 2.5
SceneOpenDoorsTicks = 60

def SceneOpenDoors(Camera,Frame):
    global SceneOpenDoorsStartTime
    SceneOpenDoorsStartTime=Bladex.GetTime()

    finaldoor1.TimerFunc=SceneOpenDoorTimer
    finaldoor1.SubscribeToList("Timer60")
    AuxFuncs.FadeTo(3.0,1.5)
    GotoMapVars.GrantRank()

def SceneOpenDoorTimer(ent, time):
    time = Bladex.GetTime()
    time = time - SceneOpenDoorsStartTime
    delta = (3.14159/2.0)/(SceneOpenDoorsTicks*SceneOpenDoorsTime)      ### Was (2.8/2.0) -LeadHead
    finaldoor1.RotateRel(0,0,0,0,0,1, delta)
    finaldoor2.RotateRel(0,0,0,0,0,1,-delta)
    if (time>SceneOpenDoorsTime):
        finaldoor1.RemoveFromList("Timer60")
        finaldoor1.TimerFunc=""

def StopCameraFinal(Camera,frame):
    bsword=Bladex.GetEntity("BladeSword") #Added -LeadHead
    cam = Bladex.GetEntity("Camera")
    cam.TType   = 0
    cam.SType   = 0

    cam.Position = 93000, -6300, 175000
    #cam.TPos     = 94000, -3400, 172000
    cam.TPos     = bsword.Position[0], bsword.Position[1], bsword.Position[2] #Added -LeadHead

    Scorer.SetVisible(0)
    #Bladex.ActivateInput()
    Bladex.GetEntity("Player1").Freeze()
    AuxFuncs.FadeFrom(2.0,0)                # Was 4.0, 0 -LeadHead

    import TutorialScorer
    import GameText
    ld=Bladex.GetEntity("LuzDiosaFinal")    #Added -LeadHead
    ld.Visible=0                            # 
    TutorialScorer.ActivateTutorialScorer(Language.LetrasMenuBig)
    GameText.Textos["THE_END"] = ["THE END"]
    TutorialScorer.ShowUC("THE_END",0)
    Bladex.AddScheduledFunc(Bladex.GetTime()+6.0,GotoCreds,())      # Added -LeadHead
    
def GotoCreds():                # Added
    Bladex.ActivateInput()      #
    Credits.Show(1)             #       -LeadHead

def CreatePlayerFinal(Kind):
    if Kind[0] =="K":
        char=Bladex.CreateEntity("PFinal","Knight_N",0,0,0)
        Bladex.LoadSampledAnimation("../../Anm/Kgt_final_blade.BMV","Kgt_final_blade",1,"Knight_N")

    if Kind[0] =="A":
        char=Bladex.CreateEntity("PFinal","Amazon_N",0,0,0)
        Bladex.LoadSampledAnimation("../../Anm/Amz_final_blade.BMV","Amz_final_blade",1)

    if Kind[0] =="D":
        char=Bladex.CreateEntity("PFinal","Dwarf_N",0,0,0)
        Bladex.LoadSampledAnimation("../../Anm/Dwf_final_blade.BMV","Dwf_final_blade",1)

    if Kind[0] =="B":
        char=Bladex.CreateEntity("PFinal","Barbarian_N",0,0,0)
        Bladex.LoadSampledAnimation("../../Anm/Bar_final_blade.BMV","Bar_final_blade",1)

    char.RotateRel(0,0,0,1,0,0,1.57)


def StartFinal():
    AuxFuncs.FadeFrom(3.0,0.0)
    char = Bladex.GetEntity("PFinal")
    char.Actor = 1

    if char.Kind[0] =="K":
        char.Position = 94131,-3078,182519
        char.Animation = "Kgt_final_blade"
    if char.Kind[0] =="B":
        char.Position = 94501,-3264,182337
        char.Animation = "Bar_final_blade"
    if char.Kind[0] =="D":
        char.Position = 94249,-2871,182456
        char.Animation = "Dwf_final_blade"
    if char.Kind[0] =="A":
        char.Position = 94249,-3081,182505
        char.Animation = "Amz_final_blade"

    char.TurnOn()

    cam = Bladex.GetEntity("Camera")
    cam.SetMaxCamera("Final_BladeCamera01.cam",0,-1)
    cam.AddCameraEvent(-1,StopCameraFinal)
    cam.AddCameraEvent(135,SceneOpenDoors)

    Scorer.SetVisible(0)
    Bladex.DeactivateInput()


main_char = ""

if MemPersistence.Get('MainChar') == None:
    main_char = "Knight_N"
else:
    main_char = MemPersistence.Get('MainChar')[0]['Kind'][0]

CreatePlayerFinal(main_char)
Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,darfuncs.HideBadGuy,("Player1",))
Bladex.AddScheduledFunc(Bladex.GetTime(),StartFinal,())

bladesword = Bladex.CreateEntity("BladeSword","BladeSword",94355.2677885, -3148.18632875, 172034.430763)

bladesword.Orientation = 0.0355769842863, 0.0296567473561, 0.705896496773, -0.706829726696
bladesword.Static=1
bladesword.Weapon=1
Reference.EntitiesSelectionData[bladesword.Name]=(0,0,"")

x, y, z = bladesword.Position                                                   #
ld=Bladex.CreateEntity("LuzDiosaFinal", "Entity Spot", x, y-260.0, z+150.0)     #   Addded
ld.Color=90, 190, 255                                                           #
ld.Intensity=7.0                                                                #
ld.Precission=0.08                                                              #
ld.Visible=1                                                                    #       -LeaHead
ld.CastShadows=0                                                                #
ld.Flick=0                                                                      #
ld.SizeFactor  = 2                                                              #

Bladex.AddScheduledFunc(Bladex.GetTime()+0.1,Bladex.TriggerEvent,(21,))
