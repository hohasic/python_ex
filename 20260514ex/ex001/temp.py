# # split(쪼갠다.)
# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
# print(f'names: {names}')
# print(f'names type: {type(names)}')

# str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
# splitedStr = str.split("-")             # list -> tuple
# print(f'splitedStr: {splitedStr}')
# print(f'splitedStr type: {type(splitedStr)}')


# # splitedStr = tuple(splitedStr)
# # print(f'splitedStr: {splitedStr}')
# # print(f'splitedStr type: {type(splitedStr)}')

# # memeber = "이고은/20/대전 중구/010-1234-5678/goeun@gmail.com"
# # memberList = memeber.split("/")
# # print(f'memberList: {memberList}')

# # print(f'이름: {memberList[0]}')
# # print(f'연락처: {memberList[3]}')



# 활당(대인) 연산
num = 10

# 구조분해할당
# [1, 2] > a = 1, b =2

# nums = [1, 2]
# a = nums[0]
# b = nums[1]

a, b = [1, 2]   # a = 1, b = 2
print(a)
print(b)

x, y = (10, 20)
print(x)
print(y)

a = 1
b = 2
a, b = b, a

a, *rest = [1, 2, 3, 4]
'''
a = 1
rest = [2, 3, 4]
'''