import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 549) - 219
    _mask = _data(721, None)
    _enc = 17
    return _mask, _enc

def run():
    matrix = ':9q2`q8F I.vN:vHuCS}z092HT-~{R'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
