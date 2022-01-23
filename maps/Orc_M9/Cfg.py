import Bladex
import LoadBar
LoadBar.ECTSProgressBar(366,"Blade_progress.jpg")


execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("orcst.lvl")

execfile("../../Scripts/BladeInit.py")

execfile("ActorsInit.py")

execfile("DefFuncs.py")

execfile("MusicEvents.py")

if Reference.PYTHON_DEBUG >= 1:
	execfile("Positions.py")

execfile ("TextureMaterials.py")

execfile ("objs.py")

execfile ("barriles.py")

execfile ("bgates.py")

execfile("puertorc.py")

execfile ("sol.py")

execfile ("sonidos.py")

execfile ("sonidospuntuales.py")

execfile ("luces.py")

execfile("propiedades.py")

execfile("elevador.py")

execfile("orchuye.py")

execfile("Enemigos.py")

execfile ("bolas.py")	## siempre tras enemigos.py

execfile("eScene.py")

execfile("armas.py")

execfile("obScene.py")	# escena del jefe orco dando ordenes para que salga a luchar los orcos

execfile("Pris.py")	# escena del prisionero, cargar tras enemigos.py

execfile("iScene.py")

execfile("musica.py")

execfile("duke.py") # Load Duke fixes


char.Position=-18514, 48390, 7584
char.Angle=6.28318291809

## orco ordenando char.Position=-5757,17107,60075