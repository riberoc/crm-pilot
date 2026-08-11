import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 113) - 209
    _mask = _data(357, None)
    _enc = 79
    return _mask, _enc

def run():
    matrix = '_8bCuS5OmH%emVlp`Rb&lBYW6VbV/V'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
