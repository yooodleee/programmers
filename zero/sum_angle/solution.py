"""
문제 설명:
    일반적으로 두 선분이 이루는 각도는 한 바퀴를 360도로 하여 표현합니다.
    따라서, 각도에 360의 배수를 더하거나 빼더라도 같은 각을 의미합니다.
    예를 들면, 30도와 390도는 같은 각도입니다.
    주어진 코드는 각 코드를 나타내는 두 정수 angle1과 angle2가 주어질 때, 이 두 각의 합을 0도 이상 360도 미만으로
        출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 보세요.

제한 사항:
    0 <= angle1 <= 5,000
    0 <= angle2 <= 5,000

입출력 예:
    입력 #1
    280, 485
    출력 #1
    45

입출력 예 설명:
    angle1과 angle2의 합은 765이고, 765에서 720을 빼면 45도 이므로 45을 출력합니다. 
"""

def solution(angle1, angle2):
    if not isinstance(angle1, int): raise TypeError(angle1)
    if not isinstance(angle2, int): raise TypeError(angle2)

    if not (0 <= angle1 <= 5000): raise ValueError(angle1)
    if not (0 <= angle2 <= 5000): raise ValueError(angle2)

    sum_ = (angle1 + angle2) % 360 
    return sum_

