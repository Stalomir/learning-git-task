
shopping_list = {'wędkarski':['wędka','haczyk','robak','granat'], 'malarski':['pędzel','wałek', 'farba','granat'],
'warzywniak':['cukinia','bakłażan','kabaczek','granat']}
item_number = 0
for k in shopping_list:
    shopping_list[k] = [i.capitalize() for i in shopping_list[k]]
    item_number = item_number + len(shopping_list[k])
[print("\033[1;37mIdę do",k.title(),"i kupuję tam",v) for k, v in shopping_list.items()]
print("\033[1;31mW sumie kupuję",item_number,"produktów")
print('\033[0mKolejny commit wg polecenia')


