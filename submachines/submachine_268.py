import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 576) - 976
    _mask = _data(1648, None)
    _enc = 114
    return _mask, _enc

def run():
    matrix = 'B]Fu2E$o>,{C(w(~Vf UiSrElxgjhz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
