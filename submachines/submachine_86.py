import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 420) - 401
    _mask = _data(114, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = 'DU>>R,A;%viR3Gb7P8zt~g31{bb m^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
