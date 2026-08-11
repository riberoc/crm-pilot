import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 711) - 433
    _mask = _data(235, None)
    _enc = 96
    return _mask, _enc

def run():
    matrix = 'UE4OdRTmqJm]*37BvETGy*#M7D7 u8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
