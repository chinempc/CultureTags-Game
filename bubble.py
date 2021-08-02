
import time
from threading import Thread
ans = None
def timing():
    time.sleep(5)
    print(ans)
    if ans != None:
        return 
    print("too play bro...Press enter to continue")
    return
    
def wat():
    for i in range(10):
        if ans != None:
            return
        time.sleep(1)
    print("Too late...Press Enter to continue")

Thread(target = wat).start()

ans = input("what is your name!!!\nName: ")
print(ans)
