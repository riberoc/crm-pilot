import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 324) - 164
    _mask = _data(440, None)
    _enc = 95
    return _mask, _enc

def run():
    matrix = '8Q=s*q]dfMzomiW-UwV4w~%T8Y{90L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
