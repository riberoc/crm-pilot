import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 973) - 738
    _mask = _data(130, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = '0`Z#= HVx9~C;LX6Uk?{h1ev;yXC~e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
