"""
문제 설명:
    수많은 마라톤 선수들이 마라톤에 참여했습니다. 
    단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주했습니다.
    마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
        완주하지 못한 선수의 이름을 return하는 solution 함수를 작성해 보세요.

제한 사항:
    마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
    completion의 길이는 participant의 길이보다 1 작습니다.
    참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
    참가자 중에는 동명 이인이 있을 수 있습니다.

입출력 예:
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    return: "leo"

    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    return: "vinko"

    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    return: "mislav"

입출력 예 설명:
    예제 #1
    "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

    예제 #2
        "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

    예제 #3
        "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
"""

def solution(participant, completion):
    if not isinstance(participant, list): raise TypeError(participant)
    if not isinstance(completion, list): raise TypeError(completion)

    if not all(isinstance(p, str) for p in participant): raise TypeError(p)
    if not all(isinstance(c, str) for c in completion): raise TypeError(c)

    if not (1 <= len(participant) <= 100000): raise ValueError(participant)
    if len(completion) != len(participant) - 1: raise ValueError(completion, participant)

    if not all(1 <= len(p) <= 20 for p in participant): raise ValueError(p)
    if not all(1 <= len(c) <= 20 for c in completion): raise ValueError(c)

    if not all(p.islower() for p in participant): raise ValueError(p)
    if not all(c.islowr() for c in completion): raise ValueError(c)

    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]