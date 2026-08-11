import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 166) - 487
    _mask = _data(635, None)
    _enc = 230
    return _mask, _enc

def run():
    matrix = 'GV8OFdHN+_8ti3;v aqd4TO`nK92/C'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
