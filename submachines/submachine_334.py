import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 544) - 891
    _mask = _data(468, None)
    _enc = 122
    return _mask, _enc

def run():
    matrix = 'fvE B:ivHD=/ws6uTC|iUV;lbroh1X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
