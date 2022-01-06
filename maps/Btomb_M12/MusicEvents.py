import Bladex
import DMusic
import Language

language = Language.CheckFallback()

if char.Kind[0] == "K":
	Bladex.AddMusicEventMP3("btomb-mural","../../Sounds/"+language+"/btomb-muralk.mp3"          , 0.1, 1.0, 1.0, 500, 0, 0 )
elif char.Kind[0] == "A":
	Bladex.AddMusicEventMP3("btomb-mural","../../Sounds/"+language+"/btomb-murala.mp3"          , 0.1, 1.0, 1.0, 500, 0, 0 )
elif char.Kind[0] == "B":
	Bladex.AddMusicEventMP3("btomb-mural","../../Sounds/"+language+"/btomb-muralb.mp3"          , 0.1, 1.0, 1.0, 500, 0, 0 )
else:
	Bladex.AddMusicEventMP3("btomb-mural","../../Sounds/"+language+"/btomb-murald.mp3"          , 0.1, 1.0, 1.0, 500, 0, 0 )


## ESCENAS

Bladex.AddMusicEventMP3("btomb-carga","../../Sounds/"+language+"/btomb-carga.mp3"          , 0.1, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("btomb-tablilla","../../Sounds/"+language+"/btomb-tablilla.mp3"    , 0.1, 1.0, 1.0, 500, 0, 0 )


###COMBATE

DMusic.AddCombatMusic("3ORC",  "../../sounds/COMBATE2.wav",           400,1,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("13ORC",  "../../sounds/ATMOSFERA6.mp3",        400,1,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("14ORC",  "../../sounds/ATMOSFERA6.mp3",        400,1,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("15ORC",  "../../sounds/ATMOSFERA6.mp3",        400,1,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("17ORC",  "../../sounds/ATMOSFERA6.mp3",        400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("18ORC",  "../../sounds/ATMOSFERA6.mp3",        400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("20ORC",  "../../sounds/ATMOSFERA6.mp3",        400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("21ORC",  "../../sounds/ATMOSFERA6.mp3",        400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("21ORCb",  "../../sounds/ATMOSFERA6.mp3",       400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("21ORCc",  "../../sounds/ATMOSFERA6.mp3",       400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("27cEsq",  "../../sounds/COMBATE4.wav",         400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("Golem1",  "../../sounds/COMBATE3.wav",         400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("TRL2",  "../../sounds/COMBATE4.wav",           400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("Golem2",  "../../sounds/COMBATE3.wav",         400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("TRL3",  "../../sounds/COMBATE4.wav",           400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("40Esq",  "../../sounds/COMBATE2.wav",          400,0,1 ,2.0 ,3.0)
DMusic.AddCombatMusic("41Esq",  "../../sounds/COMBATE2.wav",          400,0,1 ,2.0 ,3.0)
DMusic.AddCombatMusic("42Esq",  "../../sounds/COMBATE2.wav",          400,0,1 ,2.0 ,3.0)
DMusic.AddCombatMusic("43Esq",  "../../sounds/COMBATE2.wav",          400,0,1 ,2.0 ,3.0)
DMusic.AddCombatMusic("Drakula",  "../../sounds/COMBATE4.wav",        400,0,1 ,1.0 ,3.0)


### GOLPES DE EFECTO

Bladex.AddMusicEventWAV("sorpresa-1","../../Sounds/SORPRESA1.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1a","../../Sounds/SORPRESA1a.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1b","../../Sounds/SORPRESA1b.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-3","../../Sounds/SORPRESA3.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro1","../../Sounds/CORO1.mp3",             0.5, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Atm12mp3","../../Sounds/ATMOSFERA12.mp3",    0.0, 0.5, 1.0, 199, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-13","../../Sounds/SOPRESA13.wav",   0.1, 1.0, 1.0, 401, 0, 0 )

### ATMOSFERAS

Bladex.AddMusicEventMP3("Atmosfera1","../../Sounds/ATMOSFERA1.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm1MP3","../../Sounds/ATMOSFERA1.mp3",      2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera2","../../Sounds/ATMOSFERA2.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm2MP3","../../Sounds/ATMOSFERA2.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera3","../../Sounds/ATMOSFERA3.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera4","../../Sounds/ATMOSFERA4.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera5","../../Sounds/ATMOSFERA5.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm5mp3","../../Sounds/ATMOSFERA5.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera6","../../Sounds/ATMOSFERA6.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm6mp3","../../Sounds/ATMOSFERA6.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera7","../../Sounds/ATMOSFERA7.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm7mp3","../../Sounds/ATMOSFERA7.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera8","../../Sounds/ATMOSFERA8.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm8mp3","../../Sounds/ATMOSFERA8.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm9mp3","../../Sounds/ATMOSFERA9.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera10","../../Sounds/ATMOSFERA10.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera11","../../Sounds/ATMOSFERA11.mp3", 2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate2","../../Sounds/COMBATE2.wav",       2.0, 4.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate4","../../Sounds/COMBATE4.wav",       2.0, 4.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate3","../../Sounds/COMBATE3.wav",       2.0, 4.0, 1.0, 0.0, 1, -1 )

### VACIO

Bladex.AddMusicEventMP3("emptyloquesea", "", 2.0, 3.0, 1.0, 300, 0, 0)
