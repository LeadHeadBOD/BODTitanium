##///
##||| Combos/PanelFillerCommon.PY TITANIUM
##||| Change list:
##||| * v109 code merged with HD update code
##||| * Dwarf's "Biting Axe" and "Killer Axe" should now report correctly in Travelbook
##||| * Dwarf's "Sharp Axe" and "War Axe" should now report corretly in Travelbook
##\\\ 

import Language
import Raster
import BUIx
import ScorerWidgets
import MenuText
import Bladex
import os
import Reference
import string
import sys

amzIndexString = ["Bo", "Bichero", "Lanza", "Naginata", "Tridente", "Axpear", "DeathBo", "Crosspear", "Hachacuchilla", "CrushBo", "Arpon", "Naginata2", "LanzaAncha"]
barbIndexString = ["Chaosword", "Eclipse", "DeathSword", "Guadanya", "LongSword", "Alfanje", "Hacha2hojas", "FlatSword", "BigSword", "RhinoClub", "Hacharrajada", "SawSword"]
dwfIndexString = ["Garrote", "Hacha", "Hacha5", "Garropin", "Hacha4", "Hacha3", "Martillo", "Martillo2", "Garrote2", "MazaDoble", "Hacha6", "Hacha2", "Martillo3"]
kgtIndexString = ["Gladius", "Maza", "Espadaromana", "Espadaelfica", "Maza2", "HookSword", "Espadacurva", "Dagesse", "Cimitarra", "Maza3", "DoubleSword", "Espadafilo", "Espada"]

specialAmzIndexString = ["QueenSword", "IceWand", "SteelFeather", "FireBo", "BladeSword"]
specialBarbIndexString = ["QueenSword", "FireBigSword", "IceAxe", "BladeSword"]
specialDwfIndexString = ["QueenSword", "IceHammer", "CrushHammer", "FireAxe", "BladeSword"]
specialKgtIndexString = ["QueenSword", "FireSword", "IceSword", "BladeSword"]

buttonOffset = [0.07, 0] # center
buttonTextPosition = [0.32, 0.746]

relative = BUIx.B_FrameWidget.B_FR_HRelative
relativev = BUIx.B_FrameWidget.B_FR_VRelative
center = BUIx.B_FrameWidget.B_FR_HCenter
bottom = BUIx.B_FrameWidget.B_FR_Bottom
right = BUIx.B_FrameWidget.B_FR_Right
left = BUIx.B_FrameWidget.B_FR_Left

scaledCenteredSizeFactor = Raster.GetScaledCenteredSizeFactor()

def CheckButtonOffset(index, position):
	if index > 3:
		return position + 0.007
	return position

def CheckBarbRightLevelOffset(index, position):
	if index > 5:
		return position + 0.02
	return position

def GetLanguageFallback():
	char = Bladex.GetEntity("Player1")
	language = Language.Current
	if language == "EnglishUS":
		language = "English"
	return language

def SetParentScale(parent):
	Size_X, Size_Y = Raster.GetUnscaledSize()
	parent.SetSize(Size_X, Size_Y)

def CheckFontChineseFallback(elem):
	font = Language.LetrasMenuBig
	if elem == "Button":
		font = Language.LetrasMenuBig
	# if Language.Current == "Chinese":
	# 	font = Language.LetrasPanel
	# 	if elem == "Button":
	# 		font = Language.LetrasPanelButton
	return font

def CorrectPosX(x):
	Size_X, Size_Y = Raster.GetUnscaledSize()
	original_ratio = 1080.0 / 1920.0
	ratio = Size_Y / (1.0 * Size_X)
	scale = original_ratio / ratio
	return ((x - 0.5) / scale + 0.5) * scaledCenteredSizeFactor - ((scaledCenteredSizeFactor - 1) * 0.50)

def CorrectPosY(y):
	return y * scaledCenteredSizeFactor - ((scaledCenteredSizeFactor - 1 ) * 0.50)

def InitWidget(parent, name, text, font, elem, alignment = BUIx.B_TextWidget.B_TEXT_Left, color = [255, 255, 255], scale = 1, max_width = 0):
	Size_X, Size_Y = Raster.GetUnscaledSize()
	y_scale = (Size_Y / 1080.0) * scaledCenteredSizeFactor * scale
	Widget=BUIx.B_TextWidget(parent, name,"",ScorerWidgets.font_server,font)
	parent.PanelWidgets.append(Widget)
	parent.PanelWidgetsName.append(name)
	Widget.SetJustification(alignment)
	Widget.SetAlpha(1)
	Widget.SetColor(color[0],color[1],color[2])
	# Widget.SetMaximumWidth(max_width * y_scale / scale)   # Leads to a C function which probably doesn't exist in v109 -LeadHead

	if Language.Current == "Chinese" and elem != "Combo" and elem != "Combo2":
		y_scale = y_scale * 1.3

	Widget.SetScale(0.55 * y_scale)

	if elem == "Button":
		Widget.SetScale(0.61 * y_scale)
	elif elem == "Combo" or elem == "Combo2":
		Widget.SetScale(0.9 * y_scale)
	elif elem == "Title" and len(text) >= 30:
		Widget.SetScale(0.5 * y_scale)
	Widget.SetText(MenuText.GetMenuText(text))

	return Widget

def UpperCase( String ):

	String    = string.upper(String)
	StringLen = len( String )
	Index     = 0
	Result    = ''


	while Index < StringLen:

		Char = String[Index]

		if Char >= 'A' and Char <= 'Z':
			Result = Result + Char
		elif Char in 'àáâãäåÀÁÂÃÄÅ':
			Result = Result + 'A'
		elif Char in 'ç¢Ç':
			Result = Result + 'C'
		elif Char in 'èéêëÈÉÊË':
			Result = Result + 'E'
		elif Char in 'ìíîïÌÍÎÏ':
			Result = Result + 'I'
		elif Char in 'ñ':
			Result = Result + 'N'
		elif Char in 'ùúûüÙÚÛÜ':
			Result = Result + 'U'
		elif Char in 'ýÿÝ':
			Result = Result + 'Y'
		elif Char in 'Ð':
			Result = Result + 'D'
		elif Char in 'òóôõöÒÓÔÕÖ':
			Result = Result + 'O'
		else:
			Result = Result + Char
		Index = Index + 1

	return Result

def GetWeaponStringList(indexString, weaponString):
	titles = []
	for elem in indexString:
		weapon = Reference.DefaultSelectionData[elem][2]
		if GetLanguageFallback() != "Chinese":
			if GetLanguageFallback()=="Russian":
				weapon = Bladex.GetUpperCaseRussian(weapon)
			else:
				weapon =  UpperCase(Reference.DefaultSelectionData[elem][2])
		titles.append(weaponString + weapon)
	return titles

def GetAmzTitle(weaponString=""):
	return GetWeaponStringList(amzIndexString, weaponString)

def GetBarbTitle(weaponString=""):
	return GetWeaponStringList(barbIndexString, weaponString)

def GetDwfTitle(weaponString=""):
	return GetWeaponStringList(dwfIndexString, weaponString)

def GetKgtTitle(weaponString=""):
	return GetWeaponStringList(kgtIndexString, weaponString)

def GetSpecialAmzTitle(weaponString=""):
	return GetWeaponStringList(specialAmzIndexString, weaponString)

def GetSpecialBarbTitle(weaponString=""):
	return GetWeaponStringList(specialBarbIndexString, weaponString)

def GetSpecialDwfTitle(weaponString=""):
	return GetWeaponStringList(specialDwfIndexString, weaponString)

def GetSpecialKgtTitle(weaponString=""):
	return GetWeaponStringList(specialKgtIndexString, weaponString)

def GetEmptyData():
	return {
			 "English": 
					{
					 "Amazon_N": {},
					 "Dwarf_N": {},
					 "Knight_N": {},
					 "Barbarian_N": {}
					},
			 "French": 
					{
						"Amazon_N": {},
						"Dwarf_N": {},
						"Knight_N": {},
						"Barbarian_N": {}
					},
			 "Italian": 
					{
						"Amazon_N": {},
						"Dwarf_N": {},
						"Knight_N": {},
						"Barbarian_N": {}
					},
			 "German": 
					{
						"Amazon_N": {},
						"Dwarf_N": {},
						"Knight_N": {},
						"Barbarian_N": {}
					},
			 "Spanish": 
					{
						"Amazon_N": {},
						"Dwarf_N": {},
						"Knight_N": {},
						"Barbarian_N": {}
					},
			 "Russian": 
					{
						"Amazon_N": {},
						"Dwarf_N": {},
						"Knight_N": {},
						"Barbarian_N": {}
					},
			 "Chinese": 
					{
						"Amazon_N": {},
						"Dwarf_N": {},
						"Knight_N": {},
						"Barbarian_N": {}
					}
			}
