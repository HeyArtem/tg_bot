import random

'''
Здесь напишу функцию которую буду активировать в боте
'''

# функция выбирает двух неповторяющихся победителей из списка словарей
def raffle_prizes():
    my_list = [
        {'u1': 'Zina'},
        {'u2': 'Sony'},
        {'u3': 'Andre'},
        {'u4': 'Sokrat'},
        {'u5': 'Platon'},
        {'u6': 'Aristotel'}
    ]
    
    # выбираю двух победителей
    winners = random.sample(my_list, 2)
    print(winners)
    return winners
    
    
# def main():
#     raffle_prizes()


# if __name__ == '__main__':
#     main()
