import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 707) - 885
    _mask = _data(264, None)
    _enc = 75
    return _mask, _enc

def run():
    matrix = 'LUyE(C^?}pmm!`@/ZPqp6++0#QOTl '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
