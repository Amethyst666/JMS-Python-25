import dataclasses

import pytest

from .add2 import add2


@dataclasses.dataclass
class Case:
    a: int
    b: int
    result: int

    def __str__(self) -> str:
        return 'sum_of_{}_{}'.format(self.a, self.b)


TEST_CASES = [
    Case(a=1, b=2, result=3),
    Case(a=2, b=2, result=4),
    Case(a=-100, b=100, result=0),
    Case(a=100, b=2, result=102),
]


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_hello_world(t: Case) -> None:
    answer = add2(t.a, t.b)
    assert answer == t.result
