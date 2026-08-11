import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 465) - 245
    _mask = _data(33, None)
    _enc = 247
    return _mask, _enc

def run():
    matrix = '~|3`tab{T:D< Wh9SW9=-y4e!EH?>='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
