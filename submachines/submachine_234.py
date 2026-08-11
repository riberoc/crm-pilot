import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 486) - 998
    _mask = _data(1410, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = '8XwzcKMfRJ /CEYqA*3(8g7o,Ig$?~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
