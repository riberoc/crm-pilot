import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 868) - 333
    _mask = _data(690, None)
    _enc = 146
    return _mask, _enc

def run():
    matrix = 'eO%GB#ueEN1uo+n9ZX#EjF;bWab Y-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
