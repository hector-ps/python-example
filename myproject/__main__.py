import os

from parsing.parser import parse_temp


def main():
    stream = os.popen('sensors | grep Core')
    output = stream.read()
    parsed = parse_temp(output)

    print(parsed)

if __name__ == "__main__":
    main()