import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 244) - 699
    _mask = _data(994, None)
    _enc = 78
    return _mask, _enc

def run():
    matrix = 'L%+|r;+xm87r~rm@wH=4v .GzdPZ+9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
