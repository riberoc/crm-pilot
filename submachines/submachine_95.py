import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 406) - 219
    _mask = _data(357, None)
    _enc = 29
    return _mask, _enc

def run():
    matrix = '#eAuM yiv_XaqMP_MBoSsb!bZB$M8;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
