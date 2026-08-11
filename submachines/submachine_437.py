import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 510) - 258
    _mask = _data(137, None)
    _enc = 127
    return _mask, _enc

def run():
    matrix = '(jvD-,^kB~ N`ayUl15J]:&nKwUzzX'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
