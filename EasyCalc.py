what = input('что будем делать ? (+, -, *, /, **, //): ')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
if what == '+':
    c = a + b
elif what == '-':
    c = a - b
elif what == '*':
    c = a * b
elif what == '/':
    c = a / b
elif what == '**':
    c = a ** b
elif what == '//':
    c = a // b
else:
    print('такой функции пока нет')

print(f'Результат :{c}')
# программировать на самом деле весело, главное знать как это делать
