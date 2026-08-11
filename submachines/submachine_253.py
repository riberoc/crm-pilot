import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 243) - 988
    _mask = _data(1273, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = '%({Hs_[ 5lS4=MBJyPYt{U+i$PpK2x'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
