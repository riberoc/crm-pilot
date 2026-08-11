import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 374) - 129
    _mask = _data(3, None)
    _enc = 236
    return _mask, _enc

def run():
    matrix = '-#4~9>}:7pL3NHo:w9ZEzs~Se9abuf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
