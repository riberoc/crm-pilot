import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 625) - 860
    _mask = _data(1639, None)
    _enc = 166
    return _mask, _enc

def run():
    matrix = 'Vrx>x6-.~o(4~qP1$w:aSK[LF00S +'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
