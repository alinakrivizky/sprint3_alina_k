import datetime
from os import name
from webbrowser import get

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_check(self,name):
        if len(name) == 0 or len(name) > 20:
            raise ValueError('Нельзя добавить товар, если в' \
            ' его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        total_sum = sum(total)
        if len(self.__name_items) > 10:
                total_sum *= 0.9
        return total_sum
    def twenty_percent_tax(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
        for item in twenty_percent_tax:
            total.append(self.__item_price[item])
        total_sum = sum(total)
        if len(self.__name_items) > 10:
            total_sum *= 0.9
        tax= total_sum * 0.2
        return tax
    def ten_percent_tax(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
        for item in ten_percent_tax:
            total.append(self.__item_price[item])
        total_sum = sum(total)
        if len(self.__name_items) > 10:
            total_sum *= 0.9
        tax= total_sum * 0.1
        return tax
    def total_tax(self):
        total = self.twenty_percent_tax() + self.ten_percent_tax()
        return total
    @staticmethod
    def get_telephone_number(number):
         if not isinstance(number, str):
            raise TypeError('Номер телефона должен быть строкой')
         if len(str(number))!=10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
         return number

                

name_items = OnlineSalesRegisterCollector()
name_items.add_item_to_check('кола')
name_items.add_item_to_check('молоко')
name_items.add_item_to_check('кефир')
name_items.add_item_to_check('печенье')
name_items.add_item_to_check('чипсы')
print(name_items.name_items)
print(name_items.number_items)
print(name_items.check_amount())
print(name_items.twenty_percent_tax())
print(name_items.ten_percent_tax())
print(name_items.total_tax())
print(name_items.get_telephone_number('1234567890'))
    
            
