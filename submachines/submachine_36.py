import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 899) - 378
    _mask = _data(556, None)
    _enc = 36
    return _mask, _enc

def run():
    matrix = 'Mh5e#iAx3?&V*P%+. ;QK9<||}Dq:|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
