import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 177) - 171
    _mask = _data(479, None)
    _enc = 219
    return _mask, _enc

def run():
    matrix = '7FWr*ief2M^JDO0+h*~bAvTqn{P7Mm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
