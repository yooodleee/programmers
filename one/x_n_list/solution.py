"""
문제 설명:
    함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 
        return해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수 solution을 완성해 보세요.

제한 사항:
    x는 -10,000,000 이상 10,000,000 이하인 정수입니다.
    n은 1,000 이하인 자연수입니다.

입출력 예:
    x: 2, n = 5, answer = [2, 4, 6, 8, 10]
    x: 4, n = 3, answer = [4, 8, 12]
    x: -4, n = 2, answer = [-4, -8]
"""

def solution(x, n):
    if not isinstance(x, int): raise TypeError(x)
    if not isinstance(n, int): raise TypeError(x)

    if not (-10000000 <= x <= 10000000): raise ValueError(x)
    if not (1 <= n <= 1000): raise ValueError(n)

    return [x * i for i in range(1, n + 1)]