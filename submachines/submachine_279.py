import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 878) - 497
    _mask = _data(266, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = 'n.@jZ-4i,>>A)*)GI81$U3@dCqiGE='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
