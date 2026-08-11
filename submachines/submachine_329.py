import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 424) - 847
    _mask = _data(1450, None)
    _enc = 175
    return _mask, _enc

def run():
    matrix = '(<w}HdgD)F;=aX8)0HB:4A3!bqax c'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
