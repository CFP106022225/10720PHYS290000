import numpy as np
import matplotlib.pyplot as plt
N = 10000
M = 50
dM = 5
students1 = np.full(N, M)
students2 = np.full(N, M)
    
def play_a(array, dm):
    a = np.random.randint(0, len(array))
    b = np.random.randint(0, len(array))
    
    a_hand = np.random.randint(0, 3)
    b_hand = np.random.randint(0, 3)
    
    if a_hand == 0 and b_hand == 2:
        array[a] += dm
        array[b] -= dm
        
    elif b_hand == 0 and a_hand == 2:
        array[a] -= dm
        array[b] += dm
    
    elif a_hand > b_hand:  
        array[a] += dm
        array[b] -= dm
        
    elif a_hand < b_hand:
        array[a] -= dm
        array[b] += dm
    else :
        pass
        
    return array

def play_b(array, dm):
    a = np.random.randint(0, len(array))
    b = np.random.randint(0, len(array))
    if array[a] <= 0 or array[b] <= 0:
        pass
    else :
        a_hand = np.random.randint(0, 3)
        b_hand = np.random.randint(0, 3)
    
        if a_hand == 0 and b_hand == 2:
            array[a] += dm
            array[b] -= dm
        
        elif b_hand == 0 and a_hand == 2:
            array[a] -= dm
            array[b] += dm
    
        elif a_hand > b_hand:  
            array[a] += dm
            array[b] -= dm
        
        elif a_hand < b_hand:
            array[a] -= dm
            array[b] += dm
        else :
            pass
    
    return array

for _ in range(1000000):
    students1 = play_a(students1, dM)
    students2 = play_b(students2, dM)

plt.hist(students1, bins = 20, label = "Liability")
plt.hist(students2, bins = 20, label = "No Liability")
plt.legend(loc = "best")
plt.show()