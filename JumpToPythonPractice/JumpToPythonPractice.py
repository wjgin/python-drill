# 점프 투 파이썬 연습 문제 풀이

# Q1 "a:b:c:d를 "a#b#c#d"로 바꾸기
from multiprocessing import set_forkserver_preload
from operator import le
from unittest import result


Q1 = "a:b:c:d"
print(Q1.replace(":", "#"))

# Q2 딕셔너리 "C" 값에 70이 들어가게 수정
Q2 = {'A' : 90, 'B' : 80}
Q2['C'] = 70
print(Q2['C'])

#Q3 리스트에 + 와 extend의 차이점을 설명해라
"""
+는 문자열을 새로운 메모리 주소에 저장하고 교체한다.(메모리 주소가 바뀜)
extend 는 새로운 메모리 주소에 저장하지 않고 기존에 리스트에 값을 변경해서 사용한다.(메모리 주소가 바뀌지 않음)
"""
# Q4 리스트의 50점 이상의 점수의 총합을 구하여라
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
Q4 = 0
for x in A:
    if x >= 50:
        Q4 += x
print(Q4)

# Q5 피보나치 수열: 정수 n을 받았을 때, n 이하까지의 피보나치 수열 값
# n = int(input("Q5 피보나치 수열 n을 입력하세요: "))
n = 5
nums = []
for i in range(0, n):
    if i == 0:
        nums.append(0)
    elif i == 1:
        nums.append(1)
    else:
        nums.append(nums[i - 2] + nums[i - 1])
print("결과:",nums)

# Q6 숫자의 총합구하기 : 사용자로부터 숫자들을 입력 받아 총합을 하라 구분자는 콤마(,)로 한다.
# n = input("Q6 숫자의 총합을 구할 연속된 숫자를 입력하세요. 구분자는 콤마(,): ").split(',')
n = [1, 2, 3]
sum = 0
for i in n:
    sum += int(i)
print(sum)

# Q7 한 줄 구구단: 사용자의 입력을 받아서 한 줄로 구구단을 출력하세요 (2 ~ 9)
#n = int(input("구구단을 출력할 숫자를 입력하세요(2 ~ 9): "))
n = 8
if n > 9 or n < 2:
    print ("잘못된 숫자")
else:
    for i in range(1, 10):
        print(i * n, end = ' ')

# Q8 역순 저장: 텍스트 파일을 읽고 파일의 내용을 역순으로 저장하시오
# 파일의 경로는 workplace가 기준이 된다.
# abc.txt 파일의 내용을 역순으로 저장
f = open('./JumpToPythonPractice/abc.txt', 'r') # 파일 읽기
lines = f.readlines() # 파일의 모든 라인 읽기
f.close()

lines.reverse() # 저장한 라인 역순으로 만들기

f = open('./JumpToPythonPractice/abc.txt', 'w') # 파일 쓰기
for line in lines:
    line.strip() # 개행 제거
    f.write(line)
    f.write('\n')
f.close()

# Q9 평균 값 구하기: 10줄로 이뤄진 파일을 읽어서 각 줄의 숫자의 평균 값을 구하라
f = open('./JumpToPythonPractice/sample.txt', 'r')
lines = f.readlines() # 줄 단위로 읽고 리스트 저장
f.close()
total = 0
for line in lines:
    total += int(line)
print("\nQ9 평균 값:", total / len(lines))

# Q10 사치연산 계산기 클래스 만들기
class Calculator:
    def __init__(self, numList):
        self.numList = numList
    
    def sum(self):
        result = 0
        for num in self.numList:
            result += num
        return result
    
    def avg(self):
        result = self.sum()
        return result / len(self.numList)

cal1 = Calculator([1,2,3,4,5])
print("Q10 sum:", cal1.sum())
print("Q10 avg:", cal1.avg())