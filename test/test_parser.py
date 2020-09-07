from myproject.parsing.parser import parse_temp

def test_parser():
    string = r"Core 0:        +66.0°C  (high = +87.0°C, crit = +105.0°C) Core 1:        +60.0°C  (high = +87.0°C, crit = +105.0°C)"

    parsed = parse_temp(string)
    output = [('0', '66.0'), ('1', '60.0')]
    assert parsed == output