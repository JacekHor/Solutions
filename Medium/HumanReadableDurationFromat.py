'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''

def format_duration(seconds):
    temp=[]
    if seconds == 0:
        return "now"
    else:
        if seconds // 31536000 >= 1:
            temp.append(seconds // 31536000)
            seconds = seconds % 31536000
        else:
            temp.append(0)
        if seconds // 86400 >= 1:
            temp.append(seconds // 86400)
            seconds = seconds % 86400
        else:
            temp.append(0)
        if seconds // 3600 >= 1:
            temp.append(seconds // 3600)
            seconds = seconds % 3600
        else:
            temp.append(0)
        if seconds // 60 >= 1:
            temp.append(seconds // 60)
            seconds = seconds % 60
        else:
            temp.append(0)
        temp.append(seconds)

        temp3 = ["year", "day", "hour", "minute", "second"]
        temp4 = []
        for i in range(len(temp)):
            if temp[i] == 0:
                pass
            elif temp[i] == 1:
                temp4.append(str(temp[i]) + " " + temp3[i])
            elif temp[i] > 1:
                temp4.append(str(temp[i]) + " " + temp3[i] + "s")
        print(temp4)
        answer = ""
        for i in range(len(temp4)):
            if len(temp4) == 1:
                return temp4[i]
            elif i == len(temp4)-1:
                return answer + temp4[i-1] + " and " + temp4[i]
            elif i <= len(temp4)-3:
                answer = answer + temp4[i] + ", "
