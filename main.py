
def increases(measurements: list) -> int:
    idx = 0
    for key, value in enumerate(measurements):
        if value > measurements[key - 1]:
            idx += 1
    return idx

def window_increases(measurements: list) -> int:
	idx = 0
	for key, value in enumerate(measurements[:-3]):
		val1 = value + measurements[key + 1] + measurements[key +2]
		val2 = measurements[key + 1] + measurements[key +2] + measurements[key+3]
		if val2 > val1:
			idx += 1
	return idx		 