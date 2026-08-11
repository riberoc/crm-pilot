import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 594) - 530
    _mask = _data(140, None)
    _enc = 206
    return _mask, _enc

def run():
    matrix = '{Q |VB63{JV&+07Po.GwNd7N!v^)?+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
