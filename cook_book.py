def cook_book(filename):
  cook_dict = {}
  with open(filename, encoding='utf8') as file_work:

    for line in file_work:
      dish_name = line.strip()
      counter = int(file_work.readline())
      list_of_ingredient = []

      for i in range(counter):
        temp_dict = {}
        ingredient = file_work.readline()
        ingredient = ingredient.strip().split('|')
        temp_dict['ingredient'] = ingredient[0].strip()
        temp_dict['quantity'] = int(ingredient[1])
        temp_dict['measure'] = ingredient[2].strip()
        list_of_ingredient.append(temp_dict)

      cook_dict[dish_name] = list_of_ingredient
      file_work.readline()
  return cook_dict

def get_shop_list_by_dishes(dishes, person_count):
  shop_book = {}
  for dish in dishes:
    for recipe, parts in cook_book('recipes.txt').items():
      if dish == recipe:
        for ing in cook_book('recipes.txt')[recipe]:
          shop_book[ing['ingredient']] = {'measure': ing['measure'], 'quantity': ing['quantity'] * person_count}
  return shop_book

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
