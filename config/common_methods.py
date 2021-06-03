import datetime
import os


class CommonMethods:

    @property
    def create_new_folder(self):
        timestamp = str(datetime.datetime.now())
        current_time = timestamp.replace(":", "_").replace("-", "_").replace(" ", "_").replace(".", "_")
        base_dir = '../reports'
        # create dynamic name with current time stamp
        new_dir = os.path.join(base_dir, current_time)

        # create 'dynamic' dir, if it does not exist
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        return new_dir
