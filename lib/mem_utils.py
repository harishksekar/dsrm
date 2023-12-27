class Memory_Utilization(object):
    def __init__(self):
        pass

    def get_memory_info(self):
        import psutil
        mem_info = psutil.virtual_memory()
        return mem_info