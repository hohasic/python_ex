SIGN_UP                 = 1
SIGN_IN                 = 2
PRINT_MY_INFO           = 3
PRINT_ALL_MEMBER_INFO   = 4
SYSTEM_SHUTDOWN         = 99

DEV_MOD = True

members = {}            # Database

flag = True
while flag:
    selectedMenuNum = int(input('1.회원가입    2.로그인    3.나의 정보 출력     4.모든 회원 정보 출력    99.종료'))

    if selectedMenuNum == SIGN_UP:              # 1.회원가입
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')
        uMail = input('Input member EMAIL: ')
        uPhone = input('Input member PHONE: ')

        members[uId] = {
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
        }

        print('SIGN-UP SUCCESS!!')

        if DEV_MOD: print(f'members: {members}')

    elif selectedMenuNum == SIGN_IN:            # 2.로그인 
        pass
    elif selectedMenuNum == PRINT_MY_INFO:      # 3.나의 정보 출력  
        pass
    elif selectedMenuNum == PRINT_ALL_MEMBER_INFO:      # 4.모든 회원 정보 출력
        pass
    elif selectedMenuNum == SYSTEM_SHUTDOWN:    # 99.종료
        flag = False
        print('Good bye~')