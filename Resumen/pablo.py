
class Perro:
    patas = 4

    def ataque(self):
        print('ladrar')


p = Perro()
pe = Perro()

print(p.patas)
print(pe.patas)

p.patas = 6
Perro.patas = 10

print(p.patas)
print(pe.patas)
