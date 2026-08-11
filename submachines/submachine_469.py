import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 141) - 200
    _mask = _data(331, None)
    _enc = 236
    return _mask, _enc

def run():
    matrix = 'Pm,8#wEgGGGDA`E>zp zB6,iYCJ%&{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
