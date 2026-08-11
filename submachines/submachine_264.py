import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 751) - 570
    _mask = _data(41, None)
    _enc = 130
    return _mask, _enc

def run():
    matrix = '$A>0U?~yH)yc>A k/$7+BMOmQgINsO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
