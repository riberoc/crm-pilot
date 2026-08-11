import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 372) - 403
    _mask = _data(150, None)
    _enc = 89
    return _mask, _enc

def run():
    matrix = 'chxM_RU!4$T(f&P7z@<uo% JO0gd?9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
