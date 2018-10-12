import unittest
from context import app
from app.solver import solver, solver_raw
from parameterized import parameterized


def convert_and_call(color, customers, demand, solver):
    return solver({"colors": color, "customers": customers, "demands": demand})


class PaintShopTest(unittest.TestCase):

    @parameterized.expand([[solver], [solver_raw]])
    def test_impossible(self, solver):
        demand = [[1, 1, 0], [1, 1, 1]]
        self.assertEqual(convert_and_call(1, 2, demand, solver=solver), "IMPOSSIBLE")

    @parameterized.expand([[solver], [solver_raw]])
    def test_no_matte(self, solver):
        demand = [[1, 1, 0], [1, 2, 0]]
        self.assertEqual(convert_and_call(2, 2, demand, solver=solver), "0 0")

    @parameterized.expand([[solver], [solver_raw]])
    def test_all_matte(self, solver):
        demand = [[1, 1, 1], [2, 1, 0, 2, 1], [3, 1, 0, 2, 0, 3, 1]]
        self.assertEqual(convert_and_call(3, 3, demand, solver=solver), "1 1 1")

    @parameterized.expand([[solver], [solver_raw]])
    def test_color_not_requested(self, solver):
        demand = [[1, 5, 1], [2, 1, 0, 2, 1]]
        self.assertEqual(convert_and_call(5, 2, demand, solver=solver), "0 0 0 0 1")

    @parameterized.expand([[solver], [solver_raw]])
    def test_color_opposite_tastes(self, solver):
        demand = [[2, 1, 0, 2, 1], [2, 1, 1, 2, 0]]
        self.assertEqual(convert_and_call(2, 2, demand, solver=solver), "0 0")

    @parameterized.expand([[solver], [solver_raw]])
    def test_color_many_conflicts_between_tastes_but_solution_exists(self, solver):
        demand = [[2, 1, 1, 3, 0], [1, 2, 1], [2, 2, 0, 3, 1]]
        self.assertEqual(convert_and_call(4, 3, demand, solver=solver), "1 1 1 0")


if __name__ == "__main__":
     unittest.main()