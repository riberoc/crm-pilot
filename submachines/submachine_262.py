import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 910) - 949
    _mask = _data(119, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = ' BK{-jQr)pc^FjflC-7Z&64gWR#3ir'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
