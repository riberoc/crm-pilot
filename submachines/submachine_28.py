import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 508) - 440
    _mask = _data(942, None)
    _enc = 136
    return _mask, _enc

def run():
    matrix = ',`!4pCM4kOx.~H1*9# ~TfKJ4qL%Pa'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
