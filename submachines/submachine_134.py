import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 905) - 929
    _mask = _data(126, None)
    _enc = 76
    return _mask, _enc

def run():
    matrix = 'M!~uB16AK*5aD!l7NdS,mIXO7Q #nn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
