class Memory_Utilization(object):
    def __init__(self):
        pass

    def get_memory_info(self):
        import psutil
        mem_info = psutil.virtual_memory()
        return {
            "total": mem_info.total,
            "available": mem_info.available,
            "percent": mem_info.percent,
            "used": mem_info.used,
            "free": mem_info.free
        }