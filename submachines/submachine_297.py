import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 195) - 520
    _mask = _data(557, None)
    _enc = 232
    return _mask, _enc

def run():
    matrix = '?G[?*XZ:gREHg? 6c#wO+f+ZKID?y;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
