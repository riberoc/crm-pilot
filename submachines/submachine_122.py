import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 244) - 407
    _mask = _data(624, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = '$0MYfHf{XMrtE2L/>tJbQ~BY5dN/9}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
