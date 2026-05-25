import random

class Operations:
    direction_map = {
        "L": [0, -1],
        "R": [0, 1],
        "U": [-1, 0],
        "D": [1, 0]
    }

    @staticmethod
    def empty_operation(machine):
        dy, dx = Operations.direction_map[machine.direction]
        machine.pointerPos[0] = (machine.pointerPos[0] + dy) % machine.mapSize[0]
        machine.pointerPos[1] = (machine.pointerPos[1] + dx) % machine.mapSize[1]

    @staticmethod
    def move_r(m):
        m.change_direction("R")
        Operations.empty_operation(m)

    @staticmethod
    def move_l(m):
        m.change_direction("L")
        Operations.empty_operation(m)

    @staticmethod
    def move_u(m):
        m.change_direction("U")
        Operations.empty_operation(m)

    @staticmethod
    def move_d(m):
        m.change_direction("D")
        Operations.empty_operation(m)

    @staticmethod
    def move_random(m):
        m.change_direction(random.choice(["R", "L", "U", "D"]))
        Operations.empty_operation(m)

    @staticmethod
    def add(m):
        a, b = m.pop_stack(), m.pop_stack()
        m.push_stack(a + b)
        Operations.empty_operation(m)

    @staticmethod
    def sub(m):
        a, b = m.pop_stack(), m.pop_stack()
        m.push_stack(b - a)
        Operations.empty_operation(m)

    @staticmethod
    def mul(m):
        a, b = m.pop_stack(), m.pop_stack()
        m.push_stack(a * b)
        Operations.empty_operation(m)

    @staticmethod
    def div(m):
        a, b = m.pop_stack(), m.pop_stack()
        m.push_stack(b // a if a != 0 else 0)
        Operations.empty_operation(m)

    @staticmethod
    def mod(m):
        a, b = m.pop_stack(), m.pop_stack()
        m.push_stack(b % a if a != 0 else 0)
        Operations.empty_operation(m)

    @staticmethod
    def b_not(m):
        val = m.pop_stack()
        m.push_stack(1 if val == 0 else 0)
        Operations.empty_operation(m)

    @staticmethod
    def greater(m):
        a, b = m.pop_stack(), m.pop_stack()
        m.push_stack(1 if b > a else 0)
        Operations.empty_operation(m)

    @staticmethod
    def h_if(m):
        m.change_direction("R" if m.pop_stack() == 0 else "L")
        Operations.empty_operation(m)

    @staticmethod
    def v_if(m):
        m.change_direction("D" if m.pop_stack() == 0 else "U")
        Operations.empty_operation(m)

    @staticmethod
    def dup(m):
        val = m.pop_stack()
        m.push_stack(val)
        m.push_stack(val)
        Operations.empty_operation(m)

    @staticmethod
    def swap(m):
        a, b = m.pop_stack(), m.pop_stack()
        m.push_stack(a)
        m.push_stack(b)
        Operations.empty_operation(m)

    @staticmethod
    def pop(m):
        m.pop_stack()
        Operations.empty_operation(m)

    @staticmethod
    def out_int(m):
        m.print_int_output(m.pop_stack())
        Operations.empty_operation(m)

    @staticmethod
    def out_asc(m):
        m.print_output(chr(m.pop_stack()))
        Operations.empty_operation(m)

    @staticmethod
    def in_int(m):
        m.push_stack(m.get_int_input())
        Operations.empty_operation(m)

    @staticmethod
    def in_asc(m):
        char = m.get_input()
        m.push_stack(ord(char) if char else -1)
        Operations.empty_operation(m)

    @staticmethod
    def g_put(m):
        y, x, v = m.pop_stack(), m.pop_stack(), m.pop_stack()
        m.set_map(y, x, v)
        Operations.empty_operation(m)

    @staticmethod
    def g_get(m):
        y, x = m.pop_stack(), m.pop_stack()
        m.push_stack(m.get_map(y, x))
        Operations.empty_operation(m)

    @staticmethod
    def bridge(m):
        Operations.empty_operation(m)
        Operations.empty_operation(m)

    @staticmethod
    def toggle_string(m):
        m.string_mode = not m.string_mode
        Operations.empty_operation(m)

    @staticmethod
    def end(m):
        m.activated = False

MAP = {
    '>': Operations.move_r,
    '<': Operations.move_l,
    '^': Operations.move_u,
    'v': Operations.move_d,
    '?': Operations.move_random,
    '+': Operations.add,
    '-': Operations.sub,
    '*': Operations.mul,
    '/': Operations.div,
    '%': Operations.mod,
    '!': Operations.b_not,
    '`': Operations.greater,
    '_': Operations.h_if,
    '|': Operations.v_if,
    ':': Operations.dup,
    '\\': Operations.swap,
    '$': Operations.pop,
    '.': Operations.out_int,
    ',': Operations.out_asc,
    '&': Operations.in_int,
    '~': Operations.in_asc,
    'p': Operations.g_put,
    'g': Operations.g_get,
    '#': Operations.bridge,
    '"': Operations.toggle_string,
    '@': Operations.end,
    ' ': Operations.empty_operation
}