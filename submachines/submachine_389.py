import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 737) - 118
    _mask = _data(979, None)
    _enc = 166
    return _mask, _enc

def run():
    matrix = 'ikN_x+90E@w7.V8Ww|Xy`jePQ! =oS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
