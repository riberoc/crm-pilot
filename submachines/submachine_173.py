import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 185) - 379
    _mask = _data(726, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = 'fdFGeGTE2RmRlINIrlK aObL_pT}{r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
