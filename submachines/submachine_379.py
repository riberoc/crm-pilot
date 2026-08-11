import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 355) - 218
    _mask = _data(95, None)
    _enc = 127
    return _mask, _enc

def run():
    matrix = 'xh>b:4:-ZUh_P-$,}cN1q#9-+BIWu '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
