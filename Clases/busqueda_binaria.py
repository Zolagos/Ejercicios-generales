b = int(input("Digite un numero:"))
a = [15, 35, 56, 70, 72, 85, 90, 101, 105]
izq = 0
der = len(a)-1
sw = False
while sw==False and izq < der:  
    
    med = izq + (der//2)-1
    if a[med]==b:
        print("Bingo")
        sw=True
    elif a[med]>b:
        der=med
        med=izq+(der//2)-1
        #print("3")
    else:
        izq=med
        med=izq+(der//2)-1
        #print("4")

