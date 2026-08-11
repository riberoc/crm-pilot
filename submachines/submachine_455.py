import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 486) - 994
    _mask = _data(1409, None)
    _enc = 128
    return _mask, _enc

def run():
    matrix = '9MH#= 2e@i}i`qtO+jX4lk=x1-0mSF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
