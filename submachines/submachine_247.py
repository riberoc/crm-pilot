import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 356) - 340
    _mask = _data(174, None)
    _enc = 118
    return _mask, _enc

def run():
    matrix = ' qe$LcS]k{W^szBT`8&gJqp]aL{;O.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
