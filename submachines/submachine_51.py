import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 352) - 396
    _mask = _data(876, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = 'tJZXdou9#$q@a8-[4t?<J+T/o+M9:U'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
