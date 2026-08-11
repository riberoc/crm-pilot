import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 146) - 977
    _mask = _data(1081, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = '`qCgqEj[P]tArtVar~>:mI9Z0sTQ;v'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
