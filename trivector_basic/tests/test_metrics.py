import unittest
from mc6_grimoire import utilization, retention, objective

class MetricsTests(unittest.TestCase):
    def test_ratio(self): self.assertEqual(utilization(25,100), .25)
    def test_unknown(self): self.assertIsNone(utilization(None,100))
    def test_capacity_zero(self):
        with self.assertRaises(ValueError): utilization(1,0)
    def test_over_capacity(self):
        with self.assertRaises(ValueError): utilization(101,100)
    def test_nonfinite(self):
        with self.assertRaises(ValueError): utilization(float('nan'),100)
    def test_empty(self): self.assertEqual(retention([]), {'L':None,'Q':None})
    def test_partial(self): self.assertEqual(retention([True,False]), {'L':.5,'Q':.5})
    def test_nonboolean(self):
        with self.assertRaises(ValueError): retention([1])
    def test_objective(self): self.assertAlmostEqual(objective(.2,.5,2,1,.1),.9)
    def test_unknown_objective(self): self.assertIsNone(objective(None,0,1,1,1))
    def test_bad_loss(self):
        with self.assertRaises(ValueError): objective(0,2,1,1,1)

if __name__ == '__main__': unittest.main()
