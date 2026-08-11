import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 248) - 772
    _mask = _data(878, None)
    _enc = 152
    return _mask, _enc

def run():
    matrix = 'kPp@mlX3Mg T.$dY#)t58N7Ru4irm0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
