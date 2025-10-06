bekert = int(input("Hallgató jegyeinek a száma: "))

jegylista = []

print("A jegyek:")
for i in range(bekert):
    bekert2 = int(input())
    jegylista.append(bekert2)

atlag = sum(jegylista) / len(jegylista)

print(f"\nJegyek átlaga: {atlag}")

if atlag >= 4.4:
    print("A hallgató ösztöndíjra jogosult!")
else:
    print("A hallgató nem jogosult ösztöndíjra!")