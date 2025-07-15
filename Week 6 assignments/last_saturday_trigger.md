# Automate Pipeline Trigger for Last Saturday of the Month

1. In ADF, create a custom schedule trigger using a CRON expression for the last Saturday.
   - Example CRON: `0 0 0 ? * 7L` (runs at midnight on the last Saturday)
2. Attach the trigger to your pipeline.
3. Test and monitor the trigger in ADF. 