import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 900) - 988
    _mask = _data(1981, None)
    _enc = 79
    return _mask, _enc

def run():
    matrix = ',h/?Y{#7ZC5_`Ue,e7 [$sz5RW6qMI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
