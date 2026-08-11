import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 784) - 625
    _mask = _data(487, None)
    _enc = 136
    return _mask, _enc

def run():
    matrix = 'W1KH1D8a@>;aG0 IAv;}p1TmMndX+P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
