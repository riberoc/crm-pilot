import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 649) - 291
    _mask = _data(944, None)
    _enc = 17
    return _mask, _enc

def run():
    matrix = 'LT{INShiyy:CGa>E`xdtTix^o4<gC+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
