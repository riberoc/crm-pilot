import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 904) - 155
    _mask = _data(842, None)
    _enc = 33
    return _mask, _enc

def run():
    matrix = 'EUHSEZ 1`3k%lm=;ABl3)4]MG<>|u+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
