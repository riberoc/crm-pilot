import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 502) - 986
    _mask = _data(1504, None)
    _enc = 59
    return _mask, _enc

def run():
    matrix = 'A>DUaq: D8^yBLr&_4wxACF_?Vn7M8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
