import pytest

from arithmetic_arranger import arithmetic_arranger

test_cases = [
    pytest.param(
        [['3 + 855', '3801 - 2', '45 + 43', '123 + 49']],
        '    3      3801      45      123\n'
        '+ 855    -    2    + 43    +  49\n'
        '-----    ------    ----    -----',
        'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]',
        id='test_arrangement1'),
    pytest.param(
        [['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']],
        '  11      3801      1      123         1\n'
        '+  4    - 2999    + 2    +  49    - 9380\n'
        '----    ------    ---    -----    ------',
        'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]',
        id='test_arrangement2'),
    pytest.param(
        [['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']],
        'Error: Too many problems.',
        'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."',
        id='test_too_many_problems'),
    pytest.param(
        [['3 / 855', '3801 - 2', '45 + 43', '123 + 49']],
        "Error: Operator must be '+' or '-'.",
        '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''',
        id='test_incorrect_operator'),
    pytest.param(
        [['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']],
        'Error: Numbers cannot be more than four digits.',
        'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."',
        id='test_too_many_digits'),
    pytest.param(
        [['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']],
        'Error: Numbers must only contain digits.',
        'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."',
        id='test_only_digits'),
    pytest.param(
        [['32 - 698', '1 - 3801', '45 + 43', '123 + 49'], True],
        '   32         1      45      123\n'
        '- 698    - 3801    + 43    +  49\n'
        '-----    ------    ----    -----\n'
        ' -666     -3800      88      172',
        'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithmetic problems and a second argument of `True`.',
        id='test_solutions'),
]


@pytest.mark.parametrize('arguments,expected_output,fail_message', test_cases)
def test_template(arguments, expected_output, fail_message):
    actual = arithmetic_arranger(*arguments)
    assert actual == expected_output, fail_message
