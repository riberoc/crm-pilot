import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 804) - 268
    _mask = _data(693, None)
    _enc = 143
    return _mask, _enc

def run():
    matrix = '5a:0|T&>-y Ull~xtA_}7:G=?2%~dJ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
