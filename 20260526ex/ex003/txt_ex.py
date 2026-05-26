# file = open('C:/kmh/python/test.txt', 'w')  # 파일을 '쓰기' 모드로 open한다.
# result = file.write('Hello python!')        # 쓰기(write)
# print(f'result: {result}')                  # 13
# file.close()                                # 파일 닫기(close, 외부자원 해제)

# file = open('C:/kmh/python/test.txt', 'r')
# readResult = file.read()
# print(f'readResult: {readResult}')
# print(f'readResult type: {type(readResult)}')

# readResult = int(readResult)
# readResult += 1
# print(f'readResult: {readResult}')

# file.close()


# file = open('C:/kmh/python/test.txt', 'a')
# file.write('\nhello~')
# file.close()

# with open('C:/kmh/python/test.txt', 'a') as file:
#     for n in range(10):
#         file.write('\nhello~')

# file = open('C:/kmh/python/test.txt', 'a')
# file.write('\nhi~')
# file.close()

# 예외 처리(보험)
# 세상에 모든 프로그램은 100% 완벽할 수가 없어요.

print(10 + 20)      # 30

try:
    print(10 / 1)       # 에러 발생

except Exception as e:
    print(f'e: {e}')

else:
    print('에러가 발생하지 않으면 실해되는 코드')

finally:
    print('에러가 발생하든 않하든 무조건 실행되는 코드')


print(10 - 20)      # X
print(10 * 20)      # X

# 예외 처리 기본 문법
'''
try ~ except
'''