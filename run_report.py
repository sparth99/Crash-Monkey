import docker
import datetime
import json

def execute_stres_test(container_name):
    test_type = "CPU"
    start_time = datetime.datetime.utcnow()
    client = docker.from_env()
    # container_name = 'competent_proskuriakova'
    container = client.containers.get(container_name)
    try:
        m = container.exec_run("stress --cpu 1 --timeout 60s",detach=True)
    except Exception as e:
        print(e)
    # run the application
    m = container.exec_run('python tests.py')
    end_time = datetime.datetime.utcnow()
    report = generate_json_report(start_time,end_time,test_type)
    write_report_to_file(report)
    logs = container.logs(timestamps=True)
    logs = logs.decode().split("\n")
    write_container_logs(logs,container_name)

def generate_json_report(start_time, end_time, test):
    report = {}
    report['start_time'] = str(start_time)
    report['end_time'] = str(end_time)
    report['test'] = test
    json_report = json.dumps(report)
    return json_report

def write_report_to_file(report):
    with open('external-log/reports.json','a') as the_file:
        the_file.write(report + "\n")

def write_container_logs(logs,name):
    with open('external-log/containers-' + name + '.log','a') as the_file:
        for log in logs:
            the_file.write(str(log))

if __name__ == "__main__":
    execute_stres_test('competent_proskuriakova')

# docker run -it --memory="256m" --cpus=".1" chaos 
# docker exec -it competent_proskuriakova /bin/bash