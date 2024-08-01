##///
##||| Damage.PY TITANIUM
##||| Change list:
##||| * Added mutilations for skeletons on crush damage
##||| * Added sparks/dust for crush damage on DustDeathEntities
##||| * Modified dwarf combo damage data to correspond with IceHammer change
##||| * Added comments to make it easier to understand which attacks correspond to which animation
##||| * Extra entries for InflictDamageFXData for elemental weapons
##||| * Added AnimData for Gold and Dark Ork
##||| * Adapted bow camera fix from HD update
##||| * Blocking with weapons with no "brkobjdata" (special weapons) will now still cause attacker to recoil
##||| * Having a 2handed weapon broken will now remove child entities (for example arrows) before being destroyed
##\\\ 

import Reference
import Bladex
import BCopy
import pdb
import Blood
import CharStats
import Breakings
import whrandom
import Actions
import netgame
import Auras
import GenFX



if netgame.GetNetState() != 0:
	import NetWeapon

PlayerHitFunc = ""
PrintFormula=0
PrintFatigue=0




# Tabla de parametros para el efecto de impacto segun la animacion
#aura_size_var, aura_exp_time, r, g, b, light_intensity, sound, volume, pitch

InflictDamageFXData={}

###############
#  CABALLERO  #
###############
#espadaromana
InflictDamageFXData['Kgt_g_27kata_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#gladius
InflictDamageFXData['Kgt_g_28new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#maza
InflictDamageFXData['Kgt_g_01_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#elfsword
InflictDamageFXData['Kgt_g_32_5_3new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#maza2
InflictDamageFXData['Kgt_g_21_6_s8new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#hooksword
InflictDamageFXData['Kgt_g_s22low_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#espadacurva
InflictDamageFXData['Kgt_g_sb25_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#dagesse
InflictDamageFXData['Kgt_g_s19_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#cimitarra
InflictDamageFXData['Kgt_g_18_11_22_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#maza3
InflictDamageFXData['Kgt_g_b32kata_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#doublesword
InflictDamageFXData['Kgt_g_22kata_23_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#espadafilo
InflictDamageFXData['Kgt_g_09_07_s6low_new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#espada
InflictDamageFXData['Kgt_g_29_3new']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)

#############
#  BARBARO  #
#############
#chaosword
InflictDamageFXData['Bar_g2h_b6']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#eclipse
InflictDamageFXData['Bar_g_axe211']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#deathsword
InflictDamageFXData['Bar_g2h_b6low']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#guadanya
InflictDamageFXData['Bar_g_axe33']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#longsword
InflictDamageFXData['Bar_g2h_13']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#alfange
InflictDamageFXData['Bar_g2h_s8']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#hacha2hojas
InflictDamageFXData['Bar_g_axe34']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#flatsword
InflictDamageFXData['Bar_g2h_28']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#bigsword
InflictDamageFXData['Bar_g2h_b29']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#rhinoclub
InflictDamageFXData['Bar_g_axe12']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#hacharrajada
InflictDamageFXData['Bar_g_axe32']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#sawsword
InflictDamageFXData['Bar_g2h_21_7']=(250.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)

###########
#  ENANO  #
###########
#GARROTE
InflictDamageFXData['Dwf_g_14']=(40.0, 0.2, 240, 20, 0, 2.0, None, 1.0, 1.0)
#HACHA
InflictDamageFXData['Dwf_g_15']=(50.0, 0.25, 240, 20, 0, 2.0, None, 1.0, 1.0)
#HACHA5
InflictDamageFXData['Dwf_g_07']=(60.0, 0.3, 240, 20, 0, 2.0, None, 1.0, 1.0)
#GARROPIN
InflictDamageFXData['Dwf_g_11']=(70.0, 0.35, 240, 20, 0, 2.0, None, 1.0, 1.0)
#HACHA4
InflictDamageFXData['Dwf_g_16']=(80.0, 0.4, 240, 20, 0, 2.0, None, 1.0, 1.0)
#HACHA3
InflictDamageFXData['Dwf_g_05']=(90.0, 0.45, 240, 20, 0, 2.0, None, 1.0, 1.0)
#MARTILLO
InflictDamageFXData['Dwf_g_12']=(100.0, 0.5, 240, 20, 0, 2.0, None, 1.0, 1.0)
#MARTILLO2
InflictDamageFXData['Dwf_g_18']=(110.0, 0.55, 240, 20, 0, 2.0, None, 1.0, 1.0)
#GARROTE2
InflictDamageFXData['Dwf_g_13']=(120.0, 0.6, 240, 20, 0, 2.0, None, 1.0, 1.0)
#MAZADOBLE
InflictDamageFXData['Dwf_g_21']=(150.0, 0.65, 240, 20, 0, 2.0, None, 1.0, 1.0)
#HACHA6
InflictDamageFXData['Dwf_g_s3_new']=(200.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#HACHA2
InflictDamageFXData['Dwf_g_17']=(300.0, 0.8, 240, 20, 0, 2.0, None, 1.0, 1.0)
#MARTILLO3
InflictDamageFXData['Dwf_g_31']=(400.0, 0.9, 240, 20, 0, 2.0, None, 1.0, 1.0)

#############
#  AMAZONA  #
#############
#BO
InflictDamageFXData['Amz_g_spears8']=(40.0, 0.2, 240, 20, 0, 2.0, None, 1.0, 1.0)
#BICHERO
InflictDamageFXData['Amz_g_spear_2katab6low']=(50.0, 0.25, 240, 20, 0, 2.0, None, 1.0, 1.0)
#LANZA
InflictDamageFXData['Amz_g_spear19']=(60.0, 0.3, 240, 20, 0, 2.0, None, 1.0, 1.0)
#NAGINATA
InflictDamageFXData['Amz_g_spear22']=(70.0, 0.35, 240, 20, 0, 2.0, None, 1.0, 1.0)
#TRIDENTE
InflictDamageFXData['Amz_g_spear09']=(80.0, 0.4, 240, 20, 0, 2.0, None, 1.0, 1.0)
#AXPEAR
InflictDamageFXData['Amz_g_spear32kata_b2']=(90.0, 0.45, 240, 20, 0, 2.0, None, 1.0, 1.0)
#DEATHBO
InflictDamageFXData['Amz_g_spear_kata23']=(100.0, 0.5, 240, 20, 0, 2.0, None, 1.0, 1.0)
#CROSSPEAR
InflictDamageFXData['Amz_g_spear13']=(110.0, 0.55, 240, 20, 0, 2.0, None, 1.0, 1.0)
#HACHACUCHILLA
InflictDamageFXData['Amz_g_spear3s2']=(120.0, 0.6, 240, 20, 0, 2.0, None, 1.0, 1.0)
#CRUSHBO
InflictDamageFXData['Amz_g_spear_21']=(150.0, 0.65, 240, 20, 0, 2.0, None, 1.0, 1.0)
#ARPON
InflictDamageFXData['Amz_g_spear_b29']=(200.0, 0.7, 240, 20, 0, 2.0, None, 1.0, 1.0)
#NAGINATA2
InflictDamageFXData['Amz_g_spear33']=(300.0, 0.8, 240, 20, 0, 2.0, None, 1.0, 1.0)
#LANZAANCHA
InflictDamageFXData['Amz_g_spear_sb11']=(400.0, 0.9, 240, 20, 0, 2.0, None, 1.0, 1.0)



######---------######
# ELEMENTAL WEAPONS #
######---------######

### Fire
# Maybe we don't even need this? -LeadHead
# Nevermind, we do need this. Although aura is created on all fire attacks, light is not.
# So let there be light.

# # Fire Sword
InflictDamageFXData['Kgt_g_s28kata_new']=(0, 0.9, 255, 128, 0, 2.0, None, 1.0, 1.0)
# # Big Fire Sword
InflictDamageFXData['Bar_g2h_earthpow']=(0, 0.9, 255, 128, 0, 2.0, None, 1.0, 1.0)
# # Fire Axe
InflictDamageFXData['Dwf_g_22']=(0, 0.9, 255, 128, 0, 2.0, None, 1.0, 1.0)
# # Fire bo
InflictDamageFXData['Amz_g_spear_b6_26']=(0, 0.9, 255, 128, 0, 2.0, None, 1.0, 1.0)


### Ice
# Don't create aura but we want light, since it's already done by default, leave first value at 0 -LeadHead

# Ice Sword
InflictDamageFXData['Kgt_g_12_7_s1new']=(0, 0.9, 100, 200, 240, 2.0, None, 1.0, 1.0)
# Ice Axe
InflictDamageFXData['Bar_g_axe30']=(0, 0.9, 100, 200, 240, 2.0, None, 1.0, 1.0)
# Ice Hammer
InflictDamageFXData['Dwf_g_s18_2h']=(0, 0.9, 100, 200, 240, 2.0, None, 1.0, 1.0)
# Ice Wand
InflictDamageFXData['Amz_g_spear16']=(0, 0.9, 100, 200, 240, 2.0, None, 1.0, 1.0)


### Queensword
# Aura data not needed since it's done by default -LeadHead

#InflictDamageFXData
#InflictDamageFXData
#InflictDamageFXData
#InflictDamageFXData

### Venom
# Don't create additional aura, only light?

# Crush Hammer
InflictDamageFXData['Dwf_g_s22low_new']=(0, 0.9, 10, 110, 20, 2.0, None, 1.0, 1.0)

# Steel Feather
InflictDamageFXData['Amz_g_spear19_bs1']=(0, 0.9, 10, 110, 20, 2.0, None, 1.0, 1.0)



# Attacking Anim Table   (Damage Factor) ### Note that DamageFactor also determines stamina use!
###  PLAGUE: There are multiple entries here for the same animations. This must be investiagated
###          Some entries have been switched places to better match their actual combos.
AnimationData={}         #############

###############
#   BARBARO   #
###############
#inicio
AnimationData['Bar_g2h_08']=   1.0

#combos arriba
AnimationData['Bar_g2h_b6kata']=  1.25
AnimationData['Bar_g2h_b7']=  2.8           ### PLAGUE: Duplicated - Skysmash. Suspected to be the actually intended value

#combos derecha
AnimationData['Bar_g2h_11']=   1.0
AnimationData['Bar_g2h_02kata']=  1.2      

#combos izquierda
AnimationData['Bar_g2h_s7']=  1.0           ### PLAGUE: Duplicated
AnimationData['Bar_g2h_01']=   1.8

#combos bajo
AnimationData['Bar_g2h_12low']=   1.0
AnimationData['Bar_g2h_02low']=   2.0

#deathsword
AnimationData['Bar_g2h_b6low']=   8.0

#chaossword
AnimationData['Bar_g2h_b6']=   8.0

#bigsword
AnimationData['Bar_g2h_b29']=  10.0
AnimationData['Bar_g2h_s7']=   1.0          ### PLAGUE: Duplicated
AnimationData['Bar_g2h_19']=  10.0

#longsword
AnimationData['Bar_g2h_13']=    7.0

#alfange
AnimationData['Bar_g2h_s8']=   6.2
AnimationData['Bar_g2h_26']=   10.0         ### PLAGUE: Unused?

#flatsword
AnimationData['Bar_g2h_28']=   10.0
AnimationData['Bar_g2h_17']=   10.0         ### PLAGUE: Unused?
AnimationData['Bar_g2h_b7']=   10.0         ### PLAGUE: Duplicated - Skysmash. This one overrides the previous one.

#sawsword
AnimationData['Bar_g2h_21_7']=   8.0
#AnimationData['Bar_g2h_b6kata']=   70.0

#firebigsword
AnimationData['Bar_g2h_21_2']=   21.0
AnimationData['Bar_g2h_earthpow']=   60.0

#comborapidoextra1
AnimationData['Bar_g2h_21_6kata']=   3.0
#comborapidoextra2
AnimationData['Bar_g2h_26_b6']=   3.5 


#sin utilizar /// or "Unused" in English 
AnimationData['Bar_g2h_02']=   10.0


# HACHAS #
#inicio
AnimationData['Bar_g_axe08']=   1.0

#arriba
AnimationData['Bar_g_axe18']=   1.0
AnimationData['Bar_g_axe01']=  2.6
#AnimationData['Bar_g_axe08strong']= 1.2        ### PLAGUE: Unused, seems to be missing anmFlags to move it to left hand

#derecha
AnimationData['Bar_g_axe02']=   1.0

#izquierda
AnimationData['Bar_g_axe13']=   1.0

#abajo
AnimationData['Bar_g_axe111']=   1.0
AnimationData['Bar_g_axe_2katab6low']=  30.0

#comboaleatorioextra
AnimationData['Bar_g_axe31']=   3.2

#hacharrajada
AnimationData['Bar_g_axe32']=  9.0
AnimationData['Bar_g_axe_26kata']=   9.0        ### PLAGUE: Unused, one of Amazon's anims repurposed for barb?
AnimationData['Bar_g_axe_3s2']=   9.0           ### PLAGUE: Unused, one of Amazon's anims repurposed for barb?

#eclipse
AnimationData['Bar_g_axe211']=   10.0

#guadanya
AnimationData['Bar_g_axe33']=   7.0

#rhinoclub
AnimationData['Bar_g_axe12']=  10.0

#hacha2hojas
AnimationData['Bar_g_axe34']=  8.0
AnimationData['Bar_g_axe_32kata_b2']=   8.0     ### PLAGUE: Unused, one of Amazon's anims repurposed for barb?

#iceaxe
AnimationData['Bar_g_axe30']=   34.0

#sin utilizar
AnimationData['Bar_g_axe28']=   1.0

#esquivas y ataque 180
AnimationData['Bar_g2h_d_r']=   2.0
AnimationData['Bar_g2h_d_l']=   2.0
AnimationData['Bar_g_d_r_axe']=   2.0
AnimationData['Bar_g_d_l_axe']=   2.0
AnimationData['Bar_g2h_back']=   2.0

#golpes sin armas
AnimationData['Bar_g_punch1']=   2.0
AnimationData['Bar_g_punch2']=   1.0
AnimationData['Bar_g_punch3']=   1.4
AnimationData['Bar_g_punch4']=   1.0
AnimationData['Bar_g_kick']=   2.0
AnimationData['Bar_g_magic']=   37.5
AnimationData['Bar_g_magic2']=   21.0

#armas no afines
AnimationData['Bar_g_07']=   1.0
AnimationData['Bar_g_11']=   1.2
AnimationData['Bar_g_16']=   1.2
AnimationData['Bar_g_17']=   1.2
AnimationData['Bar_g_18']=   1.4
AnimationData['Bar_g_06lowkata_new']=   10.0

###############
#  CABALLERO  #
###############
AnimationData['Kgt_g_08_new']=  1.0
AnimationData['Kgt_g_01_7_new']=   1.5
AnimationData['Kgt_g_07_new']=  1.0
AnimationData['Kgt_g_s3_new']=   2.8
AnimationData['Kgt_g_12_new']=  1.0
AnimationData['Kgt_g_02_new']=   2.0
AnimationData['Kgt_g_b06_new']=  1.0
AnimationData['Kgt_g_19_bs1_new']=   2.3
AnimationData['Kgt_g_01low_new']=  1.0
AnimationData['Kgt_g_22lowkata_new']=   2.5

#gladius
AnimationData['Kgt_g_28new']=   7.5
#maza
AnimationData['Kgt_g_01_new']=   13.0
#espadaromana
AnimationData['Kgt_g_27kata_new']=   10.0
#elfsword
AnimationData['Kgt_g_32_5_3new']=   8.5
#maza2
AnimationData['Kgt_g_21_6_s8new']=   9.0
#hooksword
AnimationData['Kgt_g_s22low_new']=   9.0
#espadacurva
AnimationData['Kgt_g_sb25_new']=   10.0
#dagesse
AnimationData['Kgt_g_s19_new']=   11.0
#cimitarra
AnimationData['Kgt_g_18_11_22_new']=  10.0
#maza3
AnimationData['Kgt_g_b32kata_new']=  10.0
#doublesword
AnimationData['Kgt_g_22kata_23_new']=  8.0
#espadafilo
AnimationData['Kgt_g_09_07_s6low_new']=  9.0
#espada
AnimationData['Kgt_g_29_3new']=   9.0
#queensword
AnimationData['Kgt_g_06lowkata_new']=   7.5
#icesword
AnimationData['Kgt_g_12_7_s1new']=   70.0
#firesword
AnimationData['Kgt_g_s28kata_new']=   30.0

#south cross
AnimationData['Kgt_g_3s9_6new']=  3.5

#attack 180
AnimationData['Kgt_g_back']=   1.8

#clumsy
AnimationData['Kgt_g_bad_axe']=   1.6
AnimationData['Kgt_g_bad_sword']=   1.0
AnimationData['Kgt_g_bad_sword2']=   1.3
AnimationData['Kgt_g_bad_sword3']=   1.5
AnimationData['Kgt_g_bad_spear']=   1.9
AnimationData['Kgt_g_bad_spear2']=   1.9

#unarmed attacks
AnimationData['Kgt_g_punch1']=   1.2
AnimationData['Kgt_g_punch2']=   1.2
AnimationData['Kgt_g_kick']=   1.2

#dodge attacks
AnimationData['Kgt_g_d_r']=   1.2
AnimationData['Kgt_g_d_l']=   1.2

AnimationData['Kgt_g_magic']=   37.5
AnimationData['Kgt_g_magic2']=  21.0
AnimationData['Kgt_g_08']=   1.0
AnimationData['Kgt_g_06']=   1.3
AnimationData['Kgt_g_02']=   1.2
AnimationData['Kgt_g_07']=   1.3
AnimationData['Kgt_g_05']=   1.2

#############
#  AMAZONA  #
#############
#inicio
AnimationData['Amz_g_spears1']=  1.0

#arriba
AnimationData['Amz_g_spear08']=  1.0

#derecha
AnimationData['Amz_g_spear12']=  1.0

#izquierda
AnimationData['Amz_g_spears6']=  1.0

#abajo
AnimationData['Amz_g_spear16low']=  1.0


#EXRA ARMAS
#BO
AnimationData['Amz_g_spears8']=  5.0
#BICHERO
AnimationData['Amz_g_spear_2katab6low']= 13.0
#LANZA
AnimationData['Amz_g_spear19']= 10.0
#NAGINATA
AnimationData['Amz_g_spear22']=  8.6
#TRIDENTE
AnimationData['Amz_g_spear09']=  8.0
#AXPEAR
AnimationData['Amz_g_spear32kata_b2']= 9.0
#DEATHBO
AnimationData['Amz_g_spear_kata23']=   9.0
#CROSSPEAR
AnimationData['Amz_g_spear13']=  11.0
#HACHACUCHILLA
AnimationData['Amz_g_spear3s2']= 11.0
#CRUSHBO
AnimationData['Amz_g_spear_21']=   10.0
#ARPON
AnimationData['Amz_g_spear_b29']= 9.0
#NAGINATA2
AnimationData['Amz_g_spear33']=  7.8
#LANZAHANCHA
AnimationData['Amz_g_spear_sb11']=   9.0
#FIREBO
AnimationData['Amz_g_spear_b6_26']= 37.0
#STEELFEATHER
AnimationData['Amz_g_spear19_bs1']=  65.0
#ICEWAND
AnimationData['Amz_g_spear16']=  35.0

#QUEENSWORD
AnimationData['Amz_g_06lowkata_new']=  10.0

#extragolpe
AnimationData['Amz_g_spear26kata']= 1.5

#180
AnimationData['Amz_g_spear_back']= 2.0

#golpes torpes
AnimationData['Amz_g_bad_axe']=  1.0
AnimationData['Amz_g_bad_sword']=  1.0
AnimationData['Amz_g_bad_sword2']=  1.0
AnimationData['Amz_g_bad_sword3']= 1.0

#golpes arma 1 mano
AnimationData['Amz_g_09']=   1.0
AnimationData['Amz_g_05']=   1.2
AnimationData['Amz_g_02']=   1.2
AnimationData['Amz_g_06']=   1.2
AnimationData['Amz_g_07']=   1.2
AnimationData['Amz_g_magic']=   37.5
AnimationData['Amz_g_magic2']=   21.0


#golpes sin armas
AnimationData['Amz_g_punch2']=   1.0
AnimationData['Amz_g_kick1']=   1.5
AnimationData['Amz_g_kick2']=   1.0

#sin utilizar
AnimationData['Amz_g_spear111']=   1.0
AnimationData['Amz_g_spear17']=   1.0
AnimationData['Amz_g_spear19_13']=   1.0
AnimationData['Amz_g_spear_b06']=   1.0
AnimationData['Amz_g_spear_bs21']=   1.0
AnimationData['Amz_g_spear02']=   1.0


###########
#  ENANO  #
###########
AnimationData['Dwf_g_08']=   1.0
AnimationData['Dwf_g_01']=   1.0
AnimationData['Dwf_g_01low_new']=   1.0
AnimationData['Dwf_g_02']=   1.0
AnimationData['Dwf_g_05']=   8.0
AnimationData['Dwf_g_06']=   1.0
AnimationData['Dwf_g_07']=   11.0
AnimationData['Dwf_g_01a']=   1.0
AnimationData['Dwf_g_02a']=   1.0
AnimationData['Dwf_g_05a']=   1.0
AnimationData['Dwf_g_06a']=   1.0
AnimationData['Dwf_g_07a']=   1.0

AnimationData['Dwf_g_18']=   9.2
AnimationData['Dwf_g_15']=   6.0
AnimationData['Dwf_g_14']=   4.5
AnimationData['Dwf_g_13']=   10.5
AnimationData['Dwf_g_16']=   7.8
AnimationData['Dwf_g_11']=   8.0
AnimationData['Dwf_g_12']=   9.2
AnimationData['Dwf_g_17']=   9.0
#MAZADOBLE
AnimationData['Dwf_g_21']=   9.0
#DOOM HAMMER
AnimationData['Dwf_g_22']=   70.0
AnimationData['Dwf_g_23']=   1.5
AnimationData['Dwf_g_26']=   1.5
AnimationData['Dwf_g_27']=   1.5
#MARTILLO3 (DOOMHAMMER)
AnimationData['Dwf_g_31']=   8.0

AnimationData['Dwf_g_back']=   1.0
#ICE HAMMER 
AnimationData['Dwf_g_s18_2h']=   38.0 # g_s18_2h was unused prior to Titanium - LeadHead
#CRUSH HAMMER
AnimationData['Dwf_g_s22low_new']=   50.0
AnimationData['Dwf_g_s3_new']=   12.0
AnimationData['Dwf_g_27kata']=   1.0
AnimationData['Dwf_g_12low']=   1.0
AnimationData['Dwf_g_s11']=   1.0
#QUEENSWORD
AnimationData['Dwf_g_06lowkata_new']=   10.0
#BLADESWORD
AnimationData['Dwf_g_magic']=   37.5
AnimationData['Dwf_g_magic2']=   21.0

#Golpes Torpes
AnimationData['Dwf_g_bad_axe']=   1.0
AnimationData['Dwf_g_bad_spear']=   1.0
AnimationData['Dwf_g_bad_spear2']=   1.0
AnimationData['Dwf_g_bad_sword']=   1.0
AnimationData['Dwf_g_bad_sword1']=   1.0
AnimationData['Dwf_g_bad_sword2']=   1.0
AnimationData['Dwf_g_bad_sword3']=   1.0
AnimationData['Dwf_g_bad_no']=   1.0
AnimationData['Dwf_g_bad_1h']=   1.0

#Ataques instantaneos
AnimationData['Dwf_g_draw_rlx']=   1.0
AnimationData['Dwf_g_draw_run']=   1.0

#Esquivas
AnimationData['Dwf_g_d_r']=   2.0
AnimationData['Dwf_g_d_l']=   2.0

#golpes sin armas
AnimationData['Dwf_g_punch1']=   1.0
AnimationData['Dwf_g_punch2']=   1.0
AnimationData['Dwf_g_kick']=   1.0

#Unused animations - random damage data given as placeholders unless otherwise stated, feel free to comment/uncomment and change them if you wish to -LeadHead
#AnimationData['Dwf_g_s18']=   11.0 #Unused, added
AnimationData['Dwf_g_09']=    1.0 #Old IceHammer attack, had damage modifier of 38.0
#AnimationData['Dwf_g_32_5_3new']=   1.0 #Animation of "The Dream"
#AnimationData['Dwf_g_09a']=   1.0 #Same animation as g_09 but with weird head movement at the end
#AnimationData['Dwf_g_08a']=   1.0 #Same animation as g_08 but with weird head movement at the end




##########
#  ORCO  #
##########
AnimationData['Ork_g_01']=   1.0
AnimationData['Ork_g_02']=   1.0
AnimationData['Ork_g_06']=   1.0
AnimationData['Ork_g_15']=   1.2
AnimationData['Ork_g_16']=   1.5
AnimationData['Ork_g_18']=   1.8
###############
#  GRAN ORCO  #
###############
AnimationData['Gok_g_01']=   1.0
AnimationData['Gok_g_02']=   1.2
AnimationData['Gok_g_06']=   1.3
AnimationData['Gok_g_15']=   2.0
AnimationData['Gok_g_16']=   2.5
AnimationData['Gok_g_18']=   3.0
###############
#  ORCO  GOLD # -LeadHead
###############
AnimationData['Org_g_01']=   1.0
AnimationData['Org_g_02']=   1.0
AnimationData['Org_g_06']=   1.0
AnimationData['Org_g_15']=   1.2
AnimationData['Org_g_16']=   1.5
AnimationData['Org_g_18']=   1.8
###############
# ORCO OSCURO # -LeadHead
###############
AnimationData['Dok_g_01']=   1.0
AnimationData['Dok_g_02']=   1.0
AnimationData['Dok_g_06']=   1.0
AnimationData['Dok_g_15']=   1.2
AnimationData['Dok_g_16']=   1.5
AnimationData['Dok_g_18']=   1.8

###############
#  ESQUELETO  #
###############
AnimationData['Skl_g_01']=    1.0
AnimationData['Skl_g_02']=    1.2
AnimationData['Skl_g_07']=    1.3
AnimationData['Skl_g_09']=    1.5
AnimationData['Skl_g_16']=    2.1
AnimationData['Skl_g_18']=    1.8
AnimationData['Skl_g_22']=    2.0

##########
#  LICH  #
##########
AnimationData['Lch_g_12']=    2.8
AnimationData['Lch_g_13']=    2.8
AnimationData['Lch_g_16']=    2.8
AnimationData['Lch_g_18']=    2.8

###########
#  ZOMBI  #
###########
AnimationData['Zkn_g_12']=    3.6
AnimationData['Zkn_g_13']=    3.8
AnimationData['Zkn_g_16']=    3.6
AnimationData['Zkn_g_18']=    3.7

#######################
#  Caballero Traidor  #
#######################
AnimationData['Tkn_g_01']=    1.0
AnimationData['Tkn_g_02']=    1.2
AnimationData['Tkn_g_07']=    1.3
AnimationData['Tkn_g_08']=    1.4
AnimationData['Tkn_g_13']=    1.6
AnimationData['Tkn_g_14']=    2.3
AnimationData['Tkn_g_16']=    2.5
AnimationData['Tkn_g_18']=    2.6

#####################
#  Caballero Negro  #
#####################
AnimationData['Dkn_g_01']=    1.0
AnimationData['Dkn_g_02']=    1.2
AnimationData['Dkn_g_07']=    1.2
AnimationData['Dkn_g_08']=    1.3
AnimationData['Dkn_g_13']=    1.5
AnimationData['Dkn_g_14']=    1.6
AnimationData['Dkn_g_16']=    1.8
AnimationData['Dkn_g_18']=    1.95

############
#  RAGNAR  #
############
AnimationData['Rgn_g_01']=    1.0
AnimationData['Rgn_g_02']=    1.0
AnimationData['Rgn_g_03']=    1.0
AnimationData['Rgn_g_07']=    1.0
AnimationData['Rgn_g_d_r']=   1.5
AnimationData['Rgn_g_d_l']=   1.5
AnimationData['Rgn_g_escape']=   2.5
AnimationData['Rgn_g_17']=    1.6
AnimationData['Rgn_g_21']=    1.5

#################
#  TROLL NEGRO  #
#################
AnimationData['Trl_g_01']=    1.0
AnimationData['Trl_g_02']=    1.2
AnimationData['Trl_g_04']=    1.4
AnimationData['Trl_g_06']=    1.6
AnimationData['Trl_g_12']=    2.8
AnimationData['Trl_g_18']=    3.4
AnimationData['Trl_g_19']=    1.8
AnimationData['Trl_g_31']=    4.8

###############
#  MINOTAURO  #
###############
AnimationData['Min_g_01']=    1.0
AnimationData['Min_g_07']=    1.2
AnimationData['Min_g_08']=    1.5
AnimationData['Min_g_12']=    3.0
AnimationData['Min_g_31']=    2.8

####################
#  Caballero CAOS  #
####################
AnimationData['Chk_g_magic']=    15.0
AnimationData['Chk_g_01']=    1.0
AnimationData['Chk_g_02']=    1.2
AnimationData['Chk_g_07']=    1.0
AnimationData['Chk_g_08']=    1.2
AnimationData['Chk_g_12']=    2.0
AnimationData['Chk_g_18']=    2.5
AnimationData['Chk_g_31']=    4.0

##################
#  GOLEM PIEDRA  #
##################
AnimationData['Glm_g_01']=    1.8
AnimationData['Glm_g_114']=    4.0
AnimationData['Glm_g_12']=    4.0
AnimationData['Glm_g_21']=    1.8
AnimationData['Glm_g_21_27']=    1.5
AnimationData['Glm_g_31']=    10.0
AnimationData['Glm_g_spit']=    10.0
AnimationData['Glm_g_1tw']=    10.0

###################
#  DEMONIO MENOR  #
###################
AnimationData['Ldm_g_spit']=    3.5
AnimationData['Ldm_g_03']=    1.0
AnimationData['Ldm_g_06']=    1.2
AnimationData['Ldm_g_07']=    1.3
AnimationData['Ldm_g_22']=   3.0
AnimationData['Ldm_g_27']=   2.5
AnimationData['Ldm_g_jumpl']=    1.3
AnimationData['Ldm_g_jumpr']=    1.3

##################
#  DEMONIO JEFE  #
##################
AnimationData['Gdm_g_01']=    1.0
AnimationData['Gdm_g_12']=    1.5
AnimationData['Gdm_g_back']=    1.5
AnimationData['Gdm_g_claw']=    1.0
AnimationData['Gdm_g_quake']=    2.0

##############
#  DALGURAK  #
##############
AnimationData['Dgk_g_07_new']=    1.3
AnimationData['Dgk_g_08_new']=    1.6
AnimationData['Dgk_g_02_new']=    2.0
AnimationData['Dgk_g_01_7_new']=    4.0
AnimationData['Dgk_g_22lowkata_new']=    2.5
AnimationData['Dgk_g_21_6_s8new']=    3.0
AnimationData['Dgk_g_19_bs1_new']=    5.0
AnimationData['Dgk_g_b32kata_new']=    2.5
AnimationData['Dgk_g_29_3new']=    1.3
AnimationData['Dgk_g_d_l']=    2.3
AnimationData['Dgk_g_d_r']=    2.3
AnimationData['Dgk_g_back']=    4.3

################
#  JEFE FINAL  #
################
AnimationData['Ank_g_01']=    6.5
AnimationData['Ank_g_02']=    6.5
AnimationData['Ank_g_07']=    6.5


######
#AnimationData['g_01']=   0.3
#AnimationData['g_02']=   0.3
AnimationData['g_03']=   0.3
AnimationData['g_04']=   0.3
AnimationData['g_05']=   0.3
AnimationData['g_06']=   0.3
#AnimationData['g_07']=   0.3
#AnimationData['g_08']=   0.3
AnimationData['g_09']=   0.3
AnimationData['g_10']=   1.0
AnimationData['g_11']=   1.0
AnimationData['g_12']=   1.0
#AnimationData['g_13']=   1.0
#AnimationData['g_14']=   1.0
AnimationData['g_15']=   1.0
#AnimationData['g_16']=   1.5
AnimationData['g_17']=   1.0
#AnimationData['g_18']=   1.0
AnimationData['g_19']=   1.0
AnimationData['g_21']=   2.5
AnimationData['g_22']=   2.5
AnimationData['g_23']=   2.5
AnimationData['g_24']=   2.5
AnimationData['g_25']=   2.5
AnimationData['g_26']=   2.5
AnimationData['g_27']=   2.5
AnimationData['g_31']=   3.5

#AnimationData['g_magic']=   5.3
#AnimationData['g_magic2']=   5.3

################################################################################
# Special Damage Functions
# takes:  special damage data, victim resistance, effective normal damage, standard CalcDamage args
# returns: damage points to inflict now.

def InflictFireDamage (special, special_resistance, effective_damage, VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):	
	# Do nothing if not activated by combo
	fire_activated=1

	if fire_activated:

		# Yellow/Red halo effect on victim
		time=Bladex.GetTime()
		aura=Auras.MakeAura(VictimName,0.8,   (1  , 0.01, 1.0, 0, 0, 1), (), (), (2,  0.8, 0.6, 0.0, 0.6, 0.2  ,  0.8, 0.1, 0.0, 0.0, 0.8))
		aura.Data.AddEvent(time+0.15,         (100, 1.0 , 1.0, 0, 0, 1), (), (), (2,  0.8, 0.6, 0.0, 0.6, 0.2  ,  0.8, 0.1, 0.0, 0.0, 0.8))
		aura.Data.AddEvent(time+0.8,          (160, 0.01, 1.0, 0, 0, 1), (), (), (2,  0.8, 0.1, 0.0, 0.6, 0.2  ,  0.8, 0.0, 0.0, 0.0, 0.8))
		prtl=Bladex.CreateEntity(aura.Name+"Particles", "Entity Particle System Dperson", 0, 0, 0)
		prtl.PersonName=VictimName
		prtl.ParticleType="Llamita2"
		prtl.PPS=400
		prtl.Velocity=0.0, 0.0, 0.0
		prtl.NormalVelocity=2.0
		prtl.RandomVelocity=0.0
		prtl.YGravity=-200.0
		prtl.Friction=0.02
		prtl.FollowFactor=0.0
		prtl.Time2Live=21
		prtl.DeathTime=Bladex.GetTime()+0.2

		special_damage= special[1]*(1.0-special_resistance)
		if special_damage>0:
			victim= Bladex.GetEntity(VictimName)
			if victim and victim.Person and victim.Data:
				victim.Data.LastDamageType= special[0]
		return special_damage

	return 0.0

def InflictIceDamage (special, special_resistance, effective_damage, VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	# Do nothing if not activated by combo
	ice_activated=1

	if ice_activated:

		# Blue/White halo effect on victim
		time=Bladex.GetTime()
		aura=Auras.MakeAura(VictimName,0.7,   (1 , 0.01, 1.0, 0, 0, 1), (), (), (2,  0.8, 0.9, 1.0, 0.6, 0.3  ,  0.2, 0.6, 0.8, 0.4, 1.0))
		aura.Data.AddEvent(time+0.1,          (30, 1.0 , 1.0, 0, 0, 1), (), (), (2,  0.8, 0.9, 1.0, 0.6, 0.3  ,  0.2, 0.6, 0.8, 0.4, 1.0))
		aura.Data.AddEvent(time+0.7,          (60, 0.01, 1.0, 0, 0, 1), (), (), (2,  0.2, 0.4, 0.8, 0.6, 0.4  ,  0.0, 0.2, 0.8, 0.4, 0.5))

		special_damage= special[1]*(1.0-special_resistance)
		if special_damage>0:
			victim= Bladex.GetEntity(VictimName)
			if victim and victim.Person and victim.Data:
				victim.Data.LastDamageType= special[0]
		return special_damage

	return 0.0

def InflictVenomDamage (special, special_resistance, effective_damage, VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	if not (Shielded and effective_damage<=0.0):
		victim= Bladex.GetEntity(VictimName)
		if victim and victim.Person and victim.Data:
			# Effects in Basic_Funcs.py
			venom_damage= special[1]
			victim.Data.EnVenom (VictimName, venom_damage, AttackerName)
	
	return 0         # Does not inflict immediate damage

def InflictDrainDamage (special, special_resistance, effective_damage, VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	weapon= Bladex.GetEntity(WeaponName)
	victim= Bladex.GetEntity(VictimName)
	if AttackerName: holder= Bladex.GetEntity(AttackerName)
	else: holder= None
	LastDamage= min (effective_damage, victim.Life)*(1.0-special_resistance)
	if weapon and victim and LastDamage>0:
		# weapon gives life to user
		if holder:
			holder.Life= min(holder.Life+LastDamage, CharStats.GetCharMaxLife(holder.Kind, holder.Level))
		
		# Red halo effect on weapon
		# ...
		
		# Can we do a streaming blood effect
		# ...		
		time=Bladex.GetTime()
		aura= Auras.MakeAura (VictimName,1.5,    (55,1.0,1.0,1,0,0), (),(),(2,  0.6,0.0,0.0, 0.5, 0.0  , 0.6,0.0,0.0, 0.1, 0.1))
		# expand the blood through the skin	
		aura.Data.AddEvent(time+1.0,             (55,0.8,1.0,1,0,0), (),(),(2,  0.6,0.0,0.0, 0.5, 0.0  , 0.6,0.0,0.0, 0.1, 1.0))
		# disperse the blood through the air
		aura.Data.AddEvent(time+1.5,             (255,0.0,1.0,1,0,0), (),(),(2,  0.6,0.0,0.0, 0.5, 0.0  , 0.6,0.0,0.0, 0.1, 1.0))
		
		# more aura effects on holder in ItemTypes.py:VampWeapon
		
	return 0         # Does not inflict extra damage, just gives the life drained to the user

def InflictElectricDamage (special, special_resistance, effective_damage, VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):	
	# halo effect on victim, must be switched off on death
	special_damage= special[1]*(1.0-special_resistance)
	if special_damage>0:
		victim= Bladex.GetEntity(VictimName)
		if victim and victim.Person and victim.Data:
			victim.Data.LastDamageType= special[0]
	return special_damage	

def InflictLightDamage (special, special_resistance, effective_damage, VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	# Do nothing if not activated by combo
	light_activated=1

	if light_activated:

		time=Bladex.GetTime()
		aura=Auras.MakeAura(VictimName,0.7,   (1  , 0.01, 1.0, 0, 0, 1), (), (), (2,  0.8, 0.9, 1.0, 0.6, 0.3  ,  0.2, 0.6, 0.8, 0.4, 1.0))
		aura.Data.AddEvent(time+0.1,          (120, 1.0 , 1.0, 0, 0, 1), (), (), (2,  0.8, 0.9, 1.0, 0.6, 0.3  ,  0.2, 0.6, 0.8, 0.4, 1.0))
		aura.Data.AddEvent(time+0.7,          (240, 0.01, 1.0, 0, 0, 1), (), (), (2,  0.2, 0.4, 0.8, 0.6, 0.4  ,  0.0, 0.2, 0.8, 0.4, 0.5))
		prtl=Bladex.CreateEntity(aura.Name+"Particles", "Entity Particle System Dperson", 0, 0, 0)
		prtl.PersonName=VictimName
		prtl.ParticleType="BrillosBladeSword"
		prtl.PPS=200
		prtl.Velocity=0.0, 0.0, 0.0
		prtl.NormalVelocity=5.0
		prtl.RandomVelocity=0.0
		prtl.YGravity=0.0
		prtl.Friction=0.01
		prtl.FollowFactor=0.0
		prtl.Time2Live=8
		prtl.DeathTime=Bladex.GetTime()+0.4

		special_damage= special[1]*(1.0-special_resistance)
		if special_damage>0:
			victim= Bladex.GetEntity(VictimName)
			if victim and victim.Person and victim.Data:
				victim.Data.LastDamageType= special[0]
		return special_damage

	return 0.0


SpecialDamageFuncs={}
SpecialDamageFuncs['Fire']    = InflictFireDamage
SpecialDamageFuncs['Ice']     = InflictIceDamage
SpecialDamageFuncs['Venom']   = InflictVenomDamage
SpecialDamageFuncs['Drain']   = InflictDrainDamage
SpecialDamageFuncs['Electric']= InflictElectricDamage
SpecialDamageFuncs['Light']   = InflictLightDamage


def DropInvalidObjectsOnImpact(EntityName):
	me=Bladex.GetEntity(EntityName)
	if me:
		Actions.UnGraspString (EntityName,"UnGraspString")
		Actions.Stop_Weapon (EntityName,"Stop_Weapon")
		if me.InvRight:
			right_type= Reference.GiveObjectFlag(me.InvRight)
			if right_type==Reference.OBJ_ITEM \
			or right_type==Reference.OBJ_SHIELD \
			or right_type==Reference.OBJ_QUIVER \
			or right_type==Reference.OBJ_BOW \
			or right_type==Reference.OBJ_KEY \
			or right_type==Reference.OBJ_SPECIALKEY \
			or right_type==Reference.OBJ_USEME \
			or right_type==Reference.OBJ_SPECIALKEY \
			or right_type==Reference.OBJ_TABLET:
				Actions.DropReleaseEventHandler (EntityName, "DropRightEvent")

		if me.InvLeft:
			left_type= Reference.GiveObjectFlag(me.InvLeft)
			if left_type==Reference.OBJ_ITEM \
			or (left_type==Reference.OBJ_WEAPON and me.InvRight != me.InvLeft) \
			or (left_type==Reference.OBJ_STANDARD and me.InvRight != me.InvLeft) \
			or left_type==Reference.OBJ_QUIVER \
			or left_type==Reference.OBJ_KEY \
			or left_type==Reference.OBJ_SPECIALKEY \
			or left_type==Reference.OBJ_USEME \
			or left_type==Reference.OBJ_SPECIALKEY \
			or left_type==Reference.OBJ_TABLET:
				Actions.DropReleaseEventHandler (EntityName, "DropLeftEvent")
            ### Added below - fixes delayed attack_drink potion dropping        -LeadHead
		if me.InvLeft2:
			Actions.DropReleaseEventHandler (EntityName, "DropLeft2Event")
        
			


def BreakMyShield(EntityName):
	me=Bladex.GetEntity(EntityName)
	if me.InvLeft<>"":
		esc=Bladex.GetEntity(me.InvLeft)
		if esc:
			n_child=esc.GetNChildren()
			for n in range(n_child):
				child=Bladex.GetEntity(esc.GetChild(n))
				if child and child.Kind!="Entity Spot":     # PLAGUE: Interesting observation - this causes auras to get unlinked instead of destroyed, like for swords.
					esc.Unlink(child)
					child.Impulse(0,0,0)
		if Breakings.ExplodeSpecialObject ( me.InvLeft , 24000.0)==1:
			if Reference.EntitiesObjectData.has_key(me.InvLeft):
				del Reference.EntitiesObjectData[me.InvLeft]
			DropInvalidObjectsOnImpact (EntityName)
			me.Wuea=Reference.WUEA_ENDED
			me.LaunchAnmType("df_s_broken")
			inv=me.GetInventory()
			inv.RemoveShield(me.InvLeft)
			inv.LinkLeftHand("None")
			if me.Data.NPC:
				me.Data.ResetCombat (EntityName)


def BreakMySword(EntityName):
	me=Bladex.GetEntity(EntityName)
	if me.InvRight<>"":		
		
		sword = Bladex.GetEntity(me.InvRight)          # Added.
		n_child=sword.GetNChildren()                   # Should now properly remove child entities
		for n in range(n_child):                       # Rather than destroy them.
			child=Bladex.GetEntity(esc.GetChild(n))    #
			if child and child.Kind!="Entity Spot":    #
				esc.Unlink(child)                      #
				child.Impulse(0,0,0)                   #        -LeadHead

		Actions.Stop_Weapon (EntityName,"Stop_Weapon")
		if Breakings.ExplodeSpecialObject ( me.InvRight , 24000.0)==1:
			if Reference.EntitiesObjectData.has_key(me.InvRight):
				del Reference.EntitiesObjectData[me.InvRight]
			DropInvalidObjectsOnImpact (EntityName)
			me.Wuea=Reference.WUEA_ENDED
			me.LaunchAnmType("sword_broken")
			inv=me.GetInventory()
			inv.RemoveWeapon(me.InvRight)
			inv.LinkRightHand("None")
			if me.Data.NPC:
				me.Data.ResetCombat (EntityName)

def StuckWeaponFall (WeaponName, TargetName):
	weapon= Bladex.GetEntity(WeaponName)
	if weapon:		
		if weapon.Parent==TargetName:
			target= Bladex.GetEntity(TargetName)
			if target:
				target.Unlink(weapon)
				if target.Person:
					weapon.ExcludeHitFor(target)
				elif target.Parent:
					parent= Bladex.GetEntity(target.Parent)
					if parent and parent.Person:
						weapon.ExcludeHitFor(parent)
				weapon.Impulse(0.0, 1.0, 0.0)

def CalculateFatigue(EntityName, AnimName):     # PLAGUE: This function sucks.
	me= Bladex.GetEntity(EntityName)	
	if me:
		current_energy= me.Energy
		if current_energy > 0.0:
			
			charF = 0
			animF = 1.0
			weaponF = 0
			
			#
			# The ATTACK....
			#
			
			######################################################################################	
			# We start with the weapon component #
			######################################################################################	
			weaponData= None
			WeaponName= me.GetInventory().GetActiveWeapon()
			if not WeaponName or WeaponName==EntityName and AnimName=='g_draw_rlx' or AnimName=='g_draw_run':
				WeaponName= me.InvRightBack
			
			if WeaponName:	
				if Reference.EntitiesObjectData.has_key(WeaponName):
					if Reference.EntitiesObjectData[WeaponName][0] == Reference.OBJ_WEAPON or Reference.EntitiesObjectData[WeaponName][0] == Reference.OBJ_STANDARD:
						weaponData = Reference.EntitiesObjectData[WeaponName]
						if len (weaponData) > 1:
							weaponF = weaponData[1]
				else:
					weapon= Bladex.GetEntity(WeaponName)
					if weapon:
						kind = weapon.Kind	
						if Reference.DefaultObjectData.has_key(kind):
							if Reference.DefaultObjectData[kind][0] == Reference.OBJ_WEAPON or Reference.DefaultObjectData[kind][0] == Reference.OBJ_STANDARD:
								weaponData = Reference.DefaultObjectData[kind]
								if len (weaponData) > 1:
									weaponF = weaponData[1]	
			
			######################################################################################
			
			######################################################################################
			# character type components #
			######################################################################################
			if netgame.GetNetState() == 0:
				charF=CharStats.GetCharDamageData(me.CharType,me.Level)
			else:
				charF=NetWeapon.GetDamage(me.CharType,me.Data.NetLevel)
			
			######################################################################################
			# Animation component #
			######################################################################################
			me.LaunchAnimation(AnimName)        # PLAGUE: Why are we launching the animation BEFORE making stamina checks?
			# Animation component #
			if AnimationData.has_key(me.AnimFullName):
				animF = AnimationData[me.AnimFullName]
			elif AnimationData.has_key(me.AnimName):
				animF = AnimationData[me.AnimName]
			
			######################################################################################
			
			lvl= me.Level+1     # PLAGUE: This variable is literally never called in this function???
			energy_cost= max((charF + weaponF) * animF, 0.0)+me.Data.Energy2Lose
			if me.Data.FAttack>1.0:
				# during powerup, do not lose energy ### PLAGUE: This is a stupid way to do it - there is char.Data.PowerPotion, why not use that instead?
				energy_cost= 0.0
			if netgame.GetNetState()!=0:
				max_energy= NetWeapon.GetEnergy(me)
			else:
				max_energy= CharStats.GetCharMaxEnergy(me.Kind, me.Level)
			
			me.Data.LoseEnergyRate=0.0
			if PrintFatigue:
				print "energy_cost= (charF("+`charF`+") + weaponF("+`weaponF`+")) * (animF("+me.AnimFullName+"="+`animF`+") + prev_energy2lose("+`me.Data.Energy2Lose`+")= "+`energy_cost`
				print "max_energy= "+`max_energy`+", current_energy= "+`me.Energy`
			if energy_cost<max_energy:
				me.Data.Energy2Lose= energy_cost
				
				if energy_cost>me.Energy:
					# Launch a clumsy animation instead
					weapon= Bladex.GetEntity(me.GetInventory().GetActiveWeapon())
					if weapon and not weapon.Person:
						weapon_flag= Reference.GiveWeaponFlag(WeaponName)
						if weapon_flag==Reference.W_FLAG_2W: clumsy_anm= "g_bad_sword"
						elif weapon_flag==Reference.W_FLAG_AXE: clumsy_anm= "g_bad_axe"
						elif weapon_flag==Reference.W_FLAG_SP: clumsy_anm= "g_bad_spear"
						else: clumsy_anm= "g_bad_1h"
					else: clumsy_anm= "g_bad_no"
					me.Wuea=Reference.WUEA_ENDED
					me.LaunchAnmType(clumsy_anm)
					Actions.ReportMsg ("You need more energy for this attack")
				
				try: anim_duration= Bladex.GetAnimationDuration(me.AnimFullName)
				except RuntimeError:
					print me.AnimFullName + " has not been defined for character "+ me.Kind
					anim_duration= 0.3

				if anim_duration>0.0: me.Data.LoseEnergyRate= energy_cost / anim_duration
				else: me.Data.LoseEnergyRate= 0.0
				
				return 1
			else: 
				Actions.ReportMsg ("You need more energy for this attack")
				me.Wuea=Reference.WUEA_ENDED
		me.InterruptCombat()
		me.RaiseEvent("Interrupt")      # PLAGUE: One of these 3 lines of code + animation being launched before stamina check, cause the exploit that allows attacks with no stamina.
		return 1
	return 0



def CheckRightHandToDrop(EntityName):
    me= Bladex.GetEntity(EntityName)
    if not me.InvRight:
        return

    two_handed_on_right=0
    if Actions.IsRightHandWeaponObject(EntityName):
        w_flag=Reference.GiveWeaponFlag(me.InvRight)
        if w_flag<>Reference.W_FLAG_1H:
            two_handed_on_right=1

    special_to_drop=0
    flag=Reference.GiveObjectFlag(me.InvRight)
    if flag==Reference.OBJ_KEY or flag==Reference.OBJ_SPECIALKEY or flag==Reference.OBJ_USEME:
        print "right 2 drop"
        special_to_drop=1

    if special_to_drop==1 or (two_handed_on_right and me.InvLeft and me.InvRight<>me.InvLeft):
        if Actions.TryDropRight(EntityName):
            Actions.DropReleaseEventHandler(EntityName, "DropRightEvent")
            if me.InvRight:
                #print "...but did not work"
                return FALSE




def CalculateDamage(VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded):
	#pdb.set_trace()
    
	CheckRightHandToDrop(VictimName)

	# Additive vars set to 0
	charF = 0
	animF = 1.0
	weaponF = 0	
	randomF = 0
	throwF = 0
	shieldF = 0
	bowF = 0
	
	# Multiplicative vars set to 1.0
	locationF = 1.0
	magicF = 1.0
	thrown_flag= 0
	
	#
	# The ATTACK....
	#
	
	######################################################################################	
	# We start with the weapon component, there is always a weapon... #
	######################################################################################	
	weaponData= None
	if WeaponName:	
		if Reference.EntitiesObjectData.has_key(WeaponName):
			if Reference.EntitiesObjectData[WeaponName][0] == Reference.OBJ_WEAPON or Reference.EntitiesObjectData[WeaponName][0] == Reference.OBJ_STANDARD or Reference.EntitiesObjectData[WeaponName][0] == Reference.OBJ_ARROW:
				weaponData = Reference.EntitiesObjectData[WeaponName]
				if len (weaponData) > 1:
					weaponF = weaponData[1]
		else:
			kind = Bladex.GetEntity(WeaponName).Kind
			if Reference.DefaultObjectData.has_key(kind):
				if Reference.DefaultObjectData[kind][0] == Reference.OBJ_WEAPON or Reference.DefaultObjectData[kind][0] == Reference.OBJ_STANDARD or Reference.DefaultObjectData[kind][0] == Reference.OBJ_ARROW:
					weaponData = Reference.DefaultObjectData[kind]
					if len (weaponData) > 1:
						weaponF = weaponData[1]
		
		if (not AttackerName) and weaponData and len (weaponData) > 2:
			if PrintFormula==1:
				print "Possible thrown weapon" # get thowF from weapon
			
			weapon= Bladex.GetEntity(WeaponName)
			if weapon:
				try:
					if weapon.Data and weapon.Data.ThrownBy:
						AttackerName= weapon.Data.ThrownBy.Name
						thrown_flag= 1
						if len (weaponData) > 3:
							throwF = weaponData[3]
				except AttributeError:	# No ThrownBy set, could be an arrow thrown by a trap
					if weapon.Arrow:
						thrown_flag= 1
						if len (weaponData) > 3:
							throwF = weaponData[3]
				try:
					if weapon.Person:
						AttackerName=WeaponName
				except: pass
	

	######################################################################################

	######################################################################################
	# Animation component, character type, level and magical components #
	######################################################################################
	attacker= None
	if AttackerName:
		attacker=Bladex.GetEntity(AttackerName)
		
		if attacker and attacker.Person: 
			magicF = attacker.Data.FAttack
			if DamageType=="Impale" or DamageType=="Slash" or DamageType=="Crush":
				if netgame.GetNetState() == 0:
					charF=CharStats.GetCharDamageData(attacker.CharType,attacker.Level)
				else:
					charF=NetWeapon.GetDamage(attacker.CharType,attacker.Data.NetLevel)

			# Animation component #
			if not thrown_flag:
				if AnimationData.has_key(attacker.AnimFullName):
					animF = AnimationData[attacker.AnimFullName]
					if InflictDamageFXData.has_key(attacker.AnimFullName) and (netgame.GetNetState() != 1):
						aura_size_var, aura_exp_time, r, g, b, light_intensity, sound, volume, pitch = InflictDamageFXData[attacker.AnimFullName]
						GenFX.InflictDamageFX(VictimName, aura_size_var, aura_exp_time, r, g, b, light_intensity, sound, volume, pitch)
				elif AnimationData.has_key(attacker.AnimName):
					animF = AnimationData[attacker.AnimName]
					if InflictDamageFXData.has_key(attacker.AnimFullName) and (netgame.GetNetState() != 1):
						aura_size_var, aura_exp_time, r, g, b, light_intensity, sound, volume, pitch = InflictDamageFXData[attacker.AnimFullName]
						GenFX.InflictDamageFX(VictimName, aura_size_var, aura_exp_time, r, g, b, light_intensity, sound, volume, pitch)
		
	randomF= round(whrandom.uniform(-0.05, 0.05)*charF)
	charF= max (charF + randomF, 0)
	######################################################################################

	######################################################################################
	# Damage Zone Multipliers #
	######################################################################################
	if DamageZone==Reference.BODY_HEAD and DamageType=="Impale" and thrown_flag and weaponData[0]==Reference.OBJ_ARROW:
		locationF= 4.0
	######################################################################################
	
	######################################################################################
	# Shield component #
	######################################################################################
	if AttackerName:
		shieldName= attacker.GetInventory().GetActiveShield()
		if shieldName and not thrown_flag:
			if Reference.EntitiesObjectData.has_key(shieldName):
				if Reference.EntitiesObjectData[shieldName][0] ==  Reference.OBJ_SHIELD:
					shieldF = Reference.EntitiesObjectData[shieldName][1]
			else:
				kind = Bladex.GetEntity(shieldName).Kind	
				if Reference.DefaultObjectData.has_key(kind):
					if Reference.DefaultObjectData[kind][0] ==  Reference.OBJ_SHIELD:
						shieldF = Reference.DefaultObjectData[kind][1]
	######################################################################################	
	
	######################################################################################
	# Bow component #
	######################################################################################
	if AttackerName and attacker and attacker.GetInventory().HoldingBow and thrown_flag:
		if Reference.EntitiesObjectData.has_key(attacker.InvLeft):
			if Reference.EntitiesObjectData[attacker.InvLeft][0] ==  Reference.OBJ_BOW:
				bowF = Reference.EntitiesObjectData[attacker.InvLeft][1]
		else:
			kind = Bladex.GetEntity(attacker.InvLeft).Kind
			if Reference.DefaultObjectData.has_key(kind):
				if Reference.DefaultObjectData[kind][0] ==  Reference.OBJ_BOW:
					bowF = Reference.DefaultObjectData[kind][1]
	######################################################################################
	
    ### Bow camera fix from HD update. 
    ### Has NOT been tested extensively, but the code seems fine.
    
	me = Bladex.GetEntity(VictimName)
	if me.Data.AimPressed==0 and me.Aim==1:
		Actions.EndBowMode(VictimName)

	try:
		if me.Data.LastPViewType!=None and not me.Data.AimPressed:
			cam= Bladex.GetEntity("Camera")
			cam.PViewType= me.Data.LastPViewType
			me.Data.LastPViewType= None
	except:
		pass

    ### Again, the code is lifted directly from the HD update, it's unchanged.
    ### -LeadHead
            
    ######################################################################################

	if AttackerName and attacker and attacker.Person:
		lvl= attacker.Level+1
	else:
		lvl=0
		
	basic_damage = ((charF * magicF * locationF) + weaponF + throwF + bowF + shieldF) * animF
	basic_damage = max( basic_damage, 0 )
	
	if PrintFormula==1:
		print "Basic Damage Formula= ((charF * magicF * locationF) + weaponF + throwF + bowF + shieldF) * animF"
		print "Basic Damage = (( "+`charF`+" * "+`magicF`+" * "+`locationF`+" ) + "+`weaponF`+" + "+`throwF`+" + "+`bowF`+" + "+`shieldF`+") * "+`animF`+" = "+`basic_damage`
	
	
	
	#
	# The DEFENSE....
	#
	
	
	# target defence #
	me=Bladex.GetEntity(VictimName)
	charF = 0
	shieldF = 0	
	weaponF = 0
	magicF = me.Data.FDefense
	randomF = 0
	shield_breakable=0	
	victimsShieldData=None
	
	######################################################################################
	# Shield component OR block with 2H weapon #
	######################################################################################	
	blocking_with_weapon=0
	if Shielded:
		victimsShieldName = me.GetInventory().GetActiveShield()
		# Based on the characteristics of whatever you are carrying in the left hand
		if victimsShieldName:
			if Reference.EntitiesObjectData.has_key( victimsShieldName):
				if Reference.EntitiesObjectData[victimsShieldName][0] ==  Reference.OBJ_SHIELD:
					victimsShieldData= Reference.EntitiesObjectData[victimsShieldName]
					shieldF = victimsShieldData[2]
					shield_breakable= victimsShieldData[7]
					
			else:
				kind = Bladex.GetEntity(victimsShieldName).Kind
				if Reference.DefaultObjectData.has_key(kind):
					if Reference.DefaultObjectData[kind][0] ==  Reference.OBJ_SHIELD:
						victimsShieldData= Reference.DefaultObjectData[kind]
						shieldF = Reference.DefaultObjectData[kind][2]
						shield_breakable=Reference.DefaultObjectData[kind][7]
			
		else:
			# Blocking with a weapon
			victimsWeaponName = me.InvRight
			if not victimsWeaponName or victimsWeaponName=="" or victimsWeaponName=="None":
				print "Unexpected error in CalculateDamage"
				print "Blocking but nothing in hands?"
				return
			w_weapon=Bladex.GetEntity(victimsWeaponName)
			w_flag=Reference.GiveObjectFlag(victimsWeaponName)
			if w_flag<>Reference.OBJ_WEAPON:
				print "Error in CalculateDamage"
				print "Blocking with an unexpected type of weapon"
				return
			 
			if Reference.EntitiesObjectData.has_key( victimsWeaponName):
				victimsShieldData=Reference.EntitiesObjectData[victimsWeaponName]
			else:
				kind = Bladex.GetEntity(victimsWeaponName).Kind
				if Reference.DefaultObjectData.has_key(kind):
					victimsShieldData=Reference.DefaultObjectData[kind]

			if not victimsShieldData or len(victimsShieldData[5])<1 or victimsShieldData[5][0]==Reference.W_FLAG_1H:
				print "Error in CalculateDamage"
				print "Trying to wblock with a one handed weapon!"
			else:				
				shieldF = victimsShieldData[5][4]
				shield_breakable=victimsShieldData[5][5]
				blocking_with_weapon=1
	else:
		inv=me.GetInventory()
		if inv.GetMagicShield():
			# Patch, this damage should be shielded....
			shield= Bladex.GetEntity(inv.GetMagicShield())
			ximpulse= 1.0
			yimpulse= 0.0
			zimpulse= 0.0
			shield.HitShieldFunc (shield.Name,WeaponName,x,y,z,ximpulse,yimpulse,zimpulse,DamageType)
			return

	######################################################################################	
	
	######################################################################################
	# Character Type component #
	######################################################################################

	if netgame.GetNetState() == 0:
		charF= CharStats.GetCharDefenseData(me.CharType,me.Level) + me.Data.armour_prot_factor
	else:
		charF=NetWeapon.GetDefense(me.CharType,me.Data.NetLevel)
	
	randomF= round(whrandom.uniform(-0.05, 0.05)*charF)
	charF=  max(charF+randomF, 0)
	######################################################################################
	
	######################################################################################
	# Weapon component #
	######################################################################################
	victimsWeaponData= None
	if me.GetInventory().HoldingBow:
		victimsWeaponName = me.InvLeft
	else:
		victimsWeaponName = me.InvRight
	if victimsWeaponName and blocking_with_weapon==0:	
		if Reference.EntitiesObjectData.has_key(victimsWeaponName):
			if Reference.EntitiesObjectData[victimsWeaponName][0] == Reference.OBJ_WEAPON or Reference.EntitiesObjectData[victimsWeaponName][0] == Reference.OBJ_STANDARD or Reference.EntitiesObjectData[victimsWeaponName][0] == Reference.OBJ_ARROW or Reference.EntitiesObjectData[victimsWeaponName][0] == Reference.OBJ_BOW:
				victimsWeaponData = Reference.EntitiesObjectData[victimsWeaponName]
				if len (victimsWeaponData) > 2:
					weaponF = victimsWeaponData[2]
		else:
			kind = Bladex.GetEntity(victimsWeaponName).Kind	
			if Reference.DefaultObjectData.has_key(kind):
				if Reference.DefaultObjectData[kind][0] == Reference.OBJ_WEAPON or Reference.DefaultObjectData[kind][0] == Reference.OBJ_STANDARD or Reference.DefaultObjectData[kind][0] == Reference.OBJ_ARROW  or Reference.DefaultObjectData[kind][0] == Reference.OBJ_BOW:
					victimsWeaponData = Reference.DefaultObjectData[kind]
					if len (victimsWeaponData) > 2:
						weaponF = victimsWeaponData[2]
	######################################################################################
	
	DEF= (charF * magicF) + shieldF + weaponF
	effective_damage = basic_damage - DEF
	effective_damage = max( effective_damage, 0 )


	if PrintFormula==1:
		print "Effective Damage Formula = basic_damage - (charF * magicF) - shieldF - weaponF"
		print "Effective Damage Formula = "+`basic_damage`+" - ( "+`charF`+" * "+`magicF`+" ) - "+`shieldF`+" - "+`weaponF`+" = "+`effective_damage`

	if Shielded:
		damage_withstood= int (max (basic_damage - (DEF-shieldF), 0))
		if not blocking_with_weapon:
			shield= Bladex.GetEntity(me.GetInventory().GetActiveShield())
			try:
				if shield:                                                                                                            # Bugfix pt.1
					try:
						if shield_breakable:
							# Lower the resistance of the shield
							if victimsShieldData:
								if not Reference.EntitiesObjectData.has_key(shield.Name):
									Reference.EntitiesObjectData[shield.Name]= BCopy.deepcopy(victimsShieldData)
									victimsShieldData= Reference.EntitiesObjectData[shield.Name]
								victimsShieldData[2]= victimsShieldData[2]-damage_withstood
								
								# Break the shield if 0 resistance
								if victimsShieldData[2] <= 0.0:
									victimsShieldData[2]=0.0
									if shield.Data.brkobjdata:
										BreakMyShield(me.Name)
										Shielded=0
								elif attacker and attacker.InDestructorAttack==1 and damage_withstood > shield_breakable:
									if shield.Data.brkobjdata:
										BreakMyShield(me.Name)
										Shielded=0
										if PrintFormula==1:
											print "Shield Breaking in destructor attack, took: "+`damage_withstood`+", max: "+`shield_breakable`
					except AttributeError:                                                                                            # Bugfix pt.2
							print "~~Damage.py~~ blockng shield "+`shield.Name`+" has no 'brkobjdata' (SPECIAL SHIELD?)"              # If weapon/shield doesn't have brkobjdata,
							pass                                                                                                      # we still want the oppoenent to play the flinch animation. -LeadHead 
					if Shielded:
						#rules out cases where shield has broken
						if (not thrown_flag) and attacker and attacker.Person and attacker.GotAnmType("sw_react"):
							attacker.Wuea=Reference.WUEA_ENDED
							attacker.LaunchAnmType("sw_react")
			except AttributeError: pass
			try:
				if shield and shield.Data and shield.Data.AbsorbFunc:
					shield.Data.AbsorbFunc (AttackerName, WeaponName, damage_withstood)
			except AttributeError: pass
		else:
			weapon= Bladex.GetEntity(me.GetInventory().GetActiveWeapon())
			try:
				if weapon:
					try:                                                                                                              # Bugfix pt.3
						if weapon.Data.brkobjdata:
								# Lower the resistance of the shield
								if victimsShieldData:
									if not Reference.EntitiesObjectData.has_key(weapon.Name):
										Reference.EntitiesObjectData[weapon.Name]= BCopy.deepcopy(victimsShieldData)
										victimsShieldData= Reference.EntitiesObjectData[weapon.Name]
									victimsShieldData[5][4]= victimsShieldData[5][4]-damage_withstood
									
									# Break the shield if 0 resistance
									if victimsShieldData[5][4] <= 0.0:
										victimsShieldData[5][4]=0.0
										if weapon.Data.brkobjdata:
											BreakMySword(me.Name)
											Shielded=0
									elif attacker and attacker.InDestructorAttack==1 and damage_withstood > shield_breakable:
										if weapon.Data.brkobjdata:
											BreakMySword(me.Name)
											Shielded=0
											if PrintFormula==1:
												print "Weapon Breaking in destructor attack, took: "+`damage_withstood`+", max: "+`shield_breakable`
					except AttributeError:                                                                                            # Bugfix pt.4
							print "~~Damage.py~~ blocked weapon "+`weapon.Name`+" has no 'brkobjdata' (SPECIAL WEAPON?)"              # If weapon/shield doesn't have brkobjdata,
							pass                                                                                                      # we still want the oppoenent to play the flinch animation. -LeadHead
					if Shielded:
						#rules out cases where shield has broken
						if (not thrown_flag) and attacker and attacker.Person and attacker.GotAnmType("sw_react"):
							attacker.Wuea=Reference.WUEA_ENDED
							attacker.LaunchAnmType("sw_react")
			except AttributeError: pass
			try:
				if weapon and weapon.Data and weapon.Data.AbsorbFunc:
					weapon.Data.AbsorbFunc (AttackerName, WeaponName, damage_withstood)
			except AttributeError: pass


	# personal magical resistance can reduce this damage
	damage_resistance= me.Data.GetResistance(DamageType)
	if damage_resistance != 0.0:
		if PrintFormula==1:
			print "Resistance to "+DamageType+" at "+`damage_resistance`+" changes the effective_damage to "+`effective_damage*(1.0-damage_resistance)`
		effective_damage= effective_damage*(1.0-damage_resistance)
	
	# store the damage type for later processing
	if effective_damage>0:
		me.Data.LastDamageType= DamageType
	
	# special damage e.g. Fire, poison,
	special_damage= 0.0	
	if not (Shielded and effective_damage<=0):
		if weaponData and len (weaponData) > 6:
			for special in weaponData[6:]:
				special_resistance= me.Data.GetResistance(special[0])
				
				if SpecialDamageFuncs.has_key(special[0]):
					special_damage_func= SpecialDamageFuncs[special[0]]
					special_damage= special_damage + special_damage_func (special, special_resistance, effective_damage, VictimName, AttackerName, WeaponName, DamageType, DamageZone, DamageNode, x, y, z, Shielded)
					if PrintFormula==1:
						print "Special damage type "+`special[0]`+" (resisted at "+`special_resistance`+") adds "+`special_damage`+" to effective damage."
				else:
					if PrintFormula==1:
						print "Special damage type "+`special[0]`+" (resisted at "+`special_resistance`+") adds "+`special[1]`+" to effective damage."
					special_damage= special_damage + special[1]*(1.0-special_resistance)
		
		effective_damage= effective_damage + special_damage
	
	if(not Shielded) and (DamageType=="Impale" or DamageType=="Slash") and Bladex.GetBloodLevel()>0:
		me.Data.TakeBleedingImpact= effective_damage
	elif(me.Kind in Blood.DustDeathEntities) and DamageType=="Crush": ### Sparks and dust on crushing damage -LeadHead
		me.Data.TakeBleedingImpact= effective_damage
	else:
		me.Data.TakeBleedingImpact= 0
	
	prevLife=me.Life
	
	if not me.Data.Invincibility:
		Bladex.PlayHaptic(1)
		me.Life= me.Life - effective_damage

	"""
	### Mutilation constants ###
	#       -LeadHead
	# missing head = ( mut & 2 )
	# 
	mut = me.MutilationsMask
	RightFoot= 512
	RightLeg= 256
	LeftFoot= 128
	LeftLeg= 64
	RightHand= 32
	RightArm= 16
	LeftHand= 8
	LeftArm= 4
	Head= 2
	
	RArm = RightArm | RightHand
	LArm = LeftArm | LeftHand
	RLeg = RightLeg | RightFoot
	LLeg = LeftLeg | LeftFoot   
	
	CanMutilate = 1
    
	if effective_damage>0:
		if me.MeshName == "Great_Ork":
			print `me.Name` + " is a Great Ork"
			RArm = Head | RightArm | RightHand
		
		if (DamageZone == (Reference.BODY_FRONT or Reference.BODY_BACK)):
			CanMutilate = 0
		if (DamageZone == (Reference.BODY_RARM or Reference.BODY_RHAND)) and (mut & RArm):
			CanMutilate = 0
			print "Mutilation blocked due to Right Arm"
		elif (DamageZone == (Reference.BODY_LARM or Reference.BODY_LHAND)) and (mut & LArm):
			CanMutilate = 0
			print "Mutilation blocked due to Left Arm"
		elif (DamageZone == (Reference.BODY_RLEG or Reference.BODY_RFOOT)) and (mut & RLeg):
			CanMutilate = 0
			print "Mutilation blocked due to Right Leg"
		elif (DamageZone == (Reference.BODY_LLEG or Reference.BODY_LFOOT)) and (mut & LLeg):
			CanMutilate = 0
			print "Mutilation blocked due to Left Leg"

		me.Data.Mutilate=  me.Life <= 0 and (DamageType=="Slash" or (DamageType=="Crush" and me.Kind=="Skeleton")) and CanMutilate ### Skeletons now can be mutilated by crushing damage -LeadHead
		"""
			
	if effective_damage>0:
		me.Data.Mutilate=  me.Life <= 0 and (DamageType=="Slash" or (DamageType=="Crush" and me.Kind=="Skeleton")) ### Skeletons now can be mutilated by crushing damage -LeadHead
	else:
		me.Data.Mutilate= 0
		if not Shielded:
			effective_damage=1.0
			
	if thrown_flag==1:
		try:
			if me.Data.Respond2Thrown:
				me.Data.Respond2Thrown(me.Name,AttackerName)
		except AttributeError: pass

	me.Data.RespondToHit(me.Name, AttackerName, effective_damage, DamageType, DamageZone, Shielded)
	
	if PlayerHitFunc !="":
		PlayerHitFunc( VictimName, AttackerName, me.Life, prevLife)

	if me.Life <= 0.0:
		if (AttackerName):
			attacker=Bladex.GetEntity(AttackerName)
			if attacker and attacker.InDestructorAttack==1 and effective_damage>1:
				try:
					if victimsShieldName:
						victimsShield= Bladex.GetEntity(victimsShieldName)
						if victimsShield and victimsShield.Data.brkobjdata:
							BreakMyShield(me.Name)
				except:
					pass
				try:
					if victimsWeaponName:
						victimsWeapon= Bladex.GetEntity(victimsWeaponName)
						if victimsWeapon and victimsWeaponName.Data.brkobjdata:
							BreakMySword(me.Name)
				except:
					pass
			if (prevLife>0) and (netgame.GetNetState() == 0):
				AttackerEntity=Bladex.GetEntity(AttackerName)
				if AttackerEntity:
					AttackerEntity.Data.OnKilledEnemy(VictimName)

	# Sticking to player
	# Check type of weapon
	if thrown_flag and weapon.Arrow:
		weapon.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
		weapon.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
		weapon.Stop(x, y, z)
		# Check type of damage
		if me and (not me.Data.Mutilate) and DamageNode!=-1 and DamageZone!=Reference.BODY_HEAD and me.Life>0.0:
			# print "DamageNode is" +`DamageNode`+ ". DamageZone is" +`DamageZone`
			me.LinkToNode(weapon, DamageNode)
			sticktime= (3.0)/weapon.Mass
			# print "object "+weapon.Name+" of kind "+weapon.Kind+" of mass "+`weapon.Mass`+" sticking for "+`sticktime`+" seconds"
			Bladex.AddScheduledFunc (Bladex.GetTime()+sticktime, StuckWeaponFall, (weapon.Name, VictimName), weapon.Name+"_StuckWeaponFall")
			if weapon.StickFunc:
				weapon.StickFunc (weapon.Name, me.Name)
		else:
			weapon.Impulse (0.0,1.0,0.0)
			
	if me.Data.Mutilate:
		if PrintFormula==1:
			print "Mutilation"
	if Bladex.GetMutilationLevel()==0 or me.Kind[:5]=="Golem":
		return 0
	else:
		return me.Data.Mutilate	
