class StackOfPlates:
    def __init__(self):
        self.current_upper_stack_index = 0
        self.upper_stack = [[]]
        self.stack_limit = 5
        self.current_limit = 0

    def push(self, val):
        if self.current_limit < self.stack_limit:
            self.upper_stack[self.current_upper_stack_index].append(val)
            self.current_limit += 1
        else:
            self.current_upper_stack_index += 1
            self.upper_stack.append([val])
            self.current_limit = 1
    def pop(self):
        self.upper_stack[self.current_upper_stack_index].pop()
        self.current_limit -= 1

        if self.current_limit <= 0:
            self.upper_stack.pop()
            self.current_upper_stack_index -= 1
            self.current_limit = self.stack_limit

    def print_stack(self):
        print self.upper_stack

a = StackOfPlates()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)
a.push(7)
a.push(8)
a.push(9)
a.push(10)

a.push(11)
a.push(12)




a.print_stack()
4
