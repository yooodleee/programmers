"""
문제 설명:
    정수 number와 n, m이 주어집니다. 
    number와 n의 배수이면서, m의 배수이면 1을, 아니라면 0을 return 하는 solution 함수를 만드세요.

제한 사항:
    10 <= number <= 100
    2 <= n, m <= 10

입출력 예:
    number = 6, n = 2, m = 3 -> result = 1
    number = 55, n = 10, m = 5 -> result = 0

입출력 예 설명:
    입출력 예 #1
        60은 2의 배수이면서 3의 배수이기 때문에 1을 반환합니다.
    입출력 예 #2
        55는 5의 배수이지만 10의 배수가 아니기 때문에 0을 반환합니다.
"""

def solution(number, n, m):
    if not isinstance(number, int): TypeError(number)
    if not isinstance(n, int): TypeError(n)
    if not isinstance(m, int): TypeError(m)
    
    if not (2 <= n <= 10): ValueError(n)
    if not (2 <= m <= 10): ValueError(m)

    if number % n != 0 or number % m != 0:
        return 0
    else:
        return 1
    