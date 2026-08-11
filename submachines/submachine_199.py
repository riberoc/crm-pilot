import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 119) - 976
    _mask = _data(1228, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = 'w,27GMgw7O$.WKoN.t-^r {=}HaZ7J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
