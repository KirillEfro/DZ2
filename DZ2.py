#Задача 1,2
'''
with open('recipes.txt', 'rt') as file:
    cookbook = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline().strip())
        recipe = []
        for _ in range(ingredients_count):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            recipe.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure':  measure

            })
        file.readline()
        cookbook[dish_name] = recipe
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cookbook[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] +=\
                new_shop_list_item['quantity']
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
'''
'''
#Задание 3
files = ['1.txt', '2.txt', '3.txt']
file_info = [(filename, sum(1 for line in open(filename))) for filename in files]
file_info_sorted = sorted(file_info, key=lambda x: x[1])
with open('result.txt', 'w') as f:
    # проходим по отсортированному списку и записываем содержимое каждого файла
    for filename, lines_count in file_info_sorted:
        # записываем служебную информацию
        f.write(filename + '\n')
        f.write(str(lines_count) + '\n')
        # записываем содержимое файла
        with open(filename) as input_file:
            f.writelines(input_file.readlines())
            f.write('\n')
'''