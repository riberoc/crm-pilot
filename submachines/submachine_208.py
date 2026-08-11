import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 628) - 395
    _mask = _data(60, None)
    _enc = 166
    return _mask, _enc

def run():
    matrix = '=@p-*x0o*{:D#iK4=5/PXf&1dmH 1+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
