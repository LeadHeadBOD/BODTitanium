import Bladex
import DMusic
import Language
import AuxFuncs

AuxFuncs.SingleFrameFade()

language = Language.CheckFallback()
#### ESCENAS

Bladex.AddMusicEventMP3("btomb-tablilla","../../Sounds/"+language+"/btomb-tablilla.mp3"    , 0.1, 1.0, 1.0, 500, 0, 0 )

### GOLPES DE EFECTO

Bladex.AddMusicEventWAV("inicio4","../../Sounds/INICIOCOMBATE4.wav",  0.1, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro5","../../Sounds/CORO5.mp3",             0.5, 1.0, 1.0, 210, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-3","../../Sounds/SORPRESA3.wav",    0.1, 1.0, 1.0, 200, 0, 0 )


### COMBATE

DMusic.AddCombatMusic("ChaosKnightBak",  "../../sounds/COMBATE3.wav",           400,1,1 ,0.1 ,4.0)



### ATMOSFERAS

Bladex.AddMusicEventMP3("Atmosfera24","../../Sounds/ATMOSFERA24.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera21","../../Sounds/ATMOSFERA21.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera4","../../Sounds/ATMOSFERA4.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera5","../../Sounds/ATMOSFERA5.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera18","../../Sounds/ATMOSFERA18.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera3","../../Sounds/ATMOSFERA3.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("atmemptyloquesea", "",                          2.0, 0.5, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate3","../../Sounds/COMBATE3.wav",       0.1, 4.0, 1.0, 0.0, 1, -1 )

### VACIO

Bladex.AddMusicEventMP3("emptyloquesea", "", 2.0, 3.0, 1.0, 300, 0, 0)
