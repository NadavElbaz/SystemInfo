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
    ram_total_gb = nd.convert_function(ram.total,4)
    ram_available_gb = nd.convert_function(ram.available,1)
    ram_available_percentage =  nd.calculate_percentages(ram_available_gb,ram_total_gb)

    # Storage
    disk = shutil.disk_usage(".")
    disk_total_gb = nd.convert_function(disk.total,4)
    disk_free_gb = nd.convert_function(disk.free,3)
    disk_used_gb = nd.convert_function(disk.used,2)
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