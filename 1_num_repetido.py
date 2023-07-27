def num_repetidos(X, n):
     series = [str(X) * i for i in range(1, n + 1)]
     series_sum = sum(map(int, series))
     series_exp = " + ".join(series)
     return "({series_exp}) = {series_sum}"
     X=3
     n=5
     resultado = num_repetidos(X,n)
     print(resultado)