##///
##||| Ice_M11/Luces.PY TITANIUM
##||| * Lights at amulet recesses are turned off by default
##||| * Restored (some) unused spot lights
##||| * Added additional lights at large stained glass
##||| * PLAGUE: Suspected will need to do these in-engine, since dynamic lights are less performant
##\\\ 


#--------------------------Titanium lights------------------------------

luzTi1=Bladex.CreateEntity("LuzTi1","Entity Spot",44875.0, -15385.0, 60370.0)
luzTi1.Color=75,175,200
luzTi1.Intensity=25.0
luzTi1.Visible=0
luzTi1.CastShadows=0
luzTi1.Flick=0

luzTi2=Bladex.CreateEntity("LuzTi2","Entity Spot",-1765, -14070, 56410)
luzTi2.Color=75,175,200
luzTi2.Intensity=9.0
luzTi2.Visible=0
luzTi2.CastShadows=0
luzTi2.Flick=0


######
"""
### PLAGUE: Don't like this one, not restoring
luz1=Bladex.CreateEntity("Luz1","Entity Spot",-875,-15500,-12000)
luz1.Color=75,175,200
luz1.Intensity=9.0

### PLAGUE: Don't like this one, not restoring
luz2=Bladex.CreateEntity("Luz2","Entity Spot",38625,-16000,-11750)
luz2.Color=75,175,200
luz2.Intensity=9.0

### PLAGUE: Unused secret room, not restoring... for now.
luz3=Bladex.CreateEntity("Luz3","Entity Spot",35375,-12500,-27000)
luz3.Color=75,175,200
luz3.Intensity=9.0
"""
luz4=Bladex.CreateEntity("Luz4","Entity Spot",-2750,-9000,21960)
luz4.Color=75,75,255
luz4.Intensity=9.0
luz4.Visible=0
luz4.Flick=0
luz4.CastShadows=0

luz5=Bladex.CreateEntity("Luz5","Entity Spot",41460,-9000,22300)
luz5.Color=75,175,175
luz5.Intensity=20.0
luz5.Visible=0
luz5.Flick=0
luz5.CastShadows=0


#--------------------------DESPUES DE LAS ESCALERAS------------------------------

luz6=Bladex.CreateEntity("Luz6","Entity Spot",-2625,-14000,53875)
luz6.Color=75,75,200
luz6.Intensity=9.0
luz6.Visible=0
luz6.Flick=0


luz7=Bladex.CreateEntity("Luz7","Entity Spot",2310,-12000,47000)
luz7.Color=75,75,200
luz7.Intensity=9.0
luz7.Visible=0
luz7.Flick=0

### PLAGUE: Don't like this one, not restoring
# luz8=Bladex.CreateEntity("Luz8","Entity Spot",11375,-12000,47000)
# luz8.Color=75,175,200
# luz8.Intensity=9.0

luz9=Bladex.CreateEntity("Luz9","Entity Spot",26310,-13000,47000)
luz9.Color=75,175,175
luz9.Intensity=9.0
luz9.Visible=0
luz9.Flick=0

luz10=Bladex.CreateEntity("Luz10","Entity Spot",35312.5,-13000,47000)
luz10.Color=75,175,175
luz10.Intensity=8.0
luz10.Visible=0
luz10.Flick=0

""" 
#--------------------------TRONO------------------------------


### PLAGUE: Tablet room. Don't like this one, not restoring
luz11=Bladex.CreateEntity("Luz11","Entity Spot",19000,8000,22500)
luz11.Color=75,150,255
luz11.Intensity=2.0

"""

#--------------------------sala fea------------------------------
### Translates to "ugly room", no idea why, 
### but the lights give a cool effect and a bit more depth        -LeadHead


luz12=Bladex.CreateEntity("Luz12","Entity Spot",7125,-3000,-19717)
luz12.Color=75,255,255
luz12.Intensity=6.0
luz12.Visible=0
luz12.Flick=0

luz13=Bladex.CreateEntity("Luz13","Entity Spot",30625,-3000,-19717)
luz13.Color=75,255,255
luz13.Intensity=5.0
luz13.Visible=0
luz13.Flick=0

#--------------------------sala de la power------------------------------


luzsolida2=Bladex.CreateEntity("Luzsolida2","Entity Spot",-2025,7000,12717)
luzsolida2.Color=105,145,84
luzsolida2.Intensity=15
luzsolida2.CastShadows=0
luzsolida2.Precission=0.16
luzsolida2.Visible=0
luzsolida2.Flick=0

#########################
########## SUSTITUYE A LOS BRASEROS

luzBRA1=Bladex.CreateEntity("LuzBRA1","Entity Spot",1077.142000,-9263.218000,-12114.06300)
luzBRA1.Color=255,159,53
luzBRA1.Intensity=0
luzBRA1.CastShadows=0
luzBRA1.Precission=0.36
luzBRA1.Visible=0
luzBRA1.Flick=0

luzBRA2=Bladex.CreateEntity("LuzBRA2","Entity Spot",37627.946000,-9247.335000,-12094.45900)
luzBRA2.Color=255,159,53
luzBRA2.Intensity=0
luzBRA2.CastShadows=0
luzBRA2.Precission=0.36
luzBRA2.Visible=0
luzBRA2.Flick=0