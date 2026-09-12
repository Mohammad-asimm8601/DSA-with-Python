# Constraints 
# 1) 1<n[i]<=10
# 2) n can have 10^8 elements
# 2) m can have 10^8 elements


def findElementHowManyTimes(freq, m):
    result = {}
    length = len(m)
    for i in range(0, length):
        result[m[i]] = freq.get(m[i], 0)
    return result

def frequencyOfn(n):
    freq = {}
    length = len(n)
    for i in range(0,length):
        freq[n[i]] = freq.get(n[i], 0)+1
    return freq



n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

freq = frequencyOfn(n)
result = findElementHowManyTimes(freq, m)
print(result)

