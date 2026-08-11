import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 643) - 644
    _mask = _data(495, None)
    _enc = 245
    return _mask, _enc

def run():
    matrix = 'ln1P^JUBI@=+t1,#TbkHv=5kGy#vO '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
