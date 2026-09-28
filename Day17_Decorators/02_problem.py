import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"Execution time: {execution_time:.4f} seconds")
    return wrapper
    
    
@timer_decorator
def say_hello():
    print("Hello, Lipu!")
    
say_hello()