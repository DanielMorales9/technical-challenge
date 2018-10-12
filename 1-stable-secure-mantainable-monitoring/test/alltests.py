import unittest
from test_solver import PaintShopTest

# Run test cases first
suite = unittest.TestLoader().discover("test")
result = unittest.TextTestRunner(verbosity=2).run(suite)
