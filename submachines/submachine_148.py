import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 414) - 747
    _mask = _data(658, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = '0Zf#9OPl &kIC3{pm:zfDk>{w6xC9,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
