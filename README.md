
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

### ItemTypes.txt

* items can have the max number of sockets at any ilvl.

### MagicPrefixes.txt and MagicSuffixes.txt

* rare affixes are more common
* charges of amplify damage now appear

### Misc.txt

* health potions restore 30/60/120/240/480 hp
* mana potions restore 20/40/80/160/320 hp
* super health and mana potions are sold by vendors in late Nightmare
* rejuvenation potions are sold by vendors in late Hell

### Missiles.txt

* added entries for reworked Necromancer skill Poison Dagger

### MonStats.txt

* capped max resistances at 105% so a wand of lower resist will barely break
a monster's immunities.

### Runes.txt

* ladder only runewords available in single player
* all runewords yield best rolls possible

### SetItems.txt

* ladder-only set pieces drop in single player
* set pieces from the same item type have equal rarity
* many important rolls always get best rng (skills, resists, etc)

### SkillDesc.txt

* updates to in game description of some changed skills

### Skills.txt

* made changes to several skills in attempt to make more character builds viable

### States.txt

* added passive states for updates skills

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

* remove sockets, ethereal, rarity: Token of Absolution (`ilvl = plvl`)
* make plain item ethereal: Eth rune (`ilvl = plvl`)
* add 2 sockets: 2 rings
* add 3 sockets: 2 rings + 1 amulet
* add 4 sockets: 3 rings
* add 5 sockets: 3 rings + 1 amulet
* add 6 sockets: 4 rings

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


## Skill Changes

### Amazon

* Magic Arrow damage improved and synergizes with fire and cold bow skills
* fire bow skill damage improved, give passive fire mastery and pierce
* fold bow skill damage improved, give passive cold mastery and pierce
* poison javalin skills give poison pierce

### Assassin

* Fists of Fire gives passive fire mastery and pierce
* Blades of Ice gives passive cold mastery and pierce
* Claws of Thunder gives passive lightning mastery and pierce
* Venom gives passive poison mastery and pierce

### Barbarian

* Battle Cry lowers enemy physical resistance equal to the damage drop
* War Cry does more physical damage (similar to Druid's Tornado)


### Druid

* Fire Claws gives passive fire mastery and pierce
* Poison Creeper gives passive poison mastery and pierce
* Werewolf and Werebear can now cast Druid Fire skills and many out of class buffs and melee skills

### Necromancer

* Teeth can hit an enemy multiple times
* Poison Dagger now launches a magical dagger leaving a trail of poison clouds
* Poison Dagger gives passive bonus to knife AR and damage
* poison skills all give passive poison mastery and pierce

### Paladin

* Resist Fire/Cold/Lightning give passive element pierce
* Salvation gives passive Fire/Cold/Lightning/Poison pierce
* Conviction affects enemy poison resistance

### Sorceress

* Fire Mastery also gives passive fire pierce
* Lightning Mastery also gives passive lightning pierce
* Energy Shield now synergizes with itself instead of Telekinesis
* Chain Lightning has higher base damage


## To Do

* add class specific crafted item recipes for amulets and circlets (good +skills)
* allow replay of cow level somehow (can be done with cairn stone missiles, but messy)



