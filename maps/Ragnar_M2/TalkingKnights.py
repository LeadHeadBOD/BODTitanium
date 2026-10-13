import def_class
from math import pow
import Bladex
import pdb
import Reference
import EnemyTypes
import Sparks
import Enm_Def
import Actions
import pocimac
import Sounds

true = 1
false = 0

#######################################################
# Define the talking knight class
#######################################################

#Bladex.LoadSampledAnimation("../../Anm/Tkn_speak01.bmv","Tkn_speak01",0,"Knight_Traitor")
#Bladex.LoadSampledAnimation("../../Anm/Tkn_speak02.bmv","Tkn_speak02",0,"Knight_Traitor")


#######################################################
# Create the first knight
# (named after Eric Idle playing JAILER'S ASSISTANT in Life of Brian)
#######################################################

### tiene la LLAVE de la capilla

sword1=Bladex.CreateEntity("RagnarEricsSword","Garrote",0,0,0,"Weapon")
shield1=Bladex.CreateEntity("RagnarEricsShield","Escudo2",0,0,0)
Sparks.MakeShield("RagnarEricsShield")

knt1=Bladex.CreateEntity("Eric","Knight_Traitor",-91610, -8748, -7916,"Person")
knt1.Level=2
knt1.Angle=4.4
Actions.TakeObject(knt1.Name,"RagnarEricsSword")
Actions.TakeObject(knt1.Name,"RagnarEricsShield")
Actions.TakeObject("Eric","Llavep2")

knt1.ActionAreaMin=pow(2,0)
knt1.ActionAreaMax=pow(2,1)
knt1.Data = def_class.TalkingKnight (knt1)
knt1.Data.JoinGroup("Eric", "Talking Knights")
knt1.SetOnFloor()


#######################################################
# Create the second knight
# (named after Terry Gilliam playing JAILER in Life of Brian)
#######################################################

sword2=Bladex.CreateEntity("RagnarTerrysSword","Gladius",0,0,0,"Weapon")
shield2=Bladex.CreateEntity("RagnarTerrysShield","Escudo5",0,0,0)
Sparks.MakeShield("RagnarTerrysShield")

potion1=Bladex.CreateEntity("TerrysPotion","Pocima25",0,0,0)
potion1.Static=0
potion1.Solid=0
potion1.Scale=1.220190
pocimac.CreatePotion("TerrysPotion")

knt2=Bladex.CreateEntity("Terry","Knight_Traitor",-86500, -8748, -7250,"Person")
knt2.Level=2
knt2.Angle=1.5
Actions.TakeObject(knt2.Name,"RagnarTerrysSword")
Actions.TakeObject(knt2.Name,"RagnarTerrysShield")
Actions.TakeObject(knt1.Name,"TerrysPotion")

knt2.ActionAreaMin=pow(2,0)
knt2.ActionAreaMax=pow(2,1)
knt2.Data = def_class.TalkingKnight (knt2)
knt2.Data.JoinGroup("Terry", "Talking Knights")
knt2.SetOnFloor()
Reset()
