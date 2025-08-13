"""
문제 설명:
    문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.
    * 먼저, 첫 글자를 읽습니다. 이 글자를 x라고 합니다.
    * 이제 이 문자열을 왼쪽에서 오른쪽으로 읽어 나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를
        각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
    * s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료
        합니다.
    * 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고,
        종료합니다.
    문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return
        하는 solution 함수를 작성해 보세요.

제한 사항:
    1 <= s의 길이 <= 10,000
    s는 영어 소문자로만 이루어져 있습니다.

입출력 예:
    s = "banana"
    result = 3

    s = "abracadabra"
    result = 6

    s = "aaabbaccccabba"
    result = 3

입출력 예 설명:
    입출력 예 #1
        s = "banana"인 경우 ba - na - na와 같이 분해됩니다.

    입출력 예 #2
        s = "abracadabra"인 경우 ab - ra - ca - da - br - a와 같이 분해됩니다.

    입출력 예 #3
        s = "aaabbaccccabba"인 경우 aaabbacc - ccab - ba와 같이 분해됩니다.
"""

def solution(s):
    if not isinstance(s, str): raise TypeError(s)
    if not (1 <= len(s) <= 10000): raise ValueError(s)
    if s.upper() is True: raise ValueError(s)

    answer = 0
    sav1 = 0
    sav2 = 0
    
    for i in s:
        if sav1 == sav2:
            answer += i
            a = i
        
        if i == a:
            sav1 += 1
        else:
            sav2 += 1
    
    return answer
