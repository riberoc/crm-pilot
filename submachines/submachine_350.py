import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 253) - 664
    _mask = _data(576, None)
    _enc = 53
    return _mask, _enc

def run():
    matrix = 'Lfvv5bn&s/):ODB}o%_5c#gI!.qG9J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
