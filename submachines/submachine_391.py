import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 988) - 329
    _mask = _data(579, None)
    _enc = 91
    return _mask, _enc

def run():
    matrix = 'v&y[;t,:xjZs) iB&5Jn[Iee,s@)eA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
