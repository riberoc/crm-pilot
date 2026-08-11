import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 903) - 866
    _mask = _data(2013, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = 'hUQ>B`<zODfblnbDY%r/|a c^^b)c+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
