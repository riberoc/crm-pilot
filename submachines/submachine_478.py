import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 595) - 790
    _mask = _data(319, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = 'WZ?l@+_/^k 6X|EKXw!mfd&!/T5Odn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
