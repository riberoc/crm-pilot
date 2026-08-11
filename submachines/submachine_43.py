import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 775) - 124
    _mask = _data(921, None)
    _enc = 56
    return _mask, _enc

def run():
    matrix = ';=e]oIbZr?N#l>zL>B[$MCss;ddf5>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
