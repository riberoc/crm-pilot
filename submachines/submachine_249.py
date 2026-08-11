import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 805) - 105
    _mask = _data(582, None)
    _enc = 245
    return _mask, _enc

def run():
    matrix = '--E%R^IdCLG6XUh !RaJbPIrbnIX@;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
