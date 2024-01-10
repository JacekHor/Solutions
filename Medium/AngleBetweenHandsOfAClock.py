'''
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

Example 1:
Input: hour = 12, minutes = 30
Output: 165

Example 2:
Input: hour = 3, minutes = 30
Output: 75

Example 3:
Input: hour = 3, minutes = 15
Output: 7.5
'''
class Solution(object):
    def angleClock(self, hour, minutes):
        if hour == 12:
            hour = 0
        if minutes == 60:
            minutes = 0
            hours += 1
        angle = abs((0.5 * (60 * hour + minutes)) - (6 * minutes))
        return min(360 - angle, angle)