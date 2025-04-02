import sys
import resource

def get_all_lines(file_path):
    result = []
    with open(file_path, "r") as file:
        for line in file:
            result.append(line.strip())
    return result

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
        content_lines = get_all_lines(sys.argv[1])
        for line in content_lines:
            pass
    print_resource_usage()