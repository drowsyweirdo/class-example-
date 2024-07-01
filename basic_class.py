class InfiniteOperations:
    def __init__(self, *args):
        self.sum = sum(args) 
        self.product = 1
        self.squares = []
        
        for arg in args:
            self.product *= arg
            self.squares.append(arg ** 2)
        
    
    def get_sum(self):
        return self.sum
    
    def get_product(self):
        return self.product
    
    def get_squares(self):
        return self.squares


numbers = InfiniteOperations(1, 2, 3, 5, 10, 80, 100, 120)
print("Sum:", numbers.get_sum())         
print("Product:", numbers.get_product()) 
print("Squares:", numbers.get_squares())
