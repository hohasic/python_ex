SIGN_UP                 = 1
SIGN_IN                 = 2
PRINT_MY_INFO           = 3
PRINT_ALL_MEMBER_INFO   = 4
SYSTEM_SHUTDOWN         = 99

DEV_MOD = True

members = {}            # Database

if DEV_MOD:

    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234', '5678', '9012']
    uMails = ['gildong@gmail.com', 'chanho@naver.com', 'saeri@daum.net']
    uPhones = ['010-1234-5678', '010-9999-8888', '010-7777-6666']

    for n in range(len(uIds)):      # 3회 반복 ( 0, 1, 2 )
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMail': uMails[n],
            'uPhone': uPhones[n]
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
        for key, value in members.items():
            print(f'{key}님의 정보 ----------------')
            for key1, value1 in value.items():
                print(f'{key1}: {value1}')
            print('-' * 30)

    elif selectedMenuNum == SYSTEM_SHUTDOWN:    # 99.종료
        flag = False
        print('Good bye~')