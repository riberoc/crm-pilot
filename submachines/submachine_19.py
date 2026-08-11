import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 285) - 410
    _mask = _data(924, None)
    _enc = 225
    return _mask, _enc

def run():
    matrix = 'xy#QLEO5@.Fk]1~k6uIU_z_MGTL*?W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
