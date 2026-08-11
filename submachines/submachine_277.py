import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 942) - 594
    _mask = _data(302, None)
    _enc = 54
    return _mask, _enc

def run():
    matrix = 'H}waN@7{Tnj7/Y*<E%Yr>q(U wKOy3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
