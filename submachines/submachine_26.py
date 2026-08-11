import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 693) - 378
    _mask = _data(232, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = 'y1f1Ro8>O,.tSfl}^R%zMAt[0 E]u:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
