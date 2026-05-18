# fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
# print(f'fruits: {fruits}')
# print(f'fruits type: {type(fruits)}')

# 튜플 조회
'''
튜플은 아이템의 수정이 불가능하기 때문에 아이템의 삽입, 삭제, 정렬 등의 기능은 없고
조회하는 기능을 주로 사용합니다.
'''

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'{fruits[3]}')   # 참외

# quiz) 튜플에서 인덱스가 홀수인 아이템 조회하기
sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

for idx, item in enumerate(sports):
    if idx % 2 == 1:
        print(f'idx: {idx}, item: {item}')

# 특정 아이템의 인덱스(index) 조회
# 튜플 내 특정 아이템의 인덱스를 확인할 때는 index() 함수를 이용합니다.
fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'idx: {fruits.index('바나나')}')     # 7

# quiz) 아이템 값으로 인덱스 출력하기
# names 튜플에서 사용자가 선수 이름을 입력하면 이름에 해당하는 인덱스를 출력해봅시다.
names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

# inputData = input('선수 이름 입력: ')
# print(f'이름: {inputData}, 인덱스: {names.index(inputData)}')

# 튜플 안의 아이템 유/무 확인하기
# in과 not in 키워드를 사용하면 튜플 안에 특정 아이템의 존재 유/무를 확인할 수 있습니다.

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
print(f'{'Green+' in colors}')      # 'Green' > Ture, 'Green+' > False

if 'Green' in colors:
    print('colors에는 Green이 있습니다.')
else:
    print('colors에는 Green이 없습니다.')

if 'Green' not in colors:
    print('colors에는 Green이 없습니다.')
else:
    print('colors에는 Green이 있습니다.')

# quiz) 학점 경고 프로그램 만들기
'''
scores는 1학기 성적을 튜플로 나타낸 것입니다. F 학점이 있으면 '경고'를 출력하는 프로그램을 만들자!
scores = ('A', 'A+', 'B', 'B-', 'F')
'''
scores = ('A', 'A+', 'B', 'B-')
if 'F' in scores:
    print('경고!!!!')
else:
    print('경고 없음')

scores = ('A', 'A+', 'F', 'B', 'B-', 'F')
fCnt = scores.count('F')   # 2
print(f'F학점 개수: {fCnt}')

# 튜플 결합
# at list
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]

# 첫 번째 방법
# nums1.extend(nums2)
# print(f'nums1: {nums1}')

# 두 번째 방법
result = nums1 + nums2
print(f'nums1: {nums1}')
print(f'nums2: {nums2}')
print(f'result: {result}')

# at tuple
nums1 = (1, 2, 3)
nums2 = (10, 20, 30)

# nums1.extend(nums2)

result = nums1 + nums2
print(f'nums1: {nums1}')
print(f'nums2: {nums2}')
print(f'result: {result}')


num1 = 10
num2 = num1
print(f'num1: {num1}')      # 10
print(f'num2: {num2}')      # 10

num1 = 100
print(f'num1---: {num1}')      # 100
print(f'num2---: {num2}')      # 10

# ---------------------------------------------------------


nums1 = [1, 2, 3]
# nums2 = nums1
# print(f'nums1: {nums1}')    # [1, 2, 3]
# print(f'nums2: {nums2}')    # [1, 2, 3]

# nums1[0] = 100
# print(f'nums1+++: {nums1}')    # [100, 2, 3]
# print(f'nums2+++: {nums2}')    # [100, 2, 3]


nums1 = [1, 2, 3]
nums2 = [0, 0, 0]

for idx, num in enumerate(nums1):
    nums2[idx] = num

print(f'nums1: {nums1}')    # [1, 2, 3]
print(f'nums2: {nums2}')    # [1, 2, 3]

nums1[0] = 100
print(f'nums1: {nums1}')    # [100, 2, 3]
print(f'nums2: {nums2}')    # [1, 2, 3]


print('deep copy ----------------------')

import copy

a = [1, 2, 3, 4, 5]
# b = copy.deepcopy(a)
b = a.copy()

b[0] = 100

print(f'a : {a}')   # [1, 2, 3, 4, 5]
print(f'b : {b}')   # [100, 2, 3, 4, 5]

# 슬라이싱
animals = ('호랑이', '사자', '곰', '여우', '늑대')
print(f'animals: {animals}')

print(f'animals[:3]: {animals[:3]}')
print(f'animals[1:4]: {animals[1:4]}')
print(f'animals[:-2]: {animals[:-2]}')          # ('호랑이', '사자', '곰')
print(f'animals[:-2]: {animals[-1:-2]}')          # ()
print(f'animals[:-2]: {animals[-3:-1]}')          # ('곰', '여우')

# 슬라이싱 연습하기
'''
fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
 - 인덱스 2부터 4까지의 아이템을 출력하시오.
 - 인덱스 0부터 3까지의 아이템을 출력하시오.
 - 인덱스 3부터 끝까지의 아이템을 출력하시오.
'''

fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
print(f' fruits[2:5]: {fruits[2:5]}')           # ('plum', 'watermelon', 'peach')
print(f' fruits[0:4]: {fruits[0:4]}')           # ('apple', 'banana', 'plum', 'watermelon')
print(f' fruits[3:]: {fruits[3:]}')             # ('watermelon', 'peach')

# 리스트와 튜플간 변환(형변화, casting)
'''
불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야 합니다.
또한 리스트로 선언된 데이 터를 수정이 안 되게 하려면 튜플로 변환해야 합니다.
다음은 데이터 변환을 통해 리스트와 튜플을 변환하고 있습니다.
'''

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# Orange => 오렌지
# colors[1] = '오렌지'
colors = list(colors)
print(f'colors type: {type(colors)}')

colors[1] = '오렌지'
print(f'colors: {colors}')

colors = tuple(colors)
print(f'colors: {colors}')

# quiz) 튜플 정렬하기
# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# colors = list(colors)
# colors.sort()
# print(f'colors: {colors}')

# colors = tuple(colors)
# print(f'colors: {colors}')

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

cs = tuple(sorted(colors))
print(f'cs: {cs}')

