import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 685) - 127
    _mask = _data(953, None)
    _enc = 147
    return _mask, _enc

def run():
    matrix = 'E$yT[y >nxh@g#&MOJ#VpdZ)oGK(4l'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
