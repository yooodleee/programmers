"""
문제 설명:
    알파벳으로 이루어진 문자열 myString이 주어집니다.
    모든 알파벳을 대문자로 변환하여 return하는 solution 함수를 작성해 보세요.

제한 사항:
    1 <= myString의 길이 <= 100,000
    myString은 알파벳으로 이루어진 문자열입니다.

입출력 예:
    myString = "aBcDeFg"
    result = "ABCDEFG"

    myString = "AAA"
    result = "AAA"
"""

def solution(myString):
    if not isinstance(myString, str): raise TypeError(myString)

    result = myString.upper()
    return result
