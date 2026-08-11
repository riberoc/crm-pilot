import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 757) - 923
    _mask = _data(1723, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = 'evkf?!omItTW:&mHfh%0 uJC.~|j59'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
