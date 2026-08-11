import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 847) - 861
    _mask = _data(155, None)
    _enc = 102
    return _mask, _enc

def run():
    matrix = 'eXaZ6)0Swv0bE<~pia1Y?v5y~e(EQ`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
