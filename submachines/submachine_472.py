import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 949) - 877
    _mask = _data(2001, None)
    _enc = 230
    return _mask, _enc

def run():
    matrix = '?6]/F;6<2:/_TUE@j f`oV(r&|Vq8R'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
