import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 725) - 175
    _mask = _data(909, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = '!JP%G|T$y3jIeYJ[y<X8KRN [5p6>^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
