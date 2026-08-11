import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 765) - 403
    _mask = _data(120, None)
    _enc = 240
    return _mask, _enc

def run():
    matrix = 'i| -9#oLN_NN3l|ZsyZqL39|RMG.uo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
