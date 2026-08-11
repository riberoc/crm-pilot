import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 475) - 198
    _mask = _data(306, None)
    _enc = 33
    return _mask, _enc

def run():
    matrix = '1Wnox6iIk&4*LZo#lw|hD#[6$CZaz@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
