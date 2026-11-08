##///
##||| ORC_M9/Pris.PY TITANIUM
##||| Change list:
##||| * No longer assigns regular ork sounds to great ork
##\\\ 

import Bladex
import Sounds
import Reference
import Select
import Change
import Actions
import Bladex
import AuxFuncs
import GameText
import EnemyTypes
import Objects
import Locks
import darfuncs
import AniSound
import Breakings
import OnOff
# char.Position = 26161.7953408, 50321.9662109, 32310.1256269
pris = ""

CanaMaster = 1

_MuereLordKerman=Bladex.CreateSound("../../Sounds/muerte-traidor-2.wav","MuereLordKerman")
_MuereLordKerman.MaxDistance=40000



#  27330.9217891, 50412.1287022, 39652.2325179

OrcoCabreado=Bladex.CreateEntity("OrcoCabron","Great_Ork",0,0,0,"Person" )
OrcoCabreado.Level=10
OrcoCabreado.Blind = 1
OrcoCabreado.Deaf = 1
OrcoCabreado.SetOnFloor()
EnemyTypes.EnemyDefaultFuncs(OrcoCabreado)
# AniSound.AsignarSonidosOrco(OrcoCabreado.Name)        # Stop this nonsense at once -LeadHead

Espadaromana=Bladex.CreateEntity("OrcJJEspadaromana1_","Hacha4",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(Espadaromana)
escudo=Bladex.CreateEntity("OrcJJEscudo1_","Escudo1",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(escudo)

Actions.TakeObject(OrcoCabreado.Name,"OrcJJEspadaromana1_")
Actions.TakeObject(OrcoCabreado.Name,"OrcJJEscudo1_")
Actions.TakeObject("OrcoCabron","llave444")

Finalfinal.AddGuy(OrcoCabreado.Name)
Finalfinal.OnDeath = Ambientefinal

darfuncs.HideBadGuy(OrcoCabreado.Name)

KermanMuerte = darfuncs.E_Grup()
KermanMuerte.OnDeath = SeAcabaFin
KermanMuerte.AddGuy("OrcoCabron")

PrisioneroX()


###################################### PUERTA #################################

rastmaz1=Bladex.CreateEntity("RastMaz1","Rastrillo2",28875,49697.688972,37500)
rastmaz1.Static=0
rastmaz1.Scale=0.685153
rastmaz1.Orientation=0.495618,0.495618,0.504344,-0.504344
Sparks.SetMetalSparkling("RastMaz1")

rastmaz1din=Objects.CreateDinamicObject("RastMaz1")


###cerraduras rastrillos###

##cerradura 1##

cerradura1=Locks.PlaceLock("cerradura1","Cerraduracutre",(27742.021758,50432.984338,35090.599816),(0.000000,0.000000,0.707107,-0.707107),2.5)
cerradura1.key="llave333"


cerradura1.OnUnLockFunc=Abrerastmaz1
cerradura1.OnUnLockArgs=()

cerradura1.OnLockFunc=Cierrarastmaz1
cerradura1.OnLockArgs=()
