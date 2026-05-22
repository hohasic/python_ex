from config_dir.dir import config
from member import session
from db import member_db
from member import member_dumy

if config.DEV_MOD:
    member_dumy.memberDumyInit()
    print(f'memberDB: {member_db.memberDB}')

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
        uId = input('Please input new member ID: ')
        uPw = input('Please input new member PW: ')
        uMail = input('Please input new member MAIL: ')
        uPhone = input('Please input new member PHONE: ')

        member_db.memberDB[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
        }

        print('New member sign-up success!!')

        if config.DEV_MOD:
            print(f'memberDB: {member_db.memberDB}')

    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
        uId = input('Please input member ID: ')
        uPw = input('Please input member PW: ')

        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign-in success!!')
                session.signInedMemberId = uId
            else:
                print('sign-in fail!! -- PW error')
        else:
            print('sign-in fail!! -- ID error')

    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
        '''
        id, pw, mail, phone 이 중에서 어떤 정보들만 수정가능케 할 것인지 정해야 합니다.
        id: X, 또한 이미 탈퇴한 회원의 ID라도 절대 변경 사용할 수 없습니다.
        pw: 절대 수정이 불가하지는 않습니다. 하지만 쉽게 변경할 수는 없습니다.
        mail: 비교적 단순하게 수정할 수 있습니다.
        phone: 비교적 단순하게 수정할 수 있습니다.
        '''

        uPw = input('Please input member PW: ')
        uMail = input('Please input member MAIL: ')
        uPhone = input('Please input member PHONE: ')

        '''
            - member_db 모듈에 있는 memberDB 딕셔너리에서 회원정보를 변경한다.
            - 지금 현재 memberDB에는 'gildong', 'chanho'회원이 있죠? 네!
            - 대명씨 의견: 현재 로그인되어 있는 회원 정보를 불러와서 그 정보를 수정합니다.
            - 즉, session.signInedMemberId에서 현재 로그인 되어 있는 회원 ID를 가져와서
            - 사용하면 됩니다.
        '''

        currentSignInedMemberID = session.signInedMemberId
        memberInfo = member_db.memberDB[currentSignInedMemberID]
        if config.DEV_MOD: print(f'memberInfo: {memberInfo}')

        memberInfo['uPw'] = uPw
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        if config.DEV_MOD: print(f'after modify: memberInfo: {memberInfo}')

    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    elif menuNum == config.SIGN_OUT:
        print('5.sign_out')
        '''
         - 메뉴를 변경해야겠다.
         - 로그인 값을 없애야겠다.
         - session 모듈에 signInedMemberId 변수에 있는거죠? 넵!
        '''
        print('sign-out success!!')
        session.signInedMemberId = ''
