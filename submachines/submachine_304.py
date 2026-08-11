import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 441) - 191
    _mask = _data(339, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = 'Rr[2;/^p:LGCAWlpApf&>`8&dBi d|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
