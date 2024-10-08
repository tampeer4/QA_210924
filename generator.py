# №1(Пример из треда)
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
simple_generator = (digit for digit in numbers if digit % 3 == 0)

for digit in simple_generator:
    print(digit)

print(list(simple_generator))



# №2
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
simple_generator = [digit for digit in numbers if digit % 3 == 0]

for digit in simple_generator:
    print(digit)

print(list(simple_generator))

'''
Генератор — это объект, который возвращает элементы поочерёдно, 
не сохраняя всю последовательность в памяти. 
Он "ленивый": вычисляет следующий элемент только тогда, 
когда это нужно, что экономит память.

В нашем случае simple_generator создаёт генераторное выражение, 
которое перебирает числа из списка numbers и выдаёт только те из них, 
которые делятся на 3.


Когда этот цикл выполняется:

1. Цикл запрашивает первый элемент у генератора.
2. Генератор начинает с начала списка numbers и проверяет каждое число, делится ли оно на 3.
3. Если число делится на 3, оно возвращается циклу и распечатывается.
4. Процесс повторяется до конца списка.

Советую прогнать в https://pythontutor.com/render.html#mode=edit по шагам


- Под капотом:

Под капотом, генератор сохраняет своё текущее состояние. Например, он "помнит", 
до какого элемента в списке он уже добрался. В тот момент, когда вы запрашиваете 
следующий элемент, он продолжает с того места, где остановился, до тех пор, 
пока список не будет полностью обработан.


Когда вы пытаетесь снова вывести элементы из генератора с помощью print(list(simple_generator)), 
он уже пуст. Почему? Потому что генераторы можно итерировать только один раз. 
После того как цикл for завершился, генератор исчерпал все свои элементы. 
Повторный вызов list(simple_generator) приводит к пустому списку, так как внутри 
генератора больше не осталось элементов.

Чтобы избежать этой ситуации и иметь возможность использовать отфильтрованные данные 
неоднократно, преобразуйте генератор в список сразу №2
'''