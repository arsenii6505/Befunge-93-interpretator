import unittest
from unittest.mock import MagicMock
from src.BefungeMachine import BefungeMachine
from src.Operations import Operations


class TestBefungeOperations(unittest.TestCase):

    def setUp(self):
        with unittest.mock.patch('src.BefungeReader.BefungeReader.load', return_value=[["@"]]):
            self.machine = BefungeMachine("dummy_path")
        self.machine.stack = []
        self.machine.pointerPos = [0, 0]
        self.machine.direction = "R"

    def test_stack_push_pop(self):
        self.machine.push_stack(10)
        self.machine.push_stack(20)
        self.assertEqual(self.machine.pop_stack(), 20)
        self.assertEqual(self.machine.pop_stack(), 10)
        self.assertEqual(self.machine.pop_stack(), 0)

    def test_arithmetic_add(self):
        self.machine.push_stack(3)
        self.machine.push_stack(5)
        Operations.add(self.machine)
        self.assertEqual(self.machine.stack[-1], 8)

    def test_arithmetic_sub(self):
        self.machine.push_stack(10)
        self.machine.push_stack(3)
        Operations.sub(self.machine)
        self.assertEqual(self.machine.stack[-1], 7)

    def test_arithmetic_div_by_zero(self):
        self.machine.push_stack(10)
        self.machine.push_stack(0)
        Operations.div(self.machine)
        self.assertEqual(self.machine.stack[-1], 0)

    def test_logic_greater(self):
        self.machine.push_stack(5)
        self.machine.push_stack(3)
        Operations.greater(self.machine)
        self.assertEqual(self.machine.stack[-1], 1)

    def test_movement_direction_change(self):
        Operations.move_d(self.machine)
        self.assertEqual(self.machine.direction, "D")
        self.assertEqual(self.machine.pointerPos, [1, 0])

    def test_horizontal_if(self):
        self.machine.push_stack(0)
        Operations.h_if(self.machine)
        self.assertEqual(self.machine.direction, "R")
        self.machine.push_stack(1)
        Operations.h_if(self.machine)
        self.assertEqual(self.machine.direction, "L")

    def test_bridge_skips_cell(self):
        self.machine.direction = "R"
        self.machine.pointerPos = [0, 0]
        Operations.bridge(self.machine)
        self.assertEqual(self.machine.pointerPos, [0, 2])

    def test_get_put_commands(self):
        self.machine.push_stack(65)
        self.machine.push_stack(2)
        self.machine.push_stack(2)
        Operations.g_put(self.machine)
        self.assertEqual(self.machine.map[2][2], 'A')
        self.machine.push_stack(2)
        self.machine.push_stack(2)
        Operations.g_get(self.machine)
        self.assertEqual(self.machine.pop_stack(), 65)

    def test_string_mode_toggle(self):
        self.assertFalse(self.machine.string_mode)
        Operations.toggle_string(self.machine)
        self.assertTrue(self.machine.string_mode)
        self.machine.invoke('H')
        self.assertEqual(self.machine.stack[-1], ord('H'))


if __name__ == '__main__':
    unittest.main()