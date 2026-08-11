import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 255) - 260
    _mask = _data(300, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = 'S$d%rC}D[b?!!7zZKp_zM,tln6-cCq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
