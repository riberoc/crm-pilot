import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 976) - 157
    _mask = _data(594, None)
    _enc = 230
    return _mask, _enc

def run():
    matrix = '}.9 wgk]uB{^MZG5qnWm:[n9@lQ<2q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
