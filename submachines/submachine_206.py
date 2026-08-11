import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 627) - 234
    _mask = _data(891, None)
    _enc = 22
    return _mask, _enc

def run():
    matrix = '];.iDwW%ipywPpU+T4s!=D~kFHr;L2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
