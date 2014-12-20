parameters = [
	{"name": "ncalls",                               "description": "the number of calls"},
	{"name": "tottime",                              "description": "the total time spent in the given function (and excluding time made in calls to sub-functions)"},
	{"name": "tottime_percall", "label": "percall",  "description": "the quotient of tottime divided by ncalls"},
	{"name": "cumtime",                              "description": "is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions."},
	{"name": "cumtime_percall", "label": "percall",  "description": "is the quotient of cumtime divided by primitive calls"},
	{"name": "filename",                             "description": "filename"},
	{"name": "line",                                 "description": "line number"},
	{"name": "function",                             "description": "function"},
]
