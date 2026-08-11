import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 770) - 339
    _mask = _data(696, None)
    _enc = 125
    return _mask, _enc

def run():
    matrix = ')2D}dJN&zmn_(RdLw.Qc=+^*n3 :5w'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
