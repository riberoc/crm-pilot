import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 438) - 921
    _mask = _data(1481, None)
    _enc = 232
    return _mask, _enc

def run():
    matrix = 'kfh^fEE3d!RGGf }U_nJRz5[~hy;IZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
