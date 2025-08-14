"""
문제 설명:
    정수 n을 입력 받아 n의 약수를 모두 더한 값을 return하세요.

제한 사항:
    n은 0 이상 3,000 이하인 정수입니다.

입출력 예:
    n: 12, return: 28
    n: 5, return: 6
"""

def solution(n):
    if not isinstance(n, int): raise TypeError(n)
    if not (0 <= n <= 3000): raise ValueError(n)

    sum_ = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            sum_ += i

    return sum_

