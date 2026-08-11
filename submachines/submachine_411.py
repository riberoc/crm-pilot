import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 349) - 964
    _mask = _data(1377, None)
    _enc = 112
    return _mask, _enc

def run():
    matrix = 'VffK3_$@ _@~.t$zcyq6AaYgE!)(_W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
