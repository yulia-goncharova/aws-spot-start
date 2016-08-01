# Amazon spot instances launcher

This is a Python script that launch [AWS](http://aws.amazon.com) spot instance with lowest price, install [Miniconda] (http://conda.pydata.org/miniconda.html) with [scikit-learn] (http://scikit-learn.org/stable/) on-board and run [jupyter notebook] (http://jupyter.org)

## Install

Suppose you already have Amazon account (if not - here is some instructions how to [sing up] (http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html#cli-signup) and [download key pair] (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair)

 - First install [aws-cli] (https://aws.amazon.com/cli/):
```
$ pip install awscli
```

 - Than [make and download credentials] (http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) anf [configure cli] (http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html):

```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: ENTER
```

List of region names you can check [here] (http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region). Note that after registration Amazon allows you to use only 2 regions, you can find them in support email 'Available regions for Amazon Web Services EC2'.

You can check configuration:
```
$ aws ec2 describe-account-attributes
{
    "AccountAttributes": [
        {
            "AttributeName": "supported-platforms",
            "AttributeValues": [
                {
                    "AttributeValue": "VPC"
                }
            ]
        },
...
}
```

## Configure

 - Save *pem* file to *credentials* folder and change *PEM_FILE* value in config/config.py

 - Check and update your maximum price for instance in *MAX_PRICE*

 - Put your remote initialisation code in file config/remote_setup.sh
This repository uses development version of scikit-learn because of [MLPClassifier] (http://scikit-learn.org/dev/modules/generated/sklearn.neural_network.MLPClassifier.html) using advantages, but if it not necessary you can simply setup master brunch:
```
conda install -y scikit-learn
```

 - Check and edit config/specification.json. Examples and JSON specification is [here] (http://docs.aws.amazon.com/cli/latest/reference/ec2/request-spot-instances.html)
