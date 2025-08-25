##///
##||| TOMB_M7/tumbarey.PY TITANIUM
##||| Change list:
##||| * Removed selection data for stone upon which the fetish lies as it's distracting
##||| * Created separete sound event for second door
##\\\ 


import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import ReadGSFile
import Button

#o=Bladex.CreateEntity("lapidarey","Lapidarey",109092.427000,1310.936000,607.453000)
#o.Static=0
#o.Scale=1.257163
#o.Orientation=0.498355,0.498555,-0.501735,0.501345


#####  PUERTAS DE ACCESO A LA TUMBA DEL REY

maderadesliz=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDesliz")
maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpe")

### Added to fix only one door making this sound
maderadeslizDup=Sounds.CreateEntitySound("../../Sounds/block-sliding.wav", "MaderaDeslizDup")
maderagolpeDup=Sounds.CreateEntitySound("../../Sounds/puerta-piedra-golpe.wav", "MaderaGolpeDup")


puertadoble1=Doors.CreateDoor("PuertaDoble1", (84375,1000,3500), (0,1,0), 1000, 5300, Doors.CLOSED)


puertadoble1.opentype=Doors.UNIF
puertadoble1.o_med_vel=-800
puertadoble1.o_med_displ=4300

puertadoble1.closetype=Doors.UNIF
puertadoble1.c_med_displ=4300
puertadoble1.c_med_vel=800


puertadoble1.SetWhileOpenSound(maderadesliz)
puertadoble1.SetEndOpenSound(maderagolpe)

puertadoble1.SetWhileCloseSound(maderadesliz)
puertadoble1.SetEndCloseSound(maderagolpe)

#####
puertadoble2=Doors.CreateDoor("PuertaDoble2", (84375,1000,-2500), (0,1,0), 1000, 5300, Doors.CLOSED)

puertadoble2.opentype=Doors.UNIF
puertadoble2.o_med_vel=-800
puertadoble2.o_med_displ=4300

puertadoble2.closetype=Doors.UNIF
puertadoble2.c_med_displ=4300
puertadoble2.c_med_vel=800


puertadoble2.SetWhileOpenSound(maderadeslizDup)
puertadoble2.SetEndOpenSound(maderagolpeDup)

puertadoble2.SetWhileCloseSound(maderadeslizDup)
puertadoble2.SetEndCloseSound(maderagolpeDup)




#o=Bladex.CreateEntity("bloqueto","Bloque",83000.0,4295.092329,773.897539)
#o.Static=0
#o.Scale=1.000000
#o.Orientation=0.707107,0.707107,0.000000,0.000000

#buttonto=Button.CreateButtonCombination(0,AbrePuertadoble,"")
#buttonto.AddButton("bloqueto",3,(1,0,0),400,0,0,1)

##########   MECANISMO DEL FETICHE

###trampa cripta

###tramo A. La escalera baja

#maderadesliz=Sounds.CreateEntitySound("../../Sounds/puerta-madera-deslizando.wav", "MaderaDesliz")
#maderagolpe=Sounds.CreateEntitySound("../../Sounds/puerta-madera-golpe.wav", "MaderaGolpe")


#escalon 1a
escalon1a=Doors.CreateDoor("Escalon1a", (110500,2200,500), (1,0,0), 0, 750, Doors.CLOSED)

escalon1a.opentype=Doors.UNIF
escalon1a.o_med_vel=-600
escalon1a.o_med_displ=750

escalon1a.closetype=Doors.UNIF
escalon1a.c_med_vel=600
escalon1a.c_med_displ=750


#escalon 3a
escalon3a=Doors.CreateDoor("Escalon3a", (110500,2500,500), (0,-1,0), 0, 500, Doors.OPENED)

escalon3a.opentype=Doors.UNIF
escalon3a.o_med_vel=-300
escalon3a.o_med_displ=500

escalon3a.closetype=Doors.UNIF
escalon3a.c_med_vel=300
escalon3a.c_med_displ=500


#funci�n que sube y baja los escalones de ambos tramos al unisono



ff=Bladex.CreateEntity("Fetiche1","Fetiche",110505.761761,2469.665144,665.023759)
ff.Static=0
ff.Scale=1.000000
ff.Orientation=0.964966,-0.101762,0.145226,-0.193379


bl=Bladex.CreateEntity("bloquerey","Bloque",110491.806000,2762.897000,675.543000)
bl.Static=0
bl.Scale=1.000000
bl.Orientation=0.500000,0.500000,-0.500000,0.500000
Reference.EntitiesSelectionData[bl.Name]=(0,0,"")   # Removed selection data -LeadHead