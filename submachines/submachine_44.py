import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 303) - 530
    _mask = _data(883, None)
    _enc = 91
    return _mask, _enc

def run():
    matrix = 'aSr2mY]$bb8W(X+$9 1$(ZuN/b$;@r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
