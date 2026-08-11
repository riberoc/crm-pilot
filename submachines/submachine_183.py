import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 501) - 306
    _mask = _data(988, None)
    _enc = 253
    return _mask, _enc

def run():
    matrix = 'nxZglUIDNaT14`ggraat50<Fqll`Uc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
