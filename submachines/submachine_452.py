import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 623) - 569
    _mask = _data(344, None)
    _enc = 229
    return _mask, _enc

def run():
    matrix = '~/qD-_8?Cgh)Y?RM|k<TiMOeZ.we2v'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
