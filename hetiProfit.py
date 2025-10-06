elso = int(input("Mennyi csokit adott el az első napon? "))
maradek = 6
ossz = elso
most = elso

for i in range(maradek):
    most = most * 2
    ossz += most

print(f"Ennyi csokit adott el összesen: {ossz}")