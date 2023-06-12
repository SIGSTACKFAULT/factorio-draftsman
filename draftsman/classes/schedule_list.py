# schedulelist.py

from draftsman.classes.schedule import Schedule

from typing import MutableSequence


class ScheduleList(MutableSequence):
    """
    TODO
    """
    def __init__(self, initlist=None):
        """
        TODO
        """
        self.data = []
        if initlist is not None:
            if not isinstance(initlist, list):
                raise TypeError("'initlist' must be either a list or None")
            for elem in initlist:
                if isinstance(elem, Schedule):
                    self.append(elem)
                elif isinstance(elem, dict):
                    self.append(Schedule(**elem))
                else:
                    raise TypeError("Constructor either takes Tile or dict entries")

    def insert(self, index, schedule):
        """
        TODO
        """
        if not isinstance(schedule, Schedule):
            raise TypeError("Entry in <ScheduleList> must be an instance of <Schedule>")

        self.data.insert(index, schedule)

    def __getitem__(self, index):
        # type: (int) -> Schedule
        return self.data[index]

    def __setitem__(self, index, item):
        # type: (int, Schedule) -> None
        if not isinstance(item, Schedule):
            raise TypeError("Entry in <ScheduleList> must be an instance of <Schedule>")
        self.data[index] = item

    def __delitem__(self, index):
        # type: (int) -> None
        del self.data[index]

    def __len__(self):
        # type: () -> int
        return len(self.data)
    
    def __eq__(self, other):
        # type: (ScheduleList) -> bool
        if not isinstance(other, ScheduleList):
            return False
        if len(self.data) != len(other.data):
            return False
        for i in range(len(self.data)):
            if self.data[i] != other.data[i]:
                return False
        return True
    
    def __repr__(self):
        # type: () -> str
        return "<ScheduleList>{}".format(repr(self.data))

    # def __deepcopy__(self, memo):
    #     pass
