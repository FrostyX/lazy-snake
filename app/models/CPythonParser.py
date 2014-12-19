from pstats import Stats


class CPythonParser(object):

	@staticmethod
	def parse(dump):
		stats = []

		index = dump.rfind("Ordered by")
		for line in dump[index:].split("\n")[3:-1]:
			line = " ".join(line.split())
			l = line.split(" ")

			stats.append({
				"ncalls": int(l[0]),
				"tottime": float(l[1]),
				"tottime_percall": float(l[2]),
				"cumtime": float(l[3]),
				"cumtime_percall": float(l[4]),
				"filename": l[5].split(":")[0],
				"line": int(l[5].split(":")[1].split("(")[0]),
				"function": l[5].split(":")[1].split("(")[1][:-1],
			})

		return stats
