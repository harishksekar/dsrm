class DiskUtilization(object):
    def __init__(self):
        pass

    def get_disk_info(self):
        import psutil
        disk_info = psutil.disk_usage('/')
        return str({"disk": {
            "total": disk_info.total,
            "used": disk_info.used,
            "free": disk_info.free,
            "percent": disk_info.percent
        }})
        return str("{disk:") + str({
            "total": disk_info.total,
            "used": disk_info.used,
            "free": disk_info.free,
            "percent": disk_info.percent
        })