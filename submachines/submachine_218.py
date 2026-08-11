import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 261) - 136
    _mask = _data(507, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = 'li:SMRij#fs4@/`2EXM8nld>3P8wa-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
