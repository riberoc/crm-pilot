import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 909) - 848
    _mask = _data(118, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = 'M3b.{+f[O^zmQ?0y6[F25a$V#82ha6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
