import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 746) - 741
    _mask = _data(320, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = '.$naM6I.$?KbyjLC-q6=;!| 9jO~Mc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
