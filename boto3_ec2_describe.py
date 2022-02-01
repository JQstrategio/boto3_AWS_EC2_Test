import logging
import boto3
from botocore.exceptions import ClientError\

EC2ID = 'i-048656f95f7226d0c'


#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ecpy_describe')


#create ec2 resource
ec2 = boto3.client('ec2')


#creating starts instance function
def describe_ec2instance(instance_id):
	try:
		response = ec2.describe_instances(InstanceIds=[instance_id])
		logger.info("Describing instance %s.", instance_id)
	except ClientError:
		logger.exception("couldn't describe instance %s.",
		instance_id)
		raise
	else:
		return response


response = describe_ec2instance(EC2ID)
print(response)