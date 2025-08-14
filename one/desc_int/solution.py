"""
문제 설명:
    함수 solution은 정수 n을 매개변수로 입력 받습니다. n의 각 자릿수를 큰 것부터 작은 순으로
    정렬한 새로운 정수를 return 해주세요. 예를 들어, n이 118372면 873211을 리턴하면 됩니다.

제한 조건:
    n은 1 이상 8,000,000,000 이하인 자연수입니다.

입출력 예:
    n: 118372
    return: 873211
"""

def solution(n):
    if not isinstance(n, int): raise TypeError(n)
    if not (1 <= n <= 8000000000): raise ValueError(n)

    result = list(str(n))
    result.sort(reverse=True)

    return int("".join(result))