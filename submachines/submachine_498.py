import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 458) - 531
    _mask = _data(931, None)
    _enc = 75
    return _mask, _enc

def run():
    matrix = 'jZ!^iTQ>V(~]3z2*b-v^R<JTNglL4 '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
