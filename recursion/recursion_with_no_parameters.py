# Recursion with no parameters

# 1) Head Recursion

count = 0
def  func():
    global count
    if count == 4:
        return
    print("Asim")
    count +=1
    func()

func()

# 2) tail Recursion

count = 0
def  func():
    global count
    if count == 4:
        return
    count +=1
    func()
    print("Asim")

func()