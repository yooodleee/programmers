"""
문제 설명:
    정수 start_num와 end_num이 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 
        차례로 담은 리스트를 return 하도록 solution 함수를 작성해 보세요.

제한 사항:
    0 <= end_num <= start_num <= 50

입출력 예:
    start_num: 10
    end_num: 3
    result = [10, 9, 8, 7, 6, 5, 4, 3]

입출력 예 설명:
    10부터 3까지 1씩 감소하는 수를 담은 리스트는 [10, 9, 8, 7, 6, 5, 4, 3]입니다.
"""

def solution(start, end):
    if not isinstance(start, int): TypeError(start)
    if not isinstance(end, int): TypeError(end)

    if not (0 <= end <= start <= 50): ValueError(end, start)

    return list(range(start, end -1, -1))