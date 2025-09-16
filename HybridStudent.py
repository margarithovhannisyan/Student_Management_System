class HybridStudent():
    def set_online_lessons_time(self, online_lessons_time):
        if int(online_lessons_time) < 0:
            raise ValueError("Offline lessons time cannot be negative")
        self.__online_lessons_time = online_lessons_time

    def get_total_lessons_time(self):
        total_lessons_time = self.__online_lessons_time
        return total_lessons_time
