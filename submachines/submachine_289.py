import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 845) - 416
    _mask = _data(698, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = 'UJ|VJ+!hdsR 0D%Q2UR{}[>{Q{>GK.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
