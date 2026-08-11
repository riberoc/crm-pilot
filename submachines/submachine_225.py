import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 590) - 133
    _mask = _data(852, None)
    _enc = 154
    return _mask, _enc

def run():
    matrix = 'c2l+&o`.$}Q386Q R7!zsOn1.1iKC5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
