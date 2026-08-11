import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 848) - 757
    _mask = _data(77, None)
    _enc = 59
    return _mask, _enc

def run():
    matrix = 'c:`)b|-hmSJ=2@#/6X7 O2@;sktZ~+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
