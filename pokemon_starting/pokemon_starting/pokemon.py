class Pokemon:
    def __init__(self, name_, level_, type_):
        self.name = name_
        self.level = level_
        self.type = type_
        self.max_health = (self.level*10)
        self.current_health = self.max_health
        self.knocked_out = False
        
    
    def __repr__(self):
        return f"{self.name} is a level {self.level} {self.type} Pokémon. Health: {self.current_health}/{self.max_health}."
    
    def take_hit(self, damage, damage_type):
        
        # based on the damage type and the type of pokémon, we deal full damage or half damage. Health cannot be less than 0, so if the damage would result in negative health, we set it as 0.

        if damage_type == self.type:
            self.current_health -= (damage * 0.5)
            if self.current_health < 0:
                self.current_health = 0
            print(f"{self.name} took {damage * 0.5} in {damage_type} damage. It's not very effective. Current health: {self.current_health}.")
        elif (self.type == 'water' and damage_type == 'fire') or (self.type == 'grass' and damage_type == 'water') or (self.type == 'fire' and damage_type== 'grass'):
            self.current_health -= damage 
            if self.current_health < 0:
                self.current_health = 0
            print(f"{self.name} took {damage} in {damage_type} damage. Current health: {self.current_health}.")
        else:
            self.current_health -= (damage * 2)
            if self.current_health < 0:
                self.current_health = 0
            print(f"{self.name} took {damage * 2} in {damage_type} damage. It's very effective! Current health: {self.current_health}.")

        # once the health is 0, the pokémon will be knocked out

        if self.current_health <= 0:
            self.knocked_out = True
            print(f"{self.name} is knocked out!")

        return self.knocked_out, self.current_health
        
    
    def heal(self, heal_item):
        
        # For now, healing simply increases the current health with the healing received. We can only heal damaged pokémon.
        if self.current_health == 0:
            print(f"{self.name} is knocked out and has to be revived first!")
            return heal_item

        elif self.current_health < self.max_health:
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

    def revenge(self, other):

        # revives the pokemon to 1 health and automatically strikes back at another pokemon for double damage

        if self.knocked_out:
            self.current_health = 1
            self.knocked_out = False
            print(f"{self.name} has been revived to {self.current_health}!")
            damage = (self.level * 2) * 2
            damage_type = self.type
            print(f"{self.name} takes out revenge on {other.name}!")
            other.take_hit(damage, damage_type)
        else:
            print(f"{self.name} isn't knocked out!")

    def attack(self, other, booster=0):

        # check to see if either pokemon is knocked out

        if not self.knocked_out and not other.knocked_out:
            
            damage = self.level * 2 + booster
            damage_type = self.type
            print(f"{self.name} attacks {other.name}!")
            other.take_hit(damage, damage_type)    
            
        elif other.knocked_out:
            print(f"{other.name} is already knocked out and cannot be attacked!")
        
        else:
            print(f"{self.name} is knocked out and cannot attack!")
            


test_pokemon = Pokemon('Twan', 5, 'fire')
test_pokemon2 = Pokemon('Peter', 5, 'grass')

#test_pokemon.take_hit(20, 'ice', 2)
#test_pokemon.take_hit(50, 'fire')
#test_pokemon.take_hit(10, 'fire')
#test_pokemon.heal(100)
#test_pokemon.heal(100)
#test_pokemon.take_hit(10, 'fire')
#test_pokemon.revive()

test_pokemon.attack(test_pokemon2)
test_pokemon.attack(test_pokemon2)
test_pokemon2.attack(test_pokemon)
test_pokemon.attack(test_pokemon2)
test_pokemon2.heal(10)
test_pokemon2.revenge(test_pokemon)
print(test_pokemon2)
test_pokemon2.attack(test_pokemon)
test_pokemon2.attack(test_pokemon)
test_pokemon2.attack(test_pokemon)
test_pokemon.revenge(test_pokemon2)