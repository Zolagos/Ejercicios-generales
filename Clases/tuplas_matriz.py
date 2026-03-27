n = int(input("Digite un numero: "))
m = int(input("Digite un numero: "))

list = [[0 for _ in range(m)] for _ in range(n)] 
for i in range (0,n,1):
    for j in range (0,m,1):
        list[i][j] = input("Digite: ")
print("\n")

for i in range (0,n,1):
    print(list[i])