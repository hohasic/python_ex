'''
1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
 [3, 7, 1, 9, 5]
'''
# nums = [3, 7, 1, 9, 5]
# maxNum = 0
# for num in nums:
#     if num > maxNum:    # maxNum:9 num:5 > maxNum = 9
#         maxNum = num
    
# print(f'maxNum: {maxNum}')

# nums = [3, 7, 1, 9, 5]
# # nums.sort()     # [1, 3, 5, 7, 9]
# # # print(f'{nums[len(nums)-1]}')
# # print(f'{nums[-1:][0]}')

# print(max(nums))

'''
2. 사용자에게 숫자 입력받아서 1부터 입력한 숫자까지 합계 출력하기 (5)
'''
# userInputNum = int(input('양수 입력하세요. '))  # 5
# total = 0
# for num in range(1, userInputNum+1):
#     total += num
# print(f'total: {total}')

'''
3. 리스트에 있는 숫자 중 짝수만 출력하기 [1, 2, 3, 4, 5, 6]
'''
# nums = [1, 2, 3, 4, 5, 6]
# for num in nums:
#     if num % 2 == 0:
#         print(num)

'''
4. 리스트 숫자를 오름차순 정렬하기 [5,1,7,3]
'''
# nums = [5, 1, 7, 3]
# nums.sort()
# print(f'nums: {nums}') # [1, 3, 5, 7]

'''
5. 리스트 숫자를 내림차순 정렬하기 [5, 1, 7, 3]
'''
# nums = [5, 1, 7, 3]
# nums.sort(reverse=True)
# print(f'nums: {nums}')  # [7, 5, 3, 1]

'''
6. 리스트 안 숫자의 평균 구하기 [10, 20, 30]
'''
nums = [10, 20, 30]
total = 0
average = 0

for num in nums:
    total += num

average = total / len(nums)

print(f'total: {total}')
print(f'average: {average}')

'''
7. 리스트에서 가장 작은 숫자 찾기 (min() 사용 금지)
'''
# nums = [3, 7, 1, 9, 5]
# minNum = nums[0]        # 3
# for num in nums:
#     if num < minNum:
#         minNum = num
# print(f'minNum: {minNum}') # 1

'''
8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기
'''
# for num in range(1, 101):
#     if num % 3 == 0:
#         print(f'{num}은 3의 배수입니다.')

#     if num % 5 == 0:
#         print(f'{num}은 5의 배수입니다.')

'''
9. 사용자가 입력한 숫자를 리스트에 저장하다가 0 입력하면 종료 후 리스트 출력하기
   [입력: 3 ,입력: 7, 입력: 2, 입력: 0]  => [3, 7, 2]
'''

nums = []

while True:
    userInputNumber = int(input('정수 입력: '))
    
    if userInputNumber == 0:
        break

    nums.append(userInputNumber)

print(f'nums: {nums}')