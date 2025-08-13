"""
문제 설명:
    자연수 n이 입력으로 주어졌을 때 만약, n이 짝수이면 "n is event", 홀수이면 "n is odd"를 출력합니다.

제한 사항:
    1 <= n <= 1,000

입출력 예:
    입력 #1
        100
    출력 #1
        100 is even
    
    입력 #2
        1
    출력 #2
        1 is odd
"""

def solution(n):
    if not isinstance(n, int): TypeError(n)
    if not (1 <= n <= 1000): ValueError(n)

    print(f"{n} is {'even' if n % 2 == 0 else 'odd'}")