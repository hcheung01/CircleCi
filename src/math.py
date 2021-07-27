
class Math:
    def __init__(self):
        print("Math Class Initialized")

    def add(self, a: int, b: int) -> int:
        return a + b
    
    def subtract(self, a:int, b:int) -> int:
        return a - b
    
    def multiply(self, a:int, b:int) -> int:
        return a * b
    
    def divide(self, a:int, b:int) -> float:
        return a / b

if __name__ == "__main__":
    math = Math()
    print("Initializing Math Class")
    a = 10
    b = 20
    print("a={a} and b={b}")
    total = math.add(a, b)
    print(f"Total sum of a and b is: {total}")