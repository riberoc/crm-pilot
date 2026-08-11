import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 473) - 669
    _mask = _data(659, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = '<X(FR]Bzv.V{+Rt<`9x?tYy3#gcrLF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
