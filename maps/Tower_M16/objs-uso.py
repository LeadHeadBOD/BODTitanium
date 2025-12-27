##///
##||| Tower_M16/objs-uso.PY TITANIUM
##||| Change list:
##||| * box near minotaur now breakable
##||| * Invisible blockers no longer have selection data
##\\\ 

import Breakings
import pocimac
import Sparks

######    ENTRADA DE LA TORRE

Breakings.SetBreakable("cajon1",12,30)
Breakings.SetBreakable("cajona1",12,30) # Add
Breakings.SetBreakable("cajon2",12,30)
Breakings.SetBreakable("cajon3",12,30)
Breakings.SetBreakable("cajon4",12,30)
Breakings.SetBreakable("cajon5",12,30)
Breakings.SetBreakable("cajon6",12,30)
Breakings.SetBreakable("cajon7",12,30)


Breakings.SetBreakable("meson1",12,100)

Breakings.SetBreakable("barril1",12,30)
Breakings.SetBreakable("barril2",12,30)
Breakings.SetBreakable("barril3",12,30)


####      SALA GRANDE PLANTA BAJA
#Breakings.SetBreakable("meson2",12,100)

####------SALA ANTERIOR A LA GALERIA
Breakings.SetBreakable("cajon9",12,30)



pan=Breakings.CreateHiddenObject("towerpoci1", "Pocima50",1.2,(0.0,0.0,0.0),(0.5,0.5,0.5,-0.5))
pan.Solid=1
pan.Static=0
pocimac.CreatePotion("towerpoci1")
Breakings.SetBreakable("cajon10",12,30,"towerpoci1")


Breakings.SetBreakable("cajon11",12,30)

######    PLANTA INTERMEDIA
Breakings.SetBreakable("mesa1",8,10)
Breakings.SetBreakable("mesa2",8,10)

     ##  al lado de la galeria
Breakings.SetBreakable("cofre3",8,10)
Breakings.SetBreakable("cofre4",8,10)
Breakings.SetBreakable("cajon8",8,10)

 
######    SEGUNDA PLANTA ARMERIA

Breakings.SetBreakable("ArmeroA1",8,10)
Breakings.SetBreakable("ArmeroA2",8,10)
Breakings.SetBreakable("ArmeroA3",8,10)
Breakings.SetBreakable("ArmeroA4",8,10)

############################################
#######		BLOQUEO DE ZONAS 

###	TRAMPA DE LA LAVA


o=Bladex.CreateEntity("Bloqueo0","Bloque",-8520.564175,-57527.573203,28214.397426)
o.Scale=2.497850
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.Solid=1
o.Alpha = 0
o.CastShadows=0
darfuncs.SetHint(o,"","",0.0,0.0)

o=Bladex.CreateEntity("Bloqueo1","Bloque",-11126.859559,-59894.689921,22488.510788)
o.Scale=2.871214
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.Solid=1
o.Alpha = 0
o.CastShadows=0
darfuncs.SetHint(o,"","",0.0,0.0)


o=Bladex.CreateEntity("Bloqueo2","Bloque",-13589.186093,-62419.166691,22540.015226)
o.Scale=2.786772
o.Orientation=0.500000,0.500000,-0.500000,0.500000
o.Solid=1
o.Alpha = 0
o.CastShadows=0
darfuncs.SetHint(o,"","",0.0,0.0)
