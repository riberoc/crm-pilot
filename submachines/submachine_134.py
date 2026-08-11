import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 668) - 551
    _mask = _data(246, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = 'k7*GhCT.7`v n[Sj+_Z%4ISe)J6D{$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
