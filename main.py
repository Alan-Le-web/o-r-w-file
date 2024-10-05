with open('file.txt', encoding='utf-8') as file:
    recipes_dict = {}
    dish = None
    ingr = []
    
    for line in file:
        line = line.strip()
        if not line: 
            if dish:
                recipes_dict[dish] = ingr
                dish = None
                ingr = []
            continue
        
        if dish is None:
            dish = line
        else:
            parts = line.split('|')
            if len(parts) >= 3:
                ingr_name = parts[0].strip()  # Название ингредиента
                quantity = parts[1].strip()  # Количество
                unit = parts[2].strip()  # Единица измерения
                ingr.append({
                    'ingredient_name': ingr_name,
                    'quantity': quantity,
                    'measure': unit
                })

    if dish:
        recipes_dict[dish] = ingr

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        if dish in recipes_dict:
            for ingredient in recipes_dict[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity']
                measure = ingredient['measure']
                total_quantity = int(quantity) * person_count
                
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += total_quantity
                else:
                    shop_list[ingredient_name] = {
                        'quantity': total_quantity,
                        'measure': measure
                    }
    
    return shop_list

result = get_shop_list_by_dishes(['Суп'], 2)
print(result)
