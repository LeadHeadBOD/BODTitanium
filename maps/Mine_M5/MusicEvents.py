import Bladex
import DMusic
import Language

### PARRAFADAS

language = Language.CheckFallback()

if char.Kind[0] == "K":
	Bladex.AddMusicEventMP3("finalmina","../../Sounds/"+language+"/minamuralK.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )
elif char.Kind[0] == "A":
	Bladex.AddMusicEventMP3("finalmina","../../Sounds/"+language+"/minamuralA.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )
elif char.Kind[0] == "B":
	Bladex.AddMusicEventMP3("finalmina","../../Sounds/"+language+"/minamuralB.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )
else:
	Bladex.AddMusicEventMP3("finalmina","../../Sounds/"+language+"/minamuralD.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )


#### ESCENAS

Bladex.AddMusicEventMP3("iniciomina","../../Sounds/"+language+"/minacarga.mp3"     , 0.1, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("tablillamina","../../Sounds/"+language+"/minatablilla.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )


###COMBATE

DMusic.AddCombatMusic("18orc",  "../../sounds/COMBATE2.wav",          400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("18borc",  "../../sounds/COMBATE2.wav",         400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("18corc",  "../../sounds/COMBATE2.wav",         400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("g1ork1",  "../../sounds/COMBATE2.wav",         400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("g1ork2",  "../../sounds/COMBATE2.wav",         400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("g2ork3",  "../../sounds/COMBATE2.wav",         400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("g2ork1",  "../../sounds/COMBATE2.wav",         400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("g2ork2",  "../../sounds/COMBATE2.wav",         400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("6orc6",  "../../sounds/COMBATE2.wav",          400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("MineAmbushOrk1",  "../../sounds/ATMOSFERA30.wav", 400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("MineAmbushOrk2",  "../../sounds/ATMOSFERA30.wav", 400,1,1,1.0 ,3.0)
DMusic.AddCombatMusic("MineAmbushOrk3",  "../../sounds/ATMOSFERA30.wav", 400,1,1,1.0 ,3.0)

### GOLPES DE EFECTO

Bladex.AddMusicEventWAV("sorpresa-1","../../Sounds/SORPRESA1.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1a","../../Sounds/SORPRESA1a.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1b","../../Sounds/SORPRESA1b.wav",  0.1, 1.0, 1.0, 212, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-2b","../../Sounds/INICIO23.wav",  0.1, 1.0, 1.0, 212, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-3","../../Sounds/SORPRESA3.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-aranas","../../Sounds/SORPRESA9.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-zampon","../../Sounds/INICIOCOMBATE6.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-orkos","../../Sounds/INICIOCOMBATE6.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro1","../../Sounds/CORO1.mp3",             0.5, 1.0, 1.0, 210, 0, 0 )

### ATMOSFERAS

Bladex.AddMusicEventMP3("Atmosfera1","../../Sounds/ATMOSFERA1.mp3",   2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera2","../../Sounds/ATMOSFERA2.mp3",   0.1, 1.0, 1.0, 211, 1, -1 )
Bladex.AddMusicEventMP3("Atm2MP3","../../Sounds/ATMOSFERA2.mp3",   0.1, 1.0, 1.0, 211, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera3","../../Sounds/ATMOSFERA3.mp3",   0.1, 1.0, 1.0, 211, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera4","../../Sounds/ATMOSFERA4.wav",   0.1, 1.0, 1.0, 211, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera18","../../Sounds/Atmosfera18.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm5mp3","../../Sounds/Atmosfera18.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera6","../../Sounds/ATMOSFERA6.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera17","../../Sounds/ATMOSFERA17.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm6mp3","../../Sounds/ATMOSFERA6.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera7","../../Sounds/ATMOSFERA7.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm7mp3","../../Sounds/ATMOSFERA7.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera8","../../Sounds/ATMOSFERA8.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm8mp3","../../Sounds/ATMOSFERA8.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm9mp3","../../Sounds/ATMOSFERA9.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera10","../../Sounds/ATMOSFERA10.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera27","../../Sounds/ATMOSFERA27.wav", 2.0, 1.0, 0.5, 213, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera12","../../Sounds/ATMOSFERA12.mp3", 2.0, 1.0, 0.5, 213, 1, -1 )

### VACIO

Bladex.AddMusicEventMP3("emptyloquesea", "", 2.0, 3.0, 1.0, 300, 0, 0)
