import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 452) - 705
    _mask = _data(717, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = 'c-!#W5?O:2`8|CQs 0RTz9b?iE!),}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
