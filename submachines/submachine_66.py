import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 127) - 321
    _mask = _data(603, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = '7FV(:Rj55;0tcuV1 R/3`O[(NqjJ}+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
