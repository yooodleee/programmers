"""
문제 설명:
    정수 num이 짝수일 경우, "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수
    solution을 완성해 보세요.

제한 조건:
    num은 int 범위의 정수입니다.
    0은 짝수입니다.

입출력 예:
    num: 3, return: "Odd"
    num: 4, return: "Even"
"""

def solution(num):
    if not isinstance(num, int): TypeError(num)

    return {"Even" if num % 2 == 0 else "Odd"}