import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 602) - 895
    _mask = _data(1654, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = '*xX;z9CNJo^K}I).zJ3P%LH,Mor, 0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
