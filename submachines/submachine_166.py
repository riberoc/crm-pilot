import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 518) - 929
    _mask = _data(1690, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = 'd3v,R $R5T;`s>,7t&/@s+`F4_Sh&!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
