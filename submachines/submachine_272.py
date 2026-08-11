import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 527) - 462
    _mask = _data(50, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = '+@ v3P;}~6K=qOi^9do#T,Eo~zD):m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
