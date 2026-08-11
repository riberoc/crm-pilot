import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 547) - 359
    _mask = _data(924, None)
    _enc = 83
    return _mask, _enc

def run():
    matrix = 'XZ5vBv5-N]l JuN@Fmx~mgI,=I-y+E'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
