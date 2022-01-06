import Bladex
import DMusic
import Language
import AuxFuncs

AuxFuncs.SingleFrameFade()

language = Language.CheckFallback()

## ESCENAS

Bladex.AddMusicEventMP3("tablilla","../../Sounds/"+language+"/nubestablilla.mp3",    1.0, 1.0, 1.0, 500, 0, 0 )



### GOLPES DE EFECTO

Bladex.AddMusicEventWAV("inicio4","../../Sounds/INICIOCOMBATE4.wav",  0.1, 0.1, 1.0, 200, 0, 0 )


## COMBATE

#DMusic.AddCombatMusic("ChaosKnightBak",  "../../sounds/COMBATE3.wav",           400,1,1 ,0.1 ,4.0)


## ATMOSFERAS

Bladex.AddMusicEventWAV("Atmosfera4","../../Sounds/ATMOSFERA4.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera5","../../Sounds/ATMOSFERA5.mp3",   2.0, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera7","../../Sounds/ATMOSFERA7.mp3",   2.0, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera8","../../Sounds/ATMOSFERA8.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate3","../../Sounds/COMBATE3.wav",       0.1, 3.0, 1.0, 0.0, 1, -1 )


## VACIO


Bladex.AddMusicEventMP3("emptyloquesea", "", 2.0, 3.0, 1.0, 300, 0, 0)
