import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 308) - 612
    _mask = _data(989, None)
    _enc = 151
    return _mask, _enc

def run():
    matrix = 'G=JK{(Cm4Jb!i6sKBD Em&Dx.[hBoP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
