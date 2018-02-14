import unittest
import hw4

class TestHW4(unittest.TestCase):
    '''Test cases to be used in conjunction with HW4 assignment'''

    def testInvalidUser(self):
        self.assertEqual(hw4.retrieve_github_info('12342345234523452345234523'),'Error', 'Invalid Endpoint')

    def testInvalidRepo(self):
        self.assertEqual(hw4.retrieve_github_commit_info('bbb','mnuzzo567'), 'Error', 'Invalid URL')

    def testCommitNumber(self):
        self.assertEqual(hw4.retrieve_github_commit_info('glassducks','mnuzzo567'),3,'Num of commits on project = 3')

if __name__ == '__main__':
    unittest.main()
