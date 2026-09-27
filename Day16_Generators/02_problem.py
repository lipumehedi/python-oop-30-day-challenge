def Countdown(count):
    while count >= 1:
        yield count
        count -=1
  
    
for number in Countdown(5):
    print(number)