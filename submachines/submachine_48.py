import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 752) - 252
    _mask = _data(895, None)
    _enc = 159
    return _mask, _enc

def run():
    matrix = 'm20Wg:RZ3qB+ O)n|R&`>M!aa0!Bx2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
