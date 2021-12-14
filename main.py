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

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book('recipes.txt')
    shop_list_by_dishes = {}
    for dishe in dishes:
        if dishe in cook_book:
            for indigrient in cook_book[dishe]:
                shop_list_by_dishes[indigrient['ingredient_name']] = {'measure': indigrient['measure'], 'quantity': indigrient['quantity']*person_count}
    return shop_list_by_dishes







cook_book = create_cook_book('recipes.txt')
#print(cook_book)
shop_list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list_by_dishes)
