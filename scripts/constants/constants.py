class Constants:
    INT_ZERO = 0
    MAX_SAVE_DATA = 3
    MAX_STATUS_LENGTH = 4
    ASTERISK_COUNT = 60
    ALIGN_PAD = 10
    ALIGN_C = 'align_center'
    ALIGN_L = 'align_left'
    ALIGN_R = 'align_right'
    TITLE = 'Hello World!'
    ASTERISK = '*'
    BLANK = ''
    BR = '\n'
    YES = 'y'
    NO = 'n'
    NEW = '1'
    LOAD = '2'

    def half_count(len):
        if len > Constants.ASTERISK_COUNT:
            return 0
        else:
            return (Constants.ASTERISK_COUNT - len) // 2 - 1