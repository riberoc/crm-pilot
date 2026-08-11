import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 226) - 295
    _mask = _data(294, None)
    _enc = 134
    return _mask, _enc

def run():
    matrix = '-?PlZS3gq|qvRmN+0q!_K_a~gCX XE'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
