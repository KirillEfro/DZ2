
#Задание 1,2
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def split_text(text):
    return [i.splitlines() for i in text.split('\n\n')]


def split_ingredients_data(lst):
    return lst[:1] + [i.replace(' ', '').split('|') for i in lst[2:]]


def lst_to_dict(lst):
    return {lst[0]: [{'ingredient_name': i[0], 'quantity': int(i[1]), 'measure': i[2]} for i in lst[1:]]}


def data_loads(file_path):
    out = {}
    text = read_file(file_path)
    dish_list = split_text(text)
    format_dish_list = [split_ingredients_data(i) for i in dish_list]
    for i in format_dish_list:
        out.update(lst_to_dict(i))
    return out


res = data_loads('recipes.txt')

print(res)
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