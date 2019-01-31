
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

### CubeMain.txt

* all ladder only recipes work in single player
* removed many of the item crafting recipes
* improved some old recipes
* added several recipes
* changes listed below

### DifficultyLevels.txt

* improved gambling chances of rare/set/unique to 30%/5%/2.5%
* gambling in Nightmare difficulty can frequently yield Exceptional gear (`p=1%+5%*(ilvl-qlvl)`)
* gambling in Hell difficulty can frequently yield Elite gear (`p=1%+5%*(ilvl-qlvl)`)

### Experience.txt

* the leveling slow-down after experience level 70 is no longer as steep

### MagicPrefixes.txt and MagicSuffixes.txt

* rare affixes are more common

### Misc.txt

* health potions restore 30/60/120/240/480 hp
* mana potions restore 20/40/80/160/320 hp
* super health and mana potions are sold by vendors in late Nightmare
* rejuvenation potions are sold by vendors in late Hell

### MonStats.txt

* capped max resistances at 105% so a wand of lower resist will barely break
a monster's immunities.

### Runes.txt

* ladder only runewords available in single player
* all runewords yield best rolls possible

### Set Items.txt

* ladder-only set pieces drop in single player
* set pieces from the same item type have equal rarity
* many important rolls always get best rng (skills, resists, etc)

### TreasureClassEx.txt

* runes drop uniformly among possible rune drops
* The Countess drops 3 runes up to Sol/Um/Ber
* Exceptional and Elite items drop more often
* Blood Raven drops a bows
* Griswold drops class items
* Smith drops weapons
* Andariel drops up to 1/2/3 rings
* Radamant drops up to 1/2/3 skulls
* Summoner drops up to 1/2/3 charms
* Duriel drops up to 1/2/3 jewels
* Mephisto drops up to 1/2/3 amulets
* Izual drops 1/2/3 flawless gems
* Hephasto drops armor
* Nilathak drops up to 1/2/3 flawless skulls
* keys and essences have 25% drop rate

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

### Charm Recipes

* resistance small charm: small charm + 2 perfect ruby/sapphire/topaz/emerald
* +1 skilltab grand charm: grand charm + unique ring + 1/2/3 flawless gems

### Upgrade Recipes

* gem and rune upgrade recipes only require 2 items of the lower grade
* upgrade basic to exceptional: 3 perfect skulls + 1 magic jewel
* upgrade exceptional to elite: 3 perfect skulls + 1 rare jewel
* reroll a unique and make it ethereal: 3 perfect skulls + Eth rune (`ilvl=ilvl`)
* upgrade an item to unique rarity: Hellfire Torch + Annihilus + The Stone of Jordan (`ilvl=plvl`)
* upgrade an item to set rarity: Hellfire Torch + Annihilus + Zod rune (`ilvl=plvl`)
* Larzuk Quest sockets on magic/rare/set/unique: 3 perfect skulls + 1 unique ring

### Reroll Recipes

* reroll magic item: 3 perfect gems (`ilvl = plvl`)
* reroll rare item: 3 perfect skulls (`ilvl = 0.66*ilvl + 0.66*plvl`)
* 'regenerate' a set/unique item (reroll the item's random stats): 3 perfect gems
* Token of Absolution: Wirt's Leg + Tome of Identify

### Utility Recipes

* repair and recharge item: 1 Ral rune
* unsocket item (keeping gems/jewels/runes): 1 Hel rune + 1 Scroll of Town Portal

### Annihilus and Hellfire Torch

* Annihilus: 1 of each Key
* Hellfire Torch: 1 Annihilus + 1 of each Essence

### Misc. Recipes

* +resist jewelry recipes don't need potions and `ilvl=plvl`
* ring, amulet recycle recipes have `ilvl = plvl` (from `ilvl = 0.75*plvl`)


## To Do

* add class specific crafted item recipes for amulets and circlets (good +skills)
* allow replay of cow level somehow (will abandon if it requires hexediting)



