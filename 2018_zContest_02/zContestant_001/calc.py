class Calc:
    ops = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y,
           '%': lambda x, y: x % y}

    def __init__(self):
        self.left_operand = 0
        self.operator = '+'
        self.right_operand = 0
        self.expr = ''

    def calc(self):
        try:
            self.left_operand, self.operator, self.right_operand = self.expr.split()
            self.left_operand = float(self.left_operand)
            self.right_operand = float(self.right_operand)
            return Calc.ops[self.operator](self.left_operand, self.right_operand)

        except ValueError as ve:
            if 'not enough values to unpack' in str(ve):
                print('Please enter expression terms separated by space')
            else:
                print('Invalid Operand: ', ve)
        except KeyError as ke:
            print('Invalid operator: ', ke)

    def get_expr(self):
        self.expr = input('Arithmetic Expression: ')
        return self.expr


def menu():
    while True:
        print('1.) Enter Expression: ')
        print('2.) Done')
        op = input('Operation: ')
        if op in ['1', '2']:
            break
    return op


if __name__ == '__main__':
    calc = Calc()
    ch = menu()
    while ch != '2':
        if calc.get_expr().lower() == 'q': break
        print('result: ', calc.calc())
        ch = menu()
