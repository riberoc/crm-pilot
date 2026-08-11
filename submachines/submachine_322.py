import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 253) - 621
    _mask = _data(539, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'f@d;g?AuqUEe+up{E 7!|`TcEe|d8|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
