#Задача 1
def create_cook_book(file):
    cook_book = {}
    str_indigrient = {}
    with open(file, 'r', encoding="utf-8") as doc_file:

        for line in doc_file:
            line = line.strip()
            if line != '' and not line.isdigit():
                name_dish = line
                cook_book[name_dish] = []
            elif line.isdigit():
                count = int(line)
                list_indigrients = []
                #раз в этой строке количество индигриетов в блюде,
                # значит дальше будет Х строк с индигриентами
                for x in range(count):

                    lstind = doc_file.readline().strip()
                    splitarray = lstind.split('|')
                    str_indigrient = {}
                    str_indigrient['ingredient_name'] = splitarray[0].strip()
                    str_indigrient['quantity'] = int(splitarray[1])
                    str_indigrient['measure'] = splitarray[2].strip()
                    splitarray = []
                    list_indigrients += [str_indigrient]

                cook_book[name_dish] += list_indigrients


    return cook_book
#Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book('recipes.txt')
    shop_list_by_dishes = {}
    for dishe in dishes:
        if dishe in cook_book:
            for indigrient in cook_book[dishe]:
                if indigrient['ingredient_name'] in shop_list_by_dishes.keys():
                    oldquantity = shop_list_by_dishes[indigrient['ingredient_name']]['quantity']
                    newquantity = oldquantity + indigrient['quantity']*person_count
                    shop_list_by_dishes[indigrient['ingredient_name']] = {'measure': indigrient['measure'], 'quantity': newquantity}
                else:
                    shop_list_by_dishes[indigrient['ingredient_name']] = {'measure': indigrient['measure'],
                                                                           'quantity': indigrient[
                                                                                           'quantity'] * person_count}
    return shop_list_by_dishes

cook_book = create_cook_book('recipes.txt')
#print(cook_book)
shop_list_by_dishes = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
#print(shop_list_by_dishes)


#Задача 3

file_open1 = open('1.txt', 'r', encoding='utf-8')
file1 = file_open1.readlines()
file_open2 = open('2.txt', 'r', encoding='utf-8')
file2 = file_open2.readlines()
file_open3 = open('3.txt', 'r', encoding='utf-8')
file3 = file_open3.readlines()

input = open('input.txt', 'w')
input.close()

list_file = {'1.txt': file1, '2.txt': file2, '3.txt': file3}
sorted_values = sorted(list_file.values(), reverse=True)
sorted_dict = {}

for i in sorted_values:
    for k in list_file.keys():
        if list_file[k] == i:
            sorted_dict[k] = list_file[k]
            break

def write_file(text, linebreak = False):
    if linebreak:
        text += '\n'
    with open('input.txt', 'a') as f:
        f.write(text)

for key,value in sorted_dict.items():
    write_file('\n')
    write_file(key, True)
    write_file(str(len(list_file[key])), True)
    for line in value:
        write_file(line)


print(open('input.txt', 'r').read())
file_open1.close()
file_open2.close()
file_open3.close()

