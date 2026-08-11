import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 175) - 367
    _mask = _data(341, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = '!goT6ITGdGQmtKN#EuDsuj.%bk,LxG'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
