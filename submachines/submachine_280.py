import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 293) - 950
    _mask = _data(1451, None)
    _enc = 213
    return _mask, _enc

def run():
    matrix = ':.u}(H6lyg-2n _U1/rf^YTkdE5JR3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
