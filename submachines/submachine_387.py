import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 893) - 814
    _mask = _data(165, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = '>-X9bMRfsGD8D{ogPg3n^7h|![ (p('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
