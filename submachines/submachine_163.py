import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 157) - 321
    _mask = _data(323, None)
    _enc = 148
    return _mask, _enc

def run():
    matrix = 'mn>GSJ]H|dtZ$nWH-/(d#h9VwKn_p!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
