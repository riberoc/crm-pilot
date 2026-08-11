import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 689) - 599
    _mask = _data(56, None)
    _enc = 56
    return _mask, _enc

def run():
    matrix = '9tf^)F.3M@L`lJlnp3I1GPPr%KnW7J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
