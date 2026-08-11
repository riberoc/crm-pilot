import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 747) - 306
    _mask = _data(818, None)
    _enc = 166
    return _mask, _enc

def run():
    matrix = '1 SsQ2K<^Y(doIK,Z+~eO|@SnZ(xO_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
