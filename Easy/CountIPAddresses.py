'''
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50
* With input "10.0.0.0", "10.0.1.0"   => return  256
* With input "20.0.0.10", "20.0.1.0"  => return  246
'''

def ips_between(start, end):
    one = start.split(".")
    two = end.split(".")
    temp = []
    for i in range(4):
        temp.append(int(two[i])-int(one[i]))
    temp[0] *= 256 * 256 * 256
    temp[1] *= 256 * 256
    temp[2] *= 256
    return sum(temp)