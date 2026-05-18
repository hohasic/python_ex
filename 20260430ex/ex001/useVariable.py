str = '192.168.56.101'

print(str)
print(str)
print(str)
print(str)
print(str)


# 데이터 복사
var1 = 123
var2 = var1

print(var1)     # 123
print(var2)     # 123

var1 = 321
print(var1)     # 321
print(var2)     # 321(X), 123(O)

# Quiz
num1 = 111
num2 = 222
print(num1)     # 111
print(num2)     # 222

temp = num1     # 111
num1 = num2     # 222
num2 = temp     # 111
