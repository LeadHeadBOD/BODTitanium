##///
##||| CHAOS_M17/breaks.PY TITANIUM
##||| Change list:
##||| * Spark pass
##\\\ 

import Breakings
import Actions
import BBLib
import Reference
#breaks_firstTime= time.time()

BoxBurnTime = 6
BoxDestroyTime = 12


#####
##### Zona aposentos guardia
###MESITAS

BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Mesita")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Silla")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Barril")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Camastro")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Argolla")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Gozne")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Peanapiedra")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Gargola02")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Columna")
BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Dragon_estatua")
#BBLib.LoadResourceToMemory(BBLib.B_CID_OBJDSCR, "Gargola")

#breaks_lastTime=time.time()
#print "break objects resources loaded ("+`breaks_lastTime-breaks_firstTime`+" seconds)"
#breaks_firstTime=breaks_lastTime

o=Bladex.CreateEntity("Mesita1","Mesita",325110.880083,42561.889592,-80411.117030,"Physic")
o.Scale=1.334504
o.Orientation=0.000000,0.000000,0.707107,-0.707107

o=Bladex.CreateEntity("Mesita2","Mesita",351214.377795,44667.746535,-85500.031158,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("Mesita3","Mesita",347357.293884,44667.825077,-97754.668486,"Physic")
o.Scale=1.000000
o.Orientation=0.477714,0.477714,0.521334,-0.521334

o=Bladex.CreateEntity("Mesita4","Mesita",358846.380577,44671.195220,-98183.944543,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("Mesita5","Mesita",358846.380577,44671.195220,-98183.944543,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("Mesita6","Mesita",357236.924872,44669.827573,-85156.001304,"Physic")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000



###SILLAS

silla1=Bladex.CreateEntity("Silla1","Silla",325234.102964,42266.591323,-77777.908969,"Physic")
silla1.Scale=1.000000
silla1.Orientation=0.640856,0.640856,-0.298836,0.298836

silla2=Bladex.CreateEntity("Silla2","Silla",349802.014009,44267.868450,-86548.917322,"Physic")
silla2.Scale=1.000000
silla2.Orientation=0.579228,0.579228,-0.405580,0.405580

silla3=Bladex.CreateEntity("Silla3","Silla",356109.116422,44267.266416,-97897.510387,"Physic")
silla3.Scale=1.000000
silla3.Orientation=0.298836,0.298836,-0.640856,0.640856



###BARRILETES Y OTRAS COSAS

o=Bladex.CreateEntity("Barril8","Barril",342877.546928,42159.919508,-81351.081056,"Physic")
o.Scale=2.006763
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("Barril9","Barril",342888.990159,42401.100387,-80206.860730,"Physic")
o.Scale=1.416603
o.Orientation=0.706434,0.706434,-0.030844,0.030844

o=Bladex.CreateEntity("Barril10","Barril",344255.637853,42319.887491,-80583.411111,"Physic")
o.Scale=1.612226
o.Orientation=0.707107,0.707107,0.000000,0.000000



####objetos  no rompibles

o=Bladex.CreateEntity("Cama1","Camastro",326430.895000,42509.987000,-79920.209000,"Physic")
o.Scale=1.374941
o.Orientation=0.500000,0.500000,-0.500000,0.500000

o=Bladex.CreateEntity("Argolla1","Argolla",329145.374000,41595.352000,-78246.075000,"Physic")
o.Scale=1.000000
o.Orientation=0.589646,0.589646,-0.390278,0.390278

o=Bladex.CreateEntity("Gozne1","Gozne",323951.661000,41640.164000,-78885.278000,"Physic")
o.Scale=1.000000
o.Orientation=0.504344,0.495618,-0.486740,0.512917

o=Bladex.CreateEntity("Argolla2","Argolla",341726.194000,41635.603000,-76558.055000,"Physic")
o.Scale=1.000000
o.Orientation=0.700225,0.700225,-0.098410,0.098410

o=Bladex.CreateEntity("Camastro2","Camastro",350462.677000,44612.822000,-79770.632000,"Physic")
o.Scale=1.374941
o.Orientation=0.500000,0.500000,-0.500000,0.500000

o=Bladex.CreateEntity("Camastro3","Camastro",348562.418000,44545.461000,-99139.208000,"Physic")
o.Scale=1.295256
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("Camastro4","Camastro",352293.318000,44575.478000,-86589.027000,"Physic")
o.Scale=1.208109
o.Orientation=0.500000,0.500000,-0.500000,0.500000

o=Bladex.CreateEntity("Camastro5","Camastro",357801.436000,44558.485000,-99120.948000,"Physic")
o.Scale=1.244716
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("Camastro6","Camastro",355691.546000,44540.964000,-86517.894000,"Physic")
o.Scale=1.295256
o.Orientation=0.500000,0.500000,-0.500000,0.500000

o=Bladex.CreateEntity("Argolla3","Argolla",413735.387000,64226.004000,-29738.938000,"Physic")
o.Scale=1.000000
o.Orientation=0.706864,0.706864,-0.018510,0.018510

o=Bladex.CreateEntity("Argolla4","Argolla",413809.186000,64203.387000,-30770.706000,"Physic")
o.Scale=1.000000
o.Orientation=0.018509,0.018509,-0.706865,0.706864

peana1=Bladex.CreateEntity("Peana1","Peanapiedra",422069.000000,70431.170000,10777.980000,"Physic")
peana1.Scale=8.326311
peana1.CastShadows=0
peana1.Orientation=0.500000,0.500000,0.500000,-0.500000

gargola1=Bladex.CreateEntity("Gargola1","Gargola02",422189.857000,65120.809000,9928.146000,"Physic")
gargola1.Scale=5.704800
gargola1.CastShadows=0
gargola1.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("NoName276","Columna",362858.976382, 49350.269775, -40063.595621)
Sparks.SetStoneSparkling(o.Name)        # Add
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000


o=Bladex.CreateEntity("NoName278","Columna",370052.738448,31587.385818,-40169.053655)
Sparks.SetStoneSparkling(o.Name)        # Add
o.Static=1
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000

o=Bladex.CreateEntity("LEDEntity_temp229","Dragon_estatua",706999.069000,311260.558000,170139.189000)
o.Scale=1.694466
o.Orientation=0.500000,0.500000,0.500000,-0.500000
o.CastShadows=0

chaosbloque=Bladex.CreateEntity("Chaosbloque","Bloque",285224.897766,29315.270829,-47676.661369)
chaosbloque.Scale=8.664392
chaosbloque.Orientation=0.622053,0.741904,-0.161985,0.190759
chaosbloque.CastShadows=0
chaosbloque.Alpha=0
Reference.EntitiesSelectionData["Chaosbloque"]=[0,0,""]

"""
peana2=Bladex.CreateEntity("Peana2","Peanapiedra",507422.843000,78448.651000,-1997.494000,"Physic")
peana2.Scale=9.382295
peana2.CastShadows=0
peana2.Orientation=0.369462,0.369462,0.602908,-0.602908

gargola2=Bladex.CreateEntity("Gargola2","Gargola",506633.872000,71111.375000,-3244.411000,"Physic")
gargola2.Scale=4.817005
gargola2.CastShadows=0
gargola2.Orientation=0.690346,0.690346,0.153046,-0.153046
"""

#breaks_lastTime=time.time()
#print "break objects created ("+`breaks_lastTime-breaks_firstTime`+" seconds)"
#breaks_firstTime=breaks_lastTime

Breakings.SetBreakable("Mesita1",12,100)
Breakings.SetBreakable("Mesita2",12,100)
Breakings.SetBreakable("Mesita3",12,100)
Breakings.SetBreakable("Mesita4",12,100)
Breakings.SetBreakable("Mesita5",12,100)
Breakings.SetBreakable("Mesita6",12,100)
Breakings.SetBreakable("Silla1",12,100)
Breakings.SetBreakable("Silla2",12,100)
Breakings.SetBreakable("Silla3",12,100)
Breakings.SetBreakable("Barril8",12,100)
Breakings.SetBreakable("Barril9",12,100)
Breakings.SetBreakable("Barril10",12,100)

#breaks_lastTime=time.time()
#print "break objects SetBreakable ("+`breaks_lastTime-breaks_firstTime`+" seconds)"
#breaks_firstTime=breaks_lastTime

Actions.SetBurnable("Mesita1",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Mesita2",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Mesita3",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Mesita4",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Mesita5",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Mesita6",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Silla1",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Silla2",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Silla3",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Barril8",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Barril9",BoxBurnTime,BoxDestroyTime)
Actions.SetBurnable("Barril10",BoxBurnTime,BoxDestroyTime)

#breaks_lastTime=time.time()
#print "break objects SetBurnable ("+`breaks_lastTime-breaks_firstTime`+" seconds)"
#breaks_firstTime=breaks_lastTime
