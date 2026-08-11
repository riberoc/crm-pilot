import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 478) - 377
    _mask = _data(22, None)
    _enc = 84
    return _mask, _enc

def run():
    matrix = '?%=QOR7IZNwXX@u`TR(Hjyc:OmH JJ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
