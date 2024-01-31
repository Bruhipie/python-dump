fib_series=[0,1]
for i in range(1,15):
    fib_series.append(fib_series[i-1]+fib_series[i])
print(fib_series)