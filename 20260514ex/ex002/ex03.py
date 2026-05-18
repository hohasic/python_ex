from datetime import datetime

MENU_INCOME     = 1
MENU_EXPENSE    = 2
MENU_VIEW       = 3
EXIT            = 99

flag = False
DEV_MOD = True

bankAccount = []
currentMoney = 0

if DEV_MOD:
    txt =  '[2026-05-15 15:14:08] \t 100 \t\t aaaaa \t\t 100'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:15:08] \t 200 \t\t bbbbb \t\t 300'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:16:08] \t\t -50 \t ccccc \t\t 250'
    bankAccount.append(txt)

while flag:

    selectedMenuNum = int(input('1.수입    2.지출    3.조회    99.시스템종료 -----> '))
    if selectedMenuNum == MENU_INCOME:
        incomeMoney = int(input('수입 금액: '))
        incomeDesc = input('수입 내용: ')
        currentMoney += incomeMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t {incomeMoney} \t {incomeDesc} \t\t\t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_EXPENSE:
        expenseMoney = int(input('지출 금액: '))
        expenseDesc = input('지출 내용: ')
        currentMoney -= expenseMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t\t\t -{expenseMoney} \t {expenseDesc} \t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_VIEW:
        print('-' * 63)
        print('날짜&시간 \t\t 입금 \t 출금 \t 내역 \t\t 잔액')
        print('-' * 63)
        for item in bankAccount:
            print(item)
        print('-' * 63)

    elif selectedMenuNum == EXIT:
        flag = False