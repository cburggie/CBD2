
# DBD2 Mod Pack

Accessable Diablo II end-game content in single player. Works in patch 1.14d

## Installation

1) Copy the `Data` folder and all sub-folders and files to `C:\Program Files (x86)\Diablo II`.

2) Make a copy of your Diablo II shortcut. Right click your new Diablo II shortcut and add the `-direct` and `-txt` switches the `target` field. It should now look like `"C:\Program Files (x86)\Diablo II\Diablo II.exe" -direct -txt`.

## Mod Goals

* improve drop rates of high-end runes and uniques so they are no longer
  astronomically small
* allow access to Annihilus and Hellfire Torch
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
* normal item socketing recipes never adds only one socket (except to items with
  a max of one socket)
* added several recipes (listed below)


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
* bosses always drop from some treasure classes
* keys and essences always drop from their respective bosses
* gave most bosses a reason to be farmed
* Blood Raven drops a bow
* Griswold drops gold (probably wants a buff)
* Countess always drops 3 runes (and better ones than usual) (and her key)
* Smith drops weapons
* Andariel drops rings (and her essence)
* Radamant drops skulls
* Summoner drops jewels (and his key)
* Duriel drops extra weapons and armor (and its essence)
* Mephisto drops amulets (and his essence)
* Izual drops gems
* Hephasto drops armor
* Diablo drops extra weapons and armor
* Nilathak drops skulls (and his key)
* Baal drops charms (and his essence)

### UniqueItems.txt

* ladder-only uniques drop in single player
* unique items from the same type have equal rarity
* many important rolls always get best rng (skills, resists, etc)

## New Recipes

### Socketing Preparation Recipes

* Eld + jewel + any weapon -> normal, unsocketed weapon of same type
* El + jewel + any armor -> normal, unsocketed armor of same type
* Eth + normal, unsocketed weapon or armor -> ethereal item of same type

### Upgrade Recipes

* gem and rune upgrade recipes only require 2 items of the lower grade
* Ral + Sol + perfect emerald + basic weapon -> exceptional weapon (works for
  items of any rarity)
* Tal + Shael + perfect diamond + basic armor -> exceptional armor (works for
  items of any rarity)
* Lum + Pul + perfect emerald + exceptional weapon -> elite weapon (works for
  items of any rarity)
* Ko + Lem + perfect diamond + exceptional armor -> elite armor (works for
  items of any rarity)

### Reroll Recipes

* Zod + 3 perfect gems + rare, set, or unique item -> new item of same type and
  rarity (maybe change to different runes or different gem counts)

### ANnihilus and Hellfire Torch

* 3 Keys -> Annihilus
* 4 Essences + Annihilus -> Hellfire Torch

### Misc. Recipe Changes

* small rejuv potion recipe does not need a gem.
* rare socket recipe can use any ring (no longer just SoJ)
* repair recipes also recharge and work on ethereal items
* old repair and recharge recipes removed
* removed pandemonium quest recipes

## To Do

* allow replay of cow level somehow (give a boss a 'Cow Portal' drop?)
* maybe change weapon to armor drop ratio from bosses
* implement rarity upgrade recipe
* nerf the change to the rare socket recipe to a unique ring (from any ring)

