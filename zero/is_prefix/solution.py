"""
문제 설명:
    어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다.
    예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
    문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 
        반환하는 solution 함수를 작성해 보세요.

제한 사항:
    1 <= my_string의 길이 <= 100
    1 <= is_prefix의 길이 <= 100
    my_string과 is_prefix는 영소문자로만 이루어져 있습니다.

입출력 예:
    my_string: "banana"
    is_prefix: "ban"
    result: 1

    my_string: "banana"
    is_prefix: "nan" 
    result: 0

입출력 예 설명:
    입출력 예 #1
        예제 1번에서 is_prefix가 my_string의 접두사이기 때문에 1을 반환합니다.
    입출력 예 #2
        예제 2번에서 is_prefix가 my_string의 접두사가 아니기 때문에 0을 반환합니다.
"""

def solution(my_string, is_prefix):
    if not isinstance(my_string, str): TypeError(my_string)
    if not isinstance(is_prefix, str): TypeError(is_prefix)

    if not (1 <= len(my_string) <= 100): ValueError(my_string)
    if not (1 <= len(is_prefix) <= 100): ValueError(is_prefix)

    num = len(is_prefix)
    if is_prefix == my_string[:num]:
        return 1
    else:
        return 0