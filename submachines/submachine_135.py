import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 834) - 608
    _mask = _data(492, None)
    _enc = 69
    return _mask, _enc

def run():
    matrix = '@y`VaXPef+K KaJW.8@b~fU~1dv6>4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
