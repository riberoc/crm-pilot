import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 940) - 834
    _mask = _data(1930, None)
    _enc = 239
    return _mask, _enc

def run():
    matrix = 'jk1<*75,j(siuIpB%e-F9DXYOw3C24'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
