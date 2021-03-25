
def sqrt(n, l) :  
    x = n  
    count = 0 
    while (1) : 
        count += 1 
        root = 0.5 * (x + (n / x))  
        if (abs(root - x) < l) : 
            break   
        x = root 
    return root 

def abs(x):
    return x if x >= 0 else -x