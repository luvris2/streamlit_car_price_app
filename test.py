from anyio import current_time
import streamlit as st
import time
import numpy as np
progress_bar = st.progress(0)
status_text = st.empty()
time_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time_text.text( '{}초'.format(float(i*0.1)))
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()
#############################
import time

with st.empty():
     for seconds in range(5):
         st.write(f" {seconds} seconds have passed")
         time.sleep(1)
     st.write(" 5 sec over!")