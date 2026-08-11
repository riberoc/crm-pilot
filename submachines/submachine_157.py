import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 256) - 320
    _mask = _data(246, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = '^8)lot/A=o l#FQ$B!R9Z;Ijvvz-bB'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
