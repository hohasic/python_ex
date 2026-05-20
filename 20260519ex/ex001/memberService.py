SIGN_UP                 = 1
SIGN_IN                 = 2
PRINT_MY_INFO           = 3
PRINT_ALL_MEMBER_INFO   = 4
SYSTEM_SHUTDOWN         = 99

DEV_MOD = True

members = {}            # Database

if DEV_MOD:
    members['gildong'] = {
        'uId': 'gildong',
        'uPw': '1234',
        'uMail': 'gildong@gmail.com',
        'uPhone': '010-1234-5678'
    }

flag = True
while flag:
    selectedMenuNum = int(input('1.회원가입    2.로그인    3.나의 정보 출력     4.모든 회원 정보 출력    99.종료'))

    if selectedMenuNum == SIGN_UP:              # 1.회원가입
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')
        uMail = input('Input member EMAIL: ')
        uPhone = input('Input member PHONE: ')

        members[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
        }

        print('SIGN-UP SUCCESS!!')

        if DEV_MOD: print(f'members: {members}')

    elif selectedMenuNum == SIGN_IN:            # 2.로그인 
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN-IN SUCCESS!!')
            else:
                print('SIGN-IN FAIL!!')
        else:
            print('존재 하지 않은 ID입니다. 다시 확인하세요.')
        

    elif selectedMenuNum == PRINT_MY_INFO:      # 3.나의 정보 출력  
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN-IN SUCCESS!!')

                print('-' * 30)
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 30)

            else:
                print('SIGN-IN FAIL!!')
        else:
            print('존재 하지 않은 ID입니다. 다시 확인하세요.')

    elif selectedMenuNum == PRINT_ALL_MEMBER_INFO:      # 4.모든 회원 정보 출력
        pass
    elif selectedMenuNum == SYSTEM_SHUTDOWN:    # 99.종료
        flag = False
        print('Good bye~')