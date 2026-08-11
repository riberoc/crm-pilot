import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 366) - 856
    _mask = _data(1406, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = 'xV-9nKK}b[yHJ|h+#celAsygO[tSx.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
