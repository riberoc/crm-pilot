import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 877) - 648
    _mask = _data(450, None)
    _enc = 32
    return _mask, _enc

def run():
    matrix = '!JfIxHj 2M<U]FiQ82L<8YAkW3T-e9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
