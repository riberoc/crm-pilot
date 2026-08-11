import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 483) - 316
    _mask = _data(21, None)
    _enc = 169
    return _mask, _enc

def run():
    matrix = 'Tt9=r`NT]kn7HKJ1vZA yns/dc_j3T'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
