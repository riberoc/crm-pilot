import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 132) - 505
    _mask = _data(661, None)
    _enc = 23
    return _mask, _enc

def run():
    matrix = 'Xggt[[gG48X15Nx #Qe0s)/T|v:73;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
