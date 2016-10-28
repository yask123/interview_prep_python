[0 0 0 0 0 0 0 0 0]
       ^   ^   ^

class ThreeStack:
    def __init__(self, n):
        self.stack = [0] * n
        self.first_pointer = 0
        self.second_pointer = first_pointer + n/3
        self.third_pointer = second_poiner + n/3

    def push_first(val):
        if (self.is_first_full()):
            shift_by_one(second_poiner)

        self.first_pointer += 1
        self.stack[first_pointer % n] = val

    def push_second(val):
        if (self.is_second_full()):
            shift_by_one(third_poiner)

        self.second_pointer += 1
        self.stack[second_pointer % n] = val

    def push_third(val):
        if (self.is_third_full()):
            shift_by_one(first_pointer)

        self.third_pointer += 1
        self.stack[third_pointer % n] = val

    def shift_by_one(pointer):-
