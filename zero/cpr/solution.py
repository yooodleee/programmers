"""
문제 설명:
    심폐소생술은 다음과 같은 순서를 통해 실시합니다.
    1. 심정지 및 무호흡 확인 [check]
    2. 도움 및 119 신고 요청 [call]
    3. 가슴 압박 30회 시행 [pressure]
    4. 인공 호흡 2회 시행 [respiration]
    5. 가슴 압박, 인공 호흡 반복 [repeat]

    주어진 solution 함수는 심폐소생술을 하는 방법의 순서가 담긴 문자열들이 무작위 순서로 담긴 리스트 cpr이 주어질 때
        각각의 방법이 몇 번째 단계인지 순서대로 담아 return 하는 함수입니다. solution 함수가 올바르게 작동하도록 빈칸을
        채워 solution 함수를 완성해 보세요.

제한 사항:
    cpr은 다음 문자열들이 한 번씩 포함되어 있습니다.
    "check", "call", "pressure", "respiration", "repeat"

입출력 예:
    cpr: ["call", "respiration", "repeat", "check", "pressure"]
    result: [2, 4, 5, 1, 3]

    cpr: ["respiration", "repeat", "check", "pressure", "call"]
    result: [4, 5, 1, 3, 2]

입출력 예 설명:
    입출력 예 #1
        "call", "respiration", "repeat", "check", "pressure"는 각각 2, 4, 5, 1, 3번째 순으로 [2, 4, 5, 1, 3]을 return 합니다.
    입출력 예 #2
        "respiration", "repeat", "check", "pressure", "call"은 각각 54, 5, 1, 3, 2번째 순으로 [4, 5, 1, 3, 2]를 return 합니다.
"""

def solution(cpr):
    if not isinstance(cpr, list): raise TypeError(cpr)
    if not all(isinstance(c, str) for c in cpr): raise TypeError(cpr)
    
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]

    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i + 1)
    
    return answer

