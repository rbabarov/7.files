def create_cook_book(file):
    cook_book = {}
    name_dish = ''
    list_indigrients = []
    str_indigrient = {}

    doc_file = open(file, 'r', encoding="utf-8")
    lines = doc_file.readlines()

    for line in lines:
        line = line.replace('\n', '')
        splitarray = line.split('|')

        if line != '' and len(splitarray) < 2 and not line.isdigit():
            print(line, ' Обнаруженно название')
            name_dish = line
        elif line.isdigit():
            print(line, ' в строке одни цифры')
        elif len(splitarray) > 2:
            print(line, ' в этой строке индигриенты')
            for str_ in splitarray:

            str_indigrient




cook_book = create_cook_book('recipes.txt')

