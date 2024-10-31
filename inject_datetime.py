from obspy import read
from obspy.core import UTCDateTime

# Load the MiniSEED file
st = read("D:/RANSIKI-PRELIMINARY-RESULT/RANSIKI-PRELIMINARY-RESULT/0102-M2 DEBEK-D1/202408311620.MSD")

# New date (e.g., 2024-09-01)
new_date = UTCDateTime("2024-10-01")

# Adjust each trace's start time by modifying only the date
for tr in st:
    # Extract the current time portion
    current_time = tr.stats.starttime.time
    # Create a new start time with the new date but keeping the same time
    tr.stats.starttime = new_date.replace(hour=current_time.hour, 
                                          minute=current_time.minute, 
                                          second=current_time.second, 
                                          microsecond=current_time.microsecond)

# Save the modified file
st.write("your_new_file.mseed", format="MSEED")
