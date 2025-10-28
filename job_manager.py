from job import Job
import csv
class JobManager:
    def __init__(self, jobs=Job):
        self.list_of_jobs = []
        self.list_of_jobs.append(jobs)

    def get_jobs(self):
        return self.list_of_jobs

    def __str__(self):
        """A string representation of the job manager"""

        return f"job manager,{self.list_of_jobs}"


    def __repr__(self):
        """The formal string representation of the job manager"""
        return f"{self.list_of_jobs}"


    def add_job(self, job=Job):
        """adds a job to the job manager if the worker is available"""
        try:
            if job==type(Job) and job:
                try:
                    self.list_of_jobs.append(job)
                except AttributeError:
                    print("Error: tried to add none type to list")
            else:
                print(f"{job} not job, didn't add to list")
        except TypeError:
            print("Error: tried to enter job of none type Job.")


    def remove_job(self, job=Job):
        """removes an existing job from the job manager"""
        try:
            self.list_of_jobs.pop(self.list_of_jobs.index(job))
        except TypeError:
            print("Error: tried to enter job of none type Job.")
        except ValueError:
            print(f"{Exception}: {job} not in list")
        except AttributeError:
            print("Error: no attribute")

    def edit_job(self, old_job=Job, new_job=Job):
        """edits an existing job in the job manager if the worker is available"""
        try:
            if old_job in self.list_of_jobs: # checks if job is in list
                self.list_of_jobs[self.list_of_jobs.index(old_job)] = new_job
            else:
                print("job not in list, no edits made") # prints error to console if job is not in the list
        except TypeError:
            print("Error: TypeErorr, enter type Job")
    def search_by_category(self, category=str):
        """returns a list of all jobs that completely matches the given category (string)"""
        list_of_matching = []
        if self.list_of_jobs:
            for items in self.list_of_jobs:
                if items:
                    continue
                try:
                    if items.get_category() == category:
                        list_of_matching.append(items)
                except AttributeError:
                    print("Error: no category passed")
        return list_of_matching if list_of_matching else "No items found"

    def search_by_rate(self, rate=float):
        """returns a list of all jobs that completely matches the given rate (float)"""
        list_of_matching = []
        if self.list_of_jobs:
            for items in self.list_of_jobs:
                if items:
                    continue
                try:
                    if items.get_rate() == rate:
                        list_of_matching.append(items)
                except AttributeError:
                    print("Error: no rate passed")
        return list_of_matching if list_of_matching else "No items found"

    def search_by_name_and_date(self, name=str, date=str):
        """returns a list of all jobs that completely matches the given name (string) and date (string)"""
        list_of_matching = []
        if self.list_of_jobs:
            for items in self.list_of_jobs:
                if items:
                    continue
                try:
                    if items.get_name() == name and items.get_date() == date:
                        list_of_matching.append(items)
                except AttributeError:
                    print("Error: no name and/or date passed")
        return list_of_matching if list_of_matching else "No items found"

    def get_total_cost_per_name(self, names=list):
        """returns a dictionary that maps each worker found in names (list of string) to the total cost (float)
        of the work allocated in the system for that worker."""
        total_cost = {}
        try:
            if self.list_of_jobs:
                for items in self.list_of_jobs:
                    if items:
                        continue
                    try:
                        if items.get_name() in names:
                            total_cost[items.get_name()] = (items.get_rate() * items.get_hours())
                    except AttributeError:
                        print("Error: no name")
        except TypeError:
            print("Error: no name passed")



    def get_category_count_per_name(self):
        """returns a dictionary that maps name (string) to a dictionary,
        that maps category (string) to the total number of jobs (int) of that category found in the system."""
        category_dict = {}
        if self.list_of_jobs:
            for items in self.list_of_jobs:
                if items:
                    continue
                category_dict[items.get_name()]={items.get_category():+1}

    def load_from_file(self, file_name=str):
        """reads a csv file of job details and adds them to the list of job objects"""
        try:
            with open(f"{file_name}","r") as load:
                new_file = csv.reader(load)
                file_list = list(new_file)
                for number,temp_job in enumerate(file_list):
                    if number!=0:
                        self.list_of_jobs.append([Job(temp_job[0],temp_job[1],temp_job[3],temp_job[4])])
        except FileNotFoundError:
            print(f"Error: no such file dir: {file_name}")
        except TypeError:
            print(f"Error: type error, use csv file")
        except IndexError:
            print("Error: index error, make sure csv file is formatted correctly/ you are using a csv file with columns")

    def save_to_file(self, file_name):
        """writes to a csv file all job details found in the list of job objects"""
        try:
            with open(file_name,"w") as save_file:
                # 0 = name, 1 = category, 2 = rate, 3 = date, 4 = hours
                save_file = csv.writer(save_file,quoting=csv.QUOTE_ALL)
                for jobs in self.list_of_jobs:
                    if jobs:
                        continue
                    save_file.writerow([jobs.get_name(),jobs.get_category(),jobs.get_rate(),jobs.get_date(),jobs.get_hours()])
        except FileNotFoundError:
            print(f"Error: no such file dir: {file_name}")
        except TypeError:
            print(f"Error: type error, use csv file")
        except AttributeError:
            print(f"Error, no job found within list_of_jobs, file created but nothing written")