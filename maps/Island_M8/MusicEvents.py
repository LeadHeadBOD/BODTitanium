##///
##||| ISLAND_M8/MusicEvents.PY TITANIUM
##||| Change list:
##||| * Replaced low quality .wavs with .mp3/.ogg where applicable
##\\\ 

import Bladex
import DMusic
import string
import Language

language = Language.CheckFallback()

Bladex.AddMusicEventMP3("isla-vampiroc","../../Sounds/"+language+"/isla-vampiroc.mp3"		, 0.1, 1.0, 1.0, 1300, 0, 0 )
Bladex.AddMusicEventMP3("isla-carga","../../Sounds/"+language+"/isla-carga.mp3"			, 0.1, 1.0, 1.0, 1000, 0, 0 )
Bladex.AddMusicEventMP3("playerVampireCobarde","../../Sounds/"+language+"/isla-vamp-wyverna1.mp3" , 0.1, 1.0, 1.0, 1000, 0, 0 )
Bladex.AddMusicEventMP3("isla-tablilla","../../Sounds/"+language+"/isla-tablilla.mp3"		, 0.1, 1.0, 1.0, 1000, 0, 0 )

char=Bladex.GetEntity("Player1")

if char.Kind[0] == "K":
	Bladex.AddMusicEventMP3("isla-mural","../../Sounds/"+language+"/isla-muralK.mp3", 0.1, 1.0, 1.0, 1000, 0, 0 )
elif char.Kind[0] == "A":
	Bladex.AddMusicEventMP3("isla-mural","../../Sounds/"+language+"/isla-muralA.mp3", 0.1, 1.0, 1.0, 1000, 0, 0 )
elif char.Kind[0] == "B":
	Bladex.AddMusicEventMP3("isla-mural","../../Sounds/"+language+"/isla-muralB.mp3", 0.1, 1.0, 1.0, 1000, 0, 0 )
else:
	Bladex.AddMusicEventMP3("isla-mural","../../Sounds/"+language+"/isla-muralD.mp3", 0.1, 1.0, 1.0, 1000, 0, 0 )



###SORPRESAS
Bladex.AddMusicEventMP3("coro4","../../Sounds/CORO4.mp3",        	    1.0, 1.0, 0.2, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro5","../../Sounds/CORO5.mp3",        	    1.0, 3.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro6","../../Sounds/CORO6.mp3",        	    1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1","../../Sounds/SORPRESA1.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa3","../../Sounds/SORPRESA3.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa4","../../Sounds/SORPRESA4.wav",        0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa5","../../Sounds/SORPRESA5.wav",        0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("sorpresarmadura","../../Sounds/CORO4.mp3",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa8","../../Sounds/SORPRESA8.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa10","../../Sounds/SORPRESA10.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1a","../../Sounds/SORPRESA1a.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1b","../../Sounds/SORPRESA1b.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb33","../../Sounds/INICIOCOMBATE3.wav",    0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb4","../../Sounds/INICIOCOMBATE4.wav",     0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb6","../../Sounds/INICIOCOMBATE6.wav",     0.1, 0.1, 1.0, 500, 0, 0 )     # PLAGUE: the other troublemaker

Bladex.AddMusicEventWAV("inicc","../../Sounds/ATMOSFERA32.wav",     0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("comb2","../../Sounds/COMBATE2.wav",        1.0, 1.0, 1.0, 500, 0, -1 )


###VACIO
Bladex.AddMusicEventMP3( "empty",  "", 2.0, 3.0, 1.0, 600, 1, 1 )
Bladex.AddMusicEventMP3( "empty2",  "", 2.0, 3.0, 1.0, 300, 1, 1 )

###COMBATE
#DMusic.AddCombatMusic("Great_Ork",  "../../sounds/COMBATE2.wav", prioridad,pre-abierto 0 , vol , f in , f out)

DMusic.AddCombatMusic("1kd",  "../../sounds/combate-ligth.wav",     		300 , 0 , 1 , 1.0 , 4.0)
DMusic.AddCombatMusic("Minotaur",  "../../sounds/COMBATE3.wav",  		300 , 0 , 1 , 1.0 , 4.0)
#DMusic.AddCombatMusic("Little_Demon",  "../../sounds/combate-ligth.wav",  	300 , 0 , 1 , 1.0 , 4.0)


DMusic.AddCombatMusic("combate3",  "../../sounds/COMBATE3.wav",  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("combate4",  "../../sounds/COMBATE4.wav",  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("combate5",  "../../sounds/COMBATE5.wav",  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("combate6",  "../../sounds/COMBATE6.wav",  300 , 0 , 1 , 1.0 , 2.0)

###MUSICAS
#Bladex.AddMusicEventADPCM( "atm5","../../Sounds/ATMOSFERA5.wav",  f in , f out, vol, prioridad , 1, loop )

Bladex.AddMusicEventWAV  ("deposito","../../Sounds/COMBATE4.wav"  , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm5","../../Sounds/ATMOSFERA5.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm2","../../Sounds/ATMOSFERA2.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm3","../../Sounds/ATMOSFERA3.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm4","../../Sounds/ATMOSFERA1.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm6","../../Sounds/ATMOSFERA6.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm7","../../Sounds/ATMOSFERA7.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm8","../../Sounds/ATMOSFERA8.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm9","../../Sounds/ATMOSFERA9.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm10","../../Sounds/ATMOSFERA10.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm11","../../Sounds/ATMOSFERA11.mp3"   , 1.0, 3.0, 1.0, 100  , 1,  0 ) # PLAGUE: Stupid troublesome ear-rape
Bladex.AddMusicEventADPCM( "incomb1","../../Sounds/INICIOCOMBATE1.wav"   , 1.0, 3.0, 1.0, 100  , 1,  0 )
Bladex.AddMusicEventMP3  ( "atm12","../../Sounds/ATMOSFERA12.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm16","../../Sounds/ATMOSFERA31.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm17","../../Sounds/ATMOSFERA17.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm18","../../Sounds/ATMOSFERA8.mp3"   , 1.0, 1.0, 0.7, 1  , 1, -1 )   # PLAGUE: Double check if dev didn't actually mean Atmosfera18 as internal name suggests
Bladex.AddMusicEventMP3  ( "atm19","../../Sounds/ATMOSFERA19.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm20","../../Sounds/ATMOSFERA20.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm21","../../Sounds/ATMOSFERA21.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm22","../../Sounds/ATMOSFERA22.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm29","../../Sounds/ATMOSFERA29.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )

Bladex.AddMusicEventADPCM( "atm32","../../Sounds/ATMOSFERA32.wav"   , 1.0, 3.0, 1.0, 100  , 1,  0 )
Bladex.AddMusicEventADPCM( "combate6skl","../../Sounds/COMBATE6.wav", 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "1kd",  "../../sounds/combate-ligth.wav",  1.0, 1.0, 1.0, 1  , 1, -1 )

#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("grutas") )