
import subprocess
import json
import os
from datetime import datetime
import webbrowser

from config.config import MAX_PRICE, PEM_FILE

__author__ = 'letoveter'


def make_request(query, get_output=False, verbose=0):
    if verbose:
        start = datetime.now()
        print query
    if get_output:
        spot_result = subprocess.check_output(query.split())
        if verbose:
            print spot_result
            print datetime.now() - start
        return json.loads(spot_result)
    else:
        os.system(query)
        if verbose:
            print datetime.now() - start

debug = 1

spot_result = make_request('aws ec2 request-spot-instances --spot-price  {} --instance-count 1 --type one-time '
                           '--launch-specification file://config/specification.json'.format(MAX_PRICE), True, debug)
spot_id = spot_result['SpotInstanceRequests'][0]['SpotInstanceRequestId']

make_request('aws ec2 wait spot-instance-request-fulfilled --spot-instance-request-ids {}'.format(spot_id), False, debug)

instance_result = make_request('aws ec2 describe-spot-instance-requests --spot-instance-request-ids {}'.format(spot_id),
                               True, debug)
instance_id = instance_result['SpotInstanceRequests'][0]['InstanceId']

make_request('aws ec2 wait instance-status-ok --instance-ids {}'.format(instance_id), False, debug)

host_result = make_request('aws ec2 describe-instances --instance-ids  {}'.format(instance_id), True, debug)
host = host_result['Reservations'][0]['Instances'][0]['PublicDnsName']

make_request('ssh -o StrictHostKeyChecking=no ubuntu@{}'.format(host), False, debug)
make_request('scp -i {} -r data ubuntu@{}:~'.format(PEM_FILE, host), False, debug)
make_request('scp -i {} -r notepads ubuntu@{}:~'.format(PEM_FILE, host), False, debug)

make_request("ssh -i {} ubuntu@{} 'bash -s' < config/remote_setup.sh".format(PEM_FILE, host), False, debug)

new = 2
url = 'http://{}:8888'.format(host)
webbrowser.open(url, new=new)