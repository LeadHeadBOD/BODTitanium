import Actions
import AniSound
import Reference
import Basic_Funcs
import Sparks
import ItemTypes

#char=Bladex.CreateEntity("Player1","Amazon_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Knight_N",0,0,0,"Person")
char=Bladex.CreateEntity("Player1","Barbarian_N",0,0,0,"Person")
#char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0,"Person")

char.Position=326125.081178, -1276.36920221, -327.538538204
char.Angle=0.0
char.Level=18
inv=char.GetInventory()

char.SendTriggerSectorMsgs=1
char.Data=Basic_Funcs.PlayerPerson(char)


o=Bladex.CreateEntity("WeaponInvPrb3","Arco",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
inv.AddBow(o.Name)

o=Bladex.CreateEntity("QuiverInvPrb1","Carcaj",0,0,0)
ItemTypes.ItemDefaultFuncs (o)
inv.AddQuiver(o.Name)


###AMAZONA
"""
o=Bladex.CreateEntity("WeaponInvPrb1","LanzaAncha",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
Actions.TakeObject(char.Name,o.Name)

o=Bladex.CreateEntity("WeaponInvPrb1","BladeSword2",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs (o)
Actions.TakeObject(char.Name,o.Name)
"""


###BARBARO

o=Bladex.CreateEntity("WeaponInvPrb1","BladeSword2Barbarian",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


o=Bladex.CreateEntity("WeaponInvPrb1","SawSword",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)


###CABALLERO
"""
o=Bladex.CreateEntity("EscudoInvPrb1","Escudo1",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("WeaponInvPrb1","Espada",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("WeaponInvPrb1","BladeSword2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

"""

###ENANO
"""

o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("WeaponInvPrb1","Martillo3",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

o=Bladex.CreateEntity("WeaponInvPrb1","BladeSword2",0,0,0,"Weapon")
Actions.TakeObject(char.Name,o.Name)
ItemTypes.ItemDefaultFuncs (o)

"""
