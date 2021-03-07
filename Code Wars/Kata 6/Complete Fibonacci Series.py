def fibonacci(n):
    ciag = [0,1]
    if n < 1:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return ciag
    else:
        for i in range(n-2):
            ciag.append(ciag[-1]+ciag[-2])
        return ciag

fibonacci(10)