# calculator 모듈

def addition(n1, n2):
    print(f'덧셈 연산 결과: {n1 + n2}')

def subtraction(n1, n2):
    print(f'뺄셈 연산 결과: {n1 - n2}')

def multiplication(n1, n2):
    print(f'곱셈 연산 결과: {n1 * n2}')

def division(n1, n2):
    if n2 == 0:
        print('세상 어떤 숫자도 0으로 나눌수는 없습니다.')
        return
    
    print(f'나눗셈 연산 결과: {n1 / n2}')

def rest(n1, n2):
    print(f'나머지 연산 결과: {n1 % n2}')

def portion(n1, n2):
    print(f'몫 연산 결과: {n1 // n2}')