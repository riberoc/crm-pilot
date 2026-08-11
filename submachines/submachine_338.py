import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 675) - 710
    _mask = _data(303, None)
    _enc = 218
    return _mask, _enc

def run():
    matrix = 'f6)jI.brR*|U#0gfY[kZt?[^q){D u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
