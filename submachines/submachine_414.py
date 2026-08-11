import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 697) - 788
    _mask = _data(335, None)
    _enc = 241
    return _mask, _enc

def run():
    matrix = 'Pf(/rrqj5T,N.~w{q`Q ;L8v@#GGle'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
