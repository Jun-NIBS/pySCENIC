# coding=utf-8

import pytest
import numpy as np
from pyscenic.math import masked_rho, masked_rho_2d


def test_masked_rho():
    x = np.array([1, 2, -1, 0.0, 4], dtype=np.float)
    y = np.array([1, 2, 0.0, -8, 4],  dtype=np.float)
    assert pytest.approx(masked_rho(x, y, 0.0), 0.00001) == np.corrcoef(np.array([1.0, 2.0, 4.0]), np.array([1.0, 2.0, 4.0]))[0, 1]

