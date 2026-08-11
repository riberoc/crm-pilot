import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 278) - 750
    _mask = _data(626, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = 'Y[3>p r12N%g:(J,j8-6-JgaQ{z?/&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
