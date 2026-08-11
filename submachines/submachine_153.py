import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 956) - 380
    _mask = _data(406, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = '~_N:z0]25Z`Te0.b B-N^&&%,[-[Lo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
