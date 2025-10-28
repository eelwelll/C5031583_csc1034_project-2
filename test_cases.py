from job import Job
from job_manager import JobManager

EJM = JobManager() #EJM = Empty_job_manager

# all the tests for an empty job list

EJM.__str__()
EJM.__repr__()

print("---erroneous---")
try:
    EJM.edit_job()
except TypeError:
    print("Type error")

try:
    EJM.remove_job()
except TypeError:
    print("Type Error")
try:
    EJM.add_job()
except TypeError:
    print("Type Error")

print(EJM.get_jobs()) # returns empty list

try:
    print(EJM.get_category_count_per_name())
except IndexError:
    print("2. Index Error - no items in list")
try:
    print(EJM.get_total_cost_per_name())
except IndexError:
    print("3. Index Error - no items in list")

EJM.search_by_category()
EJM.search_by_name_and_date()
EJM.search_by_rate()
EJM.search_by_category("math")
EJM.search_by_category(213)
EJM.search_by_name_and_date("dave")
EJM.search_by_name_and_date(123)
EJM.search_by_name_and_date("Dave","2/2/2007")

#remove job which doesn't exist
EJM.remove_job(Job("dave Peel","automobile construction and destruction",14.5,"12/12/2001",10))

EJM.edit_job(Job("dave Peel","automobile construction and destruction",14.5,"12/12/2001",10),Job("Sam Peel","Television construction and destruction",14.5,"12/12/2001",10))

# add none type job
EJM.add_job(12)

#print all the jobs again to show nothing ever happens
print(EJM.get_jobs())

#loading from csv which doesn't exist
EJM.load_from_file("file.csv")

#loading from a non csv file
EJM.load_from_file("job_manager.py")

# creates new csv file with contents within it
EJM.save_to_file("write_to_test.csv")

#loading from csv file with contents
EJM.load_from_file("list_of_jobs.csv")
#print the loaded jobs
print(EJM.get_jobs())

