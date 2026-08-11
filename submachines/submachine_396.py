import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 300) - 198
    _mask = _data(28, None)
    _enc = 105
    return _mask, _enc

def run():
    matrix = 'e^5UA+cUy+N6*@`*Slml2iLFpEjMb:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
