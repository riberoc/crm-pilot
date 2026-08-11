import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 452) - 212
    _mask = _data(238, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'aIV<3/n2C#q^JXy|v!;}E7V[x{?8Rz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
