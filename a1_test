"""
Hannah Lee
Section: AE

This file has functions that tests the methods found
in the a1.py file.
"""

import a1

from cse163_utils import assert_equals


def test_total() -> None:
    """
    This function tests the behavior of the total method
    in the a1.py class.
    """
    # The regular case
    assert_equals(15, a1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, a1.total(1))
    assert_equals(0, a1.total(0))
    # TODO: add your own total test here
    assert_equals(None, a1.total(-3))


def test_funky_sum() -> None:
    """
    This function tests the behavior of the funky_sum method
    in the a1.py file.
    """
    assert_equals(2.0, a1.funky_sum(1, 3, 0.5))
    assert_equals(1, a1.funky_sum(1, 3, 0))
    assert_equals(1.5, a1.funky_sum(1, 3, 0.25))
    assert_equals(2.2, a1.funky_sum(1, 3, 0.6))
    assert_equals(3, a1.funky_sum(1, 3, 1))
    assert_equals(3, a1.funky_sum(3, 4, 0))
    assert_equals(4, a1.funky_sum(3, 4, 1))
    assert_equals(3.5, a1.funky_sum(3, 4, .5))


def test_swip_swap() -> None:
    """
    This function tests the behavior of the swip_swap method
    in the a1.py file.
    """
    assert_equals('offbar', a1.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', a1.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', a1.swip_swap('foobar', 'z', 'c'))
    assert_equals('cat', a1.swip_swap('tac', 't', 'c'))
    assert_equals('', a1.swip_swap('', 'a', 'b'))


def main():
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()
