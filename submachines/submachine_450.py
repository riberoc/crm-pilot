import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 778) - 290
    _mask = _data(689, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = '~(?y0,CVE3SVpeZc`dtXae- Wh:$&i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
