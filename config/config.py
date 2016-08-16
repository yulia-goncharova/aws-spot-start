__author__ = 'letoveter'

MAX_PRICE = .5
PEM_FILE = 'credentials/aws-fr-key-pair.pem'

"""
typical aws instances:

  instance type 	vCPUs 	Memory (GiB)	Storage (GB)	Network	    Current spot price (16/08/16, Frankfurt)
  m4.xlarge	        4	    16	            EBS only	    High	    $0.0331, good for data mining
  m4.2xlarge	    8	    32	            EBS only	    High	    $0.0659 - light calculations
  r3.4xlarge	    16	    122	            1 x 320 SSD	    High	    $0.2028 - mem optimized
  r3.8xlarge	    32	    244	            2 x 320 SSD	    10 Gigabit	$0.3557 - CPU optimized
  c4.8xlarge	    36	    60	            EBS only	    10 Gigabit	$0.4565 - CPU optimized
  x1.32xlarge	    128	    1952	        2 x 1960	    20 Gigabit	$1.867 - top spot instance

"""