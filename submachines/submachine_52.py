import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 811) - 282
    _mask = _data(538, None)
    _enc = 11
    return _mask, _enc

def run():
    matrix = 'w`e&HljJyiP9ET=MBI&O;}kA?Z(6 !'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
