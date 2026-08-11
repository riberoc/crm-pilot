import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 246) - 667
    _mask = _data(995, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = '8</bGV&c;bLbP[@v|VvwP}Sxs5@h@ '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
