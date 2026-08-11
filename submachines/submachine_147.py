import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 596) - 245
    _mask = _data(911, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = 'jnwD%K2|QuVB!Q_vqD$RT}ImwUdx8g'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
