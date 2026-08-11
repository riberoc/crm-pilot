import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 489) - 541
    _mask = _data(947, None)
    _enc = 36
    return _mask, _enc

def run():
    matrix = 'uMU8):,MZ=/1Z>-f3[nq3nC77 H@bz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
