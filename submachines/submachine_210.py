import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 601) - 762
    _mask = _data(284, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = 'f^X$owus`:hcOTK6kzpE+W|_lZ{ v}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
