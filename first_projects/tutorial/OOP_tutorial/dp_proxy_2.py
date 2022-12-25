class College:
    '''Resource-intensive object'''

    def studyingInCollege(self):
        print("Studying In College....")


class CollegeProxy:
    '''Relatively less resource-intensive proxy acting as middleman.
    Instantiates a College object only if there is no fee due.'''

    def __init__(self):

        self.feeBalance = 1000
        self.college = None

    def studyingInCollege(self):

        print("Proxy in action. Checking to see if the balance of student is clear or not...")
        if self.feeBalance <= 500:
            # If the balance is less than 500, let him study.
            self.college = College()
            self.college.studyingInCollege()
        else:
            # Otherwise, don't instantiate the college object.
            print("Your fee balance is greater than 500, first pay the fee")


if __name__ == "__main__":
    collegeProxy = CollegeProxy()

    # Client attempting to study in the college at the default balance of 1000.
    collegeProxy.studyingInCollege()

    # Altering the balance of the student
    collegeProxy.feeBalance = 100

    # Client attempting to study in college at the balance of 100. Should succeed.
    collegeProxy.studyingInCollege()
