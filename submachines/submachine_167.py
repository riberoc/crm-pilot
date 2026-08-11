import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 305) - 423
    _mask = _data(225, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = ', 68.p427i90Q,]CIgBy-4Y)3Ag`8R'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
