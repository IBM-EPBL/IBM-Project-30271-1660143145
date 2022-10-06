import random
temperature=random.randrange(0,1000)
humidity=random.randrange(0,1000)
if(temperature>=100):
    if(humidity>=55):
        print("High temperature-Alert")
else:
    print("Moderate temperature-Safe")
print(temperature)
print(humidity)
