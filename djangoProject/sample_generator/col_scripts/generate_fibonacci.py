import os
from datetime import date, datetime
def fibonacci(n):
    print("Parent:", os.getppid())
    print("Child:", os.getpid())
    first=0
    second=1
    counter=3
    if(n==0 or n==1):
        return 0
    if(n==2):
        return 1
    third=0
    while(counter<=n):
        third=first+second
        first=second
        second=third

        counter+=1
    with open(f"./sample_generator/sample_data/{os.getpid()}.txt","w+") as f:
        f.write(f"\nTimestamp: {datetime.now()}\n")
        f.write(str(third))
        f.write("\nend\n")
        f.close()
    return third      

# print(fibonacci(5))