import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 707) - 779
    _mask = _data(307, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = 'v.J(Y554&%xBH7VTc2.GDr$tt?=e :'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
