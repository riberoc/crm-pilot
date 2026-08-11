import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 652) - 581
    _mask = _data(118, None)
    _enc = 184
    return _mask, _enc

def run():
    matrix = '-+H6;B})7N&{K ki;&!~zqX=pY@S8I'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
