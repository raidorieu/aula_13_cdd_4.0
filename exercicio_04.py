c=[0,0,0,0,0,0,0,0,0,0]
contador=0
impar=0
while True:
    if contador%2!=0:
        c[impar]=contador
        impar+=1
    contador+=1
    if impar>=10:
        break
print(c)
