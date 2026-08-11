import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 262) - 809
    _mask = _data(604, None)
    _enc = 43
    return _mask, _enc

def run():
    matrix = 'n,c)GkLhBaDtKnpgs@(}clq%<%eqXp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
