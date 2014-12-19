from __meta__ import *
from app.models.CPythonParser import CPythonParser


class TestFilenameCleaner(TestCase):
	def setUp(self):
		self.parser = CPythonParser

	def test_correct_input(self):
		parsed = self.parser.parse(input)
		first = {
		    "ncalls": 1,
			"tottime": 0.000,
			"tottime_percall": 0.000,
			"cumtime": 23.063,
			"cumtime_percall": 23.063,
			"filename": "tracer.py",
			"line": 20,
			"function": "<module>",
		}
		self.assertEquals(parsed[0], first, "Incorrectly parsed line")
		self.assertEquals(len(parsed), 12)

	def test_hello_world_input(self):
		pass




input = """
You should restart:
  * Some applications using:
      kill 3230  # urxvt
      kill 22296; kill 31572  # gvim
      sudo service mpd restart

  * These applications manually:
      pidgin
         3983586 function calls (3978646 primitive calls) in 23.036 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   23.063   23.063 tracer.py:20(<module>)
        1    0.000    0.000   22.440   22.440 main.py:27(run)
        1    0.000    0.000   22.439   22.439 router.py:38(dispatch)
        1    0.000    0.000   12.095   12.095 default.py:43(render)
        1    0.000    0.000   12.095   12.095 default.py:8(render)
        3    0.000    0.000   12.093    4.031 applications.py:195(helpers)
        2    0.000    0.000   12.091    6.045 applications.py:221(affected_instances)
        2    0.000    0.000   12.089    6.045 tracer.py:109(trace_application)
        1    0.000    0.000   10.344   10.344 default.py:35(__init__)
        1    0.023    0.023   10.281   10.281 tracer.py:64(trace_affected)
       19    3.043    0.160    9.903    0.521 tracer.py:122(_affecting_processes)
      104    0.088    0.001    5.960    0.057 processes.py:51(files)
"""
