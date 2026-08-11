import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 897) - 719
    _mask = _data(248, None)
    _enc = 184
    return _mask, _enc

def run():
    matrix = 'KZFJ92}IP<D~v.I*x6 Fhq9WBt9;?M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
