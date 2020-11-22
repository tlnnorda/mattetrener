# mattetrener

import random

riktig = 0
feil = 0

print("1. Addisjon")
print("2. Subtraksjon")
print("3. Multiplikasjon")
print("4. Divisjon")

valg = input("Velg regneart")

while True:
    if valg in ('1', '2', '3', '4'):

        if valg == '1':
            
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            print(a, "+", b, "=")
            c = float(input(" "))
            
            if c == (a+b):
                print("Riktig")
                riktig = riktig + 1
                print("Antall rikitge er", riktig)
                print("Antall feil er", feil)
                
            else:
                print("Feil")
                feil = feil + 1
                print("Antall riktige er", riktig)
                print("Antall feil er", feil)
                
        elif valg == '2':
            
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            print(a, "-", b, "=")
            c = float(input(" "))
            
            if c == (a-b):
                print("Riktig")
                riktig = riktig + 1
                print("Antall rikitge er", riktig)
                print("Antall feil er", feil)
                
            else:
                print("Feil")
                feil = feil + 1
                print("Antall riktige er", riktig)
                print("Antall feil er", feil)
                
        elif valg == '3':
            
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            print(a, "*", b, "=")
            c = float(input(" "))
            
            if c == (a*b):
                print("Riktig")
                riktig = riktig + 1
                print("Antall rikitge er", riktig)
                print("Antall feil er", feil)
                
            else:
                print("Feil")
                feil = feil + 1
                print("Antall riktige er", riktig)
                print("Antall feil er", feil)
                
        elif valg == '4':
            
            a = random.randint(1, 100)
            b = random.randint(1, 10)
            print(a, "/", b, "=")
            
            c = int(input("rund av"))
            
            if c == (round(a/b)):
                print("Riktig")
                riktig = riktig + 1
                print("Antall rikitge er", riktig)
                print("Antall feil er", feil)
                
            else:
                print("Feil")
                feil = feil + 1
                print("Antall riktige er", riktig)
                print("Antall feil er", feil)
                
                
        else:
            print("Feil valg")