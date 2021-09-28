#this is the main file
def convert(seconds):
     seconds = seconds % (24 * 3600)
     hour = seconds // 3600
     seconds %= 3600
     minutes = seconds // 60
     seconds %= 60

     return "%d:%02d:%02d" % (hour, minutes, seconds)

 n = 12345
 print(convert(n))
 """Converts number (seconds) to seconds, minutes and hours.

 Parameters
 ----------
 seconds : int
     Number of seconds
 """

