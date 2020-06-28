def createArray(n):
    ret = []
    for i in range(n):
        ret.append(n - i)
    return ret

# return true if the array is sorted
def checkArray(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True