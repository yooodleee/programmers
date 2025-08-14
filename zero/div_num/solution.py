"""
문제 설명:
    2 자리 이상의 정수 number가 주어집니다. 주어진 코드는 이 수를 2 자리씩 자른 뒤, 자른 수를 모두 더해
        그 합을 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 보세요.

제한 사항:
    10 <= number <= 2,000,000,000
    number의 자릿수는 2의 배수입니다.

입출력 예:
    입력 #1
    4859
    출력 #1
    107

    입력 #2
    29
    출력 #2
    29

입출력 예 설명:
    입출력 예 #1
        입력된 수를 2자리씩 나눠 합치면 다음과 같습니다.
        48 + 59 = 107

    입출력 예 #2
        입력된 수를 2자리씩 나눠 합치면 다음과 같습니다.
        29 = 29
"""

def solution(number):
    if not isinstance(number, int): raise TypeError(number)
    if not (10 <= number <= 2000000000): raise ValueError(number)
    if (len(number) % 2 != 0): raise ValueError(number)

    answer = 0

    for i in range(number):
        answer += number % 100
        number //= 100
    
    return answer

