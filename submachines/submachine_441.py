import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 747) - 261
    _mask = _data(847, None)
    _enc = 145
    return _mask, _enc

def run():
    matrix = 'gdB**O|sePY}K7 8[l>?%SYS/!bQM@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
