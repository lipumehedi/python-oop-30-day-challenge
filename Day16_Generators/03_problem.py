def even_numbers(start, end):
    while start <= end:
        if start % 2 == 0:
            yield start
        start +=1


for number in even_numbers(1, 10):
    print(number)
       
