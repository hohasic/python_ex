from config_dir.dir import config
from member import session

flag = True

while flag:

    menuNum = ''
    if session.signInedMemberId == '':
        # sign out 상태
        menuNum = int(input('1.sign-up    2.sign-in    99.end'))
    else:
        # sign in 상태
        menuNum = int(input('3.modify    5.sign-out    4.delete    99.end'))

    if menuNum == config.SIGN_UP:
        print('1.sign-up')
    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    elif menuNum == config.SIGN_OUT:
        print('5.sign_out')
