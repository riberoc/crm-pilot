import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 343) - 825
    _mask = _data(700, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = '+6Vx@|Vt!SYs]!a{t+z4p Cz:`P-9X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
