##///
##||| PhantonFX.PY TITANIUM
##||| Change list:
##||| * Disappearing chars (fading skeletons, zombies) will now fade their lights and fires.
##||| * 
##||| * 
##\\\ 

import Bladex

Bladex.CreateTimer("AlphaTimer",0.05)

Delta  = 0.025
SecAgo = 0.0

OnAppears    = {}
OnDisappears = {}

###  TimerFunc  
#################
def Appears(e_name, time):

   esq          = Bladex.GetEntity(e_name)
   if esq.Person and esq.InvRight:
     Der          = Bladex.GetEntity(esq.InvRight)
   else:
     Der          = None

   if esq.Person and esq.InvLeft:
     Izq          = Bladex.GetEntity(esq.InvLeft)
   else:
     Izq          = None

   val    = esq.Alpha + OnAppears[e_name][1]   
   if val >= 1.0 :
     esq.TimerFunc  = ""     
     esq.RemoveFromList("AlphaTimer")
     val            = 1.0
     if OnAppears[e_name][0] <>"":
       OnAppears[e_name][0](e_name)
       del OnAppears[e_name]


   esq.Alpha      = val
   if Der:
     Der.Alpha      = val
   if Izq:
     Izq.Alpha      = val


import AuxFuncs     # Added -LeadHead

###  TimerFunc  
#################
def Disappears(e_name, time):
   
   esq          =  Bladex.GetEntity(e_name)
   if esq.Person and esq.InvRight:
     Der          = Bladex.GetEntity(esq.InvRight)
   else:
     Der          = None

   if esq.Person and esq.InvLeft:
     Izq          = Bladex.GetEntity(esq.InvLeft)
   else:
     Izq          = None

   Spt            = AuxFuncs.GetSpot(esq)           # Get spot and fire entity,
   if Spt:                                          # record its original intensity
     l_int        = Spt.Intensity                   #           -LeadHead
   Fire           = AuxFuncs.GetDynamicFires(esq)   #
   if Fire:                                         #
     f_int        = Fire[0].Intensity               #
     

   val    = esq.Alpha - OnDisappears[e_name][1]   
   if val <= 0.001:
     esq.TimerFunc  = ""
     esq.RemoveFromList("AlphaTimer")
     if esq.Person: esq.Life       = 0     
     Bladex.AddScheduledFunc(Bladex.GetTime()+OnDisappears[e_name][2], esq.SubscribeToList,("Pin",))
     val            = 0.0
     if OnDisappears[e_name][0] <>"":
       OnDisappears[e_name][0](e_name)
       del OnDisappears[e_name]
     return

   esq.Alpha        = val
   if Der:
     Der.Alpha      = val
   if Izq:
     Izq.Alpha      = val
   if Spt:                          # If we have a light, fade it
     Spt.Intensity  = l_int * val   # 
   if Fire:                         #
     for i in Fire:                 # and fade all fires
       i.Intensity = f_int / val    #                -LeadHead

#
#  If the object appears....
#------------------------------------
def AppearsChar(charnam,func=""):
        global Delta
        global SecAgo
        
        esq            = Bladex.GetEntity(charnam)
        esq.TimerFunc  = Appears
        esq.SubscribeToList("AlphaTimer")        
        OnAppears[charnam] = (func,Delta,SecAgo)

#
#  If the object Disappears....
#------------------------------------
def DisappearsChar(charnam,func=""):
        global Delta
        global SecAgo
        
        esq            = Bladex.GetEntity(charnam)
        esq.TimerFunc  = Disappears
        esq.SubscribeToList("AlphaTimer")
        OnDisappears[charnam] = (func,Delta,SecAgo)


###################################
#########    SaveStuff    #########
###################################


def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(Delta,
     SecAgo,
     OnAppears,
     OnDisappears
    )
  p.dump(d)
  funcfile.close()


def LoadData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  p.persistent_load=GameStateAux.persistent_load
  d=p.load()
  funcfile.close()
  print d

  global Delta
  global SecAgo
  global OnAppears
  global OnDisappears

  Delta        = d[0]
  SecAgo       = d[1]
  OnAppears    = d[2]
  OnDisappears = d[3]

import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))
