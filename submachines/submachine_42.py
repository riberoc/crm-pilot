import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 967) - 376
    _mask = _data(398, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = ',ZLZtA_] i`Mrm6sMTq*OzlOAfB_Y3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
