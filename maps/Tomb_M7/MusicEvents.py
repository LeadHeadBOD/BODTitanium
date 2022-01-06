import Bladex
import DMusic
import string
import Language

language = Language.CheckFallback()

Bladex.AddMusicEventMP3("iniciotomb","../../Sounds/"+language+"/tumbacarga.mp3"     ,  0.1, 1.0, 1.0, 1000, 0, 0 )
Bladex.AddMusicEventMP3("tablillatomb","../../Sounds/"+language+"/tumba-escena3.mp3" , 0.1, 1.0, 1.0, 1000, 0, 0 )
#Bladex.AddMusicEventMP3("rey","../../Sounds/escena-rey.mp3" ,   				   0.1, 1.0, 1.0, 1000, 0, 0 )


if char.Kind[0] == "K":
	Bladex.AddMusicEventMP3("fetichetomb","../../Sounds/"+language+"/tumba-escena1K.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("kingtomb","../../Sounds/"+language+"/tumba-escena2K.mp3"   , 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("ttomb","../../Sounds/"+language+"/tumba-escena4K.mp3"      , 0.1, 1.0, 1.0, 10000.0, 0, 0 )
elif char.Kind[0] == "A":
	Bladex.AddMusicEventMP3("fetichetomb","../../Sounds/"+language+"/tumba-escena1A.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("kingtomb","../../Sounds/"+language+"/tumba-escena2A.mp3"   , 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("ttomb","../../Sounds/"+language+"/tumba-escena4A.mp3"      , 0.1, 1.0, 1.0, 10000.0, 0, 0 )
elif char.Kind[0] == "B":
	Bladex.AddMusicEventMP3("fetichetomb","../../Sounds/"+language+"/tumba-escena1B.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("kingtomb","../../Sounds/"+language+"/tumba-escena2B.mp3"   , 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("ttomb","../../Sounds/"+language+"/tumba-escena4B.mp3"      , 0.1, 1.0, 1.0, 10000.0, 0, 0 )
else:
	Bladex.AddMusicEventMP3("fetichetomb","../../Sounds/"+language+"/tumba-escena1D.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("kingtomb","../../Sounds/"+language+"/tumba-escena2D.mp3"   , 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("ttomb","../../Sounds/"+language+"/tumba-escena4D.mp3"      , 0.1, 1.0, 1.0, 10000.0, 0, 0 )



###SORPRESAS
Bladex.AddMusicEventWAV("TumboRey","../../Sounds/ATMOSFERA27.wav",       1.0, 1.0, 0.9, 500, 0, 0 )
Bladex.AddMusicEventWAV("templolindo","../../Sounds/ATMOSFERA28.wav",    1.0, 1.0, 0.9, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro5","../../Sounds/CORO5.mp3",        	    1.0, 3.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro2.2","../../Sounds/CORO2.2.mp3",            1.0, 3.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro6","../../Sounds/CORO6.mp3",        	    1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1","../../Sounds/SORPRESA1.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa4","../../Sounds/SORPRESA4.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa7","../../Sounds/SORPRESA7.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1a","../../Sounds/SORPRESA1a.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1b","../../Sounds/SORPRESA1b.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb33","../../Sounds/INICIOCOMBATE3.wav",    0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb3","../../Sounds/INICIOCOMBATE33.wav",    0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("inicio23","../../Sounds/INICIO23.wav",   	    0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb6","../../Sounds/INICIOCOMBATE6.wav",    0.1, 0.1, 1.0, 500, 0, 0 )


#Bladex.AddMusicEventWAV("cementerio","../../Sounds/COMBATE4.wav",        1.0, 1.0, 1.0, 500, 0, -1 )
Bladex.AddMusicEventWAV("templo","../../Sounds/COMBATE2.wav",        1.0, 1.0, 1.0, 500, 0, -1 )


###VACIO
Bladex.AddMusicEventMP3( "empty",  "", 2.0, 3.0, 1.0, 600, 1, 1 )
Bladex.AddMusicEventMP3( "empty2",  "", 2.0, 3.0, 1.0, 300, 1, 1 )

###COMBATE
#DMusic.AddCombatMusic("Great_Ork",  "../../sounds/COMBATE2.wav", prioridad,pre-abierto 0 , vol , f in , f out)

DMusic.AddCombatMusic("TheKing",  "../../sounds/COMBATE5.wav",  		300 , 0 , 1 , 1.0 , 4.0)
DMusic.AddCombatMusic("Golem_stone",  "../../sounds/ATMOSFERA20A.mp3",	600 , 0 , 1 , 1.0 , 4.0)

DMusic.AddCombatMusic("combate3",  "../../sounds/COMBATE3.wav",  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("combate4",  "../../sounds/COMBATE4.wav",  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("combate5",  "../../sounds/COMBATE5.wav",  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("combate6",  "../../sounds/COMBATE6.wav",  300 , 0 , 1 , 1.0 , 2.0)

###MUSICAS


Bladex.AddMusicEventWAV("cementerio","../../Sounds/ATMOSFERA31.wav",   1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm1","../../Sounds/ATMOSFERA1.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm29","../../Sounds/ATMOSFERA29.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm5","../../Sounds/ATMOSFERA5.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm2","../../Sounds/ATMOSFERA2.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm3","../../Sounds/ATMOSFERA3.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm4","../../Sounds/ATMOSFERA4.wav"   , 3.0, 3.0, 0.6, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm6","../../Sounds/ATMOSFERA6.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm7","../../Sounds/ATMOSFERA7.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm8","../../Sounds/ATMOSFERA8.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm9","../../Sounds/ATMOSFERA9.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm10","../../Sounds/ATMOSFERA10.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm11","../../Sounds/ATMOSFERA11.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm12","../../Sounds/ATMOSFERA12.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm16","../../Sounds/ATMOSFERA16.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm17","../../Sounds/ATMOSFERA17.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm22","../../Sounds/ATMOSFERA22.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm18","../../Sounds/ATMOSFERA18.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm19","../../Sounds/ATMOSFERA19.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm20","../../Sounds/ATMOSFERA20.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )

#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("grutas") )
