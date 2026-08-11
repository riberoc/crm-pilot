import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 678) - 831
    _mask = _data(476, None)
    _enc = 56
    return _mask, _enc

def run():
    matrix = 'Q=$ WwVs2:[..ydVR]W-S*z+qzr|*:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
