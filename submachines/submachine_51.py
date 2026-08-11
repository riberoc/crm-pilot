import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 360) - 943
    _mask = _data(1311, None)
    _enc = 213
    return _mask, _enc

def run():
    matrix = 'jC%&b3FgmHQK57$<*ix.bgNhle@OP '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
