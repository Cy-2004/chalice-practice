from chalice import Chalice

app = Chalice(app_name='run-on-schedule')

instance_id = "id-5748298345492"
ec2 = boto3.client('ec2')

@ap.schedule('cron(0 8 * * *)'):
def daily_task():
	print("Running daily task at midnight")
	response = ec2.start_instance(instance_id)
