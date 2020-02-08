class Pokemon:
    def __init__(self, name, level, tpe):
        self.name = name
        self.level = level
        self.type = tpe
        self.max_health = (level*10)
        self.current_health = self.max_health
        self.knocked_out = False
    
    def __repr__(self):
        return f"{self.name} is a level {self.level} {self.type} Pokémon. Health: {self.current_health}/{self.max_health}."
    
    def take_hit(self, damage, damage_type, num_hits=1):
        
        # hits will only affect pokémon that are not knocked out

        if self.knocked_out == False:

            # based on the damage type and the type of pokémon, we deal full damage or half damage. Health cannot be less than 0, so if the damage would result in negative health, we set it as 0.

            if damage_type == self.type:
                self.current_health -= ((damage * 0.5) * num_hits)
                if self.current_health < 0:
                    self.current_health = 0
                print(f"{self.name} took {(damage * 0.5) * num_hits} in {damage_type} damage. Current health: {self.current_health}.")
            else:
                self.current_health -= (damage * num_hits)
                if self.current_health < 0:
                    self.current_health = 0
                print(f"{self.name} took {damage * num_hits} in {damage_type} damage. Current health: {self.current_health}.")

            # once the health is 0, the pokémon will be knocked out

            if self.current_health <= 0:
                self.knocked_out = True
                print(f"{self.name} is knocked out!")

        else:
            print(f"{self.name} is already knocked out and can't take more damage!")

        return self.knocked_out, self.current_health
        
    
    def heal(self, heal_item):
        
        # For now, healing simply increases the current health with the healing received. We can only heal damaged pokémon.

        if self.current_health < self.max_health:
            self.current_health += heal_item

            # Health is capped by max health (dependent on level), so if healing overshoots the max health, we set it to max health

            if self.current_health > self.max_health:
                self.current_health = self.max_health

            # if the pokemon was knocked out: after healing it no longer is

            self.knocked_out = False
            print(f"{self.name} has been healed to {self.current_health}")
            
        else:
            self.knocked_out = False
            print(f"{self.name} is already at max health!")
        
        return self.current_health

    def revive(self):

        # simple revive method to restore 1 health and change knocked out status

        if self.knocked_out:
            self.current_health = 1
            self.knocked_out = False
            print(f"{self.name} has been revived to {self.current_health}!")
        else:
            print(f"{self.name} isn't knocked out!")

    def attack(self, other, booster=0, num_hits=1):

        damage = self.level * 2 + booster
        damage_type = self.type      

        other.take_hit(damage, damage_type, num_hits)
            




test_pokemon = Pokemon('Twan', 5, 'fire')
test_pokemon2 = Pokemon('Peter', 5, 'fire')

#test_pokemon.take_hit(20, 'ice', 2)
#test_pokemon.take_hit(50, 'fire')
#test_pokemon.take_hit(10, 'fire')
#test_pokemon.heal(100)
#test_pokemon.heal(100)
#test_pokemon.take_hit(10, 'fire')
#test_pokemon.revive()

test_pokemon.attack(test_pokemon2)
test_pokemon.attack(test_pokemon2)
test_pokemon.attack(test_pokemon2)
test_pokemon.attack(test_pokemon2)
test_pokemon.attack(test_pokemon2)

test_pokemon.attack(test_pokemon2)
test_pokemon.attack(test_pokemon2)