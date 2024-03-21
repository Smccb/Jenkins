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
f = open('test_saved.log', 'w+')
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
url = 'http://localhost:5000/getProducts'
result = checkServiceForWord(url, 'name1')
saveResult(name, url, result)


# Test 2
name = 'Test 2'
url = 'http://localhost:5000/getTitles'
result = checkServiceForWord(url, 'name1')
saveResult(name, url, result)

#Test 3



#Test 4
name = 'Test 4'
url = 'http://localhost:5000/'
result = checkServiceForWord(url, '/getProducts')
saveResult(name, url, result)


# finish up
f.close()
