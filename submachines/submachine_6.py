import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 589) - 500
    _mask = _data(146, None)
    _enc = 228
    return _mask, _enc

def run():
    matrix = ';[1ho>kV?$)o}G<e2}_a,!lpwv#MMm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
