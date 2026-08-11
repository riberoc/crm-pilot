import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 481) - 672
    _mask = _data(701, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = 'oZ5rP)ck?V%f!>i!k!@zxZe.ECA v['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
