import Bladex
import DMusic
import Language
import AuxFuncs

language = Language.CheckFallback()

AuxFuncs.SingleFrameFade()

#### ESCENAS

Bladex.AddMusicEventMP3("tablillamina","../../Sounds/"+language+"/minatablilla.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )

### GOLPES DE EFECTO

Bladex.AddMusicEventWAV("inicio4","../../Sounds/INICIOCOMBATE4.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro1","../../Sounds/CORO1.mp3",             0.5, 1.0, 1.0, 210, 0, 0 )


### ATMOSFERAS

Bladex.AddMusicEventMP3("Atmosfera24","../../Sounds/ATMOSFERA24.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Atmosfera4","../../Sounds/ATMOSFERA4.wav",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera18","../../Sounds/ATMOSFERA18.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("atmemptyloquesea", "",                          2.0, 0.5, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate6","../../Sounds/COMBATE6.wav",       0.1, 0.1, 1.0, 0.0, 1, 0 )
Bladex.AddMusicEventMP3("atmemptyloquesea", "",                          2.0, 0.5, 1.0, 0.0, 1, -1 )

### VACIO

Bladex.AddMusicEventMP3("emptyloquesea", "", 2.0, 3.0, 1.0, 300, 0, 0)
