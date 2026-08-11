import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 317) - 803
    _mask = _data(627, None)
    _enc = 45
    return _mask, _enc

def run():
    matrix = 'q(bhx[ [J_d]|cO3C2m@l2,-?.;rYk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
