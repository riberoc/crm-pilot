import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 941) - 715
    _mask = _data(139, None)
    _enc = 79
    return _mask, _enc

def run():
    matrix = 'VjXwh$3H`hI_}L!Uosaj yZ]Z*g9FP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
