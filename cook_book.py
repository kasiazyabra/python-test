def cook_book():
  with open('recipes.txt') as f:
    book = {}
    for i in range(3):
      dish = f.readline().strip()
      ingnum = int(f.readline().strip())
      ilist = []
      for i in range(0,ingnum):
        line = f.readline().strip().split(' | ')
        idict = {}
        idict.setdefault('ingredient_name', str(line[0]))
        idict.setdefault('quantity', int(line[1]))
        idict.setdefault('measure', str(line[2]))
        ilist.append(idict)
      book.setdefault(str(dish), ilist)
      f.readline().strip()
  return book

def get_shop_list_by_dishes(dishes, person_count):
  shop_book = {}
  for dish in dishes:
    for recipe, parts in cook_book().items():
      if dish == recipe:
        for ing in cook_book()[recipe]:
          shop_book[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': ing['quantity'] * person_count}
  print(shop_book)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

