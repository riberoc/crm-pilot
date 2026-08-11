import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 286) - 716
    _mask = _data(672, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = '# %8Qnof_{UEG6V)D@ao8%+zoVOoxA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
