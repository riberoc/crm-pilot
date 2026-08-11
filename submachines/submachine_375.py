import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 476) - 645
    _mask = _data(654, None)
    _enc = 199
    return _mask, _enc

def run():
    matrix = 'ZcAucTC(i# B8x]s7{]e3kdgQFTwVD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
