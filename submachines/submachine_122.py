import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 714) - 727
    _mask = _data(504, None)
    _enc = 89
    return _mask, _enc

def run():
    matrix = 'do pi$ldSsFR=aGMIJi5L|?B044cvC'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
