import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 155) - 315
    _mask = _data(668, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = 'dF@yGn0I)eEY5V>eA#$eP*QReF=MI%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
