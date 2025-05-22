class Tester:

    def __init__(self, name): # Исправлено: __init__ - это конструктор
        self.name = name        # Исправлено: сохраняем имя в атрибуте объекта
        self.deadline = True    # Исправлено: устанавливаем deadline по умолчанию True

    def work_hard(self, deadline=True):
        if deadline:                # Исправлено: используем параметр deadline
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False) # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'
