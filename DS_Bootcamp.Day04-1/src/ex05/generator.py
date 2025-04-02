import sys
import resource

def get_all_lines_with_genarator(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

def print_resource_usage():
    usage = resource.getrusage(resource.RUSAGE_SELF)

    max_memory_gb = usage.ru_maxrss / (1024 * 1024)
    print(f"Peak Memory Usage = {max_memory_gb:.3f} GB")

    total_cpu_time = usage.ru_utime + usage.ru_stime
    print(f"User Mode Time + System Mode Time = {total_cpu_time:.3f} s")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("Incorect quantity arguments, this program has an input argument: <file_pash>")
    else:
        file_path = sys.argv[1]
        for line in get_all_lines_with_genarator(file_path):
            pass
    print_resource_usage()