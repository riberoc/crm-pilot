import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 521) - 945
    _mask = _data(1675, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = 'S<rgx&V6=,?-)H]My7Z=te;QCiTagF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
