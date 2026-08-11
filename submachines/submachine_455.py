import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 754) - 881
    _mask = _data(322, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = 'ox.uD}3BbD[>n0qT;.gNv%3jmiqrH!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
