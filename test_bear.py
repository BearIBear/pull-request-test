import sys
from bear import print_bear

def test_print_bear(capsys):
    print_bear("Test Message")
    captured = capsys.readouterr()
    assert "Test Message" in captured.out
    assert "__" in captured.out
