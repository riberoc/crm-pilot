import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 873) - 934
    _mask = _data(1801, None)
    _enc = 175
    return _mask, _enc

def run():
    matrix = '[dY>/[Ar~RN1&t.Xlz$$0 E~Fr+y.c'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
