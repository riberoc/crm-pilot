import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 956) - 579
    _mask = _data(376, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = 'Zpe0+rbkc3@;@MZgs+&0/?uakq0cse'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
