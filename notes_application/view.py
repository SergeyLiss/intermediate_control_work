# Ввод/вывод в консоль

class InterfaceConsoleNotes():

    def __init__(self) -> None:
        pass

    #
    def idView(self, size):
        flag = False
        msg = ''
        while flag != True:
            msg = input("Введите id: ") 
            if self.controlInput(msg):
                try:
                    msg = int(msg)
                    if msg < size:
                        flag = True
                    else:
                        self.resultAllView(7)
                        return -1
                except ValueError:
                    self.resultAllView(7)
                    return -1
        return msg

    #
    def commandView(self):
        flag = False
        msg = ''
        while flag != True:
            msg = input("\nВведите команду: ")
            flag = self.controlInput(msg)
        return msg

    # Открытие файла
    def openFileView(self):
        flag = False
        msg = ''
        while flag != True:
            msg = input("Введите имя файла (без расширения): ")
            flag = self.controlInput(msg)
        return msg
    
    # Результаты работы методов: открыть файл, сохранить заметку, удалить заметку
    def resultAllView(self, cod, id=None):
        if cod == 1:
            print(f"Файл {id} открыт.")
        elif cod == 11:
            print(f"Файл {id} создан.")
        elif cod == 2:
            print(f"Заметка id={id} сохранена.")
        elif cod == 3:
            print(f"Заметка id={id} удалена.")
        elif cod == 4:
            print("Неправильная команда. Чтобы узнать список команд, введите команду 'h' или 'help' ...")
        elif cod == 41:
            print("Какая-то ошибка в commandSelection()")
        elif cod == 5:
            print(f"Заметка id={id} создана.")
        elif cod == 6:
            print(f"Заметка id={id} изменена.")
        elif cod == 7:
            print(f"Введите корректное id. Чтобы вывести список всех заметок введите команду 'rl' ...")
        else:
            print(f"Проблемка: {cod}...{id}")
    
    # Добавление заметки
    def addNoteView(self):
        listMsg = ['Введите заголовок заметки: ', 'Введите тело заметки: ']
        for i in listMsg:
            yield input(i)
    
    # Изменение заметки
    def writeNoteView(self, oldNote):
        listMsg = ['Старый заголовок заметки: ', 'Тело заметки: ']
        for j in range(2):
            listMsg[j] += oldNote[j] + '\n->    '
        for i in listMsg:
            yield input(i)
    
    # Чтение заметки
    def readNoteView(self, note):
        listMsg = ['Заметка id=','Дата создания/изменения: ','Заголовок заметки: ','Тело заметки: ']
        for i in range(4):
            print(listMsg[i] + str(note[i]))
        pass
    
    # Чтение всех заметок
    def readAllNoteView(self, notes):
        print('{:>4}{:>20}{:>16}{:>20}'.format('id','Дата созд./изм.','Заголовок','Тело заметки'))

        for i in range(len(notes)):
            titleFormat = notes[i][1]
            if len(titleFormat) > 12:
                titleFormat = titleFormat[:9] + '...'
            msgFormat = notes[i][2]
            if len(msgFormat) > 16:
                msgFormat = msgFormat[:9] + '...'
            print('{:>4}{:>20}{:>16}{:>20}'.format(i,notes[i][0],titleFormat,msgFormat))
        pass
    
    # Проверка на отсутствие пустой строки
    def controlInput(self, temp) -> bool:
        if temp != '':
            return True
        else:
            print("Вы ничего не ввели. Попробуйте снова...")
            return False
    
    #
    def commandHelpView(self):
        helpMsg = 'Список команд:\n\
                    o open             - открыть файл,\n\
                    s save c close     - сохранить файл,\n\
                    a add              - создать заметку,\n\
                    r read             - прочитать заметку,\n\
                    w write            - изменить заметку,\n\
                    d del delete       - удалить заметку,\n\
                    l list rl readlist - прочитать заметку,\n\
                    h help             - помощь по командам,\n\
                    e exit             - выход из программы.\n'
        print(helpMsg)
        