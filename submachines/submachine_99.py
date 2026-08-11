import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 398) - 973
    _mask = _data(1492, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = ';Z0$ukE!rj@h(-Z1@Va`)4BKt3{nTT'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
