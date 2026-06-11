
class AST:
    def __init__(self, text):
        self.text = text
        self.sep_text = None
        self.line_pos = 0
        self.tree = {}

    def separate(self):
        lst_of_lines = self.text.strip('\n').rstrip().split('\n')
        for n, line in enumerate(lst_of_lines, start=0):
            lst_of_lines[n] = line.rstrip().split(' ')
        self.sep_text = lst_of_lines

    def __key_value(self, n):
        line = self.sep_text[n]
        key_ind = 0
        min_sign = 0
        for el in line:
            if el == '-':
                min_sign = line.index(el)
            if ':' in el:
                key_ind = line.index(el)
        key = ' '.join(line[min_sign + 1:key_ind + 1]).strip(' ')
        value = ' '.join(line[key_ind + 1:]).strip(' ')
        if value == '':
            raise TypeError("Пустое значение")
        return {key.strip(':'): value}

    def __name_of_dl(self, n):
        line = self.sep_text[n]
        num_of_spaces = line.count('')
        key_ind = 0
        for el in line:
            if el == '-':
                min_sign = line.index(el)
                for el_ in line:
                    if ':' in el_:
                        key_ind = line.index(el_)
                key = ' '.join(line[min_sign + 1:key_ind + 1]).strip(' ')

                return {key[:-1]: num_of_spaces}
            elif ':' in el:
                key_ind = line.index(el)
                key = ' '.join(line[:key_ind + 1]).strip(' ')
                return {key[:-1]: num_of_spaces}
        raise TypeError("Элемент не является именем списка/словаря")

    def read_lines(self):
        self.separate()
        dict_of_curr_name_of_dl = {}
        # print(lst_of_curr_name_of_dl, 'lst', 0)
        for n, line in enumerate(self.sep_text):
            num_of_spaces = line.count('')
            try:
                print(1 / 0)
                # self.tree.update(self.__key_value(n))
            except:  # идея проверки на такую же строку, что и в self.__name_of_dl

                # ищет словари, которые были до этого
                # TODO определить, что делать со словарем dict_of_curr_name_of_dl после начала строки с 0 пробелов
                if dict_of_curr_name_of_dl[n].keys() != self.__name_of_dl(n).keys():
                    if dict_of_curr_name_of_dl != {}:  # не пустой словарь
                        for name, n_o_s in reversed(dict_of_curr_name_of_dl.items()):
                            if n_o_s == num_of_spaces:
                                print(name)
                    else:  # пустой словарь
                        pass


                # реализовано создание новых словарей/списков
                elif dict_of_curr_name_of_dl[n].keys() == self.__name_of_dl(n).keys():
                    self.tree.update(self.__name_of_dl(n))
                    print(dict_of_curr_name_of_dl[n].keys(), 'curr')
                    print(self.__name_of_dl(n).keys(), 'all')
            self.line_pos += 1


A = AST('''
- g1: f1
  h2: 2
- g2: f2
  g3: f3
tmp:
  sg:
   h: 1     
''')
A.read_lines()
print(A.tree, 'tree')
