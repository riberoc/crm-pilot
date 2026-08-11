import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 539) - 809
    _mask = _data(440, None)
    _enc = 110
    return _mask, _enc

def run():
    matrix = 'F?Wzq$}CU_~G%D@|G8.: iuBh?5c6v'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
