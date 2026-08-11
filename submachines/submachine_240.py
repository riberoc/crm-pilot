import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 134) - 121
    _mask = _data(501, None)
    _enc = 245
    return _mask, _enc

def run():
    matrix = 'O*kfMn>L7a#<m>#cV664Y{YB4P]0Kc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
