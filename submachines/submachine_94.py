import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 484) - 538
    _mask = _data(751, None)
    _enc = 251
    return _mask, _enc

def run():
    matrix = 'q`bn4]+:g> ..0%f,+&:yXQ:W,-a4`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
