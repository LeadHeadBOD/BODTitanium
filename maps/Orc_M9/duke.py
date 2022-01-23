import Reference
import darfuncs
import DefFuncs
global pris


### Duke, you're a goddamn mess... We've been trying to rescue you for 3 whole levels
### The game tries to tell me you're a traitor
### You don't bleed
### You don't cast shadows after dying
### And you get decapitated literally 6 seconds after finally seeing you
### We can  even shoot you with an arrow to kill you and save orcs the trouble
###
###
### You are so useless that not even our hero can be bothered to try and save you,
### Even our shrieking attempts to warn you come with great reluctance,
### All this in spite of the obvious inevitable fate...
###        
###     -LeadHead
###

Bladex.ReadBitMap("../../Data/Icons/Duke.bmp","DukeIcon")               ### Load duke icon into memory
Reference.EnemiesScorerData['PPris']=("DukeIcon","Duki")                ### Assign duke icon to Prisoner               

def CortaCabezaPrisionero(x,y):         ### If Tomash is to be believed, this should overwrite the old def as we are loading this one last
	pris.Life = 0
	pris.SeverLimb(1)
	pris.CastShadows = 1                ### enable duke shadows
	ScriptSkip.SkipScriptEnd()    