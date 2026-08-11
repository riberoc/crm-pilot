import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 490) - 943
    _mask = _data(1413, None)
    _enc = 197
    return _mask, _enc

def run():
    matrix = 'f56iYnv^=+<]6:S6d&Q;3LTUh}V*?4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
