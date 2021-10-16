def factorial(num): 
    factorial = 1 
    for i in range(1, num + 1): 
        factorial *= i

    return factorial 

assert factorial(7) == 5040

def choose(num1, num2): 
    return factorial(num1) // (factorial(num2) * factorial(num1 - num2)) 

assert choose(4, 2) == 6  

def generate(numRows): 
    return [[choose(i, j) for j in range(i + 1)] for i in range(numRows)] if numRows > 1 else [[1]]
    # if numRows == 1:
    #     return [[1]] 

    # return [[choose(i, j) for j in range(i + 1)] for i in range(numRows)]  

print(generate(5))  

