import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 208) - 437
    _mask = _data(673, None)
    _enc = 160
    return _mask, _enc

def run():
    matrix = 'ox*0,l|q[<yb[M&l%t4c]{_|MxoZU|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
