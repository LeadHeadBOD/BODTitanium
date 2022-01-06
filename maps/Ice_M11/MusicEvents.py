import Bladex
import DMusic
import Language

language = Language.CheckFallback()

## ESCENAS

Bladex.AddMusicEventMP3("inicio","../../Sounds/"+language+"/nubescargamusica.mp3",   0.1, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("tablilla","../../Sounds/"+language+"/nubestablilla.mp3",    0.1, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("demonio","../../Sounds/"+language+"/nubesbalance.mp3",      0.1, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("nubesllave","../../Sounds/"+language+"/nubesllave.mp3",     0.1, 1.0, 1.0, 500, 0, 0 )


## COMBATE

DMusic.AddCombatMusic("16kngt",  "../../sounds/ATMOSFERA6.mp3",          400,1,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("17kngt",  "../../sounds/ATMOSFERA6.mp3",          400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("Demonio de Ventana",  "../../sounds/COMBATE5.wav",400,0,1 ,1.0 ,3.0)


## GOLPES DE EFECTO

Bladex.AddMusicEventWAV("sorpresa-1","../../Sounds/SORPRESA1.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1a","../../Sounds/SORPRESA1a.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1b","../../Sounds/SORPRESA1b.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-3","../../Sounds/SORPRESA3.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro1","../../Sounds/CORO1.mp3",             0.5, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Atm9mp3","../../Sounds/ATMOSFERA9.mp3",      0.5, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio1","../../Sounds/INICIOCOMBATE1.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio2","../../Sounds/INICIOCOMBATE2.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio3","../../Sounds/INICIOCOMBATE3.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio4","../../Sounds/INICIOCOMBATE4.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio5","../../Sounds/INICIOCOMBATE5.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio6","../../Sounds/INICIOCOMBATE6.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio7","../../Sounds/INICIOCOMBATE7.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("atmosfera12","../../Sounds/ATMOSFERA12.mp3", 0.5, 1.0, 1.0, 201, 0, 0 )
Bladex.AddMusicEventMP3("demonice","../../Sounds/FINAL-DEMONICE.mp3", 0.5, 1.0, 1.0, 202, 0, 0 )

## ATMOSFERAS

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
Bladex.AddMusicEventWAV("Atmosfera8","../../Sounds/ATMOSFERA36.wav",  0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm8mp3","../../Sounds/ATMOSFERA8.mp3",      0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera10","../../Sounds/ATMOSFERA10.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera11","../../Sounds/ATMOSFERA11.mp3", 2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate2","../../Sounds/COMBATE2.wav",       0.1, 4.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate3","../../Sounds/COMBATE3.wav",       0.1, 3.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate4","../../Sounds/COMBATE4.wav",       1.0, 4.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate6","../../Sounds/COMBATE6.wav",       1.0, 6.0, 1.0, 0.0, 1, -1 )


## VACIO


Bladex.AddMusicEventMP3("emptyloquesea", "", 2.0, 3.0, 1.0, 300, 0, 0)
