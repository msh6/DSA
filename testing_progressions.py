from progression import Progression
from arithmetic_progression import ArithmeticProgression
from geometric_progression import GeometricProgression
from fibonacci_progression import FibonacciProgression

if __name__ == '__main__':
    print("Default Progression :")
    Progression().print_progression(10)
    
    print("Arithmetic Progression with increment of 5 :")
    ArithmeticProgression(5).print_progression(10)
    
    print("Arithmetic Progression with increment of 5 and start from 2 :")
    ArithmeticProgression(2 , 5).print_progression(10)
    
    print("Geometric Progression with default base :")
    GeometricProgression().print_progression(10)
    
    print("Geometric Progression with default base 3 :")
    GeometricProgression(3).print_progression(10)
    
    print("Fibonacci Progression with default values :")
    FibonacciProgression().print_progression(10)
    
    print("Fibonacci Progression with start values 4 and 6 :")
    FibonacciProgression(4, 6).print_progression(10)