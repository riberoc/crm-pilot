import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 988) - 743
    _mask = _data(115, None)
    _enc = 223
    return _mask, _enc

def run():
    matrix = 'l;L;V>uzGDSL3`-N:kQa-h`ey%no~-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
