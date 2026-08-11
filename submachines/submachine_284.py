import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 916) - 974
    _mask = _data(121, None)
    _enc = 20
    return _mask, _enc

def run():
    matrix = 'RFNwXHM0!69bY7_m%([+G<aF}Cs;HO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
