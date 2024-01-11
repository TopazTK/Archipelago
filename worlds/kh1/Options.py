from dataclasses import dataclass

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions

class StrengthIncrease(Range):
    """
    Number of Strength Increases to Add to the Level Up Rewards
    """
    range_start = 0
    range_end = 100
    default = 24

class DefenseIncrease(Range):
    """
    Number of Defense Increases to Add to the Level Up Rewards
    """
    range_start = 0
    range_end = 100
    default = 24

class HPIncrease(Range):
    """
    Number of HP Increases to Add to the Level Up Rewards
    """
    range_start = 0
    range_end = 100
    default = 23

class APIncrease(Range):
    """
    Number of AP Increases to Add to the Level Up Rewards
    """
    range_start = 0
    range_end = 100
    default = 18

class MPIncrease(Range):
    """
    Number of MP Increases to Add to the Level Up Rewards
    """
    range_start = 0
    range_end = 20
    default = 7

class AccessorySlotIncrease(Range):
    """
    Number of Accessory Slot Increases to Add to the Level Up Rewards
    """
    range_start = 0
    range_end = 6
    default = 1

class ItemSlotIncrease(Range):
    """
    Number of Accessory Slot Increases to Add to the Level Up Rewards
    """
    range_start = 0
    range_end = 5
    default = 3

class Sephiroth(Toggle):
    """
    Toggle whether the win condition should be changed to defeating Sephiroth.
    """
    display_name = "Sephiroth"

class WorldComplete(Toggle):
    """
    Toggle whether the win condition should be placed behind a random world completion.
    This could be that works Chronicles or Secret Report location.  Better for fast games.
    """
    display_name = "World Complete"

class Unknown(Toggle):
    """
    Toggle whether the win condition should be changed to defeating Unknown.
    """
    display_name = "Unknown"

class Atlantica(Toggle):
    """
    Toggle whether Atlantica locations/items should be included.
    """
    display_name = "Atlantica"

@dataclass
class KH1Options(PerGameCommonOptions):
    sephiroth: Sephiroth
    world_complete: WorldComplete
    unknown: Unknown
    atlantica: Atlantica
    strength_increase: StrengthIncrease
    defense_increase: DefenseIncrease
    hp_increase: HPIncrease
    ap_increase: APIncrease
    mp_increase: MPIncrease
    accessory_slot_increase: AccessorySlotIncrease
    item_slot_increase: ItemSlotIncrease
