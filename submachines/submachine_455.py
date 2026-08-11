import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 923) - 548
    _mask = _data(290, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = '9!>)Ke&$tIG{TkOTesr[q{{bn#9L_D'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
