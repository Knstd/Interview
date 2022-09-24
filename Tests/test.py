import pytest

from main import is_balanced

test_data = [
    ('(((([{}]))))', 'Сбалансированно'),
    ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
    ('{{[()]}}', 'Сбалансированно'),
    ('}{}', 'Несбалансированно'),
    ('{{[(])]}}', 'Несбалансированно'),
    ('[[{(())}]', 'Несбалансированно')
]


class Test:
    @pytest.mark.parametrize('brackets, result', test_data)
    def test_is_balanced(self, brackets, result):
        assert is_balanced(brackets) == result
