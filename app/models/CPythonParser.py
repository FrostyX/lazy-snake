from pstats import Stats


class CPythonParser(object):

	@staticmethod
	def parse(dump):
		stats = []

		index = dump.rfind("Ordered by")
		for line in dump[index:].split("\n")[3:-3]:
			line = " ".join(line.split())
			l = line.split(" ")
			filename_line_function =  not (l[5].startswith("{") and l[-1].endswith("}"))

			stats.append({
				"ncalls": int(l[0]),
				"tottime": float(l[1]),
				"tottime_percall": float(l[2]),
				"cumtime": float(l[3]),
				"cumtime_percall": float(l[4]),
				"filename": l[5].split(":")[0] if filename_line_function else "",
				"line": int(l[5].split(":")[1].split("(")[0]) if filename_line_function else "",
				"function": l[5].split(":")[1].split("(")[1][:-1] if filename_line_function else " ".join(l[5:]),
			})

		return stats
