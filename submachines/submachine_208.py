import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 812) - 447
    _mask = _data(282, None)
    _enc = 111
    return _mask, _enc

def run():
    matrix = '#0Z*hk`,=,;4tnm)`Nl4o(a5 qY0!{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
