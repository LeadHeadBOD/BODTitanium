import Bladex
import DMusic
import Language

#### ESCENAS

language = Language.CheckFallback()

Bladex.AddMusicEventMP3("inicioorc","../../Sounds/"+language+"/orcocargamusica.mp3",      0.1, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("elevadororc","../../Sounds/"+language+"/orcobalance.mp3",        0.1, 1.0, 1.0, 500, 0, 0 )

if char.Kind[0] == "K":
	Bladex.AddMusicEventMP3("finalorc","../../Sounds/"+language+"/orcomuralK.mp3",     0.1, 1.0, 1.0, 500, 0, 0 )
	Bladex.AddMusicEventMP3("prisorc","../../Sounds/"+language+"/orcoprisioneroK.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )
elif char.Kind[0] == "A":
	Bladex.AddMusicEventMP3("finalorc","../../Sounds/"+language+"/orcomuralA.mp3",     0.1, 1.0, 1.0, 500, 0, 0 )
	Bladex.AddMusicEventMP3("prisorc","../../Sounds/"+language+"/orcoprisioneroA.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )
elif char.Kind[0] == "B":
	Bladex.AddMusicEventMP3("finalorc","../../Sounds/"+language+"/orcomuralB.mp3",     0.1, 1.0, 1.0, 500, 0, 0 )
	Bladex.AddMusicEventMP3("prisorc","../../Sounds/"+language+"/orcoprisioneroB.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )
else:
	Bladex.AddMusicEventMP3("finalorc","../../Sounds/"+language+"/orcomuralD.mp3",     0.1, 1.0, 1.0, 500, 0, 0 )
	Bladex.AddMusicEventMP3("prisorc","../../Sounds/"+language+"/orcoprisioneroD.mp3", 0.1, 1.0, 1.0, 500, 0, 0 )




## COMBATE

DMusic.AddCombatMusic("OEorc1",  "../../sounds/Atmosfera6.mp3",400,0,1 ,1.0 ,3.0)
DMusic.AddCombatMusic("OEorc2",  "../../sounds/Atmosfera6.mp3",400,0,1 ,1.0 ,3.0)


## GOLPES DE EFECTO

Bladex.AddMusicEventWAV("sorpresa-1","../../Sounds/SORPRESA1.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1a","../../Sounds/SORPRESA1a.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-1b","../../Sounds/SORPRESA1b.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa-3","../../Sounds/SORPRESA3.wav",    0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("Coro1","../../Sounds/CORO1.mp3",             0.5, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio1","../../Sounds/INICIOCOMBATE1.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio2","../../Sounds/INICIOCOMBATE2.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio3","../../Sounds/INICIOCOMBATE3.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio4","../../Sounds/INICIOCOMBATE4.wav",  0.1, 0.1, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio5","../../Sounds/INICIOCOMBATE5.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio6","../../Sounds/INICIOCOMBATE6.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventWAV("inicio7","../../Sounds/INICIOCOMBATE7.wav",  0.1, 1.0, 1.0, 200, 0, 0 )
Bladex.AddMusicEventMP3("inicioatm20","../../Sounds/INICIO-ATMOSFERA20.mp3",  0.1, 1.0, 1.0, 200, 0, 0 )


## ATMOSFERAS

Bladex.AddMusicEventMP3("Atmosfera1","../../Sounds/ATMOSFERA1.mp3",   0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm1MP3","../../Sounds/ATMOSFERA1.mp3",      2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm2MP3","../../Sounds/ATMOSFERA2.mp3",      2.0, 3.0, 1.0, 0.0, 1, -1 )
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
Bladex.AddMusicEventMP3("Atmosfera10","../../Sounds/ATMOSFERA10.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera11","../../Sounds/ATMOSFERA11.mp3", 2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera18","../../Sounds/ATMOSFERA18.mp3", 0.1, 0.5, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm18MP3","../../Sounds/ATMOSFERA18.mp3",    2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera19","../../Sounds/ATMOSFERA19.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm19MP3","../../Sounds/ATMOSFERA19.mp3",    2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera20","../../Sounds/ATMOSFERA20.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera21","../../Sounds/ATMOSFERA21.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atmosfera22","../../Sounds/ATMOSFERA22.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("Atm20MP3","../../Sounds/ATMOSFERA20.mp3",    2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("inicio2atm20","../../Sounds/INICIO-ATMOSFERA20.mp3",2.0, 1.0, 0.5, 0.0, 1, -1 )
Bladex.AddMusicEventMP3("inicio2atm20b","../../Sounds/INICIO-ATMOSFERA20.mp3",2.0, 1.0, 0.5, 0.0, 1, 0 )
Bladex.AddMusicEventMP3("Atmosfera20a","../../Sounds/ATMOSFERA20A.mp3", 0.1, 1.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate1","../../Sounds/COMBATE1.wav",       0.1, 4.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate2","../../Sounds/COMBATE2.wav",       0.1, 4.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate3","../../Sounds/COMBATE3.wav",       0.1, 3.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate4","../../Sounds/COMBATE4.wav",       1.0, 4.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combate6","../../Sounds/COMBATE6.wav",       0.1, 6.0, 1.0, 0.0, 1, -1 )
Bladex.AddMusicEventWAV("Combatelight","../../Sounds/combate-ligth.wav",  1.0, 6.0, 1.0, 0.0, 1, -1 )

Bladex.AddMusicEventMP3("atmemptyloquesea", "",                          1.0, 1.0, 1.0, 0.0, 1, -1 )



## VACIO

Bladex.AddMusicEventMP3("emptyloquesea", "", 2.0, 3.0, 1.0, 300, 0, 0)
