# -*- coding: utf-8 -*-
"""Some test fixtures"""
import numpy as np
import pytest


@pytest.fixture()
def make_dataset():
    """Make a dataset with three targets"""
    return np.arange(0, 10, 1), np.arange(10, 20, 1)
