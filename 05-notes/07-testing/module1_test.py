import pytest
from typing import List


def total(xs: List[int]) -> int:
    """Total returns the sum of xs"""
    return sum(xs)

# -------- TEST --------------
def test_total_empty() -> None:
    assert total([]) == 0.0

def test_total_single_item() -> None:
    assert total([100]) == 100
    
def test_total_multiple_items() -> None:
    assert total([100, 200]) == 300