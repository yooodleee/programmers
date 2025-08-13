"""
문제 설명:
    길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다.
    parts[i]는 [s, e] 형태로, my_strings[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
    각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return하는 solution 함수를 작성해 보세요.

제한 사항:
    1 <= my_strings의 길이 = parts의 길이 <= 100
    1 <= my_strings의 원소의 길이 <= 100
    parts[i]를 [s, e]라 할 때, 다음을 만족합니다.
        0 <= s <= e < my_strings[i]의 길이

입출력 예:
    my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
    parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
    result = "programmers"

입출력 예 설명:
    1) i = 0일 때
        my_strings[i] = "progressive" 
        parts[i] = [0, 4]
        부분 문자열 = "progr"
    2) i = 1일 때
        my_strings[i] = "hamburger"
        parts[i] = [1, 2]
        부분 문자열 = "am"
    3) i = 2일 때
        my_strings[i] = "hammer"
        parts[i] = [3, 5]
        부분 문자열 = "mer"
    4) i = 3일 때
        my_strings[i] = "ahocorasick"
        parts[i] = [7, 7]
        부분 문자열 = "s"
    
각 부분 문자열을 순서대로 이어 붙인 문자열은 "programmers"입니다. 
따라서, "programmers"를 return 합니다. 
"""

# zip()을 이용한 풀이
def solution(my_strings, parts):
    return ''.join([x[y[0]:y[1]+1] for x, y in zip(my_strings, parts)])


# 빈 문자열 선언
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer
