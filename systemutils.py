import platform
import shutil
import psutil
import nadavutils as nd

def get_system_info():
    ### Function to generate system info, including OS and Memory Details

    # CPU
    cpu_name = platform.processor()
    cpu_cores = psutil.cpu_count()

    # RAM
    ram = psutil.virtual_memory()
    ram_total_gb = nd.bytes_into_gigabytes(ram.total)
    ram_available_gb = nd.bytes_into_gigabytes(ram.available)
    ram_available_percentage =  nd.calculate_percentages(ram_available_gb,ram_total_gb)

    # Storage
    disk = shutil.disk_usage(".")
    disk_total_gb = nd.bytes_into_gigabytes(disk.total)
    disk_free_gb = nd.bytes_into_gigabytes(disk.free)
    disk_used_gb = nd.bytes_into_gigabytes(disk.used)
    disk_free_percentage = nd.calculate_percentages(disk_free_gb,disk_total_gb)

    system_info = {
        'cpu': cpu_name,
        'cpu_cores': cpu_cores,
        'ram_total_gb': ram_total_gb,
        'ram_available_gb': round(ram_available_gb,3),
        'disk_total_gb': disk_total_gb,
        'disk_free_gb': disk_free_gb,
        'disk_free_percentage': f"{disk_free_percentage}%",
        'python_version': platform.python_version(),
        'ram_available_percentage': f"{ram_available_percentage}%"
    }

    return system_info