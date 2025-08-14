"""
문제 설명:
    정수를 담고 있는 배열 arr의 평균 값을 구하는 solution 함수를 작성해 보세요.

제한 사항:
    arr은 길이 1 이상, 100 이하인 배열입니다.
    arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

입출력 예:
    arr: [1, 2, 3, 4], return: 2.5
    arr: [5, 5], return: 5
"""

def solution(arr):
    if not isinstance(arr, list): raise TypeError(arr)
    if not all(isinstance(a, int) for a in arr): raise TypeError(arr)

    if not (1 <= len(arr) <= 100): raise ValueError(arr)
    if not all(-10000 <= a <= 10000 for a in arr): raise ValueError(arr)

    return sum(arr) / len(arr)

