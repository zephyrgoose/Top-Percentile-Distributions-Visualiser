import matplotlib
matplotlib.use('Agg')

import numpy as np
from scipy.stats import norm
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from visualise_distributions import visualise_distributions


def test_ratio_no_difference():
    result = visualise_distributions(0, 10)
    assert np.isclose(result["ratio"], 1.0)
    assert np.isclose(result["proportion_A"], result["proportion_B"])
    assert np.isclose(result["mean_A"], result["mean_B"])


def test_ratio_with_difference():
    diff = 20
    cutoff = 5
    result = visualise_distributions(diff, cutoff)

    mean_A = 50 + diff / 2
    mean_B = 50 - diff / 2
    std_dev = 10
    dist_A = norm(loc=mean_A, scale=std_dev)
    dist_B = norm(loc=mean_B, scale=std_dev)
    cutoff_A = dist_A.ppf(1 - cutoff / 100)
    cutoff_B = dist_B.ppf(1 - cutoff / 100)
    cutoff_val = (cutoff_A + cutoff_B) / 2
    prop_A = dist_A.sf(cutoff_val)
    prop_B = dist_B.sf(cutoff_val)
    expected_ratio = prop_A / prop_B

    assert np.isclose(result["ratio"], expected_ratio)
    assert np.isclose(result["cutoff"], cutoff_val)
