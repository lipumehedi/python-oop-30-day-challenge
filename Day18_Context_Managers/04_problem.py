import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time

        print(f"Execution time: {execution_time:.4f} seconds")


with Timer():
    total = 0

    for number in range(1, 1000000):
        total += number
print("Calculation completed!")