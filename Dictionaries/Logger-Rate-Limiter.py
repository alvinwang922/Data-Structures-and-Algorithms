"""
Design a logger system that receive stream of messages along with its timestamps, 
each message should be printed if and only if it is not printed in the last 10 
seconds. Given a message and a timestamp (in seconds granularity), return true 
if the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.
"""


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stream = dict()

    def shouldPrintMessage(self, timestamp: int, message: str):
        """
        Returns true if the message should be printed in the given timestamp, 
        otherwise returns false. If this method returns false, the message 
        will not be printed. The timestamp is in seconds granularity.
        """
        if message in self.stream and timestamp - self.stream[message] < 10:
            return False
        else:
            self.stream[message] = timestamp
            return True


"""
Your Logger object will be instantiated and called as such:
obj = Logger()
param_1 = obj.shouldPrintMessage(timestamp,message)
Example:
Logger logger = new Logger();

logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns True; 

logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns True;

logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns False;

logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns False;

logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns False;

logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns True;
"""
