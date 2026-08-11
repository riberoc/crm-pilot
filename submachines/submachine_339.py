import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 311) - 670
    _mask = _data(679, None)
    _enc = 228
    return _mask, _enc

def run():
    matrix = ',NpP]Ra(*N|<sX~:tJobq. vO>ieY&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
