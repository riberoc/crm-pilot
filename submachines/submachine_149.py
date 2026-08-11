import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 988) - 624
    _mask = _data(272, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = '9G.n.7MXz2]p Ks]LJ)xi63ch9A7e|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
