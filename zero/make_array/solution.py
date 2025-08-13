"""
문제 설명:
    정수 n과 k가 주어졌을 때, 1 이상 n 이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을
        반환하는 solution 함수를 작성해 보세요.

제한 사항:
    1 <= n <= 1,000,000
    1 <= k <= min(1,000, n)

입출력 예:
    n = 10, k = 3, result = [3, 6, 9]
    n = 15, k = 5, result = [5, 10, 15]

입출력 예 설명:
    입출력 예 #1
        1 이상 10 이하의 3의 배수는 3, 6, 9이므로 [3, 6, 9]를 반환합니다.
    입출력 예 #2
        1 이상 15 이하의 5의 배수는 5, 10, 15이므로 [5, 10, 15]를 반환합니다.
"""

def solution(n, k):
    if not isinstance(n, int): TypeError(n)
    if not isinstance(k, int): TypeError(k)

    if not (1 <= n <= 1000000): ValueError(n)
    if not (1 <= k <= min(1000, n)): ValueError(k, n)

    result = [i for i in range(1, n + 1) if i % k == 0]
    return result