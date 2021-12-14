a=input("Enter seq 1").split()
print("Length of seq 1: ",len(a))
b=input("Enter seq 2").split()
print("Length of seq 2: ",len(b))
matrix=[]
print("Enter the entries rowwise")
for i in range(len(a)+1):
    a=[]
    for j in range(len(b)+1):
        a.append(int(input()))
    matrix.append(a)
for i in range(len(a)+1):
    for j in range(len(b)+1):
        print(matrix[i][j], end="")
    print()
