import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 950) - 166
    _mask = _data(839, None)
    _enc = 78
    return _mask, _enc

def run():
    matrix = '_pNM9 l$]>iHSB@(,7M$^?co4(JET}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
