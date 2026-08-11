import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 783) - 751
    _mask = _data(49, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = 'AuFlf4A1{yw4Tp74XY P;fRUG)yT&Y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
