import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 842) - 110
    _mask = _data(909, None)
    _enc = 76
    return _mask, _enc

def run():
    matrix = 'g$b4u[kbT9Hwg#%&q?_nW =;R-Vrbz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
