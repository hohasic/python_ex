# calculator 모듈 사용하기
import calculator
import convertUnitModule

calculator.addition(10, 20)
calculator.subtraction(10, 20)
calculator.multiplication(10, 20)
calculator.division(10, 20)
calculator.rest(10, 20)
calculator.portion(10, 20)

calculator.division(10, 0)

inputMmData = int(input('길이(mm) 입력: '))
result = convertUnitModule.convertUnit(inputMmData)
convertUnitModule.printLength(result)