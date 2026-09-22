s = "azyxyyzaaaa"
q = ['a', 'a', 'y', 'x']

def findCharHowManyTimes(freq_dict, list_char):
    result = {}
    for char in list_char:
        result[char] = freq_dict.get(char, 0)
    return result

def frequencyOfs(str):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

freq_dict = frequencyOfs(s)
result  = findCharHowManyTimes(freq_dict, q)
print(result)