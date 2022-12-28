class Constants:
    # language
    LANG_EN = 'en'
    LANG_JA = 'ja'
    LANG = LANG_JA

    # battle speed
    BATTLE_SLOW = 2.0
    BATTLE_NORMAL = 1.5
    BATTLE_FAST = 1.2
    BATTLE_SPEED = BATTLE_NORMAL

    # guard
    GUARD_AR = 100
    GUARD_MR = 50

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

    # command
    ATTACK = '1'
    MAGIC = '2'
    GUARD = '3'
    RUN = '4'

    # run
    RUN_E = 'escaped'
    RUN_F = 'failed'

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