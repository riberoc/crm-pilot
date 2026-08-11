import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 342) - 547
    _mask = _data(901, None)
    _enc = 168
    return _mask, _enc

def run():
    matrix = 'geJ`.S[@u(=0cbd^pC5-NcS1 B$3$l'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
