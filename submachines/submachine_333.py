import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 737) - 460
    _mask = _data(768, None)
    _enc = 26
    return _mask, _enc

def run():
    matrix = 'i|^l)H.tt4^Js9psxpusR88sbY_Arq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
