import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 362) - 938
    _mask = _data(1360, None)
    _enc = 159
    return _mask, _enc

def run():
    matrix = 'c)OUQcxamHRPM!p #*a*8)lcb.@,wn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
