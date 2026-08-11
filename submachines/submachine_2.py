import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 147) - 189
    _mask = _data(287, None)
    _enc = 218
    return _mask, _enc

def run():
    matrix = '}zOH&6[zIHcur#c7)Qa8m n09Ab#j8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
