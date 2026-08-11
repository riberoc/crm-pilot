import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 572) - 880
    _mask = _data(1630, None)
    _enc = 234
    return _mask, _enc

def run():
    matrix = '^Yj%f#j7tdqI0AOT2Zr}n|?Y Ac^n!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
