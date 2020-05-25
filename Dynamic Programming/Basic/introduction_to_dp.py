"""
Dynamic Programming Approach:
Memoization
Tabulation
"""

"""
Using Memoization Techniques
to solve fibonacci and factorial 
"""
def fibonacci(n):
    if n<=1 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print(fibonacci(6))
main()