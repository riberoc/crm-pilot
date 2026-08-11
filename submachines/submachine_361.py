import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 864) - 854
    _mask = _data(155, None)
    _enc = 181
    return _mask, _enc

def run():
    matrix = '*j]1:$K,MY<C4x.* `xo2<&}(>VMIe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
