import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 284) - 329
    _mask = _data(829, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = '?roP;5ym=Q5;kHl o7N>I@@Uvq)b!B'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
