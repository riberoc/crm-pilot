import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 915) - 179
    _mask = _data(667, None)
    _enc = 67
    return _mask, _enc

def run():
    matrix = '$b[d~C/p^NHv~w/Ax&,^@y xn|Jn>w'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
