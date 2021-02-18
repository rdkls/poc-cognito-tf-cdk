requirements:
	pip install -r requirements.txt

synth: requirements
	cdk synth

deploy: synth
	env AWS_PROFILE=dev awsudo arn:aws:iam::107483165697:role/intelematics/Administrator cdk deploy

destroy:
	env AWS_PROFILE=dev awsudo arn:aws:iam::107483165697:role/intelematics/Administrator cdk destroy
