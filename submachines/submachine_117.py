import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 474) - 248
    _mask = _data(183, None)
    _enc = 114
    return _mask, _enc

def run():
    matrix = 'A%v/5#hsD?FQP5,|0v.28=D~FH--G?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
