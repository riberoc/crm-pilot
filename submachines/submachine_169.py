import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 831) - 667
    _mask = _data(4, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = '&[xodlv2D2p-fLN:zg93;n?7jQ5ZAk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
