import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 188) - 366
    _mask = _data(349, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = 'N+zPX[+&rlnvRHtC l]Qz$FEGv,0ce'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
