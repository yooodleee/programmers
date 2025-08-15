"""
문제 설명:
    버스에는 좌석이 총 seat 개만큼 있습니다. 기점에서 출발한 버스가 정거장에 도착하기 전에 
        방문하는 각 정거장에서 승/하차한 승객 정보가 주어질 때, 버스에 탄 순간 빈 좌석은 
        몇 개인지 구해보세요. 현재 기다리는 정거장에서는 제일 먼저 버스에 탑승하며, 이전 
        정거장에서 버스에 탑승한 승객들은 늠는 죄석이 있다면 항상 앉는다고 가정합니다. 
        또한, 기점에서 출발하는 버스에는 승객에 0명 타고 있습니다.

        예를 들어, 좌석이 5개인 버스에 각 정거장에서 승/하차한 승객 정보를 나타냅니다. 현재 
            4번 정거장에서 기다리고 있으며, "On"은 승차한 승객, "Off"은 하차한 승객을 의미
            합니다. 
        
        * 1번 정거장: ["On", "On", "On"] (3명 승차, 0명 하차)
        * 2번 정거장: ["Off", "On", "-"] (1명 승차, 1명 하차)
        * 3번 정거장: ["Off", "-", "-"]  (0명 승차, 1명 하차)

    위와 같은 경우, 1번 정거장에서 3명이 승차, 2번 정거장에서 1명 승차, 1명 하차, 3번 정거장
        에서 1명이 하차했으므로 4번 정거장에 도착한 버스에는 2명이 타고 있습니다. 4번 정거장
        에서는 가장 먼저 탑승하므로, 남아 있는 좌석 수는 3개 입니다.

    주어진 solution 함수는 버스 좌석의 개수 seat, 기점에서 출발한 버스가 순서대로 방문한 정거장에서
        승객이 승/하차한 정보를 담은 2차원 문자열 리스트 passengers가 주어질 때, 버스에 남아있는 
        좌석의 개수를 return하는 함수입니다. 

제한 사항:
    1 <= seat <= 30
    1 <= passengers의 길이 <= 10
        passengers[0]은 1번 정거장, passengers[1]은 2번 정거장, ... passengers[i]는 i + 1번 정거장
        passengeres의 길이가 n이라면, 현재 n + 1번 정거장에서 기다리고 있습니다. 
    passengers[i]의 길이는 모두 동일합니다.
    passengers[i]의 원소는 "On", "Off", "-"입니다.
        "-"는 배열의 가로(열) 길이를 맞추기 위한 요소로, 아무런 의미도 없습니다.
        "-"가 "On", "Off" 사이에 있는 경우는 없습니다.

입출력 예:
    seat: 5
    passengers: [["On", "On", "On"], ["Off", "On", "-"], ["Off", "-", "-"]]
    result: 3

    seat: 10
    passengers: [
        ["On", "On", "On", "ON", "On", "On", "On", "On", "-", "-"],
        ["On", "On", "Off", "Off", "Off", "On", "On", "-", "-", "-"],
        ["On", "On", "On", "Off", "On", "On", "On", "Off", "Off", "Off"],
        ["On", "On", "Off", "-", "-", "-", "-", "-", "-", "-"]
    ]
    result: 0

입출력 예 설명:
    입출력 예 #2
        아래와 같이 승객이 타고 내렸고 마지막으로 12명이 버스에 타고 있으므로 남은 좌석은 0개입니다.
        - 1번 정거장 : ["On", "On", "On", "On", "On", "On", "On", "On", "-", "-"] (8명 승차, 0명 하차)
        - 2번 정거장 : ["On", "On", "Off", "Off", "Off", "On", "On", "-", "-", "-"] (4명 승차, 3명 하차)
        - 3번 정거장 : ["On", "On", "On", "Off", "On", "On", "On", "Off", "Off", "Off"] (6명 승차, 4명 하차)
        - 4번 정거장 : ["On", "On", "Off", "-", "-", "-", "-", "-", "-", "-"] (2명 승차, 1명 하차)
"""

def func1(num):
    return max(num, 0)

def func3(station):
    return sum(1 for people in station if people == "Off")

def func4(station):
    return sum(1 for people in station if people == "On")


def solution(seat, passengers):
    # Type Check
    if not isinstance(seat, int): raise TypeError(seat)
    if not isinstance(passengers, list) or not all(isinstance(st, list) for st in passengers):
        raise TypeError(passengers)
    
    # Value Range Check
    if not (1 <= seat <= 30): raise ValueError(seat)
    if not (1 <= len(passengers) <= 10): raise ValueError(passengers)
    if not all(1 <= len(st) <= 20 for st in passengers): raise ValueError(passengers)
    if not all(people in ["On", "Off", "-"] for st in passengers for people in st):
        raise ValueError(passengers)
    
    # Count passengers
    num_passengers = 0
    for station in passengers:
        num_passengers += func4(station)
        num_passengers -= func3(station)

    answer = func1(seat - num_passengers)
    return answer

