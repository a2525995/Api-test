from requestnew import sched

class Job():
    def __init__(self, name, set_time):
        """
        :rtype name: str
        :rtype set_time: list[str]  e.g: ["*", "1", "2", "*", "2"]
        """
        self.name = name
        self.time = set_time

    def __deal_time(self, time):
        time = time.strip()
        time = time.split()

        for args in range(len(time)):
            if time[args] == "*":
                time[args] = None
        return time

    def create_job(self, func):
        sched.add_job(func, "cron", id=self.name, minute=self.time[0], hour=self.time[1], day=self.time[2], month=self.time[3], week=self.time[4])

    def show_jobs(self):
        return sched.get_jobs()

    def pause_job(self):
        sched.pause_job(self.name)

    def pause_all(self):
        sched.pause()

    def resume_job(self):
        sched.resume_job(self.name)

    def resume_all(self):
        sched.resume()

    def remove_job(self):
        sched.remove_job(self.name)

    def remove_all(self):
        sched.remove_all_jobs()
        return True


if __name__ == '__main__':
    j = Job('t12', ["1", "2", "*", "*", "5"])
    def test():
        print(123)
    j.create_job(test)
    d = j.show_jobs()
    print(d)
