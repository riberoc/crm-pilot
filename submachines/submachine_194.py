import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 225) - 567
    _mask = _data(560, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = 'UXT2j>(:92M4?f8k+j)h&dHhzP-wM '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
