import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 768) - 677
    _mask = _data(115, None)
    _enc = 193
    return _mask, _enc

def run():
    matrix = 'j/D0?7==VCQFbS2 x./z30]{I+%Q|f'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
