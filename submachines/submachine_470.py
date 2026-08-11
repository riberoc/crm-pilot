import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 685) - 453
    _mask = _data(880, None)
    _enc = 27
    return _mask, _enc

def run():
    matrix = 'jPF E=65|,OFxd31B+V<bLgW#coA/e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
