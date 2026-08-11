import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 461) - 718
    _mask = _data(599, None)
    _enc = 206
    return _mask, _enc

def run():
    matrix = 'v7 K3W=EILyF8,d1g#^^YK8U};iF_2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
