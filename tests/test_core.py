import math
import unittest
from describe import describe,quantile
class StatisticsTests(unittest.TestCase):
    def test_variance_conventions(self):
        r=describe([1,2,3,4]);self.assertAlmostEqual(r['sample_sd']**2,5/3)
        self.assertAlmostEqual(r['population_sd']**2,1.25)
    def test_interpolated_quartiles(self):
        self.assertEqual(quantile([1,2,3,4],.25),1.75)
        self.assertEqual(quantile([1,2,3,4],.75),3.25)
    def test_outlier_boundary(self):
        self.assertEqual(describe([0,0,0,0,20])['outlier_count'],1)
    def test_modes(self):self.assertEqual(describe([1,1,2,2])['modes'],[1.,2.])
    def test_invalid(self):
        for x in [[],[1],[1,float('nan')],[1,float('inf')]]:
            with self.assertRaises(ValueError):describe(x)
if __name__=='__main__':unittest.main()
