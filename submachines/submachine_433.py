import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 913) - 449
    _mask = _data(469, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = '_BY]3<y#+f4WAO(slp5T[=L0eBPgTe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
