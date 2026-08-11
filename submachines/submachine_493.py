import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 108) - 844
    _mask = _data(940, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = 'RV6Wvd@V02*?,hA<SjF`H_e96g{x5E'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
