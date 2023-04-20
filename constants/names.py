from constants.constants import Constants
class Names:
    # title
    if Constants.LANG == Constants.LANG_EN:
        TITLE = 'Hello World'
    elif Constants.LANG == Constants.LANG_JA:
        TITLE = 'ハローワールド'

    # weapon
    if Constants.LANG == Constants.LANG_EN:
        SUDE_W = 'Sude'
        KATANA = 'Katana'
    elif Constants.LANG == Constants.LANG_JA:
        SUDE_W = 'すで'
        KATANA = 'かたな'

    # shield
    if Constants.LANG == Constants.LANG_EN:
        SUDE_S = 'Sude'
        WOOD_SHIELD = 'Wood Shield'
    elif Constants.LANG == Constants.LANG_JA:
        SUDE_S = 'すで'
        WOOD_SHIELD = 'きのたて'

    # armor
    if Constants.LANG == Constants.LANG_EN:
        HADAKA = 'Hadaka'
        BRONZE_ARMOR = 'Bronze Armor'
    elif Constants.LANG == Constants.LANG_JA:
        HADAKA = 'はだか'
        BRONZE_ARMOR = 'どうのよろい'
    
    # enemy
    if Constants.LANG == Constants.LANG_EN:
        SLIME = 'Slime'
    elif Constants.LANG == Constants.LANG_JA:
        SLIME = 'スライム'

    # spell
    if Constants.LANG == Constants.LANG_EN:
        FIRE = 'Fire'
    elif Constants.LANG == Constants.LANG_JA:
        FIRE = 'ファイア'