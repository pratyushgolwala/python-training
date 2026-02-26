class warrior:
    def attack(self):
        return 100
class paladin(warrior):
    def attack(self):
        base_damage = super().attack()
        return base_damage * 1.2
    def heal(self):
        return "healing"
    
p = paladin()
print(p.attack())
print(p.heal()  )  