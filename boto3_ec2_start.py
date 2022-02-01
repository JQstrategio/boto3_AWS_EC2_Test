import logging
import boto3
from botocore.exceptions import ClientError

EC2ID = 'i-048656f95f7226d0c'


#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ecpy_describe')


#create ec2 resource
ec2 = boto3.resource('ec2')


#creating starts instance function
def start_instance(instance_id):
	try:
		response = ec2.Instance(instance_id).start()
		logger.info("Started instance %s.", instance_id)
	except ClientError:
		logger.exception("couldn't start instance %s.", instance_id)
		raise
	else:
		return response


response = start_instance(EC2ID)
print(response)