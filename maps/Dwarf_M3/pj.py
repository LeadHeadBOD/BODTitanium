



import AniSound
import Reference
import Basic_Funcs
import Sparks
import Breakings

###### Player1:Dwarf  ######
char=Bladex.CreateEntity("Player1","Dwarf_N",0,0,0,"Person")
char.Angle=0.0
char.Position= 78000,3000,-136000
char.Data=Basic_Funcs.PlayerPerson(char)
inv=char.GetInventory()
AniSound.AsignarSonidosEnano('Player1')

####### Shield:Escudo2 #######
o=Bladex.CreateEntity("EscudoInvPrb2","Escudo2",0,0,0)
Sparks.MakeShield("EscudoInvPrb2")
#inv.AddShield("EscudoInvPrb2")
inv.LinkLeftHand("EscudoInvPrb2")
Breakings.SetBreakableWS("EscudoInvPrb2")


####### Weapon:Hacha #######
o=Bladex.CreateEntity("WeaponInvPrb1","Hacha",0,0,0,"Weapon")
#inv.AddWeapon("WeaponInvPrb1")
inv.LinkRightHand("WeaponInvPrb1")
Breakings.SetBreakableWS("WeaponInvPrb1")



