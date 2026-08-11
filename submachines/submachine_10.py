import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 633) - 687
    _mask = _data(338, None)
    _enc = 110
    return _mask, _enc

def run():
    matrix = 'MggS_ogA/0CkU#}&CS [,b@+.eCQ;T'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
