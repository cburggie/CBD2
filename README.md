
# DBD2 Mod Pack

Accessable Diablo II end-game content in single player. Works in patch 1.14d

## Installation

1) Copy the `Data` folder and all sub-folders and files to your Diablo II install path (eg. `C:\Program Files (x86)\Diablo II`).

2) Make a copy of your Diablo II shortcut. In the shortcut properties add the
  `-direct` and `-txt` command line switches to the target property of the
  shortcut (eg. `"C:\Program Files (x86)\Diablo II\Diablo II.exe" -direct -txt`).

3) This shortcut will now run the game with the mods active. Your old shortcut
  will run the game without mods.

## Mod Goals

* improve drop rates of high-end gear and runes
* allow access to Annihilus and Hellfire Torch
* reduce the grind to level 99
* improve ability to customize items with cube recipes

## Included Changes

### CharStats.txt

* characters start with full portal and identify books
* characters start with the Horadric Cube
* characters start with a Tal and an Eth rune
* Assassins and Barbarians start with a second weapon instead of a buckler

### Experience.txt

* the leveling slow-down after experience level 70 is no longer as steep

### CubeMain.txt

* all ladder only recipes work in single player
* removed many of the item crafting recipes
* improved some old recipes
* added several recipes
* changes listed below


### Misc.txt

* health potions restore 30/60/120/240/480 hp
* mana potions restore 20/40/80/160/320 hp
* super health and mana potions are sold by vendors in late Nightmare
* small rejuvenation potions are sold by vendors in late Hell (maybe OP)

### Runes.txt

* ladder only runewords available in single player
* all runewords yield best rolls possible

### Set Items.txt

* ladder-only set pieces drop in single player
* set pieces from the same item type have equal rarity
* many important rolls always get best rng (skills, resists, etc)

### TreasureClassEx.txt

* runes drop uniformly among possible rune drops
* The Countess is guarenteed 3 runes up to Sol/Ist/Zod
* Exceptional and Elite items drop more often
* bosses have guaranteed drops and a reason to farm them
* Blood Raven drops a bow
* Griswold drops gold (change to rejuvs? he was a blacksmith tho)
* Countess always drops 3 runesand her key
* Smith drops weapons
* Andariel drops rings and her essence
* Radamant drops skulls
* Summoner drops jewels and his key
* Duriel drops extra weapons and armor and its essence
* Mephisto drops amulets and his essence
* Izual drops gems
* Hephasto drops armor
* Diablo drops extra weapons and armor
* Nilathak drops skulls and his key
* Baal drops charms and his essence

### UniqueItems.txt

* ladder-only uniques drop in single player
* unique items from the same type have equal rarity
* many important rolls always get best rng (skills, resists, etc)

## Cube Recipes

### Runeword Preparation Recipes

* remove sockets, ethereal, rarity: 3 jewels (`ilvl = plvl`)
* make plain item ethereal: Eth rune (`ilvl = plvl`)
* add 2 sockets: 2 perfect gems
* add 3 sockets: 1 flawless + 2 perfect gems
* add 4 sockets: 3 perfect gems
* add 5 sockets: 1 flawless + 3 perfect gems
* add 6 sockets: 4 perfect gems

### Staff of Teleportation Recipe

* magic staff of teleportation: magic staff + magic ring + tome of town portal

### Upgrade Recipes

* gem and rune upgrade recipes only require 2 items of the lower grade
* upgrade basic to exceptional: 3 perfect skulls + 1 magic jewel
* upgrade exceptional to elite: 3 perfect skulls + 1 rare jewel
* +1 socket on rare item: 3 perfect skulls + 1 unique ring

### Reroll Recipes

* reroll magic item: 3 perfect gems (`ilvl = ilvl`)
* reroll rare item: 3 perfect skulls (`ilvl = 0.66*ilvl + 0.66*plvl`)
* reroll for item of same rarity: 3 perfect gems + 1 Zod rune (`ilvl = ilvl`)
* token of absolution: Wirt's Leg + Tome of Identify

### Utility Recipes

* repair and recharge item: 1 Ral rune
* unsocket item: 1 Hel rune + 1 Scroll of Town Portal

### Annihilus and Hellfire Torch

* Annihilus: 1 of each Key
* Hellfire Torch: 1 Annihilus + 1 of each Essence

### Misc. Recipes

* Horadric Staff, Khalim's Will, and Cow Portal recipes unchanged
* +resist jewelry recipes don't need potions
* ring, amulet recycle recipes have `ilvl = plvl` (from `ilvl = 0.75*plvl`)
* arrow and bolt recycle recipes unchanged


## To Do

* somehow remove anni and torch from baal drops (remove him as charms boss?)
* allow replay of cow level somehow (will abandon if it requires hexediting)
* maybe change weapon to armor drop ratio from bosses
* Add treasure classes for class items (amazon bows, necro wands/fetishes, etc)
* have a boss (Griswold?) drop a bunch of them or something

