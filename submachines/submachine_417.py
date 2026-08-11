import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 673) - 983
    _mask = _data(1539, None)
    _enc = 192
    return _mask, _enc

def run():
    matrix = '.+i-N()l_P.wJe-e3ejGa2lOXv.*|Y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
