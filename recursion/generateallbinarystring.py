def generateAllBinStr(n):
    result = []
    def generator(idx, str):
        if idx >= n:
            result.append(str)
            return
      
        generator(idx+1, str+"0")
        generator(idx+1, str+"1")

    generator(0, "")
    return result

n = 4
result = generateAllBinStr(n)
print(result)