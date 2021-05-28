################### Scope ####################
#
# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# player_health = 10
#
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(potion_strength)
#         print(player_health)
#
#     drink_potion()


#
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
#
#     print(new_enemy)

enemies = 1

def increase_enemies():
    global enemies 
    enemies = enemies + 1
    print(f"enemies inside function: {enemies}")



increase_enemies()
print(f"enemies inside function: {enemies}")

