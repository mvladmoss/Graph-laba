import itertools
dic = [] 
result = []
temp1 = []


def sochetlist(p, k):
    if k == 0:
        return
    for i in range(p, len(dic) - k + 1):
        temp1.append(dic[i])
        sochetlist(i + 1, k - 1)
        t = []
        for i in temp1:
            t.append(i)
        if(len(t) == 3):
            result.append(t)
        temp1.pop()
    
    
def main():
    print("Do you want to continue(Y/N):")
    temp = input("Enter the number of elements:")
    number = int(temp)
    for i in range(0, number):
        print("Enter  element", end=":")
        k = input()
        dic.append(str(k))
    num = input("Enter N:")
    print(dic)
    p = int(num)
    sochetlist(0, p)
    for i in result:
        print("{", end="")
        for j in i:
            if j == i[len(i) - 1]:
                print(j, end="")
            else:
                print(j, end=",")
        print("}")


main()
