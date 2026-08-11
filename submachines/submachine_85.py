import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 642) - 290
    _mask = _data(837, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = 'w0C9ah]TU7P*;Pn`TN8@<Ewwy)l~5A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
