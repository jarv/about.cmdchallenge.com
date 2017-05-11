Title: Open sourcing all of cmdchallenge.com
Date: 2017-05-11
Slug: releasing-cmdchallenge

[CMD Challenge](https://cmdchallenge.com) is a web application that presents small
shell challenges, where submissions are executed remotely in a Docker container.
I am happy to announce today that I have decided to release the entire source code and terraform 
configuration for it under the MIT license [on github](https://github.com/jarv/cmdchallenge-site).

What this means is that anyone can host their own version of the site easily
in the AWS free tier using the exact same configuration that is used for
the main production.
Kick the tires,
clone and go nuts if you want or take a look if you want a very simple
example of using API Gateway, Lambda, Dynamo and Docker. The biggest
reward for this fun little side-project would be if someone tries to spin
up their very own, please [let me know on twitter](https://twitter.com/thecmdchallenge)
if you do!

Part of the reason for doing this was to explore how I could simplify the setup using terraform.
It is now extremely easy to set up and tear down an isolated and separate version
of the site. The only part missing from the automated 
setup is hosting static assets. The production cmdchallenge.com site uses 
S3 with cloudfront in front for caching. If you try this out yourself you will
need to serve assets locally.

Before your run the below steps it is important to know what you will
be creating, the following AWS resources will be created with terraform:

* API Gateway
* Lambda function
* DynamoDB
* t2.micro EC2 Instance running coreos

<br />
<b>Here is what you will need to do to create your own cmdchallenge.com in the AWS free tier:</b>

### Step 1: Clone the cmdchallenge-site repository

```bash
git clone https://github.com/jarv/cmdchallenge-site
git submodule update --init --recursive
```

### Step 2: Create SSH keys for the EC2 instance

```bash
$ ./bin/create-ssh-keys
Creating keypair for ssh
Generating public/private rsa key pair.
Your identification has been saved in cmd_rsa.
Your public key has been saved in cmd_rsa.pub.
...
```

This will create a `private/ssh` directory in the repostory root which contains the private and public keypair for the instance used for cmdchallenge.
This `private/` directory is ignored by git and should be kept safe. In addition to the ssh keys it will contain the CA and certificates needed for tls authentication for docker after the terraform run.

### Step 3: Update the AWS configuration for terraform

Modify `terraform/site.tf` with your AWS credentials. By default it looks for a profile named "cmdchallenge".
See the [terraform documentation](https://www.terraform.io/docs/providers/aws/) if you want to use something other than an aws profile
```
provider "aws" {
  region = "us-east-1"
  shared_credentials_file = "${pathexpand("~/.aws/credentials")}"
  profile = "cmdchallenge"
}
```

### Step 4: Run terraform

```bash
cd terraform
terraform init
terraform apply
```

The process of bringing up all the resources in AWS takes around 4 or 5 minutes.
At the very end you will see some terraform outputs:


```
Outputs:

ami_id = ami-ad593cbb
ec2_public_ip = 107.23.137.206
invoke_url = https://9hz0doczmb.execute-api.us-east-1.amazonaws.com/prod
test_hello_world = curl 'https://9hz0doczmb.execute-api.us-east-1.amazonaws.com/prod/?cmd=echo+hello+world&challenge_slug=hello_world'
```

Paste the curl command into your terminal to confirm that everything is working:

```bash
$ curl 'https://9hz0doczmb.execute-api.us-east-1.amazonaws.com/prod/?cmd=echo+hello+world&challenge_slug=hello_world'
{"challenge_slug": "hello_world", "rand_error": false, "output": "hello world", "test_errors": null, "return_code": 0, "correct": true}
```

### Step 5: Serve assets

```bash
make serve
```

Point your browser to http://localhost:8000/ and profit!
