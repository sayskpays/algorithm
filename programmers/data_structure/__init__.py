# 다중 리스트 튜플 inputData = [("Java",15000),("Python",25000),("C",18000),("Java",19000)]
# 에서 항목 값이 중복되어 있다면 중복된 값을 제거하여 실행결과와 같이 출력되도록 프로그램을 작성하시오
#
# 실행결과
#
# Java 15000
# Python 25000
# C 18000


inputData = [("Java",15000),("Python",25000),("C",18000),("Java",19000)]
first_data = []
second_data = []

for i in inputData:
    first_data.append(i[0])
    second_data.append(i[1])

first_data = sorted(set(first_data), key=lambda x: first_data.index(x))
if len(inputData) != len(first_data):
    del second_data[(len(inputData) != len(first_data))*-1]

for _ in range(len(first_data)):
    print(f'{first_data[_]} {second_data[_]}', sep='\n')
