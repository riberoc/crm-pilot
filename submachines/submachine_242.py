import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 394) - 593
    _mask = _data(659, None)
    _enc = 193
    return _mask, _enc

def run():
    matrix = '1-nK+5[xG X~~hg+U=wfm=`VW7-d>}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
