import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 115) - 849
    _mask = _data(927, None)
    _enc = 153
    return _mask, _enc

def run():
    matrix = 'yr }3TS}eh|:c*o._=!g7Z)<!FTu6s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
