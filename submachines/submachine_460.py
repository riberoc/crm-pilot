import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 463) - 988
    _mask = _data(1484, None)
    _enc = 44
    return _mask, _enc

def run():
    matrix = '[8S&;B_5UCX UE27MV-0vU`Ygy.:*Z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
