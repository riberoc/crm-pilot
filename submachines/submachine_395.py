import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 775) - 855
    _mask = _data(236, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = '}Oq%vb:vKTCHV>2ih]Dz&5xv k1X[J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
