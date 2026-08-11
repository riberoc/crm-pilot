import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 779) - 472
    _mask = _data(435, None)
    _enc = 229
    return _mask, _enc

def run():
    matrix = 'EA|/7 AsIYtL|.iCF^+#AAqskq3BSc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
