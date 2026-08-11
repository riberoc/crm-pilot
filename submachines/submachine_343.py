import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 320) - 109
    _mask = _data(95, None)
    _enc = 191
    return _mask, _enc

def run():
    matrix = 'F;<tNW9VgeQD- nVa`Y$kN;4t8(@TJ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
