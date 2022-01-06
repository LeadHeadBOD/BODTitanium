import Bladex
import DMusic
import string
import Language

language = Language.CheckFallback()

Bladex.AddMusicEventMP3("iniciotower","../../Sounds/"+language+"/fortaleza-carga.mp3", 		0.1, 0.1, 1.0, 1000, 0, 0 )
Bladex.AddMusicEventMP3("fortaleza-meskal","../../Sounds/"+language+"/fortaleza-meskal.mp3", 	0.1, 0.1, 1.0, 1000, 0, 0 )
Bladex.AddMusicEventMP3("FinalBueno","../../Sounds/"+language+"/fortaleza-tablilla.mp3", 		0.1, 0.1, 1.0, 1000, 0, 0 )
Bladex.AddMusicEventMP3("FinalMalo", "../../Sounds/"+language+"/fortaleza-sintablilla.mp3",	0.1, 0.1, 1.0, 1000, 0, 0 )
Bladex.AddMusicEventMP3("fortaleza-desafio","../../Sounds/"+language+"/fortaleza-desafio.mp3", 	0.1, 0.1, 1.0, 1000, 0, 0 )




###SORPRESAS
Bladex.AddMusicEventMP3("coro1","../../Sounds/CORO1.mp3",        	    1.0, 1.0, 1.0, 1  , 0, 0 )
Bladex.AddMusicEventMP3("coro4","../../Sounds/CORO4.mp3",        	    1.0, 1.0, 0.2, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro5","../../Sounds/CORO5.mp3",        	    1.0, 3.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro6","../../Sounds/CORO6.mp3",        	    0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1","../../Sounds/SORPRESA1.wav",        0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa3","../../Sounds/SORPRESA3.wav",        0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa4","../../Sounds/SORPRESA4.wav",        0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa8","../../Sounds/SORPRESA8.wav",        0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1a","../../Sounds/SORPRESA1a.wav",      0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1b","../../Sounds/SORPRESA1b.wav",      0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb1","../../Sounds/INICIOCOMBATE1.wav",     0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb3","../../Sounds/INICIOCOMBATE3.wav",     0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb4","../../Sounds/INICIOCOMBATE4.wav",     0.1, 0.1, 1.0, 700, 0, 0 )
Bladex.AddMusicEventWAV("incomb6","../../Sounds/INICIOCOMBATE6.wav",     0.1, 0.1, 1.0, 500, 0, 0 )
#Bladex.AddMusicEventWAV("atm11","../../Sounds/ATMOSFERA11.wav",         0.1, 0.1, 1.0, 500, 0, 0 )      #This was originally targeted to .wav.wav file. 
Bladex.AddMusicEventWAV("inatm2","../../Sounds/INICIO-ATMOSFERA2.wav",        0.1, 0.1, 1.0, 500, 0, 0 ) #Must find out if atm11 is referenced anywhere else.


Bladex.AddMusicEventWAV("comb2","../../Sounds/COMBATE2.wav",        1.0, 1.0, 1.0, 500, 0, -1 )

Bladex.AddMusicEventWAV("combo1","../../Sounds/combate1.wav",        1.0, 1.0, 1.0, 500, 1, -1 )
#Bladex.AddMusicEventWAV("combo1","../../Sounds/combate1.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )

###VACIO
Bladex.AddMusicEventMP3( "empty",  "", 2.0, 3.0, 1.0, 600, 1, 1 )
Bladex.AddMusicEventMP3( "empty2",  "", 2.0, 3.0, 1.0, 900, 1, 1 )

###COMBATE
#DMusic.AddCombatMusic("Ork",  "../../sounds/COMBATE2.wav", prioridad,pre-abierto 0 , vol , f in , f out)

DMusic.AddCombatMusic("GenDalGurak3",  "../../sounds/combatedalgurak.mp3",  	900 , 0 , 1 , 1.0 , 1.0)
#DMusic.AddCombatMusic("43MINOT",  "../../sounds/combate-hard.wav",  	600 , 0 , 1 , 1.0 , 1.0)


#DMusic.AddCombatMusic("combate3",  "../../sounds/COMBATE3.wav",  300 , 0 , 1 , 1.0 , 2.0)
#DMusic.AddCombatMusic("combate4",  "../../sounds/COMBATE4.wav",  300 , 0 , 1 , 1.0 , 2.0)
#DMusic.AddCombatMusic("combate5",  "../../sounds/COMBATE5.wav",  300 , 0 , 1 , 1.0 , 2.0)
#DMusic.AddCombatMusic("combate6",  "../../sounds/COMBATE6.wav",  300 , 0 , 1 , 1.0 , 2.0)

###MUSICAS
#Bladex.AddMusicEventADPCM( "atm5","../../Sounds/ATMOSFERA5.wav",  f in , f out, vol, prioridad , 1, loop )

Bladex.AddMusicEventWAV("Acombhard","../../Sounds/combate-hard.wav",     0.1, 0.1, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventWAV("acomblh","../../Sounds/combate-ligth.wav",     0.1, 0.1, 1.0, 1  , 1, -1 )

Bladex.AddMusicEventWAV("dalcombate","../../Sounds/COMBATE1.wav",     0.1, 0.1, 1.0, 10  , 1, -1 )
Bladex.AddMusicEventWAV("dalcombskel","../../Sounds/COMBATE2.wav",    0.1, 0.1, 1.0, 9   , 1, -1 )

Bladex.AddMusicEventWAV("Acombate2","../../Sounds/COMBATE2.wav",     0.1, 0.1, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventWAV("Acombate6","../../Sounds/COMBATE6.wav",     0.1, 0.1, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventWAV("Acombate5","../../Sounds/COMBATE5.wav",     0.1, 0.1, 1.0, 1  , 1, -1 )
#Bladex.AddMusicEventWAV("Acombate4","../../Sounds/COMBATE4.wav",     1.0, 1.0, 1.0, 1  , 1, -1 )


Bladex.AddMusicEventMP3  ( "combatedalgurak","../../Sounds/combatedalgurak.mp3"   , 1.0, 1.0, 1.0, 900  , 1, -1 )

Bladex.AddMusicEventMP3  ( "atm1","../../Sounds/ATMOSFERA1.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm5","../../Sounds/ATMOSFERA5.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm2","../../Sounds/ATMOSFERA2.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm3","../../Sounds/ATMOSFERA3.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm4","../../Sounds/ATMOSFERA4.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm6","../../Sounds/ATMOSFERA6.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm7","../../Sounds/ATMOSFERA7.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm8","../../Sounds/ATMOSFERA8.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm9","../../Sounds/ATMOSFERA9.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm10","../../Sounds/ATMOSFERA10.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm11","../../Sounds/ATMOSFERA11.mp3"   , 1.0, 1.0, 1.0, 1  , 1,  0 )
Bladex.AddMusicEventMP3  ( "atm12","../../Sounds/ATMOSFERA12.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm16","../../Sounds/ATMOSFERA16.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm17","../../Sounds/ATMOSFERA17.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm18","../../Sounds/ATMOSFERA18.mp3"   , 1.0, 1.0, 0.9, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm19","../../Sounds/ATMOSFERA19.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm20","../../Sounds/ATMOSFERA20.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm20A","../../Sounds/ATMOSFERA20A.mp3" , 1.0, 1.0, 1.0, 800, 1, -1 )
Bladex.AddMusicEventADPCM( "atm444","../../Sounds/ATMOSFERA4.wav"   , 1.0, 1.0, 0.5, 850  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm21","../../Sounds/ATMOSFERA21.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm22","../../Sounds/ATMOSFERA22.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm23","../../Sounds/ATMOSFERA23.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm27","../../Sounds/ATMOSFERA27.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm29","../../Sounds/ATMOSFERA29.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm30","../../Sounds/ATMOSFERA30.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )


#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("grutas") )