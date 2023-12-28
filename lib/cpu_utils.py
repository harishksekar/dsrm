class CPU_Utilization(object):
	def __init__(self):
		pass

	def get_cpu_info(self):
		import psutil
		cpu_load = psutil.cpu_percent(interval=1)
		cpu_count = psutil.cpu_count()
		cpu_stats = psutil.cpu_stats()
		return {
			"total"	: cpu_count,
			"load"	: cpu_load,
			"ctx_sw": cpu_stats[0],
			"intr"  : cpu_stats[1]
		}
		# return "Hello from CPU_Utilization"
		# return self.get_cpu_info()
		# return self.cpu_info