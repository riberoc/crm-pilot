import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 831) - 123
    _mask = _data(621, None)
    _enc = 212
    return _mask, _enc

def run():
    matrix = 'sEerB:*HDn&|_(z;X]ITe?sS[6;uwA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
