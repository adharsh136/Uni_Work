import boto3

# Constants
#The created instance's ID
inst_ID = 'i-078581ec7b4427335'
#The security group created in previous lab (lab5)
sec_grp_id = 'sg-0ba69d87ee7933db6'
#The subnets 'a' and 'c' IDs (since my instance is a t2.micro machine)
SUBNETS = [ 'subnet-09f996d1ad81767a9', 'subnet-0b3601189181ee48e']
#The default VPC ID
VPC_ID = 'vpc-01f842220d0070f97'

#Initiating client for alb 
client = boto3.client('elbv2')

#Application Load Balancer
response = client.create_load_balancer(
   Name='23796349-ALB',
   Subnets=SUBNETS[:2],  
   SecurityGroups=[sec_grp_id],
   Scheme='internet-facing',
   Tags=[
       {
           'Key': 'Name',
           'Value': '23796349-ALB'
       },
   ]
)
lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
print(f"Load Balancer ARN: {lb_arn}")
 
#Target group
response = client.create_target_group(
   Name='23796349-TG',
   Protocol='HTTP',
   Port=80,
   HealthCheckPath='/polls/',
   VpcId=VPC_ID,
   Tags=[
       {
           'Key': 'Name',
           'Value': '23796349-TG'
       },
   ]
)
tg_arn = response['TargetGroups'][0]['TargetGroupArn']
print(f"Target Group ARN: {tg_arn}")
 
#Register the created instance as a target in the target group
client.register_targets(
   TargetGroupArn=tg_arn,
   Targets=[
       {'Id': inst_ID},
   ]
)

#Listener
client.create_listener(
   LoadBalancerArn=lb_arn,
   Protocol='HTTP',
   Port=80,
   DefaultActions=[
       {
           'Type': 'forward',
           'TargetGroupArn': tg_arn
       },
   ]
)
 
print("Application Load Balancer and listener successfully created. The instance was registered as a target")
