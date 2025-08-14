"""
문제 설명:
    자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태를 return 해주세요.
    예를 들어, n이 12345이면 [5, 4, 3, 2, 1]을 return 합니다.

제한 조건:
    n은 10,000,000,000 이하인 자연수입니다.

입출력 예:
    n: 12345
    return: [5, 4, 3, 2, 1]
"""

def solution(n):
    if not isinstance(n, int): raise TypeError(n)
    if not (1 <= n <= 10000000000): raise ValueError(n)

    num = list(str(n))
    num.reverse()

    return list(map(int, n))

