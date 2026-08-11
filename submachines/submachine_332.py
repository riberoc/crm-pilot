import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 921) - 102
    _mask = _data(713, None)
    _enc = 240
    return _mask, _enc

def run():
    matrix = 'xn751~bej,39?PXpQWXE$E4vYj bXs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
