def calculate_stock_spans(prices):
    n = len(prices)
    spans = [1] * n 

    stack = [] 

    for i in range(n):
        
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()

   
        if stack:
            spans[i] = i - stack[-1]

       
        stack.append(i)

    return spans

stock_prices = [100, 80, 60, 70, 60, 75, 85]
stock_spans = calculate_stock_spans(stock_prices)
print(stock_spans)  # Output: [1, 1, 1, 2, 1, 4, 6]
