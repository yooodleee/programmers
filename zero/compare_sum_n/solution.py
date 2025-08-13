"""
문제 설명:
    정수 배열 numbers와 정수 n이 매개변수로 주어집니다.
    numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던
    원소들의 합을 return 하는 solution 함수를 작성해 보세요.

제한 사항:
    1 <= numbers의 길이 <= 100
    1 <= numbers의 원소 <= 100
    0 <= n < numbers의 모든 원소의 합

입출력 예:
    numbers: [34, 5, 71, 29, 100, 34]
    n = 123
    result = 139

    numbers: [58, 44, 27, 10, 100]
    n = 139
    result = 239

입출력 예 설명:
    예제 1번의 number를 문제 설명대로 더해가는 과정은 다음과 같습니다.
    1) i = 0
        numbers[i] = 34, sum = 34
    2) i = 1
        numbers[i] = 5, sum = 34 + 5 = 39
    3) i = 2
        numbers[i] = 71, sum = 34 + 5 + 71 = 110
    4) i = 3
        numbers[i] = 29, sum = 34 + 5 + 71 + 29 = 139

29를 더한 뒤에 sum 값은 139이고, n 값인 123보다 크므로 139를 return 합니다. 
"""

def solution(numbers, n):
    if not isinstance(numbers, list): raise TypeError(numbers)
    if not (1 <= len(numbers) <= 100): raise ValueError(numbers)
    if not (1 <= len(numbers[i]) <= 100 for i in range(len(numbers))): raise ValueError(numbers)
    if not (0 <= n < sum(numbers[i]) for i in range(len(numbers))): raise ValueError(numbers)

    answer = 0
    i = 0
    while answer <= n:
        answer += numbers[i]
        i += 1
    return answer