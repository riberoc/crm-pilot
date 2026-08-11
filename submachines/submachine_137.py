import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 484) - 810
    _mask = _data(632, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = 'h_<s|Acwmp<SQJ%a-iyGKCm`20e[6+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
