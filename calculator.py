class Calculator:
    
    @staticmethod
    def add(x, y):
        return x + y;
    
    @staticmethod
    def subtract(x, y):
        return x - y;
    
    @staticmethod
    def multiply(x, y):
        return x * y;
    
    @staticmethod
    def divide(x, y):
        return x / y;


if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(1, 2))
    print(calc.subtract(1, 2))
    print(calc.multiply(1, 2))
    print(calc.divide(1, 2))