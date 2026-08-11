import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 780) - 394
    _mask = _data(393, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = ',Z_YRj.|^gP}[vA`43wHm/E-UN~c!u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
