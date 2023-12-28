class CPU_Utilization(object):
	def __init__(self):
		pass

	def get_cpu_info(self):
		import psutil
		cpu_info = psutil.cpu_percent(interval=1, percpu=True)
		return cpu_info
		# return "Hello from CPU_Utilization"
		# return self.get_cpu_info()
		# return self.cpu_info