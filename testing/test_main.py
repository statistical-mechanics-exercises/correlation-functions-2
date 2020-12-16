import unittest
import numpy as np
from main import *

class UnitTests(unittest.TestCase) :
    def test_spin_var(self) :
        for i in range(2,7) :
            for j in range(2^i) :
                num, spins = j, i*[0]
                for k in range(i) :
                    spins[k] = np.floor( num / 2**(4-k) )
                    num = num - spins[k]*2**(4-k)
                    if spins[k]==0 : spins[k] = -1
                av2, average = 0, sum(spins) / len(spins)
                for k in range(i) : av2 = av2 + (spins[k] - average)**2
                self.assertTrue( np.abs(av2/len(spins) - variance_spin(spins))<1e-7, "The variance that has been calculated by your program is wrong" )
