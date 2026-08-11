import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 377) - 975
    _mask = _data(1474, None)
    _enc = 224
    return _mask, _enc

def run():
    matrix = 'z0}-,n,b`)&> Imveq<15qm}6XtY*X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
