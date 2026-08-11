import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 238) - 582
    _mask = _data(545, None)
    _enc = 130
    return _mask, _enc

def run():
    matrix = "dcN3]O]r5Ve'5^U)9DRGhwPsB|jjDb"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
