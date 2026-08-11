import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 814) - 808
    _mask = _data(182, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = 'Jf!~/-~84bO$c*u(9*W5J?L7rx.ll1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
