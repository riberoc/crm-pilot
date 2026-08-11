import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 913) - 685
    _mask = _data(137, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = '>WquJX(aak@+t_%/#5 6;dPz?6a77C'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
