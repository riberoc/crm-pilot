import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 314) - 149
    _mask = _data(454, None)
    _enc = 114
    return _mask, _enc

def run():
    matrix = 'cok[bEV>u{{Lg{KJ]8@tZ GA6()tUk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
