import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 820) - 868
    _mask = _data(144, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = '-RWJiIuY bdt}x+XOU*5_EbGt~OAUH'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
