from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자
menu = Menu()
coffee_make = CoffeeMaker()
money_machine = MoneyMachine()

# print(menu.get_items())       # 결과값 : latte / espresso / cappuccino / 카라멜마키아토 /
# menu.py의 get_items 메서드 확인하기

is_on = True
# print(menu.menu)
# 현재 상황에서 menu.menu를 활용하여 espresso라는 str을 추출하려면 어떡해야 하나요?
# print(menu.menu[1].name)            # menu(객체).menu(리스트)[1](리스트 번지 수).name(객체.리스트[1]의 이름)
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? >>> {menu.get_items()}')
    if choice == '종료':
        is_on = False
        print('자판기를 종료합니다. 🎈')
    elif choice == 'report':
        coffee_make.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_make.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_make.make_coffee(drink)