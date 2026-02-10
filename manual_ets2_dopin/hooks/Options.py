# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value


class AmountOfTokensNeeded(Range):
    """Amount of Delivery Tokens needed to win. Please take in consideration that if you select a high number of Tokens without any of the other options, the majority of items will be progression items."""
    display_name = "Amount of Delivery Tokens needed to win"
    range_start = 10
    range_end = 50
    default = 20

class DLC_GoingEast(Toggle):
    """Enables Going East DLC content."""
    display_name = "DLC: Going East"
    default = 0

class DLC_Scandinavia(Toggle):
    """Enables Scandinavia DLC content."""
    display_name = "DLC: Scandinavia"
    default = 0

class DLC_France(Toggle):
    """Enables Vive la France ! DLC content."""
    display_name = "DLC: France"
    default = 0

class DLC_Italia(Toggle):
    """Enables Vive la France ! DLC content."""
    display_name = "DLC: Italia"
    default = 0

class DLC_BalticSea(Toggle):
    """Enables Beyond the Baltic Sea DLC content."""
    display_name = "DLC: Baltic Sea"
    default = 0

class DLC_BlackSea(Toggle):
    """Enables Road to the Black Sea DLC content."""
    display_name = "DLC: Black Sea"
    default = 0

class DLC_Iberia(Toggle):
    """Enables Iberia DLC content."""
    display_name = "DLC: Iberia"
    default = 0

class DLC_WestBalkans(Toggle):
    """Enables West Balkans DLC content."""
    display_name = "DLC: West Balkans"
    default = 0

class DLC_Greece(Toggle):
    """Enables Greece DLC content."""
    display_name = "DLC: Greece"
    default = 0

class Photosanity(Toggle):
    """Enables Photo Trophy content as locations."""
    display_name = "Photo Trophy"
    default = 0

class Viewpointsanity(Toggle):
    """Enables Viewpoint content as locations."""
    display_name = "Viewpoint"
    default = 0

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["amount_to_win"] = AmountOfTokensNeeded
    options["enable_going_east"] = DLC_GoingEast
    options["enable_scandinavia"] = DLC_Scandinavia
    options["enable_vive_la_france"] = DLC_France
    options["enable_italia"] = DLC_Italia
    options["enable_beyond_the_baltic_sea"] = DLC_BalticSea
    options["enable_road_to_the_black_sea"] = DLC_BlackSea
    options["enable_iberia"] = DLC_Iberia
    options["enable_west_balkans"] = DLC_WestBalkans
    options["enable_greece"] = DLC_Greece
    options["enable_photosanity"] = Photosanity
    options["enable_viewpointsanity"] = Viewpointsanity

    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:

    return options