#! usr/bin/env python3
#from kafka import SimpleProducer
from kafka import KafkaProducer
import sys
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
