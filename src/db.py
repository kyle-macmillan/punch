from datetime import datetime
from datetime import date
from datetime import timedelta
import sys
import os
from tinydb import TinyDB, Query

class Database:

    def __init__(self):
        self.db = TinyDB('db.json')

    def log(self, task):
        """ Add a new task """

        today = datetime.today().strftime("%A-%B-%d-%Y")
        time = datetime.now().time().replace(microsecond=0)
        self.db.insert({'task': task, 'date': today,
            'start': str(time), 'end': '', 'done': False})

    def end(self):
        jobs = Query()
        time = datetime.now().time().replace(microsecond=0)
        self.db.update({'end': str(time), 'done': True}, jobs.end == "")

    def status(self, num_days):
        past = date.today() - timedelta(days = num_days)
        temp = ""
        print('')

        for task in self.db:
            start_date = datetime.strptime(task['date'], "%A-%B-%d-%Y")
            
            if start_date == past:
                break

            if temp != start_date:
                print('{:<15} {:^25}'.format("", f'--- Tasks for {start_date.strftime("%A, %B %d %Y")} ---'))
                print('{:<40} {:>10} {:>10} {:>15}'.format('Task', 'Start', 'End', 'Time'))
                temp = start_date

            job = task['task']
            start = task['start']
            end = task['end']
            elapsed = 'In progress'

            if task['done']:
                elapsed = self.difference(start, end)
           
            print('{:<40} {:>10} {:>10} {:>15}'.format(job, start, end, elapsed))

    def clear(self):
        """ Deletes entire database """

        confirm = input("This will delete all history. Press 'y' to confirm\n")

        if confirm == 'y':
            self.db.truncate()
    
    def difference(self, start, end):
        start_time = datetime.strptime(start, "%H:%M:%S")
        end_time = datetime.strptime(end, "%H:%M:%S")

        elapsed = end_time - start_time

        return str(elapsed)

