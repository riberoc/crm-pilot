import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 315) - 838
    _mask = _data(690, None)
    _enc = 87
    return _mask, _enc

def run():
    matrix = '_mokKJ5C@,]Jw];GKmv2 `c7+cA7J='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
