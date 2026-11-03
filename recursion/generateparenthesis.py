def generateAllBinStr(n):
    result = []
    lst = []
    def solve(open, close):
        if open == n and close == n:
            result.append("".join(lst))

        if open < n:
            lst.append("(")
            solve(open+1, close)
            lst.pop()

        if close < open:
            lst.append(")")
            solve(open, close+1)
            lst.pop()
    solve(0,0)
    return result
        

n = 2
result = generateAllBinStr(n)
print(result)