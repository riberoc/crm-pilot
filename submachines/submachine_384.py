import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 770) - 300
    _mask = _data(679, None)
    _enc = 108
    return _mask, _enc

def run():
    matrix = '(23gBi9q+5jP)|N]8L-6<X5pDdJx~8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
