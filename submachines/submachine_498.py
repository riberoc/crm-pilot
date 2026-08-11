import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 285) - 263
    _mask = _data(55, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = ';?rd-+St~^D WVu=]vO-;4Q)i;JJ&E'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
