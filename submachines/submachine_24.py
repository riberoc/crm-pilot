import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 280) - 869
    _mask = _data(674, None)
    _enc = 89
    return _mask, _enc

def run():
    matrix = '<?Wi|lGST^%& mCEe|#dq{.Lt0apA2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
