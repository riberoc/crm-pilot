import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 857) - 575
    _mask = _data(482, None)
    _enc = 112
    return _mask, _enc

def run():
    matrix = '])<$DJwroAA4DG}gx?1kAcg7P9&ky2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
