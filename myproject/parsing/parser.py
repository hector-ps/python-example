import re

def parse_temp(temp):

    out = re.findall("Core ([0-9])*\: *\+([0-9.]*)", temp)

    return out

