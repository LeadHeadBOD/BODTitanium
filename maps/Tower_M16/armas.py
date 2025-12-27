##///
##||| Tower_M16/armas.PY TITANIUM
##||| Change list:
##||| * fix stuck spear
##\\\ 


import Breakings
import Sparks


#

##escudo en la despensa
o=Bladex.CreateEntity("NoName28","Escudo6",-32794.894535,-4757.436528,3283.029818,"Weapon")
o.Scale=1.000000
o.Orientation=0.673601,-0.211487,0.677357,0.206692
ItemTypes.ItemDefaultFuncs (o)



###EN LA ARMERIA


o=Bladex.CreateEntity("TowerVampWeapon","VampWeapon",-4366.978604,-18968.909741,-420.640111,"Weapon")
o.Scale=1.000000
o.Orientation=0.759867,0.069410,-0.140775,0.630846
ItemTypes.ItemDefaultFuncs (o)
#

o=Bladex.CreateEntity("TowerLanza1","Lanza",-8918.282387,-19304.485099,7077.626640,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
ItemTypes.ItemDefaultFuncs (o)
#

o=Bladex.CreateEntity("TowerAlabarda","Alabarda",-8756.415431,-19627.793975,11210.117686,"Weapon")
o.Scale=1.000000
o.Orientation=0.707107,0.707107,0.000000,0.000000
ItemTypes.ItemDefaultFuncs (o)
#


o=Bladex.CreateEntity("TowerLanza2","Lanza",-18251.635789,-19290.94,-99.097735,"Weapon")        ## change
o.Scale=1.000000
o.Orientation=0.629320,0.777146,0.000000,0.000000
ItemTypes.ItemDefaultFuncs (o)
#

o=Bladex.CreateEntity("TowerLanzaAncha","LanzaAncha",-17459.024326,-19276.545693,-65.185672,"Weapon")
o.Scale=1.000000
o.Orientation=0.636078,0.771625,0.000000,0.000000
ItemTypes.ItemDefaultFuncs (o)
#


o=Bladex.CreateEntity("TowerMartillo3","Martillo3",-20237.210263,-19035.119434,16618.050125,"Weapon")
o.Scale=1.000000
o.Orientation=0.000000,0.002599,-0.064107,0.997940
ItemTypes.ItemDefaultFuncs (o)
#

o=Bladex.CreateEntity("TowerEspada","Espada",-7226.678314,-18430.412862,17295.446932,"Weapon")
o.Scale=1.000000
o.Orientation=0.433701,0.896582,-0.043209,-0.078590
ItemTypes.ItemDefaultFuncs (o)
#

o=Bladex.CreateEntity("TowerSawSword","SawSword",-14757.173839,-18803.893019,18170.528552,"Weapon")
o.Scale=1.000000
o.Orientation=0.727026,-0.015552,-0.686425,0.003516
ItemTypes.ItemDefaultFuncs (o)
#



#ARMADURAS

towarmaDmed=Bladex.CreateEntity("twArmaduraEnanoMedia","ArmaduraEnanoMedia",-20218.159834,-19122.939873,1786.116812)
towarmaDmed.Scale=1.000000
towarmaDmed.Static=0
towarmaDmed.Solid=0
towarmaDmed.Orientation=0.477712,0.468143,-0.524974,0.526342
#


towarmaAl=Bladex.CreateEntity("twArmaduraAmazonaLigera","ArmaduraAmazonaLigera",-7198.749474,-18884.405424,18019.680472)
towarmaAl.Scale=1.000000
towarmaAl.Static=0
towarmaAl.Solid=0
towarmaAl.Orientation=0.707107,0.707107,0.000000,0.000000
#

towarmCC=Bladex.CreateEntity("twArmaduraCaballeroCompleta","ArmaduraCaballeroCompleta",-10744.425489,-18946.110793,18753.095939)
towarmCC.Scale=1.000000
towarmCC.Static=0
towarmCC.Solid=0
towarmCC.Orientation=0.707107,0.707107,0.000000,0.000000
#


towarmB=Bladex.CreateEntity("twArmaduraBarbaroLigera","ArmaduraBarbaroLigera",-7483.292712,-18988.349747,9170.060491)
towarmB.Scale=1.000000
towarmB.Static=0
towarmB.Solid=0
towarmB.Orientation=0.701781,0.711937,0.007967,0.024200
#






#AMULETOS ESCONDIDOS 

AMUFA=Bladex.CreateEntity("twAMUFA","Amuletofantasma",-4296.417247,-21033.730635,30934.514839,"Physic")
AMUFA.Scale=1.000000
AMUFA.Orientation=0.000000,0.999939,0.009413,0.005844
ItemTypes.ItemDefaultFuncs (AMUFA)



CORONA=Bladex.CreateEntity("twCORONA","Corona",-3232.380826,-39594.938692,16985.070480,"Physic")
CORONA.Scale=1.000000
CORONA.Orientation=0.759582,0.649147,-0.005891,0.040122
ItemTypes.ItemDefaultFuncs (CORONA)






## carcajs 
"""

carcaj2desert=Bladex.CreateEntity("Carcaj2desert","Carcaj",-9621.222037,-10722.359378,84742.497375,"Physic")
carcaj2desert.Scale=1.000000
carcaj2desert.Orientation=0.553761,0.826696,-0.084635,0.052530
ItemTypes.ItemDefaultFuncs (carcaj2desert)
carcaj2desert.Data.ArrowsLeft=10


carcaj3desert=Bladex.CreateEntity("Carcaj3desert","Carcaj",-49158.741758,-14045.017921,74325.583703,"Physic")
carcaj3desert.Scale=1.000000
carcaj3desert.Orientation=0.755753,0.652780,-0.040724,0.032515
ItemTypes.ItemDefaultFuncs (carcaj3desert)
carcaj3desert.Data.ArrowsLeft=10


"""