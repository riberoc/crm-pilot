import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 598) - 819
    _mask = _data(274, None)
    _enc = 20
    return _mask, _enc

def run():
    matrix = 'uj=*O 4@k6-/ZCt=^ePR[nGy*N/oT#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
