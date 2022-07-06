from character import Character

hero = Character("tilly", "super dead")

hero.set_power("permently tired")

hero.get_power()

print(f"{hero.real_name} is actually the hero {hero.superhero_name} and her power is {hero.power}")

# example
spidey = Character("peter parker", "spiderman")
spidey.set_power2("web-slinging")
spidey.get_power

print(f"{spidey.real_name} is actually the hero {spidey.superhero_name} and his power is {spidey.power}")