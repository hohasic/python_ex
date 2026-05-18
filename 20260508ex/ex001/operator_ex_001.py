# data = int(input('수심을 입력하세요. '))
# temperature = 20 - (data // 10 * .7)
# print(f'temperature: {temperature}')

# speed = input('주행 속도: ')
# time = input('주행 시간: ')
# distance = int(speed) * int(time)
# print(f'주행 거리: {distance}')

#quiz)
'''
A회사는 3대의 컴퓨터로 8시간을 일하면 하루 업무를 처리할 수 있습니다.
그런데 단축 근무를 하게 되어 근무 시간이 줄게 되었다면 
몇 대의 컴퓨터가 더 필요할까요? 

근무 시간을 입력하면 필요한 컴퓨터 수량을 파악하는 프로그램을 만들어봅시다.
'''
# 3 * 8 = 24
# 24 / 8 = 3 

# time = int(input('근무시간을 입력하세요. '))    # 단축 근무  시간
# computer = 3 * 8 // time
# addComputer = 1 if (3 * 8 % time) > 0 else 0

# totalComputer = computer + addComputer
# print(f'필요한 컴퓨터 개수: {totalComputer}')

# 13시 30분 25초를 초로 나타내는 프로그램을 만드시오.
# print(f'second: {25 + (60 * 30) + (60 * 60 * 13)}')

# 학생의 국어, 영어, 수학 점수를 입력하면 총점과 평균을 출력하는 프로그램을 만드시오.
# kor = int(input('국어 점수: '))
# eng = int(input('영어 점수: '))
# mat = int(input('수학 점수: '))
# totalScore = kor + eng + mat
# averageScore = totalScore / 3
# print(f'totalScore: {totalScore}')
# print(f'averageScore: {averageScore}')

# 밤 최저 기온과 낮 최고 기온을 입력하면 일교차를 출력하는 프로그램을 만드시오.
# lowtemp = int(input(f"밤 최저 기온을 입력하세요 : "))
# hightemp = int(input(f"낮 최고 기온을 입력하세요: "))
# tempd = hightemp - lowtemp
# print(f'오늘의 최저기온 : {lowtemp}')
# print(f'오늘의 최고기온 : {hightemp}')
# print(f'오늘의 일교차는 : {tempd}도 입니다.')

# 사용자가 길이(cm)를 입력하면 inch로 환산하는 프로그램을 만드시오(단, 1cm는 0.39inch로 한다).
# cm = int(input('길이(cm) 입력하세요: '))
# inch = 0.39 * cm
# print('inch :', (inch))