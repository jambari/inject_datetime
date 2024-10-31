# inject_datetime
This python script is for replacing datetime on an Mseed File. I encounter this issue when I record a short period signal using TDS. The GPS is not connected and the waveform datetime defaulted to 1970s. This datetime is not able to open in Geopsy. That's is why wee need to replace the datetime in order to be able analyze the data. 
