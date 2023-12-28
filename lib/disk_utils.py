class DiskUtilization(object):
    def __init__(self):
        pass

    def get_disk_info(self):
        import psutil
        disk_info = psutil.disk_usage('/')
        return {
            "total": disk_info.total,
            "used": disk_info.used,
            "free": disk_info.free,
            "percent": disk_info.percent
        }