# Configure FTP/SFTP Server and ADF Pipeline for Data Extraction

1. Set up FTP/SFTP server credentials and ensure network access from ADF.
2. In Azure Data Factory, create a Linked Service for FTP/SFTP.
3. Create a Dataset in ADF for the files to extract.
4. Build a pipeline with a Copy Data activity:
   - Source: FTP/SFTP Dataset
   - Sink: Desired destination (e.g., Azure Blob, SQL DB)
5. Publish and trigger the pipeline. 