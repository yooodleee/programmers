"""
문제 설명:
    양의 정수 x가 하샤드 수려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
    예를 들어, 18의 자릿수의 합은 1 + 8 = 9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
    자연수 x를 입력 받아 x가 하샤드 수인지 아닌지 검사하는 solution 함수를 작성해 보세요.

제한 조건:
    x는 1 이상, 10,000 이하인 정수입니다.

입출력 예:
    x: 10, return: true
    x: 12, return: true
    x: 11, return: false
    x: 13, return: false
"""

def solution(n):
    if not isinstance(n, int): raise TypeError(n)
    if not (1 <= n <= 10000): raise ValueError(n)

    return n % sum(int(x) for x in str(n)) == 0

