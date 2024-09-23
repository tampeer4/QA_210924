def counter():
    count = 0
    def increment():
        nonlocal count  
        count += 1
        return count
    return increment

inc = counter()
print(inc())  
print(inc())  

# -----------------------------------------------------------

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter.increment()) 
print(counter.increment()) 

'''
Использование инструкций global и nonlocal в Python является довольно редким 
и считается признаком нехорошего стиля программирования. 

Основная причина заключается в том, что они нарушают принцип локальности, 
делая код менее предсказуемым и трудным для понимания и тестирования.

Сделать вывод можно посмотрев на две реализации, что лучше выглядит?
Вывод очевиден думаю.

Код с минимальным использованием глобальных 
переменных более предсказуем и читабелен, так как вся необходимая 
информация передается через параметры и возвраты.
'''