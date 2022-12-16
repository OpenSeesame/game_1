class Constants:
    # language
    LANG = 'ja'
    LANG_EN = 'en'
    LANG_JA = 'ja'

    # zero
    INT_ZERO = 0

    # max save data
    MAX_SAVE_DATA = 3

    # max status length
    MAX_STATUS_LENGTH = 4

    # dialog setting
    ASTERISK_COUNT = 60
    ALIGN_PAD = 10

    # align
    ALIGN_C = 'align_center'
    ALIGN_L = 'align_left'
    ALIGN_R = 'align_right'

    # yes or no
    YES = 'y'
    NO = 'n'

    # new or load
    NEW = '1'
    LOAD = '2'

    # equipment type
    WEAPON = 'weapon'
    SHIELD = 'shield'
    ARMOR = 'armor'
    ALL = 'all'

    # with dialog
    WITH_DIALOG = 'with_dialog'
    WITHOUT_DIALOG = 'without_dialog'

    # char
    ASTERISK = '*'
    BLANK = ''
    BR = '\n'
    FWA = 'FWA'

    def half_count(len):
        if len > Constants.ASTERISK_COUNT:
            return 0
        else:
            return (Constants.ASTERISK_COUNT - len) // 2 - 1