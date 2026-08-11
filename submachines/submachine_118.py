import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 497) - 263
    _mask = _data(11, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = '?>b,aP|c/KR:S=M$Ce;gT*!iQpIoL '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
