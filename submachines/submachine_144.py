import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 299) - 499
    _mask = _data(854, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = 'C~pDd#tKM4^oWnS~V3vaetFu+(>WJx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
