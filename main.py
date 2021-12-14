def create_cook_book(file):
    cook_book = {}
    name_dish = ''
    list_indigrients = []
    #str_indigrient = {}

    with open(file, 'r', encoding="utf-8") as doc_file:

        for line in doc_file:
            print(line)
            line = line.strip()
            if line != '' and not line.isdigit():
                name_dish = line
            elif line.isdigit():
                count = int(line)
                #раз в этой строке количество индигриетов в блюде,
                # значит дальше будет Х строк с индигриентами
                for x in range(count):

                    lstind = doc_file.readline().strip()
                    splitarray = lstind.split('|')
                    #print(splitarray)
                    str_indigrient = {}
                    str_indigrient['ingredient_name'] = splitarray[0]
                    str_indigrient['quantity'] = int(splitarray[1])
                    str_indigrient['measure'] = splitarray[2]
                    list_indigrients += [str_indigrient]
                #print(list_indigrients)

                try:
                    cook_book[name_dish] += list_indigrients
                except:
                    cook_book[name_dish] = list_indigrients

    return cook_book






cook_book = create_cook_book('recipes.txt')
print(cook_book)

