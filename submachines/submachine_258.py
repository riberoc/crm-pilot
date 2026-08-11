import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 621) - 895
    _mask = _data(409, None)
    _enc = 102
    return _mask, _enc

def run():
    matrix = 'N:Um~@,:r4B0Bkyb#e^ ^[F`-8Ri-u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
