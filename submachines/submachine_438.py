import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 336) - 241
    _mask = _data(186, None)
    _enc = 226
    return _mask, _enc

def run():
    matrix = 'p,W7p44CCVf@F&C[8G+o,2<CJ57Ebl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
