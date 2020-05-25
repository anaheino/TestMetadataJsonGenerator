import json
import random
import sys

def main():
   generate_testdata()
   exit(0)

def generate_testdata():
   test_units = ['metric', 'celsius', 'electricity used']
   print('Generating test metadata. Default test units are: ' + ', '.join(test_units))
   console_file = open("console.txt","a") 
   console_file.write('Generating test metadata. Default test units are: ' + ', '.join(test_units))

   if len(sys.argv) > 1:
      argument_list = sys.argv[1:]
      print('Passed arguments. Arguments are used as units for generation of metadata.')
      print('Arguments passed were: ' + ', '.join(argument_list))
      test_units = argument_list
   
   statistic_list = []

   for i in [random.randint(i, 25) for i in range(0, 15)]:
       statistic_list.append(json.dumps(generateStatistic(test_units[random.randint(0, len(test_units)-1)], i)))
   print('Generated following mock data: ' + ', '.join(statistic_list))
   
   with open('execution_metadata.json', 'w') as outfile:
       json.dump(statistic_list, outfile)
   print('Dumped results to execution_metadata.json.')

def generateStatistic(unit, value):
   value_dict = {"unit": unit,
   "value": value,
   "timestamp": "10.20.2020",
   "transactionId": "23"
   } 
   return value_dict

main()