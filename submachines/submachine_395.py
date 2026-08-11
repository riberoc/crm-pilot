import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 356) - 655
    _mask = _data(906, None)
    _enc = 69
    return _mask, _enc

def run():
    matrix = '>]I6U9mdDU&MX)iN]ikj.2P/ZV J^^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
