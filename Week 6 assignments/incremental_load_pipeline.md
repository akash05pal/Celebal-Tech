# Create Incremental Load Pipeline and Automate Daily

1. Use watermarking (e.g., last modified date) or change tracking in your source.
2. In ADF, create parameters and variables to store the watermark value.
3. Build a pipeline with a Copy Data activity that filters for new/changed records.
4. Store/update the watermark after each run.
5. Add a schedule trigger to run the pipeline daily. 