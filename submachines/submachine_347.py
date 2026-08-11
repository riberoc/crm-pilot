import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 925) - 191
    _mask = _data(703, None)
    _enc = 105
    return _mask, _enc

def run():
    matrix = ',U|JIbChMs PVb+?k7>376~Uqo3`{Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
