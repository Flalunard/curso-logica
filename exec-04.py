''' Quadrado - Escrever um programa que imprima a seguinte figura:
XXXXX
X   X
X   X
X   X
XXXXX
'''
n=int(input("Digite o número 4:  " ))
print("x " * n )
for i in range(n):
    print("x" + " " *(n) + " x " )
print("x " * n)
