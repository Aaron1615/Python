import random
import Queue

class Printer:
    """Creates a Printer object which is capable of processing
    print tasks from a queue at a page rate (ppm) over time"""
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    def tick(self):
        """Goes through one unit (tick) of time.
        If there is a current task, one unit of time is removed
        from the time remaining."""
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
    def busy(self):
        """Checks if a current task is present.
        Returns true or false"""
        if self.current_task != None:
            return True
        else:
            return False
    def start_next(self,new_task):
        """Changes the current task of the printer to a new task
        with it's own time remaining.
        """
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.page_rate
    
class Task:
    """A task object for printing which includes the time it was created and
    a random number of pages between min_num_pages and max_num_pages which will be printed"""
    def __init__(self, time, min_num_pages, max_num_pages):
        self.time_stamp = time
        self.pages = random.randrange(min_num_pages, max_num_pages + 1)
    def get_stamp(self):
        """Getter function for time, returns the time a print
        request was made"""
        return self.time_stamp
    def get_pages(self):
        """Getter function for the number of pages, 
        returns the amount of timein ticks a print 
        request will take"""
        return self.pages
    def wait_time(self, current_time):
        """Returns the amount of time the task waited in
        the queue."""
        return current_time - self.time_stamp

def simulation(num_seconds, pages_per_minute,min_num_pages,max_num_pages,num_students,num_prints):
    """Runs one simulation of a number of seconds(num_seconds) at a printer
    which prints pages at a rate of (pages_per_minute) between (min_num_pages) and (max_num_pages)
    (num_prints) times for (num_students)
    """
    local_printer = Printer(pages_per_minute)
    print_queue = Queue.Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        """Iterates through the given number of seconds adding
        new print tasks to the queue if they occur and moving tasks
        to the printer when the printer finishes a task"""

        if new_print_task(num_students,num_prints):
            task = Task(current_second,min_num_pages,max_num_pages)
            print_queue.enqueue(task)

        if (not local_printer.busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            local_printer.start_next(next_task)

        local_printer.tick()
    average_wait = sum(waiting_times)/len(waiting_times)
    print("Average wait %6.2f seconds. %3d tasks remain." %(average_wait, print_queue.size()))

def new_print_task(num_students,num_prints):
    """Simulates the chance that a student will print a page.
    Given that there are num_students students who each print num_prints per hour,
    num_students * num_prints/60min * 1 min/60 seconds
    1 in 60*60//(num_students * num_prints) chance a print task will be queued
    """
    num = random.randrange(1, 1 + 60*60//(num_students * num_prints))
    if num == 60*60//(num_students * num_prints):
        return True
    else:
        return False

