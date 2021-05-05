
import pandas as pd
from tkinter import *
from random import *
from dearpygui.core import *
from dearpygui.simple import *

# data
names = ['Abaddon', 'Alchemist', 'Ancient Apparition', 'Anti-Mage', 'Arc Warden', 'Axe',
         'Bane', 'Batrider', 'Beastmaster', 'Bloodseeker', 'Bounty Hunter', 'Brewmaster', 'Bristleback', 'Broodmother',
         'Centaur Warrunner', 'Chaos Knight', 'Chen', 'Clinkz', 'Clockwerk', 'Crystal Maiden',
         'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Doom', 'Dragon Knight', 'Drow Ranger',
         'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Ember Spirit', 'Enchantress', 'Enigma',
         'Faceless Void', 'Grimstroke', 'Gyrocopter', 'Hoodwink', 'Huskar', 'Invoker', 'Io', 'Jakiro', 'Juggernaut',
         'Keeper of the Light', 'Kunkka',
         'Legion Commander', 'Leshrac', 'Lifestealer', 'Lich', 'Lina', 'Lion', 'Lone Druid', 'Luna', 'Lycan',
         'Magnus', 'Mars', 'Medusa', 'Meepo', 'Mirana', 'Monkey King', 'Morphling',
         'Naga Siren', 'Nature\'s Prophet', 'Necophos', 'Night Stalker', 'Nyx Assassin',
         'Ogre Magi', 'Omniknight', 'Oracle', 'Outworld Destroyer',
         'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Phoenix', 'Puck', 'Pudge', 'Pugna',
         'Queen of Pain', 'Razor', 'Riki', 'Rubick',
         'Sand King', 'Shadow Demon', 'Shadow Fiend', 'Shadow Shamen', 'Silencer', 'Slardar', 'Slark', 'Snapfire',
         'Sniper', 'Spectre', 'Spirit Breaker', 'Storm Spirit', 'Sven',
         'Techies', 'Terrorblade', 'Tidehunter', 'Timbersaw', 'Tinker', 'Tiny', 'Treant Protector', 'Troll Warlord',
         'Tusk',
         'Ursa', 'Underlord', 'Undying', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Visage', 'Void Spirit',
         'Warlock', 'Weaver', 'Windranger', 'Winter Wyvern', 'Witch Doctor', 'Wraith King', 'Zeus']

# melee is true ranged is false
melee = [True, True, False, True, False, True, False, False, True, True, True, True, True, True, True, True, False,
         False, True, False, True, False, False, False, False, True, True, False, True, True, True, True, False, False,
         True, False, False, False, False, False, False, False, True, False, True, True, False, True, False, False,
         False, False, False, True, True, True, True, False, False, True, False, True, False, False, True, True, True,
         True, False, False, True, True, True, False, False, True, False, False, False, True, False, True, True, True,
         False, False, True, True, False, False, True, True, False, True, False, True, True, True, False, True, True,
         True, True, True, True, True, False, False, False, False, True, False, False, False, False, False, True, False]

att = ['str', 'str', 'int', 'agi', 'agi', 'str', 'int', 'int', 'str', 'agi', 'agi', 'str', 'str', 'agi', 'str', 'str',
       'int', 'agi', 'str', 'int', 'int', 'int', 'int', 'int', 'int', 'str', 'str', 'agi', 'str', 'str', 'str', 'agi',
       'int', 'int', 'agi', 'int', 'agi', 'agi', 'str', 'int', 'str', 'int', 'agi', 'int', 'str', 'str', 'int', 'str',
       'int', 'int', 'int', 'agi', 'agi', 'str', 'str', 'str', 'agi', 'agi', 'agi', 'agi', 'agi', 'agi', 'int', 'int',
       'str', 'agi', 'int', 'str', 'int', 'int', 'agi', 'agi', 'agi', 'str', 'int', 'str', 'int', 'int', 'agi', 'agi',
       'int', 'str', 'int', 'agi', 'int', 'int', 'str', 'agi', 'str', 'agi', 'agi', 'str', 'int', 'str', 'int', 'agi',
       'str', 'str', 'int', 'str', 'str', 'agi', 'str', 'agi', 'str', 'str', 'agi', 'agi', 'agi', 'int', 'int', 'int',
       'agi', 'int', 'int', 'int', 'str', 'int']

com = ['*', '*', '**', '*', '***', '*', '**', '**', '**', '*', '*', '***', '*', '**', '*', '*', '***', '**', '**', '*',
       '*', '**', '*', '*', '**', '**', '*', '*', '***', '**', '**', '**', '**',
       '**', '**', '**', '*', '**', '*', '***', '***', '*', '*', '**', '**', '*', '*', '**', '*', '*', '*', '***', '*',
       '**', '**', '*', '*', '***', '**', '**', '***', '**', '**', '*', '*',
       '**', '*', '*', '***', '**', '**', '*', '**', '**', '**', '**', '***', '**', '*', '*', '***', '**', '**', '**',
       '*', '**', '*', '**', '*', '*', '**', '*', '**', '*', '**', '**', '*',
       '**', '**', '**', '**', '**', '*', '*', '**', '*', '*', '*', '*', '***', '**', '*', '**', '**', '**', '*', '*',
       '*']

img = ['dota heroes/Abaddon.png', 'dota heroes/Alchemist.png', 'dota heroes/Ancient Apparition.png',
       'dota heroes/Anti-Mage.png', 'dota heroes/Arc Warden.png', 'dota heroes/Axe.png', 'dota heroes/Bane.png',
       'dota heroes/Batrider.png', 'dota heroes/Beastmaster.png', 'dota heroes/Bloodseeker.png',
       'dota heroes/Bounty Hunter.png', 'dota heroes/Brewmaster.png', 'dota heroes/Bristleback.png',
       'dota heroes/Broodmother.png', 'dota heroes/Centaur Warrunner.png', 'dota heroes/Chaos Knight.png',
       'dota heroes/Chen.png', 'dota heroes/Clinkz.png', 'dota heroes/Clockwerk.png', 'dota heroes/Crystal Maiden.png',
       'dota heroes/Dark Seer.png', 'dota heroes/Dark Willow.png', 'dota heroes/Dazzle.png',
       'dota heroes/Death Prophet.png', 'dota heroes/Disruptor.png', 'dota heroes/Doom.png',
       'dota heroes/Dragon Knight.png', 'dota heroes/Drow Ranger.png', 'dota heroes/Earth Spirit.png',
       'dota heroes/Earthshaker.png', 'dota heroes/Elder Titan.png', 'dota heroes/Ember Spirit.png',
       'dota heroes/Enchantress.png', 'dota heroes/Enigma.png', 'dota heroes/Faceless Void.png',
       'dota heroes/Grimstroke.png', 'dota heroes/Gyrocopter.png', 'dota heroes/Hoodwink.png',
       'dota heroes/Huskar.png', 'dota heroes/Invoker.png', 'dota heroes/Io.png', 'dota heroes/Jakiro.png',
       'dota heroes/Juggernaut.png', 'dota heroes/Keeper of the Light.png', 'dota heroes/Kunkka.png',
       'dota heroes/Legion Commander.png', 'dota heroes/Leshrac.png', 'dota heroes/Lifestealer.png',
       'dota heroes/Lich.png', 'dota heroes/Lina.png', 'dota heroes/Lion.png', 'dota heroes/Lone Druid.png',
       'dota heroes/Luna.png', 'dota heroes/Lycan.png', 'dota heroes/Magnus.png', 'dota heroes/Mars.png',
       'dota heroes/Medusa.png', 'dota heroes/Meepo.png', 'dota heroes/Mirana.png', 'dota heroes/Monkey King.png',
       'dota heroes/Morphling.png', 'dota heroes/Naga Siren.png', "dota heroes/Nature's Prophet.png",
       'dota heroes/Necophos.png', 'dota heroes/Night Stalker.png', 'dota heroes/Nyx Assassin.png',
       'dota heroes/Ogre Magi.png', 'dota heroes/Omniknight.png', 'dota heroes/Oracle.png',
       'dota heroes/Outworld Destroyer.png', 'dota heroes/Pangolier.png', 'dota heroes/Phantom Assassin.png',
       'dota heroes/Phantom Lancer.png', 'dota heroes/Phoenix.png', 'dota heroes/Puck.png', 'dota heroes/Pudge.png',
       'dota heroes/Pugna.png', 'dota heroes/Queen of Pain.png', 'dota heroes/Razor.png', 'dota heroes/Riki.png',
       'dota heroes/Rubick.png', 'dota heroes/Sand King.png', 'dota heroes/Shadow Demon.png',
       'dota heroes/Shadow Fiend.png', 'dota heroes/Shadow Shamen.png', 'dota heroes/Silencer.png',
       'dota heroes/Slardar.png', 'dota heroes/Slark.png', 'dota heroes/Snapfire.png', 'dota heroes/Sniper.png',
       'dota heroes/Spectre.png', 'dota heroes/Spirit Breaker.png', 'dota heroes/Storm Spirit.png',
       'dota heroes/Sven.png', 'dota heroes/Techies.png', 'dota heroes/Terrorblade.png', 'dota heroes/Tidehunter.png',
       'dota heroes/Timbersaw.png', 'dota heroes/Tinker.png', 'dota heroes/Tiny.png',
       'dota heroes/Treant Protector.png', 'dota heroes/Troll Warlord.png', 'dota heroes/Tusk.png',
       'dota heroes/Ursa.png', 'dota heroes/Underlord.png', 'dota heroes/Undying.png',
       'dota heroes/Vengeful Spirit.png', 'dota heroes/Venomancer.png', 'dota heroes/Viper.png',
       'dota heroes/Visage.png', 'dota heroes/Void Spirit.png', 'dota heroes/Warlock.png',
       'dota heroes/Weaver.png', 'dota heroes/Windranger.png', 'dota heroes/Winter Wyvern.png',
       'dota heroes/Witch Doctor.png', 'dota heroes/Wraith King.png', 'dota heroes/Zeus.png']


soundByte = ['dota heroesS/dota heroes/Abaddon.mp3', 'dota heroesS/dota heroes/Alchemist.mp3',
             'dota heroesS/dota heroes/Ancient Apparition.mp3', 'dota heroesS/dota heroes/Anti-Mage.mp3',
             'dota heroesS/dota heroes/Arc Warden.mp3', 'dota heroesS/dota heroes/Axe.mp3',
             'dota heroesS/dota heroes/Bane.mp3', 'dota heroesS/dota heroes/Batrider.mp3',
             'dota heroesS/dota heroes/Beastmaster.mp3', 'dota heroesS/dota heroes/Bloodseeker.mp3',
             'dota heroesS/dota heroes/Bounty Hunter.mp3', 'dota heroesS/dota heroes/Brewmaster.mp3',
             'dota heroesS/dota heroes/Bristleback.mp3', 'dota heroesS/dota heroes/Broodmother.mp3',
             'dota heroesS/dota heroes/Centaur Warrunner.mp3', 'dota heroesS/dota heroes/Chaos Knight.mp3',
             'dota heroesS/dota heroes/Chen.mp3', 'dota heroesS/dota heroes/Clinkz.mp3',
             'dota heroesS/dota heroes/Clockwerk.mp3', 'dota heroesS/dota heroes/Crystal Maiden.mp3',
             'dota heroesS/dota heroes/Dark Seer.mp3', 'dota heroesS/dota heroes/Dark Willow.mp3',
             'dota heroesS/dota heroes/Dazzle.mp3', 'dota heroesS/dota heroes/Death Prophet.mp3',
             'dota heroesS/dota heroes/Disruptor.mp3', 'dota heroesS/dota heroes/Doom.mp3',
             'dota heroesS/dota heroes/Dragon Knight.mp3', 'dota heroesS/dota heroes/Drow Ranger.mp3',
             'dota heroesS/dota heroes/Earth Spirit.mp3', 'dota heroesS/dota heroes/Earthshaker.mp3',
             'dota heroesS/dota heroes/Elder Titan.mp3', 'dota heroesS/dota heroes/Ember Spirit.mp3',
             'dota heroesS/dota heroes/Enchantress.mp3', 'dota heroesS/dota heroes/Enigma.mp3',
             'dota heroesS/dota heroes/Faceless Void.mp3', 'dota heroesS/dota heroes/Grimstroke.mp3',
             'dota heroesS/dota heroes/Gyrocopter.mp3', 'dota heroesS/dota heroes/Hoodwink.mp3',
             'dota heroesS/dota heroes/Huskar.mp3', 'dota heroesS/dota heroes/Invoker.mp3',
             'dota heroesS/dota heroes/Io.mp3', 'dota heroesS/dota heroes/Jakiro.mp3',
             'dota heroesS/dota heroes/Juggernaut.mp3', 'dota heroesS/dota heroes/Keeper of the Light.mp3',
             'dota heroesS/dota heroes/Kunkka.mp3', 'dota heroesS/dota heroes/Legion Commander.mp3',
             'dota heroesS/dota heroes/Leshrac.mp3', 'dota heroesS/dota heroes/Lifestealer.mp3',
             'dota heroesS/dota heroes/Lich.mp3', 'dota heroesS/dota heroes/Lina.mp3',
             'dota heroesS/dota heroes/Lion.mp3', 'dota heroesS/dota heroes/Lone Druid.mp3',
             'dota heroesS/dota heroes/Luna.mp3', 'dota heroesS/dota heroes/Lycan.mp3',
             'dota heroesS/dota heroes/Magnus.mp3', 'dota heroesS/dota heroes/Mars.mp3',
             'dota heroesS/dota heroes/Medusa.mp3', 'dota heroesS/dota heroes/Meepo.mp3',
             'dota heroesS/dota heroes/Mirana.mp3', 'dota heroesS/dota heroes/Monkey King.mp3',
             'dota heroesS/dota heroes/Morphling.mp3', 'dota heroesS/dota heroes/Naga Siren.mp3',
             "dota heroesS/dota heroes/Nature's Prophet.mp3", 'dota heroesS/dota heroes/Necophos.mp3',
             'dota heroesS/dota heroes/Night Stalker.mp3', 'dota heroesS/dota heroes/Nyx Assassin.mp3',
             'dota heroesS/dota heroes/Ogre Magi.mp3', 'dota heroesS/dota heroes/Omniknight.mp3',
             'dota heroesS/dota heroes/Oracle.mp3', 'dota heroesS/dota heroes/Outworld Destroyer.mp3',
             'dota heroesS/dota heroes/Pangolier.mp3', 'dota heroesS/dota heroes/Phantom Assassin.mp3',
             'dota heroesS/dota heroes/Phantom Lancer.mp3', 'dota heroesS/dota heroes/Phoenix.mp3',
             'dota heroesS/dota heroes/Puck.mp3', 'dota heroesS/dota heroes/Pudge.mp3',
             'dota heroesS/dota heroes/Pugna.mp3', 'dota heroesS/dota heroes/Queen of Pain.mp3',
             'dota heroesS/dota heroes/Razor.mp3', 'dota heroesS/dota heroes/Riki.mp3',
             'dota heroesS/dota heroes/Rubick.mp3', 'dota heroesS/dota heroes/Sand King.mp3',
             'dota heroesS/dota heroes/Shadow Demon.mp3', 'dota heroesS/dota heroes/Shadow Fiend.mp3',
             'dota heroesS/dota heroes/Shadow Shamen.mp3', 'dota heroesS/dota heroes/Silencer.mp3',
             'dota heroesS/dota heroes/Slardar.mp3', 'dota heroesS/dota heroes/Slark.mp3',
             'dota heroesS/dota heroes/Snapfire.mp3', 'dota heroesS/dota heroes/Sniper.mp3',
             'dota heroesS/dota heroes/Spectre.mp3', 'dota heroesS/dota heroes/Spirit Breaker.mp3',
             'dota heroesS/dota heroes/Storm Spirit.mp3', 'dota heroesS/dota heroes/Sven.mp3',
             'dota heroesS/dota heroes/Techies.mp3', 'dota heroesS/dota heroes/Terrorblade.mp3',
             'dota heroesS/dota heroes/Tidehunter.mp3', 'dota heroesS/dota heroes/Timbersaw.mp3',
             'dota heroesS/dota heroes/Tinker.mp3', 'dota heroesS/dota heroes/Tiny.mp3',
             'dota heroesS/dota heroes/Treant Protector.mp3', 'dota heroesS/dota heroes/Troll Warlord.mp3',
             'dota heroesS/dota heroes/Tusk.mp3', 'dota heroesS/dota heroes/Ursa.mp3',
             'dota heroesS/dota heroes/Underlord.mp3', 'dota heroesS/dota heroes/Undying.mp3',
             'dota heroesS/dota heroes/Vengeful Spirit.mp3', 'dota heroesS/dota heroes/Venomancer.mp3',
             'dota heroesS/dota heroes/Viper.mp3', 'dota heroesS/dota heroes/Visage.mp3',
             'dota heroesS/dota heroes/Void Spirit.mp3', 'dota heroesS/dota heroes/Warlock.mp3',
             'dota heroesS/dota heroes/Weaver.mp3', 'dota heroesS/dota heroes/Windranger.mp3',
             'dota heroesS/dota heroes/Winter Wyvern.mp3', 'dota heroesS/dota heroes/Witch Doctor.mp3',
             'dota heroesS/dota heroes/Wraith King.mp3', 'dota heroesS/dota heroes/Zeus.mp3']


heroDict = {'names': names,
            'melee/ranged': melee,
            'Attribute': att,
            'Complexity': com,
            'image': img,
            'soundByte': soundByte}

heroDF = pd.DataFrame(heroDict)

heroDF.index = names

#change to True to use trait
#to be changed for gui
mrValue = False
attValue = False
comValue = False

if mrValue == True :
    cond = heroDF.loc[:, 'melee/ranged']
    x = cond == True

if attValue == True :
    cond = heroDF.loc[:, 'Attribute']
    x = cond == 'int'

if comValue == True :
    cond = heroDF.loc[:, 'Complexity']
    x = cond == '***'

result = heroDF[x]

randNum = randrange(len(result))

hero = result['names'][randNum]
print(hero)
#print(len(att))

#heroesGraph = pd.DataFrame(randDic)

#use to change or add new data
#temp = []

#for value in soundByte :
 #   print(value)
  #  inText = "dota heroes/"
   # temp.append(inText + value)


