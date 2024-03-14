import HtmlTestRunner
import unittest

# class TestStringMethods(unittest.TestCase):
#     def test_twoValuesAreEqual(self):
#         value1=True
#         value2=True
#         self.assertEqual(value1, value2)

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_output'))

import requests
f = open('test.log', 'w+')
def saveResult(name, url, result):
    f.write('Test name:' + str(name) + '\n')
    f.write('Test URL:' + str(url) + '\n')
    f.write('Test result:' + str(result) + '\n')
    f.write('---------------------------------------------\n ')
def checkServiceForWord(url, keyword):
    result = False
    try:
        x = requests.get(url)
        print(x.text)
        serverStatus=1
        if keyword in x.text:
            print("found keyword")
            result=True
    except:
        print("error")
        result= False
        return result
# Test 1
name = 'Test 1'
url = 'https://jsonplaceholder.typicode.com/todos/1'
result = checkServiceForWord(url, 'userId')
saveResult(name, url, result)
# finish up
f.close()
