class Truck:
    def __init__(self, max_fuel, km_per_liter, repair_price_per_km, brand):
        self.max_fuel = max_fuel
        self.km_per_liter = km_per_liter
        self.repair_price_per_km = repair_price_per_km
        self.brand = brand
        self.total_repair_price = 0
        self.current_fuel = max_fuel

        self.total_km_driven = 0
        self.max_wheel_damage = 100
        self.wheel_damage = 0

        self.mental_health = 100

    def remaining_distance(self):
        return (self.max_fuel * self.km_per_liter) - self.total_km_driven

    def consume_fuel(self, fuel):
        print(f"The fuel consumption {fuel}")
        self.current_fuel -= fuel
        print(f"The current fuel amount {self.current_fuel}")
        self.total_km_driven += fuel * self.km_per_liter
        print(f"The total km that the truck drove {self.total_km_driven}")
        if self.current_fuel <= 0:
            print("The fuel has run out, causing the truck to stop, and it cannot continue the ride.")
            return False
        return True

    def update_wheel_damage(self, damage, length):
        print(f"The wheel damage {damage}")
        self.wheel_damage += damage
        print(f"The total wheel damage {self.wheel_damage}")
        self.total_repair_price += self.repair_price_per_km * self.wheel_damage
        print(f"The total repair wheels price until now {self.total_repair_price}")
        if self.wheel_damage >= 100:
            print("The wheel sustained maximum damage!,Truck stopped and can't continue the ride")
            return False
        return True

    def update_mental_health(self, change):
        print(f"The mental health effect {change}")
        self.mental_health += change
        print(f"The driver mental health {self.mental_health}")
        if self.mental_health <= 0:
            print("The driver died!!!!")
            return False
        return True

    def apply_terrain_effects(self, road, length):
        self.update_mental_health(road.mental_effect)
        self.update_wheel_damage(road.wheel_damage_effect, length)
        self.consume_fuel(length / self.km_per_liter)
