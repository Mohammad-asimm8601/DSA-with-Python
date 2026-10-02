def stockBuyAndSell(nums):
    buy = nums[0]
    profit = 0

    for num in nums:
        if num < buy:
            buy = num
        else:
            profit = max(profit, num-buy)
    
    return profit


    
prices = [7, 10, 2, 5]
result = stockBuyAndSell(prices)
print(result)
