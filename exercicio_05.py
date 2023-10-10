d=[0,0,0,0,0,0,0,0,0,0]
for y in range(10):
    d[y]=int(input("digite um número: "))
for z in range(10):
    if d[z]%2!=0:
            print(f"este é impar e é {d[z]}")
    elif d[z]%2==0:
            print(f"este é par e é {d[y]}")
    else:
            print("é 0")
