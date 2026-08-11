import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 853) - 479
    _mask = _data(327, None)
    _enc = 51
    return _mask, _enc

def run():
    matrix = ' ZrCF82gKJg>2S7o@L#TDq`iNe,DAC'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
