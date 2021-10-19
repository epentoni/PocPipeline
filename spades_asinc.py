# script para ejecutar varios spades.py de forma asincrona
# name: spades_asinc.py
# call as:  python3 spades_asinc.py output_path file1 file2 file3 file4 file5...

import sys
import threading
import subprocess

spades_cmd = 'python3 spades.py'
timeout_minutes = 15

def run_spades(file_name, output_path):
    f1 = output_path + '/cleaned_reads/' + file_name + '.ok_1.fastq.gz'
    f2 = output_path + '/cleaned_reads/' + file_name + '.ok_2.fastq.gz'
    out = output_path + '/assembly/' + file_name + '_assembly'
    proc_args = ['--careful', '-1', f1, '-2', f2, '-o', out, '-t', '$CPUS']
    command = spades_cmd + ' ' + ' '.join(proc_args)
    print('run: ' + command)
    try:
        subprocess.call(command, timeout=(timeout_minutes*60), shell=True)
    except subprocess.TimeoutExpired:
        print('Timeout on command: ' + command)


def spades_asinc(output_path, files):
    for file in files:
        thread = threading.Thread(target=run_spades, args=(file, output_path))
        thread.start()


if __name__ == '__main__':
    parameters = sys.argv[1:]
    output_path = parameters[0]
    files = parameters[1:]
    spades_asinc(output_path, files)
