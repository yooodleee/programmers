"""
문제 설명:
    OO 시에는 저수지가 하나 있는데, 도시 내에서 사용하는 모든 물은 이 저수지에 저장된 물을 사용합니다.
        이상 기후로 인해 극심한 가뭄이 예고된 상황에서, 지난 달의 물 사용량과 이번 달부터 일정 기간
        동안의 월별 물 사용량의 변화를 예측한 값을 이용해 몇 달 뒤 물이 부족해지는지 예측하려고 합니다.
        이번 달부터의 월별 물 사용량 변화를 예측한 값은 다음과 같이 리스트에 담겨 주어집니다.
    
    * [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]
    * 리스트의 각 원소는 해당 월의 물 사용량이 전 달에 비해 몇 %만큼 증가/감소하는지를 나타냅니다.
    * 예를 들어, 이번 달의 물 사용량(리스트 첫 번째 원소)은 지난 달보다 10% 증가했으며, 다음 달은 10% 감소한 값입니다.

    현재 저수지에 저장된 물의 양 storage와 지난 달 물 사용량 usage, 월별 물 사용량이 전 달 대비 어떻게 변하는지 저장된 정수
        리스트 change가 주어질 때 몇 달 뒤 물이 부족해지는지 return하도록 solution 함수를 작성해 보세요. 가뭄이 끝날 때까지 
        저수지의 물이 남아 있다면 -1을 return 합니다.

제한 사항:
    1,000 <= storage <= 1,000,000
    500 <= usage <= 30,000
    1 <= change의 길이 <= 30
        -99 <= change[i] <= 500
        change[i]가 양수일 경우 물 사용량은 전 달보다 chagne[i]%만큼 증가
        change[i]가 음수일 경우 물 사용량은 전 달보다 change[i]%만큼 감소
        change[i]가 0일 경우 물 사용량은 전 달과 동일함
        매달 물 사용량은 소수점 이하를 버린 정수로 계산합니다. 

입출력 예:
    storage: 5141
    usage: 500
    change: [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]
    result: -1

    storage: 1000
    usage: 2000
    change: [-10, 25, -33]
    result: 1

입출력 예 설명:
    입출력 예 #1:
        지난 달 물 사용량(storage)는 500이므로, 이번 달 물 사용량은 10% 증가한 550입니다.
        다음 달 storage는 이번 달 사용량에서 10%감소한 495이며, 나머지 달도 동일하게 계산합니다.
        9달 뒤까지 계산한 물 사용량은 총 5115이며, 현재 저수지에 저장된 storage는 5141입니다. 
        따라서 물이 부족해지지 않으므로 -1을 return합니다.

    입출력 예 #2:
        총 사용 가능한 물의 양이 1,000인데, 2,000 * 0.9 = 1800이 필요하므로 이번 달부터 물이 
        부족합니다. 따라서 0을 return합니다. 
"""

def solution(storage, usage, change):
    if not isinstance(storage, int): raise TypeError(storage)
    if not isinstance(usage, int): raise TypeError(usage)
    if not isinstance(change, list): raise TypeError(change)
    if not all(isinstance(c, int) for c in change): raise TypeError(change)

    if not (1000 <= storage <= 1000000): raise ValueError(storage)
    if not (500 <= usage <= 30000): raise ValueError(usage)
    if not (-99 <= change[i] <= 500 for i in range(len(change))): raise ValueError(change)

    total_usage = 0
    for i in range(len(change)):
        usage += int(usage * change[i] / 100)
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1

